import { spawnSync } from 'node:child_process';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=resolve(fileURLToPath(new URL('..',import.meta.url)));
const tests=[
 'scripts/runtime-selftest.mjs','scripts/provisioning-selftest.mjs','scripts/forwarding-selftest.mjs','scripts/ir-runtime-selftest.mjs','scripts/setup-doctor.mjs',
 'runtime/chatgpt-pro-line/scripts/cli-init-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/rooms-lifecycle-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/project-identity-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/room-fixtures-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/atomic-json-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/transport-negative-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/upload-metadata-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/non-interference-selftest.mjs',
 'runtime/chatgpt-pro-line/scripts/operation-boundary-selftest.mjs',
];
const result=[];
for(const name of tests){
 const r=spawnSync(process.execPath,[resolve(root,name)],{cwd:name.includes('runtime/chatgpt-pro-line')?resolve(root,'runtime/chatgpt-pro-line'):root,encoding:'utf8',maxBuffer:16*1024*1024});
 result.push({test:name,status:r.status===0?'PASS':'FAIL',error:r.status===0?'':(r.stderr||r.stdout).slice(-1000)});
}
console.log(JSON.stringify({ok:result.every(x=>x.status==='PASS'),tested:result.length,result},null,2));
if(result.some(x=>x.status!=='PASS'))process.exitCode=1;
