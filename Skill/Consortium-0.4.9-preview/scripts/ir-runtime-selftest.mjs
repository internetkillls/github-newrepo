import assert from 'node:assert/strict';
import { mkdtempSync,rmSync,writeFileSync,readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { transduce,promptFromIR,extractSnippets,normalizeCitations,toCsv,repairCase,makePostmortem } from '../lib/operations.mjs';
import { startLocalServer } from '../lib/local-server.mjs';
import { extractVisibleDom } from '../lib/browser-dom.mjs';
const root=resolve(fileURLToPath(new URL('..',import.meta.url)));
const d=mkdtempSync(resolve(tmpdir(),'rcc-ir-selftest-'));
const originalCwd=process.cwd();
process.chdir(d);
try{
 const request='Inspect existing repo first; improve Mermaid diagrams and run tests, do not implement code.';
 const ir=transduce(request,{caseId:'check-1'});
 assert.equal(ir.schema,'rcc.task-ir.v1');assert.equal(ir.objective.userText,request);
 const p=promptFromIR(ir);assert.ok(p.includes(request));assert.ok(p.includes('do not implement'));
 const snippet=extractSnippets('```mermaid\nflowchart LR; A-->B\n```\n```json\n{"a":1}\n```');assert.deepEqual(snippet.items.map(x=>x.kind),['mermaid','json']); assert.equal(extractSnippets('<svg><path d="M0 0" /></svg>').items[0].kind,'svg'); assert.equal(extractSnippets('```python\nprint(1)\n```').items[0].kind,'python');
 const cites=normalizeCitations(JSON.stringify([{ref:'A',url:'https://example.org',title:'source'}]),{thinkingMode:'High',thinkingEvidence:'unspecified'});
 assert.equal(cites.reasoning.visibleMode,'unknown');assert.equal(cites.items.length,1);assert.ok(toCsv(cites).includes('example.org'));
 await assert.rejects(extractVisibleDom({urlPrefix:'http://localhost/'}),/allowlisted/);
 const res=spawnSync(process.execPath,[resolve(root,'bin/rcc-consortium'),'transduce','--case=cli-check',`--text=${request}`],{cwd:d,encoding:'utf8'});
 assert.equal(res.status,0,res.stderr);const cli=JSON.parse(res.stdout);assert.equal(cli.ir.schema,'rcc.task-ir.v1');
 assert.ok(makePostmortem('cli-check').stepCount>=1);
 const srv=await startLocalServer({caseId:'cli-check',port:0});
 try{const health=await fetch(srv.url+'/health');assert.equal(health.status,200);const o=await health.json();assert.equal(o.writeAccess,false);assert.match(await (await fetch(srv.url+'/ascii')).text(),/ASCII PROCESS NETWORK/);assert.equal((await fetch(srv.url+'/notfound')).status,404);}finally{srv.server.close();}
 const state=resolve(d,'.devspace','rcc','broken','state.json');
 const {mkdirSync,existsSync}=await import('node:fs');mkdirSync(resolve(d,'.devspace','rcc','broken'),{recursive:true});writeFileSync(state,'{INVALID');
 assert.equal(repairCase('broken').status,'CORRUPT');
 const repaired=repairCase('broken',{apply:true});assert.equal(repaired.status,'QUARANTINED');assert.equal(existsSync(repaired.backup),true);assert.equal(existsSync(state),false);
 const bad=spawnSync(process.execPath,[resolve(root,'bin/rcc-consortium'),'doctor','--case=broken'],{cwd:d,encoding:'utf8'});assert.equal(bad.status,0);
 console.log(JSON.stringify({ok:true,tested:['verbatim-ir','prompt-patch','snippet-types','mode-proof-gate','citation-csv','origin-allowlist','cli-transduce','event-receipt','loopback-server','doctor']},null,2));
}finally{process.chdir(originalCwd);if(!d.startsWith(resolve(tmpdir(),'rcc-ir-selftest-')))throw Error('Unexpected fixture cleanup path');rmSync(d,{recursive:true,force:true,maxRetries:3,retryDelay:100});}
