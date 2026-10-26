import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, copyFileSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=resolve(fileURLToPath(new URL('..',import.meta.url)));
const tmp=mkdtempSync(resolve(tmpdir(),'rcc-completion-fixture-'));
const script=resolve(tmp,'scripts/completion-guard-install.mjs');
const helper=resolve(tmp,'runtime/chatgpt-pro-line/src/completion-evidence.mjs');
const composer=resolve(tmp,'runtime/chatgpt-pro-line/src/chatgpt-composer.mjs');
for(const dir of [resolve(tmp,'scripts'),resolve(tmp,'runtime/chatgpt-pro-line/src')])mkdirSync(dir,{recursive:true});
copyFileSync(resolve(root,'scripts/completion-guard-install.mjs'),script);
copyFileSync(resolve(root,'runtime/chatgpt-pro-line/src/completion-evidence.mjs'),helper);
const source=`import { now, sleep, evaluate } from './cdp-client.mjs';
export async function waitForSubmission(cdp, opts) { return { submitted:false }; }
export async function submitPrompt(cdp, opts) { return null; }
export async function waitForReadyProbe(cdp) { return null; }
function cleanAssistantText(s){return String(s||'').trim();}
function isProgressPlaceholder(){return false;}
async function generationState(cdp) { return { active:false }; }
export async function waitForAssistantResponse(cdp) { return null; }
export async function waitForAssistantResponseAfterUser(cdp, userMessage) {
  const error = new Error('Old behavior');
  error.errorCode = 'old';
  throw error;
}`;
function run(args){return spawnSync(process.execPath,[script,...args],{encoding:'utf8'});}
try{
 writeFileSync(composer,source);
 const dry=run([]);assert.equal(dry.status,0,dry.stderr);assert.equal(readFileSync(composer,'utf8'),source);
 const applied=run(['--apply']);assert.equal(applied.status,0,applied.stderr);
 const modified=readFileSync(composer,'utf8');
 assert.match(modified,/CompletionEvidence/);assert.match(modified,/send.submission_uncertain/);assert.match(modified,/response.completion_uncertain/);
 assert.doesNotMatch(modified,/anchored_dom_stable/);
 const idem=run(['--apply']);assert.equal(idem.status,0,idem.stderr);assert.equal(readFileSync(composer,'utf8'),modified);
 const check=spawnSync(process.execPath,['--check',composer],{encoding:'utf8'});assert.equal(check.status,0,check.stderr);
 console.log(JSON.stringify({ok:true,tests:['dry-run-no-mutation','apply','no-reclick-after-click','anchored-evidence','syntax','idempotent']},null,2));
}finally{rmSync(tmp,{recursive:true,force:true});}
