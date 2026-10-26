import {createHash} from 'node:crypto';
import {listTargets,sleep} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
import {conversationIdFromUrl,sameConversationUrl} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
export function conversationId(value){return conversationIdFromUrl(value)||null}
export function reconcileBindings(state,targets){
 const bindings=state.workers||state.jobs;
 if(!Array.isArray(bindings))throw Error('recovery.binding_array_required');
 return bindings.map(w=>{
  const url=w.conversationUrl||w.activeConversationUrl||w.url,id=conversationId(url);
  const pages=targets.filter(t=>t.type==='page'&&id&&sameConversationUrl(t.url,url));
  const exact=pages.find(t=>t.id===w.targetId);
  const status=!id?'MISSING_CONVERSATION_REFERENCE':pages.length>1?'AMBIGUOUS':exact?'MATCHED_HINT_VERIFIED':pages.length===1?'UNIQUE_REBIND_CANDIDATE':'CONVERSATION_NOT_OPEN';
  return {role:w.role||w.alias||null,jobId:w.id||null,conversationId:id,savedTargetId:w.targetId||null,status,candidates:pages.map(t=>t.id),nextAction:status==='MATCHED_HINT_VERIFIED'?'OBSERVE_EXACT_TURN':status==='UNIQUE_REBIND_CANDIDATE'?'VERIFY_EXACT_TURN_BEFORE_REBIND':'RECONCILIATION_REQUIRED',sendAllowed:false};
 });
}
export async function inspectRecovery(state,{port=9222,attempts=3,timeoutMs=3000,discover=listTargets,wait=sleep}={}){
 if(!Number.isInteger(port)||port<1||port>65535||!Number.isInteger(attempts)||attempts<1||attempts>3)throw Error('recovery.invalid_budget_or_port');
 const observations=[];let targets;
 for(let i=0;i<attempts;i++){try{targets=await discover(port,{timeoutMs});observations.push({attempt:i+1,ok:true});break}catch(e){observations.push({attempt:i+1,ok:false,errorCode:e.errorCode||e.name,message:String(e.message).slice(0,180)});if(i+1<attempts)await wait(250*2**i);}}
 return {schema:'rcc.recovery.inspection.v1',observedAt:new Date().toISOString(),stateHash:createHash('sha256').update(JSON.stringify(state)).digest('hex'),endpoint:'127.0.0.1:'+port,status:targets?'OBSERVED':'ENDPOINT_UNAVAILABLE',attempts:observations,bindings:targets?reconcileBindings(state,targets):[],mutatedExternalState:false,sendAllowed:false,limitations:['Target metadata is not proof of prompt delivery or completion','No queue or binding was changed','Unavailable endpoint is not proof of Chrome crash']};
}
