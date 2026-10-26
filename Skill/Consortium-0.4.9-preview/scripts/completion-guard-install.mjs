#!/usr/bin/env node
/** One-time guarded local patch for RCC's vendored chatgpt-pro-line.
 * Default: dry-run. --apply modifies source with a timestamped backup.
 * A published overlay alone does not activate this patch on existing local installs.
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const target = resolve(root, 'runtime/chatgpt-pro-line/src/chatgpt-composer.mjs');
const helper = resolve(root, 'runtime/chatgpt-pro-line/src/completion-evidence.mjs');
const shouldApply = process.argv.includes('--apply');
const isCheck = process.argv.includes('--check');
if (!existsSync(target) || !existsSync(helper)) {
  console.error(JSON.stringify({ok:false,code:'completion.patch_sources_unavailable',target,helper}));
  process.exit(2);
}
let source = readFileSync(target, 'utf8');
const marker = 'import { CompletionEvidence } from "./completion-evidence.mjs";';
if (source.includes(marker)) {
  console.log(JSON.stringify({ok:true,status:'already_applied',target}));
  process.exit(0);
}
function replaceBetween(text, start, end, replacement) {
  const i = text.indexOf(start);
  const j = i < 0 ? -1 : text.indexOf(end, i + start.length);
  if (i < 0 || j < 0 || text.indexOf(start, i+1) !== -1 || text.indexOf(end, j+1) !== -1) {
    throw new Error(`completion.patch_anchor_mismatch: ${start.slice(0,60)} / ${end.slice(0,60)}`);
  }
  return text.slice(0,i) + replacement + '\n\n' + text.slice(j);
}
const waitSubmission = `export async function waitForSubmission(cdp, { initialUserCount, timeoutMs = 8_000 }) {
  const startedAt = now();
  let lastProbe = null;
  while (now() - startedAt < timeoutMs) {
    lastProbe = await pageProbe(cdp);
    if (lastProbe.userTurns.length > initialUserCount) return { submitted: true, probe: lastProbe };
    await sleep(250);
  }
  return { submitted: false, probe: lastProbe };
}`;
const safeSubmit = `export async function submitPrompt(cdp, { composer, initialUserCount, responseToken = "", attempts = 3 }) {
  const submitAttempts = [];
  for (let attempt = 1; attempt <= attempts; attempt++) {
    const clicked = await clickComposerSendButton(cdp);
    submitAttempts.push({ attempt, clicked: Boolean(clicked?.clicked), label: clicked?.label || "" });
    if (!clicked?.clicked) {
      await sleep(500);
      continue;
    }
    // A successful click crosses the uncertain side-effect boundary.
    // Never click again merely because the echo has not appeared yet.
    const acknowledged = await waitForSubmission(cdp, { initialUserCount });
    if (acknowledged.submitted) return { ...clicked, attempts: submitAttempts };
    const error = new Error("Send button clicked, but no new user turn was observed; submission uncertain.");
    error.errorCode = "send.submission_uncertain";
    error.details = { attempts: submitAttempts, observedUserTurnCount: acknowledged.probe?.userTurns?.length ?? null };
    throw error;
  }
  const error = new Error("ChatGPT send button was not found or was disabled.");
  error.errorCode = "page.send_button_not_found";
  error.details = { attempts: submitAttempts };
  throw error;
}`;
const generation = `async function generationState(cdp) {
  return evaluate(cdp, \`(() => {
    const visible = (el) => { const r=el.getBoundingClientRect(); const s=getComputedStyle(el); return r.width>0 && r.height>0 && s.visibility!=="hidden" && s.display!=="none"; };
    const buttons = [...document.querySelectorAll('button')].filter(visible);
    const labels = buttons.map(b => [b.innerText, b.getAttribute('aria-label'), b.title, b.getAttribute('data-testid')].filter(Boolean).join(' ').trim());
    const thinking = [...document.querySelectorAll('div, span, p')].filter(visible).some(el => /^(pro thinking|reading documents|thinking|working)$/i.test((el.innerText||'').trim()));
    const active = thinking || labels.some(label => /stop answering|stop generating|interrupt|cancel response|stop streaming/i.test(label));
    const assistants = [...document.querySelectorAll('[data-message-author-role="assistant"]')];
    const latest = assistants.at(-1);
    const turn = latest?.closest('article') || latest?.parentElement?.parentElement || null;
    const finalActions = turn ? [...turn.querySelectorAll('button')].filter(visible).map(b => [b.getAttribute('aria-label'), b.getAttribute('data-testid'), b.title].filter(Boolean).join(' ')) : [];
    const terminal = finalActions.some(label => /copy.turn|copy.turn.action|copy response|regenerate response|thumbs.up|thumbs.down/i.test(label));
    return { active, terminal, labels: labels.filter(x => /stop|interrupt|thinking|reading documents/i.test(x)) };
  })()\`);
}`;
const anchoredWait = `export async function waitForAssistantResponseAfterUser(cdp, userMessage, {
  timeoutMs = 240_000,
  stableMs = 4_000,
} = {}) {
  const startedAt = now();
  const guard = new CompletionEvidence({ stableMs });
  let lastSnapshot = [];
  let lastText = '';
  let lastEvidence = null;
  while (now() - startedAt < timeoutMs) {
    lastSnapshot = await snapshotConversationMessages(cdp);
    const run = assistantRunAfterUser(lastSnapshot, userMessage);
    const rawText = run.text;
    lastText = cleanAssistantText(rawText);
    const state = await generationState(cdp).catch(() => ({ active: null, terminal: false }));
    lastEvidence = guard.observe({
      at: now(),
      text: lastText,
      active: state.active,
      terminal: Boolean(state.terminal),
      bound: Boolean(run.last || run.first),
      placeholder: isProgressPlaceholder(rawText),
    });
    if (lastEvidence.completed) {
      // Final readback rejects a changed response or renewed generation.
      const snapshot = await snapshotConversationMessages(cdp);
      const confirmed = assistantRunAfterUser(snapshot, userMessage);
      const probe = await generationState(cdp).catch(() => ({ active: null }));
      if (cleanAssistantText(confirmed.text) === lastText && probe.active === false) {
        return {
          probe: await pageProbe(cdp),
          snapshot,
          assistantMessage: confirmed.last || confirmed.first,
          assistantRun: confirmed,
          assistantText: lastText,
          stableMs: lastEvidence.stableForMs,
          finishDetectedBy: lastEvidence.reason,
          completionEvidence: lastEvidence,
        };
      }
      guard.polls = 0;
      guard.completed = false;
      guard.firstCandidateAt = null;
    }
    await sleep(750);
  }
  const error = new Error('Generation completion could not be verified for the anchored assistant response.');
  error.errorCode = 'response.completion_uncertain';
  error.details = { timeoutMs, userOrdinal: userMessage.ordinal, observedMessageCount: lastSnapshot.length,
    partialAssistantTextLength: lastText.length, completionEvidence: lastEvidence };
  throw error;
}`;
try {
  if (!source.includes('export async function waitForSubmission(') || !source.includes('export async function waitForAssistantResponseAfterUser(')) throw new Error('completion.unsupported_runtime_version');
  source = replaceBetween(source, 'export async function waitForSubmission(', 'export async function submitPrompt(', waitSubmission);
  source = replaceBetween(source, 'export async function submitPrompt(', 'export async function waitForReadyProbe(', safeSubmit);
  source = replaceBetween(source, 'async function generationState(cdp) {', 'export async function waitForAssistantResponse(', generation);
  const anchor = 'export async function waitForAssistantResponseAfterUser(';
  const finalStart = source.indexOf(anchor);
  if (finalStart < 0 || source.indexOf(anchor,finalStart+1) !== -1) throw new Error('completion.anchored_wait_not_unique');
  if (source.slice(finalStart).trim().endsWith('throw error;\n}') === false) throw new Error('completion.unexpected_tail');
  source = source.slice(0, finalStart) + anchoredWait + '\n';
  source = marker + '\n' + source;
  if (!shouldApply) {
    console.log(JSON.stringify({ok:true,status:'dry_run',target,code:'completion.patch_available',wouldChange:['submission_ambiguity','generation_state','anchored_completion'],note:'Use --apply to create a timestamped backup and patch local runtime.'}));
    process.exit(0);
  }
  const backup = target + '.backup-' + new Date().toISOString().replace(/[:.]/g,'-');
  writeFileSync(backup, readFileSync(target));
  writeFileSync(target, source);
  try { execFileSync(process.execPath, ['--check', target], { stdio:'pipe' }); }
  catch(error) { writeFileSync(target, readFileSync(backup)); throw new Error('completion.syntax_check_failed: ' + String(error.stderr||error.message)); }
  console.log(JSON.stringify({ok:true,status:'applied',target,backup}));
} catch(error) {
  console.error(JSON.stringify({ok:false,error:String(error.message||error),target}));
  process.exit(1);
}
