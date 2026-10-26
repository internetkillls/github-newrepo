/** Committed queue snapshots. Caller must hold queue.lock for append. No browser actions. */
import {readdirSync,existsSync,mkdirSync,readFileSync} from 'node:fs';
import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import {writeTextExclusive} from './durable-record.mjs';
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
export const stateHash=x=>createHash('sha256').update(JSON.stringify(canonical(x))).digest('hex');
const recordHash=r=>{const {hash,...body}=r;return stateHash(body)};
const folder=dir=>resolve(dir,'queue-journal');
export function readQueueJournal(dir){
 const path=folder(dir);if(!existsSync(path))return null;
 const names=readdirSync(path).filter(n=>/^\d{8}\.json$/.test(n)).sort();
 if(names.length>10000)throw Error('journal.limit_requires_archival');
 let last=null;
 for(const name of names){
  const bytes=readFileSync(resolve(path,name));if(bytes.length>16*1024*1024)throw Error('journal.record_too_large');
  let r;try{r=JSON.parse(bytes.toString('utf8'))}catch{throw Error('journal.corrupt_record')}
  if(r.schema!=='rcc.queue.commit.v1'||r.sequence!==(last?.sequence||0)+1||name!==String(r.sequence).padStart(8,'0')+'.json'||r.previousHash!==(last?.hash||null)||r.hash!==recordHash(r)||!Number.isInteger(r.state?.revision)||r.state.revision!==r.beforeRevision+1||r.stateHash!==stateHash(r.state)||last&&(r.beforeRevision!==last.state.revision||r.beforeStateHash!==last.stateHash))throw Error('journal.invalid_chain');
  last=r;
 }
 return last;
}
export function effectiveQueueState(dir,projection){
 const last=readQueueJournal(dir);if(!last)return projection;
 if(projection&&(projection.caseId!==last.state.caseId||projection.revision>last.state.revision||projection.revision===last.state.revision&&stateHash(projection)!==last.stateHash))throw Error('journal.projection_conflict');
 if(projection&&projection.revision<last.state.revision){
  // Only a projection that exactly matches a committed predecessor (or bootstrap input) is recoverable.
  const hash=stateHash(projection);const path=folder(dir);const known=readdirSync(path).filter(n=>/^\d{8}\.json$/.test(n)).some(n=>{const r=JSON.parse(readFileSync(resolve(path,n),'utf8'));return r.stateHash===hash||r.beforeStateHash===hash});
  if(!known)throw Error('journal.unknown_projection');
 }
 return last.state;
}
export function appendQueueCommit(dir,before,after){
 const last=readQueueJournal(dir);
 if(after.revision!==before.revision+1||last&&stateHash(before)!==last.stateHash)throw Error('journal.writer_conflict');
 const sequence=(last?.sequence||0)+1;
 if(sequence>10000)throw Error('journal.limit_requires_archival');
 const body={schema:'rcc.queue.commit.v1',sequence,at:new Date().toISOString(),previousHash:last?.hash||null,beforeRevision:before.revision,beforeStateHash:stateHash(before),stateHash:stateHash(after),state:after};
 const record={...body,hash:stateHash(body)};
 const directory=folder(dir);mkdirSync(directory,{recursive:true,mode:0o700});const file=resolve(directory,String(sequence).padStart(8,'0')+'.json');
 if(existsSync(file))throw Error('journal.commit_already_exists');
 // The complete flushed temp file is linked exclusively; no transport runtime is required.
 if(!writeTextExclusive(file,JSON.stringify(record)+'\n'))throw Error('journal.commit_already_exists');return record;
}
