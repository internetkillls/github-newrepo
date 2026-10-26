import {conversationMessageNodes} from '../runtime/chatgpt-pro-line/src/message-nodes.mjs';
/** Independent read-only response re-observation. It never submits, adopts a binding or advances a queue. */
import {createHash} from 'node:crypto';
import {evaluate,sleep} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
import {CompletionEvidence} from '../runtime/chatgpt-pro-line/src/completion-evidence.mjs';
import {conversationId} from './recovery-inspect.mjs';
import {sameConversationUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
import {reviewPolicy,boundedObservation} from './control-policy.mjs';
const sha=text=>createHash('sha256').update(String(text)).digest('hex');
export async function sampleBoundTurn(cdp,userOrdinal,options={}){
 if(!Number.isInteger(userOrdinal)||userOrdinal<0)throw Error('witness.invalid_user_ordinal');
 const value=await evaluate(cdp,`(() => {
  const visible=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'};
  const role=e=>e.getAttribute('data-message-author-role')||(e.hasAttribute('data-user-message-bubble')?'user':'assistant');
  const nodes=(${conversationMessageNodes.toString()})();
  if(nodes.length>2000)return {unsupported:true,url:location.href};
  const user=nodes[${userOrdinal}];
  if(!user||role(user)!=='user'||!visible(user))return {unsupported:true,url:location.href};
  const following=nodes.slice(${userOrdinal}+1),next=following.findIndex(e=>role(e)==='user');
  const assistants=(next<0?following:following.slice(0,next)).filter(e=>role(e)==='assistant');
  if(assistants.some(e=>!visible(e)))return {unsupported:true,url:location.href};
  const last=assistants.at(-1),scope=last?.closest('[data-turn-key]')||last?.closest('article');
  const labels=[...document.querySelectorAll('button')].filter(visible).map(b=>[b.innerText,b.getAttribute('aria-label'),b.getAttribute('data-testid')].filter(Boolean).join(' ').trim());
  const actions=scope?[...scope.querySelectorAll('button')].filter(visible).map(b=>[b.getAttribute('aria-label'),b.getAttribute('data-testid'),b.title].filter(Boolean).join(' ')):[];
  const userText=(user.innerText||'').trim(),assistantText=assistants.map(e=>(e.innerText||'').trim()).filter(Boolean).join('\\n\\n').trim();
  if(userText.length>2000000||assistantText.length>2000000)return {unsupported:true,url:location.href};
  const codeBlocks=assistants.flatMap(e=>[...e.querySelectorAll('pre')].filter(visible).map(p=>(p.querySelector('code')||p).innerText));
  return {url:location.href,userOrdinal:${userOrdinal},userText,assistantText,codeBlocks,hasLaterUser:next>=0,assistantCount:assistants.length,
   active:labels.some(s=>/\\bstop\\b|stop-button|stop generating|stop answering|stop streaming|interrupt response|cancel response/i.test(s)),
   terminal:actions.some(s=>/copy.turn|copy response|regenerate response|thumbs.up|thumbs.down/i.test(s)),
   assistantAnchor:last?.getAttribute('data-message-id')||last?.getAttribute('data-chatgpt-search-message-ids')||scope?.getAttribute('data-turn-key')||null};
 })()`,options);
 return value;
}
export async function reviewAnchoredResponse(cdp,expected,{timeoutMs=20000,stableMs=4000,pollMs=1000,sampleTimeoutMs=2000,clock=()=>performance.now(),wait=sleep,sample=sampleBoundTurn,includeDeliveryBlocks=false}={}){
 if(!conversationId(expected?.conversationUrl)||!Number.isInteger(expected.userOrdinal)||expected.userOrdinal<0||![expected.userTextSha256,expected.assistantTextSha256].every(h=>/^[a-f0-9]{64}$/.test(h||'')))throw Error('witness.pinned_expectation_required');
 const policy=reviewPolicy({timeoutMs,stableMs,pollMs,sampleTimeoutMs});
 const guard=new CompletionEvidence(policy),start=clock(),samples=[];let anchor=null;
 const remaining=()=>timeoutMs-(clock()-start);
 const read=async()=>{const s=await boundedObservation(opts=>sample(cdp,expected.userOrdinal,opts),{timeoutMs:Math.min(sampleTimeoutMs,remaining())});if(remaining()<=0)throw Error('witness.observation_timeout');return s};
 const unverified=reason=>({status:'RESPONSE_UNVERIFIED',reason,samples,policy,sendAllowed:false});
 while(clock()-start<timeoutMs){
  let s;try{s=await read()}catch(e){if(e.message==='witness.observation_timeout'||e.errorCode==='browser.cdp_command_timeout'||e.errorCode==='browser.cdp_aborted')return unverified('observation_budget_exhausted');throw e}const at=clock();
  if(s.unsupported||!sameConversationUrl(s.url,expected.conversationUrl)||s.userOrdinal!==expected.userOrdinal||sha(s.userText)!==expected.userTextSha256||s.hasLaterUser)return {status:'RESPONSE_UNVERIFIED',reason:'identity_or_turn_changed',samples,policy,sendAllowed:false};
  if(!s.assistantAnchor||!s.assistantCount)return unverified('assistant_anchor_missing');
  if(anchor&&s.assistantAnchor!==anchor)return unverified('assistant_anchor_changed');
  anchor=s.assistantAnchor;
  const responseHash=sha(s.assistantText),bound=responseHash===expected.assistantTextSha256;
  const evidence=guard.observe({at,text:s.assistantText,active:s.active,terminal:s.terminal,bound,placeholder:!s.assistantText.trim()});
  samples.push({at,userOrdinal:s.userOrdinal,userTextSha256:sha(s.userText),assistantTextSha256:responseHash,assistantAnchor:s.assistantAnchor,active:s.active,terminal:s.terminal,bound});
  if(samples.length>policy.maxSamples)return unverified('sample_budget_exhausted');
  if(evidence.completed){
   // An additional independent read must agree after the terminal detector has qualified.
   let final;try{final=await read()}catch(e){if(e.message==='witness.observation_timeout'||e.errorCode==='browser.cdp_command_timeout'||e.errorCode==='browser.cdp_aborted')return unverified('final_readback_budget_exhausted');throw e}
   if(!final.unsupported&&sameConversationUrl(final.url,expected.conversationUrl)&&final.userOrdinal===expected.userOrdinal&&sha(final.userText)===expected.userTextSha256&&!final.hasLaterUser&&final.assistantAnchor===anchor&&sha(final.assistantText)===expected.assistantTextSha256&&final.active===false&&final.terminal===true)
    return {status:'RESPONSE_UI_WITNESSED',scope:'Exact response UI and bytes only; required output files and task correctness not evaluated',conversationUrl:expected.conversationUrl,userOrdinal:expected.userOrdinal,userTextSha256:expected.userTextSha256,assistantTextSha256:expected.assistantTextSha256,assistantAnchor:anchor,evidence,samples,policy,sendAllowed:false,...(includeDeliveryBlocks?{deliveryBlocks:final.codeBlocks||[]}: {})};
   return unverified('final_readback_changed');
  }
  await wait(Math.max(0,Math.min(pollMs,remaining())));
 }
 return unverified('completion_budget_exhausted');
}
