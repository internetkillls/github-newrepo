import {createHash} from 'node:crypto';import {readFileSync,existsSync,mkdirSync,realpathSync,lstatSync} from 'node:fs';import {resolve,relative,isAbsolute} from 'node:path';
import {writeTextExclusive} from './durable-record.mjs';
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
export function safeOutputPath(path){
 if(typeof path!=='string'||!path||path.length>240||path.startsWith('/')||path.includes('\\')||path.includes(':')||path.split('/').some(p=>!p||p==='.'||p==='..'||p==='.git'||/[. ]$/.test(p)||/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(p)))throw Error('output.unsafe_path');return path;
}
export function normalizeOutputContract(value){
 if(value===null||value===undefined)return null;
 if(value.schema!=='rcc.output-contract.v1'||!['response','files','json'].includes(value.mode)||Object.keys(value).some(k=>!['schema','mode','required','path','schemaId','identity','maxBytes'].includes(k)))throw Error('output.invalid_contract');
 if(value.mode==='json'){
  const path=safeOutputPath(value.path),maxBytes=value.maxBytes??65536,identity=value.identity??{};
  if(typeof value.schemaId!=='string'||!value.schemaId||value.schemaId.length>200||!Number.isInteger(maxBytes)||maxBytes<1||maxBytes>1048576||!identity||Array.isArray(identity)||typeof identity!=='object'||Object.keys(identity).length>20||Object.values(identity).some(v=>!['string','number','boolean'].includes(typeof v))||value.required?.length)throw Error('output.invalid_json_contract');
  return {schema:value.schema,mode:'json',path,schemaId:value.schemaId,identity,maxBytes};
 }
 if(['path','schemaId','identity','maxBytes'].some(k=>Object.hasOwn(value,k)))throw Error('output.json_fields_require_explicit_json_mode');
 const required=value.required||[];if(!Array.isArray(required)||required.length>100||value.mode==='files'&&!required.length||value.mode==='response'&&required.length)throw Error('output.invalid_required_set');
 const names=required.map(safeOutputPath);if(new Set(names.map(p=>p.toLowerCase())).size!==names.length)throw Error('output.duplicate_required_path');
 return {schema:value.schema,mode:value.mode,required:names};
}
function decode(base64,hash){if(typeof base64!=='string'||base64.length>48*1024*1024||!/^[A-Za-z0-9+/]*={0,2}$/.test(base64)||base64.length%4)throw Error('output.invalid_base64');const bytes=Buffer.from(base64,'base64');if(bytes.toString('base64')!==base64||!/^[a-f0-9]{64}$/.test(hash||'')||sha(bytes)!==hash)throw Error('output.hash_mismatch');return bytes;}
export function decodeDeliveryBlocks(blocks){
 if(!Array.isArray(blocks)||blocks.length>200)throw Error('output.invalid_block_set');
 if(blocks.reduce((n,s)=>n+(typeof s==='string'?s.length:0),0)>48*1024*1024)throw Error('output.delivery_too_large');
 const files=new Map(),chunks=new Map();let total=0;
 const add=(path,bytes)=>{safeOutputPath(path);if(files.has(path.toLowerCase()))throw Error('output.duplicate_file');total+=bytes.length;if(total>32*1024*1024)throw Error('output.delivery_too_large');files.set(path.toLowerCase(),{path,bytes});};
 for(const raw of blocks){if(typeof raw!=='string'||raw.length>48*1024*1024)throw Error('output.invalid_block');let v;try{v=JSON.parse(raw.replace(/^json\s*/i,''))}catch{continue}
  if(v.rcc_delivery==='v1'){
   if(!Array.isArray(v.files)||v.files.length>100)throw Error('output.invalid_file_set');for(const f of v.files)add(f.path,decode(f.content_base64,f.sha256));
  }else if(['rcc.file-chunk.v1','paperfold.file-chunk.v1'].includes(v.schema)){
   safeOutputPath(v.path);if(!Number.isInteger(v.index)||!Number.isInteger(v.total)||v.total<1||v.total>200||v.index<0||v.index>=v.total||!/^[a-f0-9]{64}$/.test(v.fileSha256||''))throw Error('output.invalid_chunk');
   const key=v.path.toLowerCase(),prior=chunks.get(key)||{path:v.path,total:v.total,hash:v.fileSha256,parts:new Map()};
   if(prior.path!==v.path||prior.total!==v.total||prior.hash!==v.fileSha256||prior.parts.has(v.index))throw Error('output.chunk_conflict');
   const bytes=decode(v.content_base64,v.chunkSha256);prior.parts.set(v.index,bytes);chunks.set(key,prior);
   if([...chunks.values()].reduce((n,c)=>n+[...c.parts.values()].reduce((s,b)=>s+b.length,0),0)>32*1024*1024)throw Error('output.delivery_too_large');
  }
 }
 for(const c of chunks.values()){if(c.parts.size!==c.total)throw Error('output.incomplete_chunks');const bytes=Buffer.concat(Array.from({length:c.total},(_,i)=>c.parts.get(i)));if(sha(bytes)!==c.hash)throw Error('output.hash_mismatch');add(c.path,bytes);}
 return [...files.values()];
}
function inside(root,file){const rel=relative(root,file);if(rel.startsWith('..')||isAbsolute(rel))throw Error('output.path_escape');}
export function captureOutputs(contract,blocks,directory){
 const spec=normalizeOutputContract(contract);if(!spec)throw Error('output.contract_required');if(spec.mode==='response')return {mode:'response',files:[],scope:'Response only; no artifact delivery or content correctness asserted'};
 let selected;
 if(spec.mode==='json'){
  if(!Array.isArray(blocks)||blocks.length>200||blocks.some(s=>typeof s!=='string'||s.length>2*1048576)||blocks.reduce((n,s)=>n+s.length,0)>2*1048576)throw Error('output.invalid_block_set');
  const matches=blocks.flatMap(raw=>{try{const text=raw.replace(/^json\s*/i,''),v=JSON.parse(text);return v&&v.schema===spec.schemaId?[{text,v}]:[]}catch{return []}});
  if(matches.length!==1)throw Error('output.exactly_one_json_response_required');
  const {text,v}=matches[0],bytes=Buffer.from(text,'utf8');
  if(bytes.length>spec.maxBytes||Object.entries(spec.identity).some(([k,value])=>v[k]!==value))throw Error('output.json_identity_or_size_mismatch');
  selected=[{path:spec.path,bytes}]; // exact response bytes, new host-computed hash
 }else{
  const decoded=decodeDeliveryBlocks(blocks),map=new Map(decoded.map(f=>[f.path.toLowerCase(),f]));
  selected=spec.required.map(path=>{const f=map.get(path.toLowerCase());if(!f||f.path!==path)throw Error('output.required_file_missing: '+path);return f;});
 }
 // Verify the entire required set before publishing any file; never execute or unzip payloads.
 mkdirSync(directory,{recursive:true,mode:0o700});const root=realpathSync(directory);const files=[];
 for(const f of selected){const file=resolve(directory,f.path);inside(resolve(directory),file);mkdirSync(resolve(file,'..'),{recursive:true,mode:0o700});inside(root,realpathSync(resolve(file,'..')));
  if(existsSync(file)&&lstatSync(file).isSymbolicLink())throw Error('output.symlink_rejected');
  if(!writeTextExclusive(file,f.bytes)&&sha(readFileSync(file))!==sha(f.bytes))throw Error('output.existing_file_conflict');
  inside(root,realpathSync(file));files.push({path:f.path,bytes:f.bytes.length,sha256:sha(f.bytes)});
 }
 return {mode:'files',directory:resolve(directory),files,scope:'Required local file bytes/hash verified; content correctness not certified'};
}
export function recheckOutputs(result){
 if(result?.mode==='response')return true;if(result?.mode!=='files'||!Array.isArray(result.files)||!result.files.length)throw Error('output.invalid_captured_set');
 const root=realpathSync(result.directory);for(const f of result.files){safeOutputPath(f.path);const file=resolve(result.directory,f.path);inside(root,realpathSync(file));if(lstatSync(file).isSymbolicLink())throw Error('output.symlink_rejected');const bytes=readFileSync(file);if(bytes.length!==f.bytes||sha(bytes)!==f.sha256)throw Error('output.changed_after_capture');}return true;
}
