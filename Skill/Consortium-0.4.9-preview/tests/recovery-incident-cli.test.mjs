import test from 'node:test';import assert from 'node:assert/strict';import {createServer} from 'node:http';import {execFile} from 'node:child_process';import {promisify} from 'node:util';import {fileURLToPath} from 'node:url';
import {mkdtempSync,writeFileSync,readFileSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';
const exec=promisify(execFile),cli=fileURLToPath(new URL('../bin/rcc-recovery',import.meta.url));
test('CLI persists diagnostic outbox and resumes only observation against loopback fixture',async()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-outbox-cli-')),server=createServer((req,res)=>{res.setHeader('Content-Type','application/json');res.end('[]')});await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{const state=join(root,'state.json'),original=JSON.stringify({caseId:'test',workers:[{role:'critic',conversationUrl:'https://chatgpt.com/c/one'}]});writeFileSync(state,original);const args=['--state='+state,'--root='+root,'--port='+server.address().port];
 let stdout;try{await exec(process.execPath,[cli,'incident',...args]);assert.fail('pending escalation must not exit as success')}catch(e){assert.equal(e.code,2);stdout=e.stdout;}
 const saved=JSON.parse(stdout);assert.equal(saved.status,'PERSISTED_LOCAL_NOT_DELIVERED');assert.equal(saved.incident.delivery.attempted,false);assert.equal(readFileSync(state,'utf8'),original);
 const d=join(root,'decision.json');writeFileSync(d,JSON.stringify({schema:'rcc.recovery.decision.v1',decisionId:'a'.repeat(64),incidentId:saved.incident.incidentId,checkpointHash:saved.incident.checkpointHash,decision:'REOBSERVE',action:{kind:'RECONNECT_READ_ONLY',parameters:{}},expiresAt:new Date(Date.now()+60000).toISOString()}));
 const resumed=await exec(process.execPath,[cli,'resume-observation',...args,'--incident='+saved.incident.incidentId,'--decision-file='+d]);const result=JSON.parse(resumed.stdout);assert.equal(result.sendAllowed,false);assert.equal(result.inspection.status,'OBSERVED');assert.equal(readFileSync(state,'utf8'),original);
 }finally{await new Promise(r=>server.close(r));rmSync(root,{recursive:true,force:true});}
});
