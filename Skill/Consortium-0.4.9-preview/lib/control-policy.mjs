import {createHash} from 'node:crypto';
export const REVIEW_DEFAULTS=Object.freeze({timeoutMs:20000,stableMs:4000,pollMs:1000,sampleTimeoutMs:2000,minTerminalPolls:3,minPollSpanMs:1000});
export function reviewPolicy(options={}){
 const p={...REVIEW_DEFAULTS,...options};
 const bounds={timeoutMs:[1000,60000],stableMs:[1000,30000],pollMs:[100,5000],sampleTimeoutMs:[10,5000],minTerminalPolls:[3,10],minPollSpanMs:[1000,5000]};
 if(Object.keys(p).some(k=>!Object.hasOwn(bounds,k)))throw Error('witness.unknown_policy_parameter');
 for(const [key,[lo,hi]] of Object.entries(bounds))if(!Number.isInteger(p[key])||p[key]<lo||p[key]>hi)throw Error('witness.invalid_budget: '+key);
 const minimumMs=2*p.stableMs+(p.minTerminalPolls-1)*p.pollMs+p.minPollSpanMs+2*p.sampleTimeoutMs;
 if(p.timeoutMs<minimumMs)throw Error('witness.infeasible_budget');
 const body={schema:'rcc.review-policy.v1',...p,maxSamples:Math.ceil(p.timeoutMs/p.pollMs)+1};
 return Object.freeze({...body,sha256:createHash('sha256').update(JSON.stringify(body)).digest('hex')});
}
export const DEFAULT_REVIEW_POLICY=reviewPolicy();

// Every bounded operation observes its result before the parent deadline and cancels children.
export async function boundedObservation(read,{timeoutMs}={}){
 if(!Number.isFinite(timeoutMs)||timeoutMs<=0)throw Error('witness.observation_timeout');
 const controller=new AbortController();let timer;
 try{return await Promise.race([
  Promise.resolve().then(()=>read({timeoutMs:Math.max(1,Math.floor(timeoutMs)),signal:controller.signal})),
  new Promise((_,reject)=>{timer=setTimeout(()=>{controller.abort();reject(Error('witness.observation_timeout'))},Math.ceil(timeoutMs))}),
 ])}finally{clearTimeout(timer)}
}
