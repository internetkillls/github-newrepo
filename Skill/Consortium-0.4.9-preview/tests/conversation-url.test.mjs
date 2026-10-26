import test from 'node:test';import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';import {spawnSync} from 'node:child_process';import {fileURLToPath} from 'node:url';
import {parseChatGptUrl,conversationIdFromUrl,sameConversationUrl,uniqueConversationTarget} from '../runtime/chatgpt-pro-line/src/conversation-url.mjs';
import {conversationId,reconcileBindings} from '../lib/recovery-inspect.mjs';

test('shared grammar accepts supported committed identities including legacy references and query changes',()=>{
 for(const url of ['https://chatgpt.com/c/one','https://chatgpt.com/c/one/?q=2#anchor','https://chatgpt.com:443/c/one','https://chat.openai.com/c/one']){assert.equal(conversationIdFromUrl(url),'one');assert.equal(conversationId(url),'one')}
 assert.equal(conversationIdFromUrl('https://chatgpt.com/g/g-example/c/one'),'one');
 assert(sameConversationUrl('https://chat.openai.com/c/one','https://chatgpt.com/c/one#different'));
 assert(!sameConversationUrl('https://chatgpt.com/g/a/c/one','https://chatgpt.com/g/b/c/one'));
 assert(!sameConversationUrl('https://chatgpt.com/g/a/c/one','https://chatgpt.com/c/one'));
});
test('identity grammar rejects unsafe origins, normalized paths, unsupported routes and encoded identities',()=>{
 for(const url of ['http://chatgpt.com/c/one','https://other.chatgpt.com/c/one','https://chatgpt.com.example.invalid/c/one','https://fixture:fixture@chatgpt.com/c/one','https://chatgpt.com:444/c/one','https://chatgpt.com/c/one/other','https://chatgpt.com/c/one%2Ftwo','https://chatgpt.com/c/%2e%2e/one','https://chatgpt.com/c/a/../one','https://chatgpt.com\\c\\one',' https://chatgpt.com/c/one','https://chatgpt.com/c/one\n','https://chatgpt.com/g/a/project','file:///c/one']){assert.equal(parseChatGptUrl(url),null,url);assert.equal(conversationId(url),null,url)}
 assert.equal(parseChatGptUrl('https://chatgpt.com/').kind,'uncommitted');
 assert.equal(conversationIdFromUrl('https://chatgpt.com/'),'');
});
test('duplicate targets never use a saved transient hint to bypass ambiguity',()=>{
 assert.equal(parseChatGptUrl('https://@chatgpt.com/c/one'),null);
 const url='https://chatgpt.com/c/one',targets=[{id:'old',type:'page',url},{id:'new',type:'page',url}];
 assert.throws(()=>uniqueConversationTarget(targets,url),e=>e.errorCode==='room.target_ambiguous');
 assert.equal(reconcileBindings({workers:[{targetId:'old',url}]},targets)[0].status,'AMBIGUOUS');
 assert.equal(uniqueConversationTarget([{type:'page',id:'wrong-scope',url:'https://chatgpt.com/g/a/c/one'}],url),null);
});

test('actual vendor resolver rejects duplicate, invalid and changed-uncommitted bindings before any activation/open',()=>{
 const root=mkdtempSync(join(tmpdir(),'rcc-url-resolver-'));
 try{
 const moduleUrl=new URL('../runtime/chatgpt-pro-line/src/chatgpt-sessions.mjs',import.meta.url).href;
 const script=`import assert from 'node:assert/strict';import {readFileSync,writeFileSync} from 'node:fs';
 const mod=await import(${JSON.stringify(moduleUrl)});
 const page=(id,url)=>({id,url,type:'page',webSocketDebuggerUrl:'ws://127.0.0.1:9222/devtools/page/'+id});
 let pages=[page('old','https://chatgpt.com/c/one')],effects=[];
 globalThis.fetch=async uri=>{const u=new URL(uri);if(u.pathname==='/json')return {ok:true,json:async()=>pages};effects.push(u.pathname);return {ok:true,json:async()=>({})}};
 await mod.aliasChatGptSession(9222,{name:'worker',targetId:'old'});
 `;
 // Keep parity expectations literal: the module shares the parser, without source extraction.
 const body=script+`
 assert.equal(mod.conversationIdFromUrl('https://chat.openai.com/c/one'),'one');
 assert.equal(mod.conversationIdFromUrl('http://chatgpt.com/c/one'),'');
 pages.push(page('new','https://chatgpt.com/c/one'));
 await assert.rejects(mod.resolveVerifiedRoomTarget(9222,'worker'),e=>e.errorCode==='room.target_ambiguous');assert.equal(effects.length,0);
 await assert.rejects(mod.resolveChatGptSession(9222,'worker'),e=>e.errorCode==='room.target_ambiguous');
 await assert.rejects(mod.aliasChatGptSession(9222,{name:'duplicate',conversationUrl:'https://chatgpt.com/c/one'}),e=>e.errorCode==='room.target_ambiguous');
 await assert.rejects(mod.rebindChatGptSessionAlias(9222,{name:'worker',conversationUrl:'https://chatgpt.com/c/one'}),e=>e.errorCode==='room.target_ambiguous');assert.equal(effects.length,0);
 pages=[page('new','https://chatgpt.com/c/one')];
 assert.equal((await mod.resolveVerifiedRoomTarget(9222,'worker')).target.id,'new');assert.equal(effects.length,1);effects=[];
 const registry=JSON.parse(readFileSync(mod.sessionRegistryPath));registry.rooms.worker.activeConversationUrl='https://chatgpt.com/c/one/other';writeFileSync(mod.sessionRegistryPath,JSON.stringify(registry));
 await assert.rejects(mod.resolveVerifiedRoomTarget(9222,'worker'),e=>e.errorCode==='room.conversation_url_invalid');assert.equal(effects.length,0);
 pages=[page('blank','https://chatgpt.com/')];await mod.aliasChatGptSession(9222,{name:'blank-worker',targetId:'blank'});
 pages=[page('blank','https://chatgpt.com/c/already-sent')];
 await assert.rejects(mod.resolveVerifiedRoomTarget(9222,'blank-worker'),e=>e.errorCode==='room.uncommitted_target_changed');assert.equal(effects.length,0);
 let opens=0;globalThis.fetch=async(uri,opts)=>{if(new URL(uri).pathname==='/json/new'){opens++;assert.equal(opts.method,'PUT');throw Error('lost create acknowledgement')}return {ok:true,json:async()=>pages}};
 await assert.rejects(mod.newChatGptSession(9222,{bind:false}),e=>e.automaticRetryAllowed===false&&e.remoteOutcome==='unknown');assert.equal(opens,1);
 console.log('resolver fixture: verified');`;
 const file=join(root,'fixture.mjs');writeFileSync(file,body);
 const r=spawnSync(process.execPath,[file],{cwd:root,env:{...process.env,CHATGPT_REPO_ROOT:root,CHATGPT_PRO_HOME:join(root,'private-home')},encoding:'utf8',timeout:10000,windowsHide:true});
 assert.equal(r.status,0,r.stderr);assert.match(r.stdout,/resolver fixture: verified/);
 }finally{rmSync(root,{recursive:true,force:true,maxRetries:3,retryDelay:100})}
});
