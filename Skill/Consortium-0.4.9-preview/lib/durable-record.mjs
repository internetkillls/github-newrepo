import {mkdirSync,writeFileSync,openSync,closeSync,fsyncSync,linkSync,unlinkSync} from 'node:fs';
import {dirname} from 'node:path';import {randomUUID} from 'node:crypto';
/** Commit a fully flushed immutable record without overwriting any prior writer. */
export function writeTextExclusive(file,text){
 mkdirSync(dirname(file),{recursive:true,mode:0o700});const tmp=file+'.'+randomUUID()+'.tmp';
 try{
  const fd=openSync(tmp,'wx',0o600);try{writeFileSync(fd,text);fsyncSync(fd)}finally{closeSync(fd)}
  try{linkSync(tmp,file);return true}catch(e){if(e.code==='EEXIST')return false;throw e}
 }finally{try{unlinkSync(tmp)}catch(e){if(e.code!=='ENOENT')throw e}}
}
