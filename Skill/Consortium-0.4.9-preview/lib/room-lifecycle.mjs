import {readFileSync,openSync,writeFileSync,closeSync,unlinkSync} from 'node:fs';
import {resolve} from 'node:path';
import {randomUUID} from 'node:crypto';
import {inspectQueue,queuePaths} from './queue-manager.mjs';
import {assertExecution} from './execution-contract.mjs';
import {parseChatGptUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
import {listTargets} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
import {acquireChatGptOperation} from '../runtime/chatgpt-pro-line/src/chatgpt-operation.mjs';
import {writeJsonAtomic} from '../runtime/chatgpt-pro-line/src/atomic-json.mjs';

export function assertUnusedRoom(state,queue,worker,room,approval) {
  if(approval!==`PROVISION-${state.caseId}-${worker.role}`)throw Error('room.explicit_provision_approval_required');
  if(worker.provisionAttempt && worker.provisionAttempt.status!=='BOUND')throw Error('room.prior_provision_claim_requires_reconciliation');
  const jobs=queue.jobs.filter(j=>j.role===worker.role);
  if(!jobs.length||!jobs.some(j=>j.status==='PENDING')||jobs.some(j=>!['PENDING','NOT_SENT_CONFIRMED'].includes(j.status)||j.status==='PENDING'&&j.attempts!==0))throw Error('room.role_send_history_not_proven_unused');
  const key=p=>process.platform==='win32'?resolve(p).toLowerCase():resolve(p);
  if(!room||(room.alias||room.name)!==worker.alias||(state.repoRoot&&(!room.repoRoot||key(room.repoRoot)!==key(state.repoRoot)))||room.callCount>0||room.lastRunId||room.recentRuns?.length)throw Error('room.existing_role_history_requires_reconciliation');
  for(const url of [worker.conversationUrl,room.activeConversationUrl,room.conversationUrl,room.url]) {
    if(url&&parseChatGptUrl(url)?.kind!=='uncommitted')throw Error('room.committed_or_unsupported_history_never_replace');
  }
}

export async function provisionUnusedRoom(root,id,{role,approval,pluginRoot,port=9222}={}) {
  const {newChatGptSession,sessionRegistryPath}=await import('../runtime/chatgpt-pro-line/src/chatgpt-sessions.mjs');
  const paths=queuePaths(root,id),file=resolve(paths.dir,'state.json');
  const state=JSON.parse(readFileSync(file,'utf8'));
  if(state.caseId!==id)throw Error('room.case_identity_mismatch');
  const worker=state.workers.find(w=>w.role===role);if(!worker)throw Error('room.role_not_found');
  const op=await acquireChatGptOperation({name:'rcc-explicit-unused-room-provision',alias:worker.alias,requiresBrowser:true,lockTimeoutMs:10000});
  let fd;
  try {
    // Never clear an existing queue/runner lock. This claim also excludes new dispatches.
    fd=openSync(paths.lock,'wx');writeFileSync(fd,JSON.stringify({pid:process.pid,createdAt:new Date().toISOString(),nonce:randomUUID(),purpose:'explicit unused-room provision'}));
    const queue=inspectQueue(root,id),registry=JSON.parse(readFileSync(sessionRegistryPath,'utf8')),room=registry.rooms?.[worker.alias];
    assertUnusedRoom({...state,repoRoot:root},queue,worker,room,approval);
    const pending=queue.jobs.find(j=>j.role===role&&j.status==='PENDING');
    assertExecution(root,id,{pluginRoot,role,prompt:readFileSync(pending.prompt.path,'utf8')});
    const targets=await listTargets(port),old=targets.find(t=>t.id===worker.targetId);
    if(old) {
      if(parseChatGptUrl(old.url)?.kind!=='uncommitted')throw Error('room.original_target_may_have_sent_history');
      return {ok:true,status:'EXISTING_UNCOMMITTED_TARGET_RETAINED',targetId:old.id,created:false,sendAllowed:false,next:'Normal sender must verify empty composer and exact room; no prompt sent here.'};
    }
    worker.provisionAttempt={status:'OPENING',nonce:randomUUID(),pid:process.pid,claimedAt:new Date().toISOString(),previousTargetId:worker.targetId};
    writeJsonAtomic(file,state); // durable claim BEFORE an external new-tab side effect
    try {
      const target=await newChatGptSession(port,{name:worker.alias,bind:true});
      if(parseChatGptUrl(target.url)?.kind!=='uncommitted')throw Error('room.new_target_not_blank');
      const fresh=JSON.parse(readFileSync(sessionRegistryPath,'utf8')).rooms[worker.alias];
      Object.assign(worker,{targetId:target.id,conversationUrl:target.url,room:fresh,status:'BOUND',verifiedAt:new Date().toISOString()});
      worker.provisionAttempt.status='BOUND';writeJsonAtomic(file,state);
      return {ok:true,status:'UNUSED_ROLE_REPROVISIONED_NOT_SENT',alias:worker.alias,targetId:target.id,created:true,sendAllowed:false,next:'Send existing pending task once through queue; first verified prompt persists committed conversation identity.'};
    } catch(e) {worker.provisionAttempt.status='UNCERTAIN';worker.provisionAttempt.error=String(e.message);writeJsonAtomic(file,state);throw e;}
  } finally {if(fd!==undefined){closeSync(fd);unlinkSync(paths.lock)}await op.release();}
}
