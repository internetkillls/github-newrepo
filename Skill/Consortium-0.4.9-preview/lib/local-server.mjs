import { createServer } from 'node:http';
import { resolve } from 'node:path';
import { existsSync } from 'node:fs';
import { readText,homeDir,makePostmortem } from './operations.mjs';

function ascii(caseId,events){
 const lines=[`+--- RCC ASCII PROCESS NETWORK : ${caseId.slice(0,32)} ---+`,'| Intake -> IR -> Evidence -> Router -> Worker(s) |','|                  |                         |','|                  +--> Verify --> Merge -----+'];
 for(const e of events.slice(-12))lines.push(`| ${String(e.kind).slice(0,23).padEnd(23)} ${String(e.status).slice(0,12).padEnd(12)} |`);
 lines.push('+-----------------------------------------------+');return lines.join('\n')+'\n';
}
export async function startLocalServer({caseId='default',port=0}={}){
 if(!Number.isInteger(port)||port<0||port>65535)throw new Error('Invalid port');
 const srv=createServer((req,res)=>{
   // Host must match loopback; no CORS or side-effect commands; local-only state reader.
   const host=req.headers.host||'';
   if(!/^127\.0\.0\.1:\d+$/.test(host)&&!/^localhost:\d+$/.test(host)){res.writeHead(403);res.end('Forbidden');return;}
   const route=(req.url||'').split('?')[0];
   if(req.method!=='GET'||!['/','/health','/ascii','/events','/postmortem'].includes(route)){res.writeHead(404);res.end('Not found');return;}
   const packet=makePostmortem(caseId);let body,ct;
   if(route==='/health') {body=JSON.stringify({ok:true,caseId,transport:'loopback',writeAccess:false});ct='application/json'}
   else if(route==='/events'||route==='/postmortem'){body=JSON.stringify(route==='/events'?packet.events:packet,null,2);ct='application/json'}
   else{body=ascii(caseId,packet.events);ct='text/plain; charset=utf-8'}
   res.writeHead(200,{'content-type':ct,'cache-control':'no-store','x-content-type-options':'nosniff','content-security-policy':"default-src 'none'"});res.end(body);
 });
 await new Promise((yes,no)=>{srv.once('error',no);srv.listen(port,'127.0.0.1',yes)});
 const addr=srv.address();return {server:srv,url:`http://127.0.0.1:${addr.port}`,caseId};
}
