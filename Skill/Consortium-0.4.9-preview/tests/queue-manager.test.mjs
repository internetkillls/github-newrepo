import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, mkdirSync, readFileSync,rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join, dirname } from 'node:path';
import { createHash } from 'node:crypto';
import { spawnSync as spawnRunner } from 'node:child_process';
import { enqueue, inspectQueue, queuePaths, dispatchOne, reviewJob, recoverQueue } from '../lib/queue-manager.mjs';
const sha = (s)=>createHash('sha256').update(s).digest('hex');
function fixture(){
 const root=mkdtempSync(join(tmpdir(),'rccq-'));
 const path=join(root,'prompt.md');writeFileSync(path,'Independent review of evidence.');
 return {root,path,id:'demo',role:'skeptic'};
}
function add(f,opts={}) {return enqueue(f.root,{case:f.id,role:f.role,promptFile:f.path,...opts});}
function receipt(f,job,decision='witnessed') {
 const p=resolve(f.root,'receipt.json');const anchor='user-anchor-verified-123';
 const obj={schema:'rcc.queue.review.v1',jobId:job.id,caseId:f.id,role:f.role,decision,reviewer:'human-reviewed-CDP-log',sourceArtifact:'path-to-reviewed-browser-receipt.json',
  witness:{userEchoVerified:true,userAnchor:anchor,assistantBoundToUserAnchor:anchor,completionVerified:true,completionEvidence:'anchored_terminal_controls_and_stability',assistantTextSha256:sha('response')},
  reason:'Confirmed no user message was transmitted by inspecting the local chat history.'};
 writeFileSync(p,JSON.stringify(obj));return p;
}
test('idempotent queue add does not duplicate and stores no raw prompt',()=>{
 const f=fixture(),a=add(f),b=add(f);assert.equal(a.duplicate,false);assert.equal(b.duplicate,true);assert.equal(a.job.id,b.job.id);
 const disk=readFileSync(queuePaths(f.root,f.id).file,'utf8');assert.doesNotMatch(disk,/Independent review of evidence/);
 assert.equal(inspectQueue(f.root,f.id).jobs.length,1);
});
test('status follows PENDING -> DISPATCHING -> TRANSPORT_RETURNED, not COMPLETED',async()=>{
 const f=fixture(),j=add(f).job;let seen;
 const r=await dispatchOne(f.root,f.id, async(jb)=>{seen=inspectQueue(f.root,f.id).jobs[0].status;return {code:0,stdout:'assistant reply',stderr:''};});
 assert.equal(seen,'DISPATCHING');assert.equal(r.status,'TRANSPORT_RETURNED');
 assert.equal(inspectQueue(f.root,f.id).jobs[0].status,'TRANSPORT_RETURNED');
 const after=await dispatchOne(f.root,f.id, async()=>{throw Error('must not send');});
 assert.equal(after.code,'queue.reconciliation_required');assert.equal(after.blockedJobId,j.id);
});
test('uncertain nonzero/throw never automatically retried',async()=>{
 const f=fixture(),j=add(f).job;let calls=0;
 const first=await dispatchOne(f.root,f.id,async()=>{calls++;throw Error('transport maybe clicked');});
 assert.equal(first.status,'UNCERTAIN');
 const second=await dispatchOne(f.root,f.id,async()=>{calls++;return {code:0};});
 assert.equal(second.code,'queue.reconciliation_required');assert.equal(calls,1);
 assert.equal(inspectQueue(f.root,f.id).jobs[0].attempts,1);
});
test('no fabricated witness or auto-canonical; manual receipt required',async()=>{
 const f=fixture(),job=add(f).job;await dispatchOne(f.root,f.id,async()=>({code:0}));
 let file=receipt(f,job);let data=JSON.parse(readFileSync(file));data.witness.userAnchor='different-message';writeFileSync(file,JSON.stringify(data));
 assert.throws(()=>reviewJob(f.root,f.id,{jobId:job.id,receiptFile:file}),/insufficient_completion_evidence/);
 file=receipt(f,job);
 const r=reviewJob(f.root,f.id,{jobId:job.id,receiptFile:file});
 assert.equal(r.status,'REVIEWED_WITNESS');assert.match(r.review.provenance,/operator_supplied/);
 assert.throws(()=>reviewJob(f.root,f.id,{jobId:job.id,receiptFile:file}),/already_reviewed/);
});
test('input mutates after enqueue -> blocked, never sends',async()=>{
 const f=fixture();add(f);writeFileSync(f.path,'Completely changed prompt.');let count=0;
 const r=await dispatchOne(f.root,f.id,async()=>{count++;return {code:0};});
 assert.equal(r.code,'queue.blocked_input');assert.equal(count,0);
 assert.equal(inspectQueue(f.root,f.id).jobs[0].status,'BLOCKED_INPUT');
});
test('review uncertain as not_sent terminates without automatic retry',async()=>{
 const f=fixture(),job=add(f).job;await dispatchOne(f.root,f.id,async()=>({code:1,stderr:'no echo'}));
 const result=reviewJob(f.root,f.id,{jobId:job.id,receiptFile:receipt(f,job,'not_sent')});
 assert.equal(result.status,'NOT_SENT_CONFIRMED');
 assert.equal((await dispatchOne(f.root,f.id,async()=>{throw Error('should not dispatch');})).code,'queue.empty');
});
test('lock protects all awaited external operations, including competing add',async()=>{
 const f=fixture();add(f);let release;const pending=dispatchOne(f.root,f.id,()=>new Promise(r=>{release=r;}));
 assert.throws(()=>add(f,{key:'independent-job'}),/queue.locked/);
 release({code:0});await pending;
 assert.equal(inspectQueue(f.root,f.id).lock,null);
});
test('legacy queue crash recovery bootstraps journal, requires approval and never requeues sends',()=>{
 const f=fixture(),j=add(f).job;const paths=queuePaths(f.root,f.id);
 const q=inspectQueue(f.root,f.id);q.jobs[0].status='DISPATCHING';
 // Model a pre-journal installation. Current-format crash coverage kills a real dispatcher in queue-journal.test.mjs.
 const journal=resolve(paths.dir,'queue-journal');assert.ok(journal.startsWith(resolve(f.root)));
 rmSync(journal,{recursive:true,force:true});
 writeFileSync(paths.file,JSON.stringify(q));
 assert.throws(()=>recoverQueue(f.root,f.id,{}),/explicit_recovery_approval/);
 const result=recoverQueue(f.root,f.id,{approval:'RECOVER-demo'});
 assert.equal(result.recoveredJobs[0],j.id);
 assert.equal(inspectQueue(f.root,f.id).jobs[0].status,'UNCERTAIN');
});
test('invalid state remains untouched and rejects overwrite',()=>{
 const f=fixture();const paths=queuePaths(f.root,f.id);mkdirSync(dirname(paths.file),{recursive:true});writeFileSync(paths.file,'{ corrupt');
 assert.throws(()=>add(f),SyntaxError);assert.equal(readFileSync(paths.file,'utf8'),'{ corrupt');
});

test('same explicit idempotency key for different packet is rejected',()=>{
 const f=fixture();add(f,{key:'manual-key'});const other=join(f.root,'other.md');writeFileSync(other,'distinct input');
 assert.throws(()=>add(f,{key:'manual-key',promptFile:other}),/idempotency_key_payload_conflict/);
});
test('CLI add/list work without Chrome or vendor runtime and add has no send side effect',()=>{
 const {spawnSync}=requireSpawn(); const f=fixture();const cli=resolve(import.meta.dirname,'../bin/rcc-queue');
 const addRun=spawnSync(process.execPath,[cli,'queue','add',`--case=${f.id}`,`--role=${f.role}`,`--prompt-file=${f.path}`],{cwd:f.root,encoding:'utf8'});
 assert.equal(addRun.status,0,addRun.stderr);assert.equal(JSON.parse(addRun.stdout).job.status,'PENDING');
 const listRun=spawnSync(process.execPath,[cli,'queue','list',`--case=${f.id}`],{cwd:f.root,encoding:'utf8'});
 assert.equal(listRun.status,0,listRun.stderr);assert.equal(JSON.parse(listRun.stdout).jobs.length,1);
 assert.equal(inspectQueue(f.root,f.id).jobs[0].attempts,0);
});
function requireSpawn(){return {spawnSync: spawnRunner};}
