import {openSync,closeSync,readFileSync,statSync} from 'node:fs';import {spawn} from 'node:child_process';
/** Child writes directly to owned log files, so output survives delivery-controller death. */
export function runDurableDiagnostic(command,args,{cwd,input,timeoutMs,stdoutFile,stderrFile,onSpawn=()=>{}}={}){
 const out=openSync(stdoutFile,'wx',0o600);let err;
 try{err=openSync(stderrFile,'wx',0o600)}catch(e){closeSync(out);throw e}
 return new Promise(resolve=>{
  let child,started=false,finished=false,timer,monitor,stoppedFor=null;
  const finish=(code,error=null,signal=null)=>{
   if(finished)return;finished=true;clearTimeout(timer);clearInterval(monitor);
   const read=p=>{try{return statSync(p).size<=2*1024*1024?readFileSync(p,'utf8'):''}catch{return ''}};
   resolve({code,error:error?String(error):stoppedFor,signal,started,stdout:read(stdoutFile),stderr:read(stderrFile)});
  };
  try{child=spawn(command,args,{cwd,windowsHide:true,stdio:['pipe',out,err]})}catch(e){closeSync(out);closeSync(err);finish(null,e.message);return}
  closeSync(out);closeSync(err);
  child.once('spawn',()=>{started=true;try{onSpawn(child.pid)}catch(e){stoppedFor='diagnostic.claim_write_failed';child.kill()}});
  child.once('error',e=>finish(e.code||null,e.message));child.once('exit',(code,signal)=>finish(code,null,signal));
  child.stdin.on('error',()=>{});child.stdin.end(input);
  timer=setTimeout(()=>{stoppedFor='diagnostic.deadline_exceeded';child.kill()},timeoutMs);
  monitor=setInterval(()=>{try{if(statSync(stdoutFile).size>2*1024*1024||statSync(stderrFile).size>2*1024*1024){stoppedFor='diagnostic.output_limit';child.kill()}}catch{}},250);
 });
}
