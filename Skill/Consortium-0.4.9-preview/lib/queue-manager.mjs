import {classifySubmission} from './transport-phase.mjs';
import {operationalStatus} from './operational-status.mjs';
/** RCC C0 queue. Dispatch and opt-in live review remain separate, evidence-gated operations. */
import { createHash, randomUUID } from 'node:crypto';
import { existsSync, mkdirSync, openSync, closeSync, unlinkSync, readFileSync, writeFileSync, renameSync, statSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import {appendQueueCommit,effectiveQueueState} from './queue-journal.mjs';
import {normalizeOutputContract,captureOutputs,recheckOutputs} from './output-gate.mjs';
import {writeTextExclusive} from './durable-record.mjs';

export const QUEUE_SCHEMA = 'rcc.queue.v1';
const ACTIVE_BLOCKERS = new Set(['DISPATCHING', 'UNCERTAIN', 'TRANSPORT_RETURNED']);
const TERMINAL = new Set(['REVIEWED_WITNESS', 'NOT_SENT_CONFIRMED']);
const stamp = () => new Date().toISOString();
const hash = (s) => createHash('sha256').update(s).digest('hex');
function caseId(value) {
  const id = String(value || '').trim();
  if (!/^[a-z0-9][a-z0-9._-]{0,79}$/i.test(id) || id === '..') throw new Error('queue.invalid_case_id');
  return id.toLowerCase();
}
function roleId(value) {
  const id = String(value || '').trim();
  if (!/^[a-z0-9][a-z0-9._-]{0,79}$/i.test(id) || id === '..') throw new Error('queue.invalid_role');
  return id.toLowerCase();
}
export function queuePaths(root, id) {
  const dir = resolve(root, '.devspace', 'rcc', caseId(id));
  return { dir, file: resolve(dir, 'queue.json'), lock: resolve(dir, 'queue.lock') };
}
function writeAtomic(path, data) {
  mkdirSync(dirname(path), { recursive: true, mode: 0o700 });
  const tmp = `${path}.${process.pid}.${randomUUID()}.tmp`;
  try {
    writeFileSync(tmp, JSON.stringify(data, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
    renameSync(tmp, path);
  } finally { if (existsSync(tmp)) unlinkSync(tmp); }
}
function getQueue(root, id) {
  const { file,dir } = queuePaths(root, id);
  if (!existsSync(file)) {
    const restored=effectiveQueueState(dir,null);
    if(restored&&(restored.schema!==QUEUE_SCHEMA||restored.caseId!==caseId(id)||!Array.isArray(restored.jobs)))throw Error('journal.queue_identity_mismatch');
    return restored||{ schema: QUEUE_SCHEMA, caseId: caseId(id), revision: 0, createdAt: stamp(), jobs: [] };
  }
  const q = JSON.parse(readFileSync(file, 'utf8'));
  if (q.schema !== QUEUE_SCHEMA || q.caseId !== caseId(id) || !Array.isArray(q.jobs) || !Number.isInteger(q.revision)) throw new Error('queue.invalid_state; inspect or repair manually, do not overwrite');
  return effectiveQueueState(dir,q);
}
export function inspectQueue(root, id) {
  const paths = queuePaths(root, id);
  const state = getQueue(root, id);
  let lock = null;
  if (existsSync(paths.lock)) {
    try { lock = JSON.parse(readFileSync(paths.lock, 'utf8')); } catch { lock = { invalid: true }; }
  }
  return { ...state, lock };
}
function withLock(root, id, fn) {
  const { dir, file, lock } = queuePaths(root, id);
  mkdirSync(dir, { recursive: true, mode: 0o700 });
  let fd;
  try { fd = openSync(lock, 'wx', 0o600); } catch (e) {
    if (e.code === 'EEXIST') throw new Error('queue.locked; inspect owner; do not auto-unlock or retry sends');
    throw e;
  }
  const release = () => { closeSync(fd); unlinkSync(lock); };
  try {
    writeFileSync(fd, JSON.stringify({ pid: process.pid, createdAt: stamp(), nonce: randomUUID() }) + '\n');
    const q = getQueue(root, id);
    let committed=JSON.parse(JSON.stringify(q));
    const save = () => {
      q.revision++; q.updatedAt = stamp();
      // The flushed journal commit is authoritative; queue.json remains a compatibility projection.
      // A restart may observe a stale projection, but cannot rewind a committed DISPATCHING event.
      appendQueueCommit(dir,committed,q); committed=JSON.parse(JSON.stringify(q));
      writeAtomic(file, q);
      writeAtomic(resolve(dir,'activity.json'),{...operationalStatus({...q,lock:{pid:process.pid}}),at:stamp(),queueRevision:q.revision});
    };
    const result = fn(q, save);
    if (result && typeof result.then === 'function') return result.finally(release);
    release();
    return result;
  } catch (error) { release(); throw error; }
}
function fileFingerprint(path, maxBytes = 32 * 1024 * 1024) {
  const full = resolve(path);
  const st = statSync(full);
  if (!st.isFile() || st.size > maxBytes) throw new Error('queue.invalid_or_oversize_file');
  return { path: full, bytes: st.size, sha256: hash(readFileSync(full)) };
}
export function enqueue(root, { case: id, role, promptFile, model = null, level = null, uploadFiles = [], key = null,outputContract=null } = {}) {
  if (!promptFile) throw new Error('queue.prompt_file_required');
  const jobCase = caseId(id), jobRole = roleId(role);
  const prompt = fileFingerprint(promptFile, 2 * 1024 * 1024);
  if (prompt.bytes === 0) throw new Error('queue.empty_prompt');
  const uploads = uploadFiles.map(x => fileFingerprint(x));
  if (model !== null && (!String(model).trim() || String(model).length > 200)) throw new Error('queue.invalid_model');
  if (level !== null && (!String(level).trim() || String(level).length > 200)) throw new Error('queue.invalid_level');
  const contract=normalizeOutputContract(outputContract);
  const payloadHash = hash(JSON.stringify([jobCase,jobRole,prompt,model,level,uploads,...(contract?[contract]:[])]));
  const idempotencyKey = key || payloadHash;
  if (!/^[a-zA-Z0-9:._-]{1,128}$/.test(idempotencyKey)) throw new Error('queue.invalid_idempotency_key');
  return withLock(root, jobCase, (q, save) => {
    const prior = q.jobs.find(j => j.idempotencyKey === idempotencyKey);
    if (prior) {
      if (prior.payloadHash !== payloadHash) throw new Error('queue.idempotency_key_payload_conflict');
      return { ok: true, duplicate: true, job: prior, caseId: jobCase };
    }
    const job = { id: randomUUID(), caseId: jobCase, role: jobRole, idempotencyKey, payloadHash, status: 'PENDING', prompt, uploads,
      model, level, createdAt: stamp(), attempts: 0, events: [{ at:stamp(),status:'PENDING',kind:'enqueued' }] };
    if(contract)job.outputContract=contract;
    q.jobs.push(job); save();
    return { ok: true, duplicate: false, job, caseId: jobCase };
  });
}
function assertInputs(job) {
  for (const file of [job.prompt, ...job.uploads]) {
    const current = fileFingerprint(file.path, file === job.prompt ? 2*1024*1024 : 32*1024*1024);
    if (current.bytes !== file.bytes || current.sha256 !== file.sha256) throw new Error('queue.source_changed; enqueue a fresh job after review');
  }
}
export async function dispatchOne(root, id, execute) {
  // Lock covers the entire external call. A killed process leaves DISPATCHING, never PENDING.
  return withLock(root, id, async (q, save) => {
    const blocked = q.jobs.find(j => ACTIVE_BLOCKERS.has(j.status));
    if (blocked) return { ok: false, code: 'queue.reconciliation_required', blockedJobId: blocked.id, blockedStatus: blocked.status };
    const job = q.jobs.find(j => j.status === 'PENDING');
    if (!job) return { ok: true, code: 'queue.empty' };
    try { assertInputs(job); } catch (err) {
      job.status = 'BLOCKED_INPUT'; job.events.push({ at: stamp(), status: job.status, code: String(err.message) });save();
      return { ok: false, code: 'queue.blocked_input', jobId: job.id };
    }
    job.status = 'DISPATCHING'; job.attempts++; job.startedAt = stamp(); job.invocationToken = randomUUID();
    job.events.push({ at: stamp(), status: 'DISPATCHING', code: 'pre_side_effect_commit' }); save();
    try {
      const result = await execute({ ...job, uploads: job.uploads.map(x => ({ ...x })) });
      // Nonzero transport exits may occur AFTER submission; do not retry.
      const isZero = result && result.code === 0 && !result.error && !result.signal;
      const noSend = !isZero && !result?.error && !result?.signal && classifySubmission(result?.phaseReceipt,{token:job.invocationToken,job,root})==='NOT_SENT_CONFIRMED';
      job.status = noSend ? 'NOT_SENT_CONFIRMED' : isZero ? 'TRANSPORT_RETURNED' : 'UNCERTAIN';
      if(noSend)job.submissionEvidence={receiptSha256:hash(JSON.stringify(result.phaseReceipt)),scope:'Fresh invocation-bound no-Send proof; NOT task completion or permission to retry'};
      job.transport = { exitCode: result?.code ?? null, signal: result?.signal ?? null,
        errorName: result?.error ? String(result.error.name || 'error') : null,
        stdoutSha256: hash(String(result?.stdout || '')), stdoutBytes: Buffer.byteLength(String(result?.stdout || '')),
        stderrSha256: hash(String(result?.stderr || '')), stderrBytes: Buffer.byteLength(String(result?.stderr || '')) };
      job.events.push({ at: stamp(), status: job.status, code: noSend ? 'verified_pre_send_failure_NO_automatic_retry' : isZero ? 'transport_exit_zero_NOT_completion' : 'transport_unknown_NO_retry' });
      save();
      return { ok: isZero, code: noSend ? 'queue.not_sent_confirmed' : isZero ? 'queue.awaiting_completion_witness' : 'queue.transport_uncertain', jobId: job.id, status: job.status };
    } catch (error) {
      job.status = 'UNCERTAIN'; job.transport = { errorName: String(error?.name || 'Error'), message: String(error?.message || error).slice(0, 256) };
      job.events.push({ at: stamp(), status: job.status, code: 'execution_exception_NO_retry' }); save();
      return { ok: false, code: 'queue.transport_uncertain', jobId: job.id, status: job.status };
    }
  });
}
export function reviewJob(root, id, { jobId, receiptFile } = {}) {
  if (!jobId || !receiptFile) throw new Error('queue.job_and_receipt_required');
  const receipt = JSON.parse(readFileSync(resolve(receiptFile), 'utf8'));
  return withLock(root, id, (q, save) => {
    const job = q.jobs.find(j => j.id === jobId);
    if (!job) throw new Error('queue.job_not_found');
    if (TERMINAL.has(job.status)) throw new Error('queue.already_reviewed');
    if (job.status !== 'UNCERTAIN' && job.status !== 'TRANSPORT_RETURNED') throw new Error('queue.job_not_reviewable');
    if (receipt.schema !== 'rcc.queue.review.v1' || receipt.jobId !== job.id || receipt.caseId !== job.caseId || receipt.role !== job.role) throw new Error('queue.receipt_identity_mismatch');
    if (receipt.decision === 'witnessed') {
      const w = receipt.witness;
      if (!w || w.userEchoVerified !== true || typeof w.userAnchor !== 'string' || w.userAnchor.length < 8 ||
         w.assistantBoundToUserAnchor !== w.userAnchor || w.completionVerified !== true ||
         !['observed_active_then_stable_inactive','anchored_terminal_controls_and_stability'].includes(w.completionEvidence) ||
         !/^[a-f0-9]{64}$/.test(w.assistantTextSha256 || '') || !receipt.reviewer || !receipt.sourceArtifact)
        throw new Error('queue.insufficient_completion_evidence');
      job.status = 'REVIEWED_WITNESS';
    } else if (receipt.decision === 'not_sent') {
      if (!receipt.reviewer || !receipt.sourceArtifact || !receipt.reason || String(receipt.reason).length < 20) throw new Error('queue.insufficient_no_send_evidence');
      job.status = 'NOT_SENT_CONFIRMED';
    } else throw new Error('queue.unsupported_review_decision');
    job.review = { at: stamp(), receiptSha256: hash(readFileSync(resolve(receiptFile))), decision: receipt.decision,
      sourceArtifact: String(receipt.sourceArtifact), reviewer: String(receipt.reviewer),
      provenance: 'operator_supplied_not_independently_verified' };
    job.events.push({ at: stamp(), status: job.status, code: 'operator_review_not_auto_canonical' });
    save();return { ok: true, jobId: job.id, status: job.status, review: job.review };
  });
}
async function persistReviewIncident(root,q,job){
 const {persistIncident}=await import('./recovery-incidents.mjs'),checkpointHash=hash(JSON.stringify(q));
 const packet={schema:'rcc.recovery.escalation.v1',event:'RCC_RECOVERY_ESCALATION',incidentId:hash(JSON.stringify([job.id,job.payloadHash,checkpointHash,'queue.auto_review_exhausted'])),caseId:job.caseId,jobId:job.id,payloadHash:job.payloadHash,checkpointHash,checkpointSource:'queue_snapshot_excluding_lock',observedAt:stamp(),signature:'queue.auto_review_exhausted',status:'PERSISTED_LOCAL_NOT_DELIVERED',expectedState:'Exact response and all declared output bytes verified before progression',observedState:job.status,attempts:job.events.filter(e=>e.code==='auto_review_unresolved'),bindings:[{role:job.role,jobId:job.id,status:'AUTO_REVIEW_UNRESOLVED'}],requestedDecision:'Diagnose the smallest safe repair; do not repeat the worker prompt or assume files were delivered',forbiddenActions:['RESEND_UNCERTAIN_PROMPT','CLAIM_TASK_COMPLETE','EXECUTE_RETURNED_CODE'],delivery:{attempted:false,acknowledged:false}};
 const incident=persistIncident(root,packet);return {incidentId:packet.incidentId,escalationFile:incident.file,created:incident.created};
}
export async function verifyQueuedJob(root,id,{jobId,observe,port=9222,recoveryIncidentId=null}={}){
 return withLock(root,id,async(q,save)=>{
  const job=q.jobs.find(j=>j.id===jobId);if(!job)throw Error('queue.job_not_found');
  if(job.status!=='TRANSPORT_RETURNED')return {ok:false,code:'queue.transport_return_required',status:job.status};
  if(!job.outputContract)return {ok:false,code:'queue.output_contract_required',status:job.status};
  if((job.recoveryVerificationAttempts||0)>=1)return {ok:false,code:'queue.recovery_verification_exhausted',status:job.status,incidentId:job.recoveryIncidentId};
  let recoveryAttempt=false,recheckRecovery=()=>{};
  if(recoveryIncidentId){
   const {validatedEmergencyDecision}=await import('./emergency-delivery.mjs'),{ensureRecoveryBudget,RECOVERY_POLICY}=await import('./recovery-budget.mjs');
   const allowed=validatedEmergencyDecision(root,recoveryIncidentId,{checkpointHash:hash(JSON.stringify(q))});
   if(allowed.packet.jobId!==job.id||allowed.packet.payloadHash&&allowed.packet.payloadHash!==job.payloadHash||allowed.decision.decision!=='REVERIFY_JOB')throw Error('queue.recovery_job_mismatch');
   if((job.recoveryVerificationAttempts||0)>=RECOVERY_POLICY.extraVerificationAttempts)return {ok:false,code:'queue.recovery_verification_exhausted',status:job.status};
   if(Math.min(ensureRecoveryBudget(root,recoveryIncidentId).remainingMs,Date.parse(allowed.decision.expiresAt)-Date.now())<RECOVERY_POLICY.verificationAdmissionMs)throw Error('queue.insufficient_recovery_budget');
   recheckRecovery=()=>validatedEmergencyDecision(root,recoveryIncidentId,{checkpointHash:allowed.packet.checkpointHash});
   recoveryAttempt=true;job.recoveryVerificationAttempts=(job.recoveryVerificationAttempts||0)+1;job.recoveryIncidentId=recoveryIncidentId;
  }else if((job.verificationAttempts||0)>=3){
   const incident=await persistReviewIncident(root,q,job);return {ok:false,code:incident.created?'queue.auto_review_escalated':'queue.auto_review_budget_exhausted',status:job.status,...incident};
  }
  if(!recoveryAttempt)job.verificationAttempts=(job.verificationAttempts||0)+1;save();
  try{
   assertInputs(job);
   const observer=observe||(await import('./queue-live-review.mjs')).observeQueuedResponse;
   const result=await observer(root,JSON.parse(JSON.stringify(job)),{port});
   recheckRecovery();
   if(result.jobId!==job.id||result.payloadHash!==job.payloadHash||result.status!=='RESPONSE_UI_WITNESSED')throw Error('queue.live_response_not_verified');
   assertInputs(job);
   const outputs=captureOutputs(job.outputContract,result.deliveryBlocks||[],resolve(queuePaths(root,id).dir,'verified-output',job.id));
   recheckOutputs(outputs);
   recheckRecovery();
   const {deliveryBlocks,...witness}=result;
   const proof={schema:'rcc.queue.machine-review.v1',jobId:job.id,payloadHash:job.payloadHash,caseId:job.caseId,role:job.role,at:stamp(),witness,outputs,scope:'Response UI plus declared output bytes; task quality is not certified'};
   const file=resolve(queuePaths(root,id).dir,'reviews',job.id+'-'+randomUUID()+'.json'),text=JSON.stringify(proof,null,2)+'\n';
   if(!writeTextExclusive(file,text))throw Error('queue.review_file_conflict');
   job.status='REVIEWED_WITNESS';job.review={at:stamp(),decision:'witnessed',reviewer:'rcc-live-review',provenance:'machine_live_response_and_output_gate',sourceArtifact:file,receiptSha256:hash(text)};
   job.events.push({at:stamp(),status:job.status,code:'machine_response_and_declared_outputs_verified'});save();
   return {ok:true,status:job.status,jobId:job.id,review:job.review};
  }catch(e){
   job.lastVerification={at:stamp(),code:String(e.message).slice(0,250)};job.events.push({at:stamp(),status:job.status,code:'auto_review_unresolved',error:job.lastVerification.code});save();
   if(recoveryAttempt)return {ok:false,code:'queue.recovery_review_failed',reason:job.lastVerification.code,status:job.status,incidentId:recoveryIncidentId};
   if(job.verificationAttempts>=3)return {ok:false,code:'queue.auto_review_escalated',reason:job.lastVerification.code,status:job.status,...await persistReviewIncident(root,q,job)};
   return {ok:false,code:'queue.auto_review_unresolved',reason:job.lastVerification.code,status:job.status};
  }
 });
}
export function recheckMachineReview(job){
 const bytes=readFileSync(job.review.sourceArtifact);if(hash(bytes)!==job.review.receiptSha256)throw Error('queue.review_evidence_changed');
 const proof=JSON.parse(bytes.toString('utf8'));if(proof.schema!=='rcc.queue.machine-review.v1'||proof.jobId!==job.id||proof.payloadHash!==job.payloadHash)throw Error('queue.review_identity_mismatch');
 recheckOutputs(proof.outputs);return true;
}
function pidIsAlive(pid) {
  if (!Number.isInteger(pid) || pid < 1) return true; // Unknown identity: fail closed.
  try { process.kill(pid, 0); return true; } catch (err) { return err.code !== 'ESRCH'; }
}
export function recoverQueue(root, id, { approval } = {}) {
  const paths = queuePaths(root,id);
  if (approval !== `RECOVER-${caseId(id)}`) throw new Error('queue.explicit_recovery_approval_required');
  if (existsSync(paths.lock)) {
    let lock;
    try { lock = JSON.parse(readFileSync(paths.lock,'utf8')); } catch { throw new Error('queue.unreadable_lock; manual investigation required'); }
    if (pidIsAlive(lock.pid)) throw new Error('queue.lock_owner_may_be_live; recovery denied');
    // Recovery is manual and conservative; only the explicit stopped owner may be released.
    unlinkSync(paths.lock);
  }
  return withLock(root,id,(q,save)=>{
    const jobs=q.jobs.filter(j=>j.status==='DISPATCHING');
    for (const job of jobs) {
      job.status='UNCERTAIN';job.events.push({at:stamp(),status:'UNCERTAIN',code:'crash_recovery_NO_retry'});
    }
    if (jobs.length) save();
    return {ok:true,recoveredJobs:jobs.map(j=>j.id),status:jobs.length?'UNCERTAIN':'NO_IN_FLIGHT'};
  });
}
