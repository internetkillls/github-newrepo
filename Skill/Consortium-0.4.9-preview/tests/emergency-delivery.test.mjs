import test from 'node:test';import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';import {fileURLToPath} from 'node:url';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,existsSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';import {createHash} from 'node:crypto';import {spawn} from 'node:child_process';import {once} from 'node:events';
import {failurePacket,persistIncident,resumeObservation} from '../lib/recovery-incidents.mjs';
import {configureEmergencyRoute,deliverEmergency,recoverEmergency,emergencyDeliveryStatus} from '../lib/emergency-delivery.mjs';
import {ensureRecoveryBudget} from '../lib/recovery-budget.mjs';
import {prepareHandoff,armHandoff,runnerTick,status as handoffStatus} from '../lib/deferred-handoff.mjs';
import {enqueue,inspectQueue,dispatchOne,verifyQueuedJob} from '../lib/queue-manager.mjs';
const sha=x=>createHash('sha256').update(x).digest('hex'),session='11111111-1111-4111-8111-111111111111';
const fakeCli=`import {readFileSync,writeFileSync,appendFileSync} from 'node:fs';
 if(process.argv.includes('--version')){console.log('codex-cli fixture');process.exit(0)}
 if(process.argv.includes('--help')){console.log('codex exec resume --json --output-schema --output-last-message');process.exit(0)}
 let input='';for await(const chunk of process.stdin)input+=chunk;
 const {request:r,packet:p}=JSON.parse(input.split('\\n').at(-1)),mode=JSON.parse(readFileSync('mode.json'));
 if(mode.kind==='writer-conflict'){console.error('failed to initialize thread persistence: thread-store conflict: thread '+r.sessionId+' already has an active writer');process.exit(1)}
 appendFileSync('sends.txt','sent\\n');if(['slow','slow-no-ack'].includes(mode.kind))await new Promise(resolve=>setTimeout(resolve,600));
 const decision={schema:'rcc.recovery.decision.v1',incidentId:r.incidentId,checkpointHash:r.checkpointHash,decisionId:r.decisionId,expiresAt:r.decisionExpiresAt,decision:p.jobId?'REVERIFY_JOB':'REOBSERVE',action:{kind:p.jobId?'VERIFY_RESPONSE_AND_OUTPUTS':'RECONNECT_READ_ONLY',parameters:{}}};
 if(mode.kind==='unsafe')decision.action={kind:'RUN_SHELL',parameters:{command:'forbidden'}};
 const reply={schema:'rcc.recovery.agent-reply.v1',incidentId:r.incidentId,checkpointHash:r.checkpointHash,deliveryKey:mode.kind==='wrong-key'?'wrong':r.deliveryKey,sessionId:r.sessionId,acknowledgement:'DIAGNOSTIC_RECEIVED',diagnosis:'Synthetic diagnosis; not production reasoning.',decision:mode.kind==='unresolved'||(r.diagnosticOnly&&mode.kind!=='ignore-diagnostic-only')?null:decision};
 const out=process.argv[process.argv.indexOf('--output-last-message')+1];if(!['no-ack','slow-no-ack'].includes(mode.kind))writeFileSync(out,JSON.stringify(reply));
 console.log(JSON.stringify({type:'thread.started',thread_id:mode.kind==='wrong-session'?'other':r.sessionId}));console.log(JSON.stringify({type:'turn.started'}));
 console.log(JSON.stringify({type:'item.completed',item:{type:'agent_message',text:JSON.stringify(reply)}}));if(mode.kind!=='missing-terminal')console.log(JSON.stringify({type:'turn.completed'}));
 if(mode.kind==='ack-then-delay')await new Promise(resolve=>setTimeout(resolve,1000));
 if(mode.kind==='nonzero')process.exitCode=2;
`;
async function fixture({mode='good',auto=true,configure=true,queue=false}={}){
 const root=mkdtempSync(join(tmpdir(),'rcc-emergency-')),entrypoint=join(root,'fake-codex.mjs'),state={caseId:'case',workers:[{role:'critic',conversationUrl:'https://chatgpt.com/c/one'}]};writeFileSync(entrypoint,fakeCli);writeFileSync(join(root,'mode.json'),JSON.stringify({kind:mode}));
 let packet;
 if(queue){const prompt=join(root,'prompt.md');writeFileSync(prompt,'Fixture prompt.');const job=enqueue(root,{case:'case',role:'critic',promptFile:prompt,outputContract:{schema:'rcc.output-contract.v1',mode:'response'}}).job;await dispatchOne(root,'case',()=>({code:0}));let exhausted;for(let i=0;i<3;i++)exhausted=await verifyQueuedJob(root,'case',{jobId:job.id,observe:async()=>{throw Error('offline fixture')}});packet=JSON.parse(readFileSync(exhausted.escalationFile)).body;}
 else{packet=failurePacket({caseId:'case',inspection:{schema:'rcc.recovery.inspection.v1',observedAt:new Date().toISOString(),stateHash:sha(JSON.stringify(state)),endpoint:'127.0.0.1:9222',status:'ENDPOINT_UNAVAILABLE',attempts:[],bindings:[]}});persistIncident(root,packet)}
 const config={caseId:'case',sessionId:session,executable:process.execPath,entrypoint,authorizationRef:'EXPLICIT_TEST_OPERATOR_FIXTURE',expiresAt:new Date(Date.now()+600000).toISOString(),autoReobserve:auto,allowNonGit:true};
 if(configure)await configureEmergencyRoute(root,config);
 return {root,packet,state,config,cleanup:()=>rmSync(root,{recursive:true,force:true,maxRetries:3,retryDelay:100}),sends:()=>existsSync(join(root,'sends.txt'))?readFileSync(join(root,'sends.txt'),'utf8').trim().split('\n').length:0};
}

test('explicit destination, validated ACK and typed proposal permit one observation; delivery replay never resends',async()=>{
 const f=await fixture();try{let reads=0;const options={loadState:async()=>f.state,inspect:async()=>{reads++;return {status:'OBSERVED'}}};const r=await recoverEmergency(f.root,f.packet.incidentId,options);assert.equal(r.status,'OBSERVATION_RETURNED_NOT_TASK_COMPLETION');assert.equal(f.sends(),1);assert.equal(reads,1);const next=await recoverEmergency(f.root,f.packet.incidentId,options);assert.equal(next.replayed,true);assert.equal(f.sends(),1);assert.equal(reads,1);assert.equal(emergencyDeliveryStatus(f.root,f.packet.incidentId).acknowledgement,'DIAGNOSTIC_RECEIVED');}finally{f.cleanup()}
});
for(const mode of ['no-ack','wrong-key','wrong-session','missing-terminal','nonzero'])test(mode+' cannot claim delivery or retry a possibly accepted diagnostic',async()=>{
 const f=await fixture({mode});try{const r=await deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state});assert.equal(r.status,'DELIVERY_OUTCOME_UNKNOWN_NO_RESEND');await deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state});assert.equal(f.sends(),1)}finally{f.cleanup()}
});
test('unsafe decision is rejected after ACK; it cannot execute or cause a replacement message',async()=>{
 const f=await fixture({mode:'unsafe'});try{let reads=0;const r=await recoverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state,inspect:async()=>{reads++}});assert.equal(r.status,'AGENT_ACKNOWLEDGED_DECISION_REJECTED');assert.equal(reads,0);assert.equal(f.sends(),1)}finally{f.cleanup()}
});
test('unresolved diagnosis and application-disabled route remain explicit, without observation',async()=>{
 for(const options of [{mode:'unresolved'},{auto:false}]){const f=await fixture(options);try{let reads=0;const r=await recoverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state,inspect:async()=>{reads++}});assert(['AGENT_ACKNOWLEDGED_UNRESOLVED','AGENT_ACKNOWLEDGED_LOCAL_APPLICATION_DISABLED'].includes(r.status));assert.equal(reads,0)}finally{f.cleanup()}}
});
test('missing route, changed checkpoint and changed executable produce no diagnostic send',async()=>{
 const missing=await fixture({configure:false});try{assert.equal((await deliverEmergency(missing.root,missing.packet.incidentId,{loadState:async()=>missing.state})).status,'DELIVERY_ROUTE_UNAVAILABLE');assert.equal(missing.sends(),0)}finally{missing.cleanup()}
 const f=await fixture();try{await assert.rejects(deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>({changed:true})}),/checkpoint_changed/);writeFileSync(f.config.entrypoint,fakeCli+'\n// changed');await assert.rejects(deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state}),/launcher_changed/);assert.equal(f.sends(),0)}finally{f.cleanup()}
});
test('concurrent deliverers share one durable claim',async()=>{
 const f=await fixture({mode:'slow'});try{const results=await Promise.all([deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state}),deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state})]);assert.equal(f.sends(),1);assert(results.some(r=>r.status==='AGENT_ACKNOWLEDGED_DECISION_READY'));}finally{f.cleanup()}
});

test('app writer conflict is an explicit preacceptance rejection, with no automatic retry',async()=>{
 const f=await fixture({mode:'writer-conflict'});try{const options={loadState:async()=>f.state};const r=await deliverEmergency(f.root,f.packet.incidentId,options);assert.equal(r.status,'DELIVERY_REJECTED_THREAD_WRITER_CONFLICT');assert.equal(r.sendAccepted,false);assert.equal(r.automaticRetryAllowed,false);assert.equal((await deliverEmergency(f.root,f.packet.incidentId,options)).replayed,true);assert.equal(f.sends(),0)}finally{f.cleanup()}
});

test('runner recovery consumes one extra verification and cannot dispatch a second copy',async()=>{
 const f=await fixture({configure:false});try{const prompt=join(f.root,'queue-prompt.md');writeFileSync(prompt,'Synthetic queue task');const job=enqueue(f.root,{case:'case',role:'critic',promptFile:prompt,outputContract:{schema:'rcc.output-contract.v1',mode:'response'}}).job;const prepared=prepareHandoff(f.root,{caseId:'case',sessionId:session,autoReview:true,workspace:f.root});armHandoff(f.root,{caseId:'case',sessionId:session,marker:prepared.marker});await configureEmergencyRoute(f.root,f.config);let dispatches=0,reviews=0,diagnostics=0;
 const options={now:Date.now()+5000,dispatch:()=>{dispatches++;return {code:0}},review:(r,id,o)=>verifyQueuedJob(r,id,{...o,observe:async()=>{reviews++;throw Error('synthetic offline')}}),emergency:async(r,id)=>{diagnostics++;const ack=await deliverEmergency(r,id);assert.equal(ack.status,'AGENT_ACKNOWLEDGED_DECISION_READY');return verifyQueuedJob(r,'case',{jobId:job.id,recoveryIncidentId:id,observe:async(_root,j)=>({jobId:j.id,payloadHash:j.payloadHash,status:'RESPONSE_UI_WITNESSED',deliveryBlocks:[]})})}};
 assert.equal((await runnerTick(f.root,'case',options)).status,'TRANSPORT_RETURNED');await runnerTick(f.root,'case',options);await runnerTick(f.root,'case',options);assert.equal((await runnerTick(f.root,'case',options)).status,'REVIEWED_WITNESS');assert.equal((await runnerTick(f.root,'case',options)).status,'READY');assert.equal(dispatches,1);assert.equal(reviews,3);assert.equal(diagnostics,1);assert.equal(f.sends(),1);assert.equal(handoffStatus(f.root,'case').lastRecovery.status,'REVIEWED_WITNESS');
 }finally{f.cleanup()}
});

test('unavailable emergency handler exits the runner recovery path with a persisted incident reference',async()=>{
 const f=await fixture({configure:false});try{const prompt=join(f.root,'queue-prompt.md');writeFileSync(prompt,'Synthetic');const job=enqueue(f.root,{case:'case',role:'critic',promptFile:prompt,outputContract:{schema:'rcc.output-contract.v1',mode:'response'}}).job;const p=prepareHandoff(f.root,{caseId:'case',sessionId:session,autoReview:true,workspace:f.root});armHandoff(f.root,{caseId:'case',sessionId:session,marker:p.marker});await dispatchOne(f.root,'case',()=>({code:0}));const options={now:Date.now()+5000,review:(r,id,o)=>verifyQueuedJob(r,id,{...o,observe:async()=>{throw Error('offline')}}),emergency:async()=>{throw Error('route expired')}};await runnerTick(f.root,'case',options);await runnerTick(f.root,'case',options);const r=await runnerTick(f.root,'case',options);assert.equal(r.status,'RECOVERY_ESCALATED');assert.equal(r.reason,'EMERGENCY_HANDLER_UNAVAILABLE');assert.equal(handoffStatus(f.root,'case').lastRecovery.incidentId,r.incidentId);assert.equal(inspectQueue(f.root,'case').jobs[0].attempts,1);assert.equal(f.sends(),0);
 }finally{f.cleanup()}
});
test('observer budget and elapsed deadline persist across different agent decision IDs',async()=>{
 const f=await fixture({configure:false});try{let reads=0;for(let i=0;i<4;i++){const d={schema:'rcc.recovery.decision.v1',incidentId:f.packet.incidentId,checkpointHash:f.packet.checkpointHash,decisionId:sha(String(i)),expiresAt:new Date(Date.now()+60000).toISOString(),decision:'REOBSERVE',action:{kind:'RECONNECT_READ_ONLY',parameters:{}}};const r=await resumeObservation(f.root,{incidentId:f.packet.incidentId,decision:d,loadState:async()=>f.state,inspect:async()=>{reads++;return {status:'OBSERVED'}}});if(i===3)assert.equal(r.status,'OBSERVATION_INCIDENT_BUDGET_EXHAUSTED')}assert.equal(reads,3);const b=ensureRecoveryBudget(f.root,f.packet.incidentId);assert.throws(()=>ensureRecoveryBudget(f.root,f.packet.incidentId,{now:b.deadlineMs+1}),/elapsed_budget_exhausted/);}finally{f.cleanup()}
});
test('diagnosis can authorize one extra verification, without resetting the original attempts or sending again',async()=>{
 const f=await fixture({queue:true});try{const result=await deliverEmergency(f.root,f.packet.incidentId);assert.equal(result.status,'AGENT_ACKNOWLEDGED_DECISION_READY');const job=inspectQueue(f.root,'case').jobs[0];const observed=async(_root,j)=>({jobId:j.id,payloadHash:j.payloadHash,status:'RESPONSE_UI_WITNESSED',deliveryBlocks:[]});const verified=await verifyQueuedJob(f.root,'case',{jobId:job.id,recoveryIncidentId:f.packet.incidentId,observe:observed});assert.equal(verified.ok,true);const q=inspectQueue(f.root,'case');assert.equal(q.jobs[0].attempts,1);assert.equal(q.jobs[0].verificationAttempts,3);assert.equal(q.jobs[0].recoveryVerificationAttempts,1);assert.equal(f.sends(),1);}finally{f.cleanup()}
});

test('late recovery evidence cannot commit completion after the persisted elapsed deadline',async()=>{
 const f=await fixture({queue:true}),originalNow=Date.now;try{await deliverEmergency(f.root,f.packet.incidentId);const job=inspectQueue(f.root,'case').jobs[0],before=originalNow();const result=await verifyQueuedJob(f.root,'case',{jobId:job.id,recoveryIncidentId:f.packet.incidentId,observe:async(_root,j)=>{Date.now=()=>before+300001;return {jobId:j.id,payloadHash:j.payloadHash,status:'RESPONSE_UI_WITNESSED',deliveryBlocks:[]}}});assert.equal(result.code,'queue.recovery_review_failed');assert.equal(inspectQueue(f.root,'case').jobs[0].status,'TRANSPORT_RETURNED');assert.equal(inspectQueue(f.root,'case').jobs[0].review,undefined);assert.equal(f.sends(),1)}finally{Date.now=originalNow;f.cleanup()}
});
test('real controller death without durable reply proof leaves an uncertain claim and never launches a second child',async()=>{
 const f=await fixture({mode:'slow-no-ack'});let child;try{
 const mod=new URL('../lib/emergency-delivery.mjs',import.meta.url).href;const code=`import {deliverEmergency} from ${JSON.stringify(mod)};await deliverEmergency(process.argv[1],process.argv[2],{loadState:async()=>JSON.parse(process.argv[3])});`;
 child=spawn(process.execPath,['--input-type=module','-e',code,f.root,f.packet.incidentId,JSON.stringify(f.state)],{stdio:['ignore','ignore','ignore'],windowsHide:true});
 for(let i=0;i<100&&f.sends()===0;i++)await new Promise(r=>setTimeout(r,25));assert.equal(f.sends(),1);const exited=once(child,'exit');child.kill('SIGKILL');await exited;
 const result=await deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state});assert.equal(result.status,'DELIVERY_OUTCOME_UNKNOWN_NO_RESEND');assert.equal(f.sends(),1);await new Promise(r=>setTimeout(r,750));
 const reconciled=await deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state});assert.equal(reconciled.status,'DELIVERY_OUTCOME_UNKNOWN_NO_RESEND');assert.equal(f.sends(),1);
 }finally{child?.kill();f.cleanup()}
});

test('lost or corrupt checkpoints permit diagnostic-only delivery and prohibit a proposed action',async()=>{
 for(const mode of ['good','ignore-diagnostic-only']){const f=await fixture({mode});try{let observations=0;const result=await recoverEmergency(f.root,f.packet.incidentId,{inspect:async()=>{observations++}});assert.equal(result.status,mode==='good'?'AGENT_ACKNOWLEDGED_UNRESOLVED':'AGENT_ACKNOWLEDGED_DECISION_REJECTED');assert.equal(observations,0);assert.equal(f.sends(),1)}finally{f.cleanup()}}
});

test('a deferred concurrent decision can run later instead of caching a permanent running result',async()=>{
 const f=await fixture({configure:false});try{let release,entered;const began=new Promise(r=>entered=r),held=new Promise(r=>release=r);const d=i=>({schema:'rcc.recovery.decision.v1',incidentId:f.packet.incidentId,checkpointHash:f.packet.checkpointHash,decisionId:sha(String(i)),expiresAt:new Date(Date.now()+60000).toISOString(),decision:'REOBSERVE',action:{kind:'RECONNECT_READ_ONLY',parameters:{}}});
 const first=resumeObservation(f.root,{incidentId:f.packet.incidentId,decision:d(0),loadState:async()=>f.state,inspect:async()=>{entered();await held;return {status:'OBSERVED'}}});await began;
 const second=d(1),options={incidentId:f.packet.incidentId,decision:second,loadState:async()=>f.state,inspect:async()=>({status:'OBSERVED'})};assert.equal((await resumeObservation(f.root,options)).status,'OBSERVATION_RUNNING_OR_OWNER_UNKNOWN');release();await first;assert.equal((await resumeObservation(f.root,options)).status,'OBSERVATION_RETURNED_NOT_TASK_COMPLETION');
 }finally{f.cleanup()}
});

test('delivery CLI can inspect an outbox and configure a route without a state file',async()=>{
 const f=await fixture({configure:false});try{const cli=fileURLToPath(new URL('../bin/rcc-recovery',import.meta.url)),exec=args=>spawnSync(process.execPath,[cli,...args],{encoding:'utf8',windowsHide:true});
 const configured=exec(['configure-route','--root='+f.root,'--case=case','--session='+session,'--executable='+process.execPath,'--entrypoint='+f.config.entrypoint,'--authorization-ref=EXPLICIT_TEST_OPERATOR_FIXTURE','--expires-at='+f.config.expiresAt,'--allow-non-git']);assert.equal(configured.status,0,configured.stderr);assert.equal(JSON.parse(configured.stdout).status,'ROUTE_CONFIGURED_NO_MESSAGE_SENT');
 const status=exec(['delivery-status','--root='+f.root,'--incident='+f.packet.incidentId]);assert.equal(status.status,2);assert.equal(JSON.parse(status.stdout).status,'NOT_ATTEMPTED');
 const delivered=exec(['deliver','--root='+f.root,'--incident='+f.packet.incidentId]);assert.equal(delivered.status,0,delivered.stderr);assert.equal(JSON.parse(delivered.stdout).status,'AGENT_ACKNOWLEDGED_UNRESOLVED');assert.equal(f.sends(),1);
 }finally{f.cleanup()}
});

test('controller death after durable terminal evidence permits reconciliation without a second diagnostic',async()=>{
 const f=await fixture({mode:'ack-then-delay'});let child;try{
 const mod=new URL('../lib/emergency-delivery.mjs',import.meta.url).href,code=`import {deliverEmergency} from ${JSON.stringify(mod)};await deliverEmergency(process.argv[1],process.argv[2],{loadState:async()=>JSON.parse(process.argv[3])});`;
 child=spawn(process.execPath,['--input-type=module','-e',code,f.root,f.packet.incidentId,JSON.stringify(f.state)],{stdio:['ignore','ignore','ignore'],windowsHide:true});
 const output=join(f.root,'.devspace','rcc','recovery-incidents',f.packet.incidentId,'delivery','stdout.jsonl');
 for(let i=0;i<100;i++){if(existsSync(output)&&readFileSync(output,'utf8').includes('turn.completed'))break;await new Promise(r=>setTimeout(r,25))}
 assert(existsSync(output),'durable event stream exists');assert(readFileSync(output,'utf8').includes('turn.completed'),'terminal evidence precedes fault injection');
 const exited=once(child,'exit');child.kill('SIGKILL');await exited;
 const reconciled=await deliverEmergency(f.root,f.packet.incidentId,{loadState:async()=>f.state});assert.equal(reconciled.status,'AGENT_ACKNOWLEDGED_DECISION_READY');assert.equal(reconciled.reconciled,true);assert.equal(f.sends(),1);
 }finally{child?.kill();f.cleanup()}
});
