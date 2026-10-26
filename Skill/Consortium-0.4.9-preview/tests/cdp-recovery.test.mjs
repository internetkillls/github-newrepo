import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {createHash} from 'node:crypto';
import {CdpSession} from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';
class Socket extends EventTarget {
  sent=[]; close(){this.dispatchEvent(new Event('close'));}
  send(s){this.sent.push(JSON.parse(s));}
  reply(id,result){const e=new Event('message');e.data=JSON.stringify({id,result});this.dispatchEvent(e);}
}
test('healthy reply settles and removes pending entry',async()=>{const s=new Socket(),c=new CdpSession(s);const p=c.send('Probe');s.reply(1,{ok:true});assert.deepEqual(await p,{ok:true});assert.equal(c.pending.size,0);await c.close();});
for(const event of ['close','error']) test(event+' rejects every pending request',async()=>{const s=new Socket(),c=new CdpSession(s);const checks=[c.send('A'),c.send('B')].map(p=>assert.rejects(p,e=>e.automaticResendAllowed===false&&e.remoteOutcome==='unknown'));s.dispatchEvent(new Event(event));await Promise.all(checks);assert.equal(c.pending.size,0);assert.equal(c.closed,true);await assert.rejects(c.send('C'));assert.equal(s.sent.length,2);});
test('explicit close rejects pending and is repeatable',async()=>{const c=new CdpSession(new Socket());const p=assert.rejects(c.send('A'),{errorCode:'browser.cdp_closed'});await c.close();await c.close();await p;assert.equal(c.pending.size,0);});
test('deadline rejects once and late reply is ignored',async()=>{const s=new Socket(),c=new CdpSession(s);await assert.rejects(c.send('A',{}, {timeoutMs:5}),{errorCode:'browser.cdp_command_timeout'});s.reply(1,{late:true});assert.equal(c.pending.size,0);const p=c.send('B');s.reply(2,{ok:1});assert.deepEqual(await p,{ok:1});await c.close();});
test('cancel before send has no socket action; cancel after send never retries',async()=>{const s=new Socket(),c=new CdpSession(s),a=new AbortController();a.abort();await assert.rejects(c.send('A',{}, {signal:a.signal}));assert.equal(s.sent.length,0);const b=new AbortController(),p=assert.rejects(c.send('B',{}, {signal:b.signal}),{errorCode:'browser.cdp_aborted'});b.abort();await p;assert.equal(c.pending.size,0);assert.equal(s.sent.length,1);await c.close();});
test('synchronous send exception cleans pending',async()=>{const s=new Socket();s.send=()=>{throw Error('closed')};const c=new CdpSession(s);await assert.rejects(c.send('A'),{errorCode:'browser.cdp_send_failed'});assert.equal(c.pending.size,0);await c.close();});
test('open timeout closes unconnected socket; pre-abort never constructs socket',async()=>{let n=0;class Never extends Socket{constructor(){super();n++}}await assert.rejects(CdpSession.open('ws://unused',{WebSocketImpl:Never,timeoutMs:5}),{errorCode:'browser.cdp_connect_timeout'});const a=new AbortController();a.abort();await assert.rejects(CdpSession.open('ws://unused',{WebSocketImpl:Never,signal:a.signal}));assert.equal(n,1);});
test('real loopback WebSocket disconnect rejects pending command',async()=>{
 const server=createServer();let socket;
 server.on('upgrade',(req,s)=>{socket=s;const accept=createHash('sha1').update(req.headers['sec-websocket-key']+'258EAFA5-E914-47DA-95CA-C5AB0DC85B11').digest('base64');s.write('HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: '+accept+'\r\n\r\n');});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));let c;
 try{c=await CdpSession.open('ws://127.0.0.1:'+server.address().port);const p=assert.rejects(c.send('Runtime.evaluate'),e=>['browser.cdp_closed','browser.cdp_socket_error'].includes(e.errorCode));socket.destroy();await p;assert.equal(c.pending.size,0);}
 finally{await c?.close();socket?.destroy();await new Promise(r=>server.close(r));}
});
