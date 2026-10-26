import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {sameConversationUrl,conversationIdFromUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
const sha=b=>createHash('sha256').update(b).digest('hex');
export function controllerReuseProof({receiptPath,receiptSha256,worker,root,bundlePath}) {
  const raw=readFileSync(receiptPath);
  if(raw.length>4*1024*1024||sha(raw)!==receiptSha256)throw Error('controllers.reuse_receipt_changed');
  const r=JSON.parse(raw),bundle=readFileSync(bundlePath),bundleSha256=sha(bundle);
  const key=p=>process.platform==='win32'?resolve(p).toLowerCase():resolve(p);
  if(r.ok!==true||r.room?.alias!==worker.alias||!r.project?.repoRoot||key(r.project.repoRoot)!==key(root)
    ||!conversationIdFromUrl(worker.conversationUrl)||!sameConversationUrl(r.response?.conversationUrl||'',worker.conversationUrl)
    ||!['exact','exact_with_attachment'].includes(r.messageAnchor?.sentUserMessage?.promptEchoVerification)
    ||r.messageAnchor?.responseBoundToSentPrompt!==true||r.upload?.ok!==true
    ||!r.upload.files?.some(f=>f.bytes===bundle.length&&f.sha256===bundleSha256))throw Error('controllers.same_room_delivered_source_proof_required');
  return {schema:'rcc.controller-reuse.v1',receiptPath:resolve(receiptPath),receiptSha256,alias:worker.alias,conversationUrl:worker.conversationUrl,bundleSha256,bundleBytes:bundle.length,scope:'Same role, exact committed conversation and previously delivered unchanged instructions; no new upload or tool activation claimed'};
}
