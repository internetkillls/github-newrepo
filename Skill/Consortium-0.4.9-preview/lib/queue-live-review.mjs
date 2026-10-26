import {readFileSync,realpathSync} from 'node:fs';import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import {CdpSession,listTargets} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
import {acquireChatGptOperation} from '../runtime/chatgpt-pro-line/src/chatgpt-operation.mjs';
import {conversationId} from './recovery-inspect.mjs';import {reviewAnchoredResponse} from './live-completion-review.mjs';
import {sameConversationUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex');
const key=p=>process.platform==='win32'?realpathSync(p).toLowerCase():realpathSync(p);
function json(path){const bytes=readFileSync(path);if(bytes.length>4*1024*1024)throw Error('review.record_too_large');return {bytes,value:JSON.parse(bytes.toString('utf8'))};}
export async function observeQueuedResponse(root,job,{port=9222}={}){
 if(!Number.isInteger(port)||port<1||port>65535)throw Error('review.invalid_port');
 const dir=resolve(root,'.devspace','rcc',job.caseId),state=json(resolve(dir,'state.json')).value;
 if(state.caseId!==job.caseId)throw Error('review.case_identity_mismatch');
 const workers=(state.workers||[]).filter(w=>w.role===job.role);if(workers.length!==1)throw Error('review.worker_not_unique');const worker=workers[0];
 if(worker.lastReceiptStatus!=='VERIFIED_TRANSPORT_BINDING_NOT_TASK_COMPLETION')throw Error('review.fresh_transport_binding_required');
 const source=json(resolve(dir,'outputs',job.role+'-transport.json')),r=source.value;
 if(hash(source.bytes)!==worker.lastTransportReceiptSha256||r.ok!==true||r.queueBinding?.jobId!==job.id||r.queueBinding?.payloadHash!==job.payloadHash||r.room?.alias!==worker.alias||!r.project?.repoRoot||key(r.project.repoRoot)!==key(root)||r.input?.promptSha256!==job.prompt.sha256)throw Error('review.transport_identity_mismatch');
 const sent=r.messageAnchor?.sentUserMessage,url=r.response?.conversationUrl;
 if(!['exact','exact_with_attachment'].includes(sent?.promptEchoVerification)||r.messageAnchor?.responseBoundToSentPrompt!==true||!conversationId(url)||!sameConversationUrl(worker.conversationUrl,url))throw Error('review.exact_prompt_anchor_required');
 // The transport's response text is cleaned for display. Pin the unmodified anchored run hash instead.
 if(r.messageAnchor.assistantRun?.afterUserOrdinal!==sent.ordinal)throw Error('review.raw_assistant_run_required');
 const expected={conversationUrl:url,userOrdinal:sent.ordinal,userTextSha256:sent.textSha256,assistantTextSha256:r.messageAnchor.assistantRun.textSha256};
 const op=await acquireChatGptOperation({name:'rcc-auto-response-review',project:r.project,alias:worker.alias,requiresBrowser:true,lockTimeoutMs:10000});let cdp;
 try{
  const targets=(await listTargets(port)).filter(t=>t.type==='page'&&sameConversationUrl(t.url,url));
  if(targets.length!==1)throw Error('review.target_missing_or_ambiguous');
  cdp=await CdpSession.open(targets[0].webSocketDebuggerUrl);
  const result=await reviewAnchoredResponse(cdp,expected,{includeDeliveryBlocks:true});
  if(hash(readFileSync(resolve(dir,'outputs',job.role+'-transport.json')))!==hash(source.bytes))throw Error('review.transport_changed_during_observation');
  return {jobId:job.id,payloadHash:job.payloadHash,...result};
 }finally{await cdp?.close();await op.release();}
}
