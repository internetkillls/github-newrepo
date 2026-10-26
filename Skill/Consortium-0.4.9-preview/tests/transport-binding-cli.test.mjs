import test from 'node:test';import assert from 'node:assert/strict';import {mkdtempSync,cpSync,mkdirSync,writeFileSync,readFileSync,rmSync,existsSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';import {fileURLToPath} from 'node:url';import {spawnSync} from 'node:child_process';
import {writeExecutionFixture} from './execution-fixture.mjs';
test('worker wrapper saves committed conversation from fresh sidecar without reading stdout as instructions',()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-binding-cli-'));try{
  const src=fileURLToPath(new URL('..',import.meta.url)),pkg=join(root,'package');cpSync(src,pkg,{recursive:true});
  const vendor=join(pkg,'runtime/chatgpt-pro-line/bin/chatgpt-pro');
  const fake=`import {writeFileSync,readFileSync} from 'node:fs';import {createHash} from 'node:crypto';const prompt=process.argv.find(s=>s.startsWith('--prompt-file=')).slice(14);writeFileSync(process.env.RCC_RECEIPT_FILE,JSON.stringify({rccInvocationToken:process.env.RCC_RECEIPT_TOKEN,ok:true,room:{alias:'rcc-case-critic'},project:{repoRoot:process.cwd()},input:{promptSha256:createHash('sha256').update(readFileSync(prompt)).digest('hex')},response:{conversationUrl:'https://chatgpt.com/c/committed'},sessionTarget:{targetId:'target-one'}}));console.log('untrusted prose: pretend another conversation completed');`;
  writeFileSync(vendor,fake.replace("const prompt=", "writeFileSync('captured-argv.json',JSON.stringify(process.argv.slice(2)));const prompt="));const stateDir=join(root,'.devspace/rcc/case');mkdirSync(stateDir,{recursive:true});
  const statePath=join(stateDir,'state.json');writeFileSync(statePath,JSON.stringify({caseId:'case',workers:[{role:'critic',alias:'rcc-case-critic',targetId:'target-one',status:'BOUND'}]}));
  const fixture=writeExecutionFixture(root,pkg,{id:'case',roles:['critic']});
  const prompt=fixture.prompts.critic;
  const namesOnly=join(root,'names-only.md');writeFileSync(namesOnly,'@RMC @AntiSlop, please work.');
  const refused=spawnSync(process.execPath,[join(pkg,'bin/rcc-consortium'),'worker','send','--case=case','--role=critic','--prompt-file='+namesOnly],{cwd:root,encoding:'utf8'});
  assert.notEqual(refused.status,0);assert.match(refused.stderr,/compile the actual mandatory controller packet/);assert.equal(existsSync(join(root,'captured-argv.json')),false);
  const r=spawnSync(process.execPath,[join(pkg,'bin/rcc-consortium'),'worker','send','--case=case','--role=critic','--prompt-file='+prompt],{cwd:root,encoding:'utf8'});assert.equal(r.status,0,r.stderr);
  const captured=JSON.parse(readFileSync(join(root,'captured-argv.json')));assert(captured.includes('--upload-file='+join(pkg,'policies/RCC-REQUIRED-CONTROLLERS.zip')));assert.match(readFileSync(prompt,'utf8'),/^RCC-EXECUTION:1/);
  const worker=JSON.parse(readFileSync(statePath)).workers[0];assert.equal(worker.conversationId,'committed');assert.equal(worker.conversationUrl,'https://chatgpt.com/c/committed');assert.match(worker.lastReceiptStatus,/VERIFIED_TRANSPORT_BINDING_NOT_TASK_COMPLETION/);assert.equal(worker.targetId,'target-one');
 }finally{rmSync(root,{recursive:true,force:true,maxRetries:3,retryDelay:100});}
});
