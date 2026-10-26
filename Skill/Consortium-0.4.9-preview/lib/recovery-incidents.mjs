/** Durable local diagnostic outbox. It has no messaging, shell, restart or dispatch capability. */
import {readFileSync,existsSync} from 'node:fs';
import {resolve} from 'node:path';import {randomUUID,createHash} from 'node:crypto';
import {stateHash} from './queue-journal.mjs';import {inspectRecovery} from './recovery-inspect.mjs';
import {writeTextExclusive} from './durable-record.mjs';
import {ensureRecoveryBudget,claimObservationBudget,RECOVERY_POLICY} from './recovery-budget.mjs';
import {boundedObservation} from './control-policy.mjs';
const digest=x=>createHash('sha256').update(x).digest('hex');
const id=x=>{if(!/^[a-f0-9]{64}$/.test(String(x)))throw Error('incident.invalid_id');return x;};
const paths=(root,key)=>resolve(root,'.devspace','rcc','recovery-incidents',id(key));
function boundedJson(value){const text=JSON.stringify(value);if(Buffer.byteLength(text)>4*1024*1024)throw Error('incident.record_too_large');return text;}
function commit(file,body){
 const envelope={schema:'rcc.incident.record.v1',body,hash:stateHash(body)};
 return writeTextExclusive(file,boundedJson(envelope)+'\n');
}
function read(file){const bytes=readFileSync(file);if(bytes.length>4*1024*1024)throw Error('incident.record_too_large');const r=JSON.parse(bytes);if(r.schema!=='rcc.incident.record.v1'||r.hash!==stateHash(r.body))throw Error('incident.corrupt_record');return r.body;}
export {commit as commitIncidentRecord,read as readIncidentRecord,paths as incidentDirectory};
export function failurePacket({caseId,goalRef=null,inspection}){
 if(!/^[a-z0-9][a-z0-9._-]{0,79}$/i.test(caseId||''))throw Error('incident.case_required');
 caseId=caseId.toLowerCase();
 if(inspection?.schema!=='rcc.recovery.inspection.v1'||!['OBSERVED','ENDPOINT_UNAVAILABLE'].includes(inspection.status)||!Array.isArray(inspection.bindings)||!Array.isArray(inspection.attempts))throw Error('incident.inspection_required');
 if(inspection.status==='OBSERVED'&&inspection.bindings.length&&inspection.bindings.every(b=>b.status==='MATCHED_HINT_VERIFIED'))return null;
 const signature=inspection.status==='ENDPOINT_UNAVAILABLE'?'browser.endpoint_unavailable':inspection.bindings.length?'browser.binding_reconciliation_required':'browser.no_worker_bindings';
 const checkpointHash=id(inspection.stateHash),endpoint=inspection.endpoint||null;const incidentId=digest(JSON.stringify([caseId,checkpointHash,signature,endpoint]));
 return {schema:'rcc.recovery.escalation.v1',event:'RCC_RECOVERY_ESCALATION',incidentId,caseId,goalRef:goalRef?String(goalRef).slice(0,1000):null,checkpointHash,endpoint,observedAt:inspection.observedAt,signature,status:'PERSISTED_LOCAL_NOT_DELIVERED',expectedState:'Unique authorized conversation binding followed by exact-turn verification',observedState:inspection.status,attempts:inspection.attempts,bindings:inspection.bindings,runtime:{node:process.version,platform:process.platform,arch:process.arch,implementation:'rcc.recovery-incidents.v1'},rootCause:{status:'UNVERIFIED',confirmed:null,hypothesis:null},regressionStatus:'NOT_ESTABLISHED_BY_RUNTIME_DIAGNOSTIC',capabilities:['READ_ONLY_LOOPBACK_DISCOVERY'],forbiddenActions:['RESEND_UNCERTAIN_PROMPT','EXECUTE_RETURNED_CODE','CLEAR_LIVE_LOCK','CLAIM_TASK_COMPLETE'],requestedDecision:'Return a checkpoint-bound REOBSERVE decision, or diagnose the unresolved cause. No action is implied by this packet.',delivery:{attempted:false,acknowledged:false}};
}
export function persistIncident(root,packet){
 if(!packet||packet.schema!=='rcc.recovery.escalation.v1')throw Error('incident.packet_required');
 const file=resolve(paths(root,packet.incidentId),'incident.json');const created=commit(file,packet);const saved=read(file);
 if(saved.caseId!==packet.caseId||saved.checkpointHash!==packet.checkpointHash||saved.signature!==packet.signature)throw Error('incident.identity_conflict');
 const observation={observedAt:packet.observedAt,attempts:packet.attempts,bindings:packet.bindings,signature:packet.signature};
 commit(resolve(paths(root,packet.incidentId),'observations',stateHash(observation)+'.json'),observation);
 return {created,file,incident:saved};
}
export function inspectIncident(root,incidentId){const r=read(resolve(paths(root,incidentId),'incident.json'));if(r.schema!=='rcc.recovery.escalation.v1'||r.incidentId!==incidentId)throw Error('incident.identity_mismatch');return r;}
function ownerDead(pid){if(!Number.isInteger(pid)||pid<1)return false;try{process.kill(pid,0);return false}catch(e){return e.code==='ESRCH'}}
export async function resumeObservation(root,{incidentId,decision,loadState,inspect=inspectRecovery,port=9222,now=Date.now()}={}){
 const start=performance.now(),operationNow=()=>now+(performance.now()-start);
 const incident=inspectIncident(root,incidentId);
 if(incident.endpoint&&incident.endpoint!=='127.0.0.1:'+port)throw Error('incident.endpoint_changed');
 if(Object.keys(decision?.action||{}).some(k=>!['kind','parameters'].includes(k)))throw Error('incident.decision_not_allowed');
 if(decision?.schema!=='rcc.recovery.decision.v1'||decision.incidentId!==incidentId||decision.checkpointHash!==incident.checkpointHash||decision.decision!=='REOBSERVE'||decision.action?.kind!=='RECONNECT_READ_ONLY'||!decision.action.parameters||typeof decision.action.parameters!=='object'||Array.isArray(decision.action.parameters)||Object.keys(decision.action.parameters).length)throw Error('incident.decision_not_allowed');
 const decisionId=id(decision.decisionId);const expiry=Date.parse(decision.expiresAt);if(!Number.isFinite(expiry)||expiry<=now)throw Error('incident.decision_expired');
 if(expiry-now>RECOVERY_POLICY.decisionMaxTtlMs)throw Error('incident.decision_ttl_exceeded');
 const state=await loadState();const current=digest(JSON.stringify(state));if(current!==incident.checkpointHash)throw Error('incident.checkpoint_changed');
 const dir=resolve(paths(root,incidentId),'decisions',decisionId);const decisionFile=resolve(dir,'decision.json');
 commit(decisionFile,decision);if(stateHash(read(decisionFile))!==stateHash(decision))throw Error('incident.decision_id_conflict');
 for(let attempt=1;attempt<=3;attempt++){
  const claimPath=resolve(dir,attempt+'.claim.json'),resultPath=resolve(dir,attempt+'.result.json');
  if(existsSync(resultPath))return {...read(resultPath),replayed:true};
  const claim={attempt,pid:process.pid,nonce:randomUUID(),at:new Date().toISOString(),action:'READ_ONLY_DISCOVERY'};
  if(existsSync(claimPath)){const owner=read(claimPath);if(!ownerDead(owner.pid))return {status:'OBSERVATION_RUNNING_OR_OWNER_UNKNOWN',attempt,sendAllowed:false};continue;}
  const ticket=claimObservationBudget(root,incidentId,decisionId,{now:operationNow()});
  if(ticket.status!=='CLAIMED')return {status:ticket.status,incidentId,sendAllowed:false};
  if(!commit(claimPath,claim)){const result={status:'OBSERVATION_NOT_RUN_DECISION_CLAIM_CONFLICT',incidentId,sendAllowed:false};commit(ticket.resultFile,result);return result;}
  // Recheck immediately before observation; this API has no capability to send or mutate external state.
  let result;try{const fresh=await loadState();if(digest(JSON.stringify(fresh))!==incident.checkpointHash)throw Error('incident.checkpoint_changed');const budget=ensureRecoveryBudget(root,incidentId,{now:operationNow()});if(Date.parse(decision.expiresAt)<=operationNow())throw Error('incident.decision_expired');const inspection=await boundedObservation(opts=>inspect(fresh,{port,timeoutMs:Math.min(3000,opts.timeoutMs),signal:opts.signal}),{timeoutMs:Math.min(budget.remainingMs,expiry-operationNow())});ensureRecoveryBudget(root,incidentId,{now:operationNow()});if(expiry<=operationNow())throw Error('incident.decision_expired');result={status:'OBSERVATION_RETURNED_NOT_TASK_COMPLETION',attempt,incidentAttempt:ticket.attempt,incidentId,checkpointHash:incident.checkpointHash,inspection,sendAllowed:false};}
  catch(e){result={status:'OBSERVATION_FAILED',attempt,incidentId,errorCode:e.errorCode||e.name,message:String(e.message).slice(0,250),sendAllowed:false};}
  commit(ticket.resultFile,result);commit(resultPath,result);return result;
 }
 return {status:'OBSERVATION_RESTART_BUDGET_EXHAUSTED',incidentId,sendAllowed:false};
}
