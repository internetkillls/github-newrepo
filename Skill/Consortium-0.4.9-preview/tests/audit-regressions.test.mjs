import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {mkdtempSync,writeFileSync,readFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {pageProbe} from '../runtime/chatgpt-pro-line/src/chatgpt-page.mjs';
import {snapshotConversationMessages} from '../runtime/chatgpt-pro-line/src/chatgpt-messages.mjs';
import {uploadEvidenceReady,removeComposerAttachments} from '../runtime/chatgpt-pro-line/src/chatgpt-upload.mjs';
import {waitForSubmission} from '../runtime/chatgpt-pro-line/src/chatgpt-composer.mjs';
import {controllerReuseProof} from '../lib/controller-reuse.mjs';
import {classifySubmission} from '../lib/transport-phase.mjs';
import {operationalStatus} from '../lib/operational-status.mjs';
import {assertUnusedRoom} from '../lib/room-lifecycle.mjs';
import {enqueue,dispatchOne,inspectQueue} from '../lib/queue-manager.mjs';
import {captureOutputs,recheckOutputs,normalizeOutputContract} from '../lib/output-gate.mjs';

function node(role,text,index,{legacy=true,modern=false,hidden=false,children=[]}={}){
 return {role,index,legacy,modern,innerText:text,childElementCount:children.length,
  getAttribute:k=>k==='data-message-author-role'&&legacy?role:k==='data-markdown-text-style'&&modern&&role==='assistant'?'assistant-message':null,
  hasAttribute:k=>k==='data-user-message-bubble'&&modern&&role==='user',
  contains:e=>children.includes(e),compareDocumentPosition:e=>index<e.index?4:index>e.index?2:0,
  getBoundingClientRect:()=>({width:100,height:hidden?0:20}),style:{display:'block',visibility:'visible'}};
}
function dom(nodes,sidebar=[]){
 const query=s=>s==='[data-message-author-role]'?nodes.filter(n=>n.legacy):s.includes('data-user-message-bubble')?nodes.filter(n=>n.modern):[];
 const root={querySelectorAll:query};
 const document={title:'fixture',body:{innerText:''},querySelector:s=>s==='main'?root:null,querySelectorAll:s=>[...query(s),...(s.includes('data-message')?sidebar:[])]};
 return {send:async(_,p)=>({result:{value:vm.runInNewContext(p.expression,{document,location:{href:'https://chatgpt.com/c/fixture'},getComputedStyle:e=>e.style})}})};
}
test('mixed, old-only and modern-only messages share one ordered collector; no sidebar or hidden reads',async()=>{
 const old=node('user','one',0),modern=node('user','two',2,{legacy:false,modern:true}),answer=node('assistant','reply',3,{legacy:false,modern:true});
 const hidden=node('assistant','',1,{hidden:true});Object.defineProperty(hidden,'innerText',{get(){throw Error('hidden text read')}});
 for(const rows of [[old],[modern,answer],[old,hidden,modern,answer]]){
  const c=dom(rows,[node('user','sidebar',-1)]),snapshot=await snapshotConversationMessages(c),probe=await pageProbe(c);
  assert.equal(snapshot.length,rows.filter(n=>n!==hidden).length);assert.equal(probe.userTurns.length,snapshot.filter(n=>n.role==='user').length);
  assert(!snapshot.some(n=>n.text==='sidebar'));
 }
});
test('nested alternate wrappers deduplicate by node ancestry, not identical message text',async()=>{
 const inner=node('user','same',0,{legacy:false,modern:true}),outer=node('user','same',0,{children:[inner]}),second=node('user','same',1,{legacy:false,modern:true});
 const snapshot=await snapshotConversationMessages(dom([inner,second,outer]));assert.equal(snapshot.length,2);assert.equal(JSON.stringify(snapshot.map(x=>x.text)),JSON.stringify(['same','same']));
});
test('ready uploads ignore unrelated errors but reject errors/progress for the requested file',()=>{
 const ready=[{aria:'SOURCE.zip'},{aria:'CONTROLLERS.zip'}];
 assert(uploadEvidenceReady(['SOURCE.zip','CONTROLLERS.zip'],[...ready,{aria:'Unrelated error details'}]));
 assert(!uploadEvidenceReady(['SOURCE.zip'],[{aria:'Uploading SOURCE.zip'}]));
 assert(!uploadEvidenceReady(['SOURCE.zip'],[...ready,{aria:'Failed SOURCE.zip'}]));
 assert(!uploadEvidenceReady(['missing.zip'],ready));
});
test('cleanup recognizes current Remove filename labels and leaves unrelated Remove controls alone',async()=>{
 let clicks=[];const button=label=>({getAttribute:()=>label,click:()=>clicks.push(label)});
 const scope={querySelectorAll:()=>[button('Remove file'),button('Remove SOURCE.2026-10-22.zip'),button('Remove account')]};
 const cdp={send:async(_,p)=>({result:{value:vm.runInNewContext(p.expression,{document:{querySelector:()=>({closest:()=>scope})}})}})};
 const r=await removeComposerAttachments(cdp);assert.equal(r.removed,2);assert.equal(clicks.length,2);assert(!clicks.includes('Remove account'));
});
test('submission ACK uses exact new prompt with mixed markup, rather than needing a count increase',async()=>{
 const before=await snapshotConversationMessages(dom([node('user','previous',0)]));
 const c=dom([node('user','previous',0),node('user','authorized prompt',1,{legacy:false,modern:true})]);
 const r=await waitForSubmission(c,{initialUserCount:99,beforeSnapshot:before,prompt:'authorized prompt',timeoutMs:1000});
 assert.equal(r.submitted,true);assert.equal(r.echo,'exact_new_turn');
});
function phase(root,job,token){return {ok:false,rccInvocationToken:token,queueBinding:{jobId:job.id,payloadHash:job.payloadHash},project:{repoRoot:root},input:{promptSha256:job.prompt.sha256},submission:{phase:'NOT_ATTEMPTED'},errorCode:'input.attachment_upload_failed',steps:[{step:'uploaded-files',ok:false}]};}
test('phase-aware no-Send proof is fresh and job-bound; clicked, stale, foreign and missing records remain uncertain',async()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-phase-regression-')),prompt=join(root,'prompt.md');writeFileSync(prompt,'source review');
 const job=enqueue(root,{case:'demo',role:'worker',promptFile:prompt}).job;
 const result=await dispatchOne(root,'demo',j=>({code:1,phaseReceipt:phase(root,j,j.invocationToken)}));
 assert.equal(result.status,'NOT_SENT_CONFIRMED');assert.equal(inspectQueue(root,'demo').jobs[0].attempts,1);
 const good=phase(root,job,'token');assert.equal(classifySubmission(good,{root,job,token:'token'}),'NOT_SENT_CONFIRMED');
 for(const bad of [{...good,rccInvocationToken:'stale'},{...good,steps:[{step:'sent-prompt',ok:false}]},{...good,submission:{phase:'ATTEMPTING'}},{...good,queueBinding:{jobId:'wrong'}},null])assert.equal(classifySubmission(bad,{root,job,token:'token'}),'UNKNOWN');
});
test('operational status never equates scheduler/process existence with verified browser generation',()=>{
 const q={caseId:'demo',jobs:[{id:'j',role:'r',status:'DISPATCHING'}],lock:{pid:1}};
 assert.equal(operationalStatus(q,{pidAlive:()=>false}).status,'BLOCKED_ORPHANED_DISPATCH');
 const live=operationalStatus(q,{pidAlive:()=>true});assert.equal(live.status,'DISPATCHING');assert.equal(live.generationVerified,false);
 assert.equal(operationalStatus({...q,jobs:[{status:'UNCERTAIN'}]}).status,'BLOCKED');
 assert.equal(operationalStatus({jobs:[{status:'PENDING'}]}).status,'QUEUED');
});
test('unused-room provision rejects missing approval, any prior send, committed history and ambiguous provisioning',()=>{
 const state={caseId:'demo'},worker={role:'w4',alias:'w4',conversationUrl:'https://chatgpt.com/'},queue={jobs:[{role:'w4',status:'PENDING',attempts:0}]},room={name:'w4',url:'https://chatgpt.com/',callCount:0};
 assertUnusedRoom(state,queue,worker,room,'PROVISION-demo-w4');
 assert.throws(()=>assertUnusedRoom(state,queue,worker,room,''),/approval/);
 for(const s of ['UNCERTAIN','DISPATCHING','TRANSPORT_RETURNED','REVIEWED_WITNESS'])assert.throws(()=>assertUnusedRoom(state,{jobs:[{role:'w4',status:s}]},worker,room,'PROVISION-demo-w4'),/history/);
 assert.throws(()=>assertUnusedRoom(state,queue,worker,{...room,url:'https://chatgpt.com/c/old'},'PROVISION-demo-w4'),/never_replace/);
 assert.throws(()=>assertUnusedRoom(state,queue,{...worker,provisionAttempt:{status:'OPENING'}},room,'PROVISION-demo-w4'),/reconciliation/);
});
test('raw JSON contract saves exact UTF8 with host hash; wrong identity, duplicates and old file contracts stay strict',()=>{
 const spec={schema:'rcc.output-contract.v1',mode:'json',path:'review.json',schemaId:'demo.review.v1',identity:{workerId:'W4'},maxBytes:1000};
 const raw='{ "schema":"demo.review.v1", "workerId":"W4", "note":"日本語 α" }';
 const dir=mkdtempSync(join(tmpdir(),'rcc-json-response-')),r=captureOutputs(spec,[raw],dir);
 assert.equal(readFileSync(join(dir,'review.json'),'utf8'),raw);assert.equal(recheckOutputs(r),true);
 assert.equal(r.files[0].sha256,createHash('sha256').update(raw).digest('hex'));
 assert.throws(()=>captureOutputs(spec,[raw,raw],dir),/exactly_one/);
 assert.throws(()=>captureOutputs({...spec,identity:{workerId:'W5'}},[raw],dir),/identity/);
 assert.throws(()=>captureOutputs({schema:spec.schema,mode:'files',required:['review.json']},[raw],dir),/required_file_missing/);
 assert.throws(()=>normalizeOutputContract({...spec,path:'../escape.json'}),/unsafe_path/);
});
test('controller reuse requires pinned prior delivery in the SAME committed role and unchanged bundle',()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-controller-reuse-')),file=join(root,'receipt.json'),bundlePath=join(root,'controllers.zip');writeFileSync(bundlePath,'controller fixture');
 const hash=b=>createHash('sha256').update(b).digest('hex'),worker={alias:'w4',conversationUrl:'https://chatgpt.com/c/one'};
 const receipt={ok:true,room:{alias:'w4'},project:{repoRoot:root},response:{conversationUrl:worker.conversationUrl},messageAnchor:{sentUserMessage:{promptEchoVerification:'exact'},responseBoundToSentPrompt:true},upload:{ok:true,files:[{bytes:18,sha256:hash('controller fixture')}]}};
 const raw=JSON.stringify(receipt);writeFileSync(file,raw);const options={root,worker,bundlePath,receiptPath:file,receiptSha256:hash(raw)};
 assert.equal(controllerReuseProof(options).bundleBytes,18);
 assert.throws(()=>controllerReuseProof({...options,worker:{...worker,alias:'w5'}}),/same_room/);
 assert.throws(()=>controllerReuseProof({...options,worker:{...worker,conversationUrl:'https://chatgpt.com/c/other'}}),/same_room/);
 assert.throws(()=>controllerReuseProof({...options,receiptSha256:hash('changed')}),/changed/);
 writeFileSync(bundlePath,'different');assert.throws(()=>controllerReuseProof(options),/same_room/);
});
test('twelve role rooms are explicitly configurable and remain serial, default cap still rejects twelve',()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-roles-regression-')),cli=new URL('../bin/rcc-consortium',import.meta.url).pathname.replace(/^\/(\w:)/,'$1');
 const roles=Array.from({length:12},(_,i)=>'role'+i).join(',');
 const run=args=>spawnSync(process.execPath,[cli,'workers','spawn','--case=demo','--dry-run','--roles='+roles,...args],{cwd:root,encoding:'utf8',timeout:10000,windowsHide:true});
 assert.notEqual(run([]).status,0);const accepted=run(['--max-roles=12']);assert.equal(accepted.status,0,accepted.stderr);
 const value=JSON.parse(accepted.stdout);assert.equal(value.state.workers.length,12);assert.equal(value.state.runtime.parallelGenerationVerified,false);
});
test('actual room provisioning claims once and persists lost-ACK debt; first prompt binding preserves history without double-counting',()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-room-lifecycle-'));
 const url=p=>new URL(p,import.meta.url).href;
 const script=`import assert from 'node:assert/strict';import {readFileSync,writeFileSync} from 'node:fs';import {resolve} from 'node:path';
 const sessions=await import(${JSON.stringify(url('../runtime/chatgpt-pro-line/src/chatgpt-sessions.mjs'))});
 const {provisionUnusedRoom}=await import(${JSON.stringify(url('../lib/room-lifecycle.mjs'))});
 const {enqueue}=await import(${JSON.stringify(url('../lib/queue-manager.mjs'))});
 const {writeExecutionFixture}=await import(${JSON.stringify(url('./execution-fixture.mjs'))});
 const root=process.cwd(),pluginRoot=${JSON.stringify(new URL('..',import.meta.url).pathname.replace(/^\/(\w:)/,'$1'))};
 const f=writeExecutionFixture(root,pluginRoot,{id:'demo'});
 let pages=[{id:'old',type:'page',webSocketDebuggerUrl:'ws://127.0.0.1:9222/devtools/page/fixture',url:'https://chatgpt.com/'}],opens=0,lose=false;
 globalThis.fetch=async uri=>{const u=new URL(uri);if(u.pathname==='/json')return {ok:true,json:async()=>pages};if(u.pathname==='/json/new'){opens++;if(lose)throw Error('lost create ACK');pages=[{id:'new',type:'page',webSocketDebuggerUrl:'ws://127.0.0.1:9222/devtools/page/fixture',url:'https://chatgpt.com/'}];return {ok:true,json:async()=>pages[0]};}return {ok:true,json:async()=>({})}};
 await sessions.aliasChatGptSession(9222,{name:'test-room-builder',targetId:'old'});
 const file=resolve(root,'.devspace/rcc/demo/state.json');writeFileSync(file,JSON.stringify({caseId:'demo',workers:[{role:'builder',alias:'test-room-builder',targetId:'old',conversationUrl:'https://chatgpt.com/'}]}));
 enqueue(root,{case:'demo',role:'builder',promptFile:f.prompts.builder});pages=[];
 const made=await provisionUnusedRoom(root,'demo',{role:'builder',approval:'PROVISION-demo-builder',pluginRoot});assert.equal(made.created,true);assert.equal(opens,1);
 const bound=sessions.recordChatGptPromptBinding({name:'test-room-builder',target:{id:'new',url:'https://chatgpt.com/c/first'},runId:'run1',receiptPath:'receipt.json'});
 assert.equal(bound.activeConversationUrl,'https://chatgpt.com/c/first');assert.equal(bound.callCount,0);assert.equal(bound.lineage.filter(x=>x.status==='active').length,1);
 assert.throws(()=>sessions.recordChatGptPromptBinding({name:'test-room-builder',target:{id:'wrong',url:'https://chatgpt.com/c/other'}}),e=>e.errorCode==='room.prompt_binding_target_changed');
 sessions.recordChatGptAliasUse({name:'test-room-builder',target:{id:'new',url:'https://chatgpt.com/c/first'},runId:'run1'});
 assert.equal(JSON.parse(readFileSync(sessions.sessionRegistryPath)).rooms['test-room-builder'].callCount,1);
 pages=[{id:'old2',type:'page',webSocketDebuggerUrl:'ws://127.0.0.1:9222/devtools/page/fixture',url:'https://chatgpt.com/'}];await sessions.aliasChatGptSession(9222,{name:'test-room-verifier',targetId:'old2'});
 const state=JSON.parse(readFileSync(file));state.workers.push({role:'verifier',alias:'test-room-verifier',targetId:'old2',conversationUrl:'https://chatgpt.com/'});writeFileSync(file,JSON.stringify(state));enqueue(root,{case:'demo',role:'verifier',promptFile:f.prompts.verifier});pages=[];lose=true;
 await assert.rejects(provisionUnusedRoom(root,'demo',{role:'verifier',approval:'PROVISION-demo-verifier',pluginRoot}));const before=opens;
 await assert.rejects(provisionUnusedRoom(root,'demo',{role:'verifier',approval:'PROVISION-demo-verifier',pluginRoot}),/reconciliation/);assert.equal(opens,before);
 assert.equal(JSON.parse(readFileSync(file)).workers[1].provisionAttempt.status,'UNCERTAIN');console.log('offline lifecycle verified');`;
 const file=join(root,'fixture.mjs');writeFileSync(file,script);
 const r=spawnSync(process.execPath,[file],{cwd:root,env:{...process.env,CHATGPT_REPO_ROOT:root,CHATGPT_PRO_HOME:join(root,'private-home')},encoding:'utf8',timeout:15000,windowsHide:true});
 assert.equal(r.status,0,r.stderr);assert.match(r.stdout,/offline lifecycle verified/);
});
