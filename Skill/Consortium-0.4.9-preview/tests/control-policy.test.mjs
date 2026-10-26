import test from 'node:test';import assert from 'node:assert/strict';import {createHash} from 'node:crypto';
import {reviewPolicy,boundedObservation} from '../lib/control-policy.mjs';import {reviewAnchoredResponse,sampleBoundTurn} from '../lib/live-completion-review.mjs';
import {CdpSession,evaluate} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
const sha=s=>createHash('sha256').update(s).digest('hex');
const expected={conversationUrl:'https://chatgpt.com/c/one',userOrdinal:0,userTextSha256:sha('prompt'),assistantTextSha256:sha('answer')};
const good={url:expected.conversationUrl,userOrdinal:0,userText:'prompt',assistantText:'answer',assistantCount:1,assistantAnchor:'anchor',hasLaterUser:false,active:false,terminal:true};
test('impossible and malformed budgets are rejected before sampling',async()=>{
 let reads=0;for(const options of [{timeoutMs:1000,stableMs:4000},{pollMs:100.5},{stableMs:Infinity},{sampleTimeoutMs:0}])await assert.rejects(reviewAnchoredResponse(null,expected,{...options,sample:async()=>{reads++;return good}}));assert.equal(reads,0);
 const a=reviewPolicy(),b=reviewPolicy();assert.equal(a.sha256,b.sha256);assert.notEqual(reviewPolicy({pollMs:1100}).sha256,a.sha256);assert.throws(()=>reviewPolicy({surprise:true}),/unknown_policy_parameter/);
});
test('accepted fast poll configuration reaches time budget instead of hidden hundred-sample cap',async()=>{
 let at=0;const r=await reviewAnchoredResponse(null,expected,{timeoutMs:60000,pollMs:100,clock:()=>at,wait:async ms=>{at+=ms},sample:async()=>({...good,active:true})});assert.equal(r.reason,'completion_budget_exhausted');assert.equal(r.samples.length,600);assert.equal(r.policy.maxSamples,601);
});
test('late sampling and late final readback cannot produce a witness',async()=>{
 for(const lateFinal of [false,true]){let at=0,calls=0;const r=await reviewAnchoredResponse(null,expected,{timeoutMs:10000,stableMs:1000,clock:()=>at,wait:async ms=>{at+=ms},sample:async()=>{if(!lateFinal||++calls===6)at+=10001;return good}});assert.equal(r.status,'RESPONSE_UNVERIFIED');assert.match(r.reason,/budget_exhausted/)}
});
test('a hung observer is bounded and receives cancellation without another read or send',async()=>{
 let reads=0,signal;const r=await reviewAnchoredResponse(null,expected,{stableMs:1000,timeoutMs:10000,sampleTimeoutMs:25,sample:async(_c,_o,opts)=>{reads++;signal=opts.signal;return new Promise(()=>{})}});assert.equal(r.reason,'observation_budget_exhausted');assert.equal(reads,1);assert(signal.aborted);
});
test('DOM evaluation forwards the per-read deadline and cancels real CDP pending bookkeeping',async()=>{
 class Socket extends EventTarget{sent=[];send(x){this.sent.push(x)}close(){}}
 const socket=new Socket(),cdp=new CdpSession(socket);
 try{await assert.rejects(boundedObservation(opts=>sampleBoundTurn(cdp,0,opts),{timeoutMs:25}));assert.equal(cdp.pending.size,0);assert.equal(socket.sent.length,1)}finally{await cdp.close()}
 let captured;await evaluate({send:async(_m,_p,opts)=>{captured=opts;return {result:{value:true}}}},'1',{timeoutMs:77});assert.equal(captured.timeoutMs,77);
});
