import test from 'node:test';import assert from 'node:assert/strict';
import {bindingFromReceipt} from '../lib/transport-binding.mjs';
import {sessionTargetReceipt} from '../runtime/chatgpt-pro-line/src/transport-receipt.mjs';
const token='11111111-1111-4111-8111-111111111111',root=process.cwd(),worker={role:'critic',alias:'rcc-case-critic',targetId:'target-one'},promptHash='a'.repeat(64);
const receipt=()=>({rccInvocationToken:token,ok:true,room:{alias:worker.alias},project:{repoRoot:root},input:{promptSha256:promptHash},response:{conversationUrl:'https://chatgpt.com/c/committed'},sessionTarget:{id:'target-one'}});
test('committed conversation is recovered from a fresh invocation-scoped receipt',()=>{const r=bindingFromReceipt(receipt(),{token,worker,promptHash,root});assert.equal(r.conversationId,'committed');assert.match(r.receiptStatus,/NOT_TASK_COMPLETION/);});
test('stale receipt and wrong worker, source or project cannot rewrite a binding',()=>{for(const patch of [{rccInvocationToken:'old'},{ok:false},{room:{alias:'other'}},{project:{repoRoot:root+'/other'}},{input:{promptSha256:'b'.repeat(64)}}])assert.throws(()=>bindingFromReceipt({...receipt(),...patch},{token,worker,promptHash,root}));});
test('uncommitted URL and changed target require reconciliation',()=>{for(const patch of [{response:{conversationUrl:'https://chatgpt.com/'}},{sessionTarget:{id:'new-target'}}])assert.throws(()=>bindingFromReceipt({...receipt(),...patch},{token,worker,promptHash,root}));});

test('actual producer targetId field is accepted and conflicting aliases are rejected',()=>{
 const actual={...receipt(),sessionTarget:sessionTargetReceipt({id:'target-one',url:'https://chatgpt.com/c/committed'})};
 assert.equal(bindingFromReceipt(actual,{token,worker,promptHash,root}).targetId,'target-one');
 assert.throws(()=>bindingFromReceipt({...actual,sessionTarget:{targetId:'target-one',id:'other'}},{token,worker,promptHash,root}),/conflicting_target_fields/);
 assert.throws(()=>bindingFromReceipt({...actual,response:{conversationUrl:'https://chat.openai.com/c/committed'}},{token,worker,promptHash,root}),/committed_conversation_missing/);
});
