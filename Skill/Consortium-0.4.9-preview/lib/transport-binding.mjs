import {resolve} from 'node:path';import {conversationId} from './recovery-inspect.mjs';
import {parseChatGptUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
export function bindingFromReceipt(receipt,{token,worker,promptHash,root}){
 if(!/^[0-9a-f-]{36}$/i.test(token||'')||receipt?.rccInvocationToken!==token)throw Error('transport.receipt_invocation_mismatch');
 const pathKey=p=>process.platform==='win32'?resolve(p).toLowerCase():resolve(p);
 if(receipt.ok!==true||receipt.room?.alias!==worker.alias||!receipt.project?.repoRoot||pathKey(receipt.project.repoRoot)!==pathKey(root)||receipt.input?.promptSha256!==promptHash)throw Error('transport.receipt_identity_mismatch');
 const url=receipt.response?.conversationUrl,targetId=receipt.sessionTarget?.targetId??receipt.sessionTarget?.id;
 if(receipt.sessionTarget?.targetId&&receipt.sessionTarget?.id&&receipt.sessionTarget.targetId!==receipt.sessionTarget.id)throw Error('transport.conflicting_target_fields');
 if(!conversationId(url)||parseChatGptUrl(url)?.legacy||typeof targetId!=='string'||!targetId)throw Error('transport.committed_conversation_missing');
 if(worker.targetId&&targetId!==worker.targetId)throw Error('transport.target_changed_requires_reconciliation');
 return {conversationUrl:url,conversationId:conversationId(url),targetId,receiptStatus:'VERIFIED_TRANSPORT_BINDING_NOT_TASK_COMPLETION'};
}
