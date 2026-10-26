import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { CdpSession, connectToPage } from '../src/cdp-client.mjs';
import { doctorWarm } from '../src/chatgpt-doctor.mjs';
import { assertSelectedChoices } from '../src/chatgpt-choices.mjs';

let targets = [];
let rejectCreation = true;
const server = createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  if (req.url === '/json/version') return res.end('{}');
  if (req.url.startsWith('/json/new')) {
    res.statusCode = rejectCreation ? 503 : 200;
    return res.end(JSON.stringify(rejectCreation ? {} : targets[0]));
  }
  res.end(JSON.stringify(targets));
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const port = server.address().port;
const originalOpen = CdpSession.open;
let connections = [];
CdpSession.open = async url => { connections.push(url); return { url }; };
const options = { matchUrl: 'https://chatgpt.com/', retries: 1, delayMs: 0 };
try {
  await assert.rejects(connectToPage(port, options), {errorCode: 'browser.target_unavailable'});
  targets = [{type:'page',url:'https://example.com/',webSocketDebuggerUrl:'ws://other'}];
  await assert.rejects(connectToPage(port, options), {errorCode:'browser.target_unavailable'});
  assert.equal(connections.length, 0, 'Must not connect to unrelated tab');
  await assert.rejects(doctorWarm({port}), {errorCode:'browser.target_unavailable'});
  targets = [{type:'page',url:'https://chatgpt.com/',webSocketDebuggerUrl:'ws://wanted'}];
  assert.equal((await connectToPage(port, options)).url, 'ws://wanted');
  assert.equal((await doctorWarm({port})).browser.targetFound, true);
  targets = [];
  rejectCreation = false;
  await assert.rejects(doctorWarm({port}), {errorCode:'browser.target_unavailable'});
  const observed = {intelligence:{current:'High'},model:{current:'Sol test'}};
  assertSelectedChoices(observed, {level:'High',model:'Sol test'});
  assert.throws(() => assertSelectedChoices(observed, {level:'Low'}), {errorCode:'model.selection_unverified'});
  assert.throws(() => assertSelectedChoices(observed, {model:'Sol unavailable'}), {errorCode:'model.selection_unverified'});
  assert.throws(() => assertSelectedChoices({}, {model:'Sol test'}), {errorCode:'model.selection_unverified'});
} finally {
  CdpSession.open = originalOpen;
  await new Promise(resolve => server.close(resolve));
}
await assert.rejects(connectToPage(port, options), {errorCode:'browser.cdp_unreachable'});
console.log(JSON.stringify({ok:true,tested:['missing-target','unrelated-tab-refused','warm-create-failure','warm-invalid-target','positive-target','positive-selection','wrong-level','wrong-model','missing-readback','offline-endpoint']}));

const {uploadEvidenceReady}=await import("../src/chatgpt-upload.mjs");
assert.equal(uploadEvidenceReady(["a.md"],[{aria:"Uploading a.md"}]),false);
assert.equal(uploadEvidenceReady(["a.md"],[{aria:"Failed a.md"}]),false);
assert.equal(uploadEvidenceReady(["a.md"],[]),false);
assert.equal(uploadEvidenceReady(["a.md"],[{aria:"Remove a.md"}]),true);
console.log(JSON.stringify({ok:true,tested:["upload-pending-rejected","upload-failed-rejected","upload-absent-rejected","upload-ready"]}));
