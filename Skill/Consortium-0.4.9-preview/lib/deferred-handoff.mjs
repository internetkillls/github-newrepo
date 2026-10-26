/** RCC Deferred Handoff v0.4.3-preview: local, bounded, no model requests while waiting. */
import { createHash, randomUUID } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, writeFileSync, renameSync, unlinkSync, openSync, closeSync, statSync, realpathSync, readdirSync, watch } from 'node:fs';
import { resolve, dirname, sep, join } from 'node:path';
import { execFile } from 'node:child_process';
import { inspectQueue, dispatchOne, queuePaths,verifyQueuedJob,recheckMachineReview } from './queue-manager.mjs';
import {controllerInstructions} from './execution-contract.mjs';

export const HANDOFF_SCHEMA = 'rcc.deferred.v1';
const SESSION = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const stamp = () => new Date().toISOString();
const digest = value => createHash('sha256').update(value).digest('hex');
const safeCase = id => { if (!/^[a-z0-9][a-z0-9._-]{0,79}$/i.test(String(id||'')) || id==='..') throw new Error('handoff.invalid_case');return id.toLowerCase(); };
export const handoffPaths = (root,id) => {
  const dir=queuePaths(resolve(root),safeCase(id)).dir;
  return {dir, file:join(dir,'handoff.json'), lock:join(dir,'handoff.lock'), runnerLock:join(dir,'deferred-runner.lock'), summary:join(dir,'handoff-summary.json'), codexLog:join(dir,'codex-resume.log')};
};
function atomic(file,data){ const tmp=file+'.'+process.pid+'.'+randomUUID()+'.tmp';try {writeFileSync(tmp,JSON.stringify(data,null,2)+'\n',{flag:'wx',mode:0o600});renameSync(tmp,file);}finally{if(existsSync(tmp))unlinkSync(tmp);} }
function withLock(root,id,fn){const p=handoffPaths(root,id);mkdirSync(p.dir,{recursive:true,mode:0o700});let fd;try{fd=openSync(p.lock,'wx',0o600);}catch(e){if(e.code==='EEXIST')throw new Error('handoff.locked; reconcile before retry');throw e;}try{const state=existsSync(p.file)?JSON.parse(readFileSync(p.file,'utf8')):null;if(state&&state.schema!==HANDOFF_SCHEMA)throw new Error('handoff.bad_state_schema'); const save=next=>atomic(p.file,{...next,updatedAt:stamp()});return fn(state,save,p);}finally{closeSync(fd);unlinkSync(p.lock);} }
export function status(root,id){const p=handoffPaths(root,id);return existsSync(p.file)?JSON.parse(readFileSync(p.file,'utf8')):null;}
export function prepareHandoff(root,{caseId,sessionId,autoResume=false,autoReview=false,workspace=resolve(root)}={}){
  if(!SESSION.test(String(sessionId||'')))throw new Error('handoff.invalid_codex_session_uuid');
  const c=safeCase(caseId), source=inspectQueue(root,c);
  if(source.lock)throw new Error('handoff.queue_locked');
  if(!source.jobs.length)throw new Error('handoff.empty_queue');
  if(source.jobs.some(j=>!['PENDING','REVIEWED_WITNESS'].includes(j.status)))throw new Error('handoff.queue_not_prepared');
  if(autoReview&&source.jobs.some(j=>j.status==='PENDING'&&!j.outputContract))throw Error('handoff.output_contract_required_for_auto_review');
  const jobs=source.jobs.map(j=>({id:j.id,payloadHash:j.payloadHash,role:j.role}));
  if(new Set(jobs.map(j=>j.id)).size!==jobs.length)throw new Error('handoff.duplicate_job');
  const resolvedWorkspace=realpathSync(resolve(workspace));
  if(!statSync(resolvedWorkspace).isDirectory())throw new Error('handoff.bad_workspace');
  return withLock(root,c,(current,save)=>{
    if(current)throw new Error('handoff.existing_case_no_overwrite');
    const nonce=randomUUID();
    const next={schema:HANDOFF_SCHEMA,caseId:c,sessionId:sessionId.toLowerCase(),workspace:resolvedWorkspace,
      queueRevision:source.revision,jobs,autoResume:Boolean(autoResume),autoReview:Boolean(autoReview),nonce,
      wakeupKey:digest(JSON.stringify([c,sessionId.toLowerCase(),jobs.map(j=>j.id)])),
      status:'PREPARED',preparedAt:stamp(),armedAt:null,wakeup:null};
    save(next);
    return {ok:true,caseId:c,status:'PREPARED',autoResume:next.autoResume,
      marker:'HANDOFF_ACCEPTED:'+nonce,next:'Finish the current Codex turn with this exact marker; a trusted Stop hook or explicit arm activates the runner.'};
  });
}
export function armHandoff(root,{caseId,sessionId,marker}={}){
  return withLock(root,caseId,(state,save)=>{
    if(!state)throw new Error('handoff.not_found');
    if(state.sessionId!==String(sessionId||'').toLowerCase()||marker!=='HANDOFF_ACCEPTED:'+state.nonce)throw new Error('handoff.session_or_marker_mismatch');
    if(state.status==='ARMED')return {ok:true,duplicate:true,status:state.status};
    if(state.status!=='PREPARED')throw new Error('handoff.not_prepared');
    state.status='ARMED';state.armedAt=stamp();save(state);
    return {ok:true,caseId:state.caseId,status:state.status,autoResume:state.autoResume};
  });
}
export function armFromStopEvent(root,event){
  if(event?.hook_event_name!=='Stop'||!SESSION.test(String(event?.session_id||'')))return {armed:false,reason:'not_stop_or_session'};
  const last=String(event.last_assistant_message||'');
  const match=last.match(/HANDOFF_ACCEPTED:([0-9a-f-]{36})/i);
  if(!match)return {armed:false,reason:'no_handoff_marker'};
  const directory=resolve(root,'.devspace','rcc');if(!existsSync(directory))return {armed:false,reason:'no_case_directory'};
  const candidates=readdirSync(directory,{withFileTypes:true}).filter(x=>x.isDirectory()).slice(0,128).map(x=>x.name)
    .filter(id=>{try{const s=status(root,id);return s?.status==='PREPARED'&&s?.sessionId===event.session_id.toLowerCase()&&s?.nonce===match[1].toLowerCase();}catch{return false;}});
  if(candidates.length!==1)return {armed:false,reason:'ambiguous_or_missing_handoff'};
  armHandoff(root,{caseId:candidates[0],sessionId:event.session_id,marker:'HANDOFF_ACCEPTED:'+match[1].toLowerCase()});
  return {armed:true,caseId:candidates[0]};
}
function reconcile(root,id){
  const s=status(root,id),q=inspectQueue(root,id);
  if(q.lock)return {status:'WAITING_LOCK'};
  if(!s||!['ARMED','WAITING_REVIEW','WAITING_INPUT','READY'].includes(s.status))return {status:s?.status??'NO_HANDOFF'};
  if(q.jobs.length!==s.jobs.length||s.jobs.some((p,i)=>q.jobs[i]?.id!==p.id||q.jobs[i]?.payloadHash!==p.payloadHash))return {status:'BLOCKED',reason:'queue_identity_changed'};
  for(const j of q.jobs.filter(j=>j.status==='REVIEWED_WITNESS'&&j.review?.provenance==='machine_live_response_and_output_gate')){
    try{recheckMachineReview(j)}catch{return {status:'BLOCKED',reason:'machine_review_or_output_changed'}}
  }
  if(q.jobs.some(j=>j.status==='NOT_SENT_CONFIRMED'||j.status==='BLOCKED_INPUT'))return {status:'BLOCKED',reason:'negative_or_changed_input'};
  if(q.jobs.some(j=>['DISPATCHING','UNCERTAIN'].includes(j.status)))return {status:'WAITING_REVIEW',reason:'ambiguous_submission'};
  if(q.jobs.some(j=>j.status==='TRANSPORT_RETURNED'))return {status:'WAITING_REVIEW',reason:'completion_witness_required'};
  if(q.jobs.every(j=>j.status==='REVIEWED_WITNESS')){
    // Operator review is asserted, not a proof of independently verified browser state.
    for(const j of q.jobs){
      if(j.review?.decision!=='witnessed'||!['operator_supplied_not_independently_verified','machine_live_response_and_output_gate'].includes(j.review?.provenance))return {status:'BLOCKED',reason:'unsupported_review'};
      const src=resolve(j.review.sourceArtifact||'');
      if(!existsSync(src)||!statSync(src).isFile())return {status:'BLOCKED',reason:'review_source_missing'};
    }
    return {status:'READY',reason:'all_jobs_operator_reviewed',jobs:q.jobs};
  }
  if(q.jobs.some(j=>j.status==='PENDING'))return {status:'DISPATCH_ONE'};
  return {status:'WAITING_INPUT'};
}
export function evaluateHandoff(root,id){return reconcile(root,id);}
function mark(root,id,newStatus,meta={}){return withLock(root,id,(state,save)=>{if(!state)throw new Error('handoff.not_found');if(!['ARMED','WAITING_REVIEW','WAITING_INPUT','READY'].includes(state.status))return {ok:false,status:state.status};state.status=newStatus;if(meta.blocker)state.blocker=meta.blocker;save(state);return {ok:true,status:newStatus};});}
function createSummary(root,id,jobs){const p=handoffPaths(root,id);const state=status(root,id);const obj={schema:'rcc.deferred.summary.v1',caseId:id,sessionId:state.sessionId,generatedAt:stamp(),completion:jobs.some(j=>j.review.provenance==='machine_live_response_and_output_gate')?'RESPONSE_AND_OUTPUT_GATES_NOT_TASK_QUALITY':'OPERATOR_REVIEWED_NOT_INDEPENDENTLY_PROVEN',jobs:jobs.map(j=>({jobId:j.id,role:j.role,payloadHash:j.payloadHash,receiptSha256:j.review.receiptSha256,sourceArtifact:j.review.sourceArtifact,provenance:j.review.provenance})),wakeupKey:state.wakeupKey};atomic(p.summary,obj);return p.summary;}
export function finalizeReady(root,id,jobs){const summary=createSummary(root,id,jobs);return withLock(root,id,(state,save)=>{
  if(!['ARMED','WAITING_REVIEW','WAITING_INPUT','READY'].includes(state.status))throw new Error('handoff.not_ready_state');
  // Reconfirm the evidence right before READY; no forged state by transport exit zero.
  const evidence=reconcile(root,id);if(evidence.status!=='READY')throw new Error('handoff.evidence_changed');
  state.status='READY';state.summaryPath=summary;state.readyAt=stamp();save(state);return {status:'READY',summaryPath:summary,autoResume:state.autoResume};
});}
export function claimWake(root,id,{manual=false,approval=null}={}){return withLock(root,id,(s,save)=>{
 if(!s)throw new Error('handoff.not_found');
 if(s.status!=='READY')throw new Error('handoff.not_ready_to_resume');
 if(manual){if(approval!==`WAKE-${s.caseId}`)throw new Error('handoff.wake_approval_required');}
 else if(!s.autoResume)throw new Error('handoff.auto_resume_disabled');
 const proof=reconcile(root,id);if(proof.status!=='READY')throw new Error('handoff.review_no_longer_valid');
 const key=s.wakeupKey;s.status='RESUME_CLAIMED';s.wakeup={key,claimedAt:stamp(),origin:manual?'explicit_manual':'opt_in_runner',attempts:1};save(s);
 return {caseId:s.caseId,sessionId:s.sessionId,workspace:s.workspace,summaryPath:s.summaryPath,wakeupKey:key};
});}
export function recordWake(root,id,{key,exitCode,error=null,signal=null}={}){return withLock(root,id,(s,save)=>{
 if(!s||s.status!=='RESUME_CLAIMED'||s.wakeup?.key!==key)throw new Error('handoff.wakeup_not_claimed');
 s.status=exitCode===0&&!error&&!signal?'RESUME_EXITED':'RESUME_UNCERTAIN';
 s.wakeup={...s.wakeup,returnedAt:stamp(),exitCode,signal,error:error?String(error).slice(0,250):null};save(s);
 return {status:s.status,completionClaim:'Codex process exit only; not agent task correctness'};
});}
export function execCodex(command,args,opts={}){return new Promise(done=>{
 let started=false;const child=execFile(command,args,{cwd:opts.cwd,env:{...process.env,...opts.env},encoding:'utf8',timeout:opts.timeoutMs??900000,maxBuffer:2*1024*1024,windowsHide:true},(error,stdout,stderr)=>{
  done({code:error?error.code??null:0,error:error?String(error.message):null,signal:error?.signal??null,started,stdout:stdout||'',stderr:stderr||''});
 });
 child.once('spawn',()=>{started=true});if(opts.input!==undefined){child.stdin.on('error',()=>{});child.stdin.end(opts.input)}
});}
export async function wakeCodex(root,id,{manual=false,approval,run=execCodex,command='codex'}={}){
 const controllers=controllerInstructions();
 const claim=claimWake(root,id,{manual,approval});const p=handoffPaths(root,id);
 const prompt=controllers+`\nRCC deferred handoff ${claim.caseId}. Read the local evidence summary at ${claim.summaryPath}. Respect each receipt's recorded provenance: operator assertions and machine response/output gates do not certify task quality. Verify source artifacts and source state before any action. Do not blindly resend prior worker prompts. Resume original work only within granted permissions.`;
 let result;try{result=await run(command,['exec','resume',claim.sessionId,'-'],{cwd:claim.workspace,timeoutMs:900000,input:prompt});}
 catch(e){result={code:null,error:String(e),signal:null,stdout:'',stderr:''};}
 const preview=[`exit=${String(result.code)} signal=${String(result.signal)} error=${String(result.error)}`,String(result.stdout||''),String(result.stderr||'')].join('\n').slice(0,2*1024*1024);
 writeFileSync(p.codexLog,preview,{mode:0o600});
 return {...recordWake(root,id,{key:claim.wakeupKey,exitCode:result.code,error:result.error,signal:result.signal}),logPath:p.codexLog};
}
export function transportExecutor(pluginRoot,root){const target=resolve(pluginRoot,'bin/rcc-consortium');return job=>{
 const args=[target,'worker','send',`--case=${job.caseId}`,`--role=${job.role}`,`--prompt-file=${job.prompt.path}`];
 if(job.model)args.push(`--model=${job.model}`);if(job.level)args.push(`--level=${job.level}`);
 for(const f of job.uploads)args.push(`--upload-file=${f.path}`);
 return execCodex(process.execPath,args,{cwd:root,timeoutMs:420000,env:{RCC_QUEUE_JOB_ID:job.id,RCC_QUEUE_PAYLOAD_HASH:job.payloadHash}});
};}
export async function runnerTick(root,id,{dispatch=()=>{throw new Error('handoff.no_dispatch_executor')},wake=()=>{throw new Error('handoff.no_wake_executor')},review=verifyQueuedJob,emergency=null,now=Date.now()}={}){
 const s=status(root,id);if(!s)return {status:'NO_HANDOFF'};
 if(!['ARMED','WAITING_REVIEW','WAITING_INPUT','READY'].includes(s.status))return {status:s.status};
 if(!s.armedAt)return {status:'PREPARED'};
 // Stop hook fires just before the Codex turn finishes: afford host process time to go idle.
 if(now-Date.parse(s.armedAt)<3000)return {status:'ARMED',reason:'stop_hook_settle_window'};
 const next=reconcile(root,id);
 if(s.autoReview&&next.status==='WAITING_REVIEW'&&next.reason==='completion_witness_required'){
  const job=inspectQueue(root,id).jobs.find(j=>j.status==='TRANSPORT_RETURNED');
  try{const result=await review(root,id,{jobId:job.id});
   if(['queue.recovery_review_failed','queue.recovery_verification_exhausted'].includes(result.code))return {status:'RECOVERY_EXHAUSTED',reason:result.code,jobId:job.id};
   if(emergency&&result.incidentId){let recovery;try{recovery=await emergency(root,result.incidentId)}catch(e){recovery={status:'EMERGENCY_HANDLER_UNAVAILABLE',error:String(e.message).slice(0,200)}}
    const outcome={status:recovery.ok?'REVIEWED_WITNESS':'RECOVERY_ESCALATED',reason:recovery.code||recovery.status,jobId:job.id,incidentId:result.incidentId,recovery};
    withLock(root,id,(state,save)=>{state.lastRecovery={incidentId:result.incidentId,status:outcome.status,reason:outcome.reason,at:stamp()};save(state)});return outcome;}
   return {status:result.ok?'REVIEWED_WITNESS':['queue.auto_review_escalated','queue.auto_review_budget_exhausted'].includes(result.code)?'REVIEW_ESCALATED':'WAITING_REVIEW',reason:result.code||'machine_review_returned',jobId:job.id,...(result.escalationFile?{escalationFile:result.escalationFile}:{})};}
  catch(e){return {status:'WAITING_REVIEW',reason:'machine_review_unavailable',error:String(e.message).slice(0,200)};}
 }
 if(next.status==='DISPATCH_ONE'){
  const result=await dispatchOne(root,id,dispatch);
  mark(root,id,result.code==='queue.blocked_input'?'BLOCKED':'WAITING_REVIEW', {blocker:result.code});
  return {status:result.status||'WAITING_REVIEW',code:result.code};
 }
 if(next.status==='READY'){
  if(s.status!=='READY')finalizeReady(root,id,next.jobs);
  if(status(root,id).autoResume)return await wake(root,id);
  return {status:'READY',reason:'manual_resume_required'};
 }
 if(['BLOCKED','WAITING_REVIEW','WAITING_INPUT'].includes(next.status)){
  if(s.status!==next.status)mark(root,id,next.status,{blocker:next.reason});
 }
 return {status:next.status,reason:next.reason};
}
export async function runService(root,id,{dispatch,wake,review,emergency,signal,intervalMs=5000,onTick=()=>{}}={}){
 const p=handoffPaths(root,id);mkdirSync(p.dir,{recursive:true,mode:0o700});let fd;
 try{fd=openSync(p.runnerLock,'wx',0o600);}catch(e){if(e.code==='EEXIST')throw new Error('handoff.runner_already_started_or_stale_lock');throw e;}
 try{
  writeFileSync(fd,JSON.stringify({pid:process.pid,startedAt:stamp()})+'\n');
  while(!signal?.aborted){const r=await runnerTick(root,id,{dispatch,wake,review,emergency});onTick(r);
    if(['RESUME_EXITED','RESUME_UNCERTAIN','BLOCKED','REVIEW_ESCALATED','RECOVERY_ESCALATED','RECOVERY_EXHAUSTED'].includes(r.status))return r;
    if(r.status==='READY'&&!status(root,id)?.autoResume)return r;
    // Event-triggered filesystem wake plus a bounded consistency timer; neither requests model inference.
    await new Promise(resolveWait=>{let watcher=null,listener,settled=false;const timer=setTimeout(done,intervalMs);
      function done(){if(settled)return;settled=true;clearTimeout(timer);watcher?.close();signal?.removeEventListener('abort',listener);resolveWait();}
      listener=done;signal?.addEventListener('abort',listener,{once:true});
      try{watcher=watch(p.dir,{persistent:false},(_event,file)=>{const name=String(file||'');if(!name||name==='queue.json'||name==='handoff.json')done();});}catch{/* consistency timer fallback */}
    });
  }
  return {status:'STOPPED'};
 }finally{closeSync(fd);unlinkSync(p.runnerLock);}
}
