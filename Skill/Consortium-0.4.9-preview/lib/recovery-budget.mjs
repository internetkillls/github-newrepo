import {existsSync} from 'node:fs';import {resolve} from 'node:path';import {randomUUID} from 'node:crypto';
import {stateHash} from './queue-journal.mjs';import {commitIncidentRecord,readIncidentRecord,incidentDirectory,inspectIncident} from './recovery-incidents.mjs';
export const RECOVERY_POLICY=Object.freeze({schema:'rcc.recovery-policy.v1',incidentElapsedMs:300000,observationAttempts:3,extraVerificationAttempts:1,verificationAdmissionMs:45000,decisionMaxTtlMs:300000,deliveryTimeoutMs:180000,deliveryAttempts:1,routeMaxTtlMs:86400000,maxReplyBytes:65536});
export const RECOVERY_POLICY_HASH=stateHash(RECOVERY_POLICY);
export function ensureRecoveryBudget(root,incidentId,{now=Date.now()}={}){
 inspectIncident(root,incidentId);if(!Number.isFinite(now))throw Error('recovery.invalid_clock');now=Math.floor(now);
 const file=resolve(incidentDirectory(root,incidentId),'budget.json');
 commitIncidentRecord(file,{schema:'rcc.recovery.budget.v1',incidentId,startedAtMs:now,deadlineMs:now+RECOVERY_POLICY.incidentElapsedMs,policy:RECOVERY_POLICY,policyHash:RECOVERY_POLICY_HASH});
 const b=readIncidentRecord(file);
 if(b.schema!=='rcc.recovery.budget.v1'||b.incidentId!==incidentId||b.policyHash!==RECOVERY_POLICY_HASH||stateHash(b.policy)!==b.policyHash||!Number.isFinite(b.startedAtMs)||b.deadlineMs!==b.startedAtMs+b.policy.incidentElapsedMs)throw Error('recovery.budget_conflict');
 if(now<b.startedAtMs)throw Error('recovery.clock_regressed');
 if(now>=b.deadlineMs)throw Error('recovery.incident_elapsed_budget_exhausted');
 return {...b,remainingMs:b.deadlineMs-now};
}
function dead(pid){if(!Number.isInteger(pid)||pid<1)return false;try{process.kill(pid,0);return false}catch(e){return e.code==='ESRCH'}}
export function claimObservationBudget(root,incidentId,decisionId,{now=Date.now()}={}){
 const budget=ensureRecoveryBudget(root,incidentId,{now}),dir=resolve(incidentDirectory(root,incidentId),'budget-observations');
 for(let n=1;n<=budget.policy.observationAttempts;n++){
  const file=resolve(dir,n+'.claim.json'),resultFile=resolve(dir,n+'.result.json');
  if(existsSync(file)){const prior=readIncidentRecord(file);if(!existsSync(resultFile)&&!dead(prior.pid))return {status:'OBSERVATION_RUNNING_OR_OWNER_UNKNOWN'};continue}
  const claim={schema:'rcc.recovery.observation-claim.v1',incidentId,decisionId,attempt:n,pid:process.pid,nonce:randomUUID(),atMs:now};
  if(!commitIncidentRecord(file,claim))return {status:'OBSERVATION_RUNNING_OR_OWNER_UNKNOWN'};
  return {status:'CLAIMED',attempt:n,resultFile,budget};
 }
 return {status:'OBSERVATION_INCIDENT_BUDGET_EXHAUSTED'};
}
