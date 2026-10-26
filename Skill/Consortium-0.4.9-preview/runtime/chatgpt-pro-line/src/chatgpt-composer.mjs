import {conversationMessageNodes} from './message-nodes.mjs';
import { CompletionEvidence } from "./completion-evidence.mjs";
import { evaluate, now, sleep } from "./cdp-client.mjs";
import { pageProbe } from "./chatgpt-page.mjs";
import {
  assistantRunAfterUser,
  findNewUserMessage,
  expandUserMessage,
  findAssistantAfterUser,
  normalizeMessageText,
  snapshotConversationMessages,
} from "./chatgpt-messages.mjs";

export function findExactTokenTurn(turns, token) {
  return turns.find((turn) =>
    String(turn)
      .split(/\n+/)
      .some((line) => line.trim() === token),
  );
}

export async function inputPrompt(cdp, composer, prompt) {
  const beforeClear = await composerText(cdp).catch(() => "");
  await clearComposer(cdp);
  const afterClear = await composerText(cdp).catch(() => "");
  if (afterClear.trim()) {
    const error = new Error("ChatGPT composer could not be cleared before typing.");
    error.errorCode = "composer.clear_failed";
    error.details = {
      beforeClearCharCount: beforeClear.length,
      afterClearCharCount: afterClear.length,
    };
    throw error;
  }
  await focusComposer(cdp);
  let inputMethod = "cdp-insert-text";
  let firstInsertError = null;
  await cdp.send("Input.insertText", { text: prompt });
  await sleep(750);
  let afterInsert = "";
  try {
    await sleep(750);
    afterInsert = await waitForComposerText(cdp, prompt);
  } catch (error) {
    firstInsertError = {
      errorCode: error?.errorCode || "composer.input_mismatch",
      error: String(error?.message || error),
      details: error?.details || null,
    };
    inputMethod = "dom-paste-fallback";
    await clearComposer(cdp);
    await setComposerTextDom(cdp, prompt);
    afterInsert = await waitForComposerText(cdp, prompt);
  }
  return {
    beforeClearCharCount: beforeClear.length,
    promptCharCount: prompt.length,
    composerCharCount: afterInsert.length,
    inputMethod,
    ...(firstInsertError ? { firstInsertError } : {}),
  };
}

export async function focusComposer(cdp) {
  return evaluate(
    cdp,
    `(() => {
      const visible = (el) => {
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
      };
      const composer = document.querySelector("#prompt-textarea")
        || [...document.querySelectorAll('textarea[aria-label="Chat with ChatGPT"], textarea[placeholder], [contenteditable="true"][role="textbox"], [role="textbox"][aria-label="Chat with ChatGPT"]')]
          .find(visible);
      if (!composer) return false;
      composer.focus();
      if (composer.isContentEditable) {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(composer);
        range.collapse(false);
        selection.removeAllRanges();
        selection.addRange(range);
      }
      return document.activeElement === composer || composer.contains(document.activeElement);
    })()`,
  );
}

export async function clearComposer(cdp) {
  return evaluate(
    cdp,
    `(() => {
      const visible = (el) => {
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
      };
      const composer = document.querySelector("#prompt-textarea")
        || [...document.querySelectorAll('textarea[aria-label="Chat with ChatGPT"], textarea[placeholder], [contenteditable="true"][role="textbox"], [role="textbox"][aria-label="Chat with ChatGPT"]')]
          .find(visible);
      if (!composer) return false;
      composer.focus();
      if ("value" in composer) {
        composer.value = "";
      } else {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(composer);
        selection.removeAllRanges();
        selection.addRange(range);
        document.execCommand("delete");
        composer.textContent = "";
      }
      composer.dispatchEvent(new InputEvent("input", { bubbles: true, inputType: "deleteContentBackward", data: null }));
      composer.dispatchEvent(new Event("change", { bubbles: true }));
      return true;
    })()`,
  );
}

export async function composerText(cdp) {
  return evaluate(
    cdp,
    `(() => {
      const visible = (el) => {
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
      };
      const composer = document.querySelector("#prompt-textarea")
        || [...document.querySelectorAll('textarea[aria-label="Chat with ChatGPT"], textarea[placeholder], [contenteditable="true"][role="textbox"], [role="textbox"][aria-label="Chat with ChatGPT"]')]
          .find(visible);
      if (!composer) return "";
      return "value" in composer ? composer.value || "" : composer.innerText || "";
    })()`,
  );
}

export async function setComposerTextDom(cdp, prompt) {
  return evaluate(
    cdp,
    `(() => {
      const text = ${JSON.stringify(prompt)};
      const visible = (el) => {
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
      };
      const composer = document.querySelector("#prompt-textarea")
        || [...document.querySelectorAll('textarea[aria-label="Chat with ChatGPT"], textarea[placeholder], [contenteditable="true"][role="textbox"], [role="textbox"][aria-label="Chat with ChatGPT"]')]
          .find(visible);
      if (!composer) return { ok: false, reason: "composer_missing" };
      composer.focus();

      try {
        const data = new DataTransfer();
        data.setData("text/plain", text);
        const event = new ClipboardEvent("paste", { bubbles: true, cancelable: true, clipboardData: data });
        composer.dispatchEvent(event);
      } catch {
        // Fall back to direct DOM state below.
      }

      const current = "value" in composer ? composer.value || "" : composer.innerText || "";
      if (current.trim() !== text.trim()) {
        if ("value" in composer) {
          composer.value = text;
        } else {
          const escape = (value) => value
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
          composer.innerHTML = text
            .split("\\n")
            .map((line) => line ? \`<p>\${escape(line)}</p>\` : "<p><br></p>")
            .join("");
        }
      }

      composer.dispatchEvent(new InputEvent("input", { bubbles: true, inputType: "insertText", data: text }));
      composer.dispatchEvent(new Event("change", { bubbles: true }));
      return {
        ok: true,
        textLength: ("value" in composer ? composer.value || "" : composer.innerText || "").length,
      };
    })()`,
  );
}

export async function waitForComposerText(cdp, expected, timeoutMs = 5_000) {
  const startedAt = now();
  let lastText = "";
  const normalizedExpected = normalizeMessageText(expected);
  while (now() - startedAt < timeoutMs) {
    lastText = await composerText(cdp).catch(() => "");
    if (lastText === expected) return lastText;
    if (normalizeMessageText(lastText) === normalizedExpected) return lastText;
    await sleep(100);
  }
  const error = new Error("ChatGPT composer text did not match the prompt before sending.");
  error.errorCode = "composer.input_mismatch";
  error.details = {
    expectedCharCount: expected.length,
    observedCharCount: lastText.length,
    expectedNormalizedCharCount: normalizedExpected.length,
    observedNormalizedCharCount: normalizeMessageText(lastText).length,
  };
  throw error;
}

export async function clickComposerSendButton(cdp, { timeoutMs = 5_000 } = {}) {
  const startedAt = now();
  let lastButtonState = null;
  while (now() - startedAt < timeoutMs) {
    const result = await evaluate(
      cdp,
      `(() => {
        const visible = (el) => {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
        };
        const composer = document.querySelector("#prompt-textarea")
          || [...document.querySelectorAll('[contenteditable="true"][role="textbox"], [role="textbox"][aria-label="Chat with ChatGPT"], [role="textbox"]')]
            .find(visible);
        const form = composer?.closest("form") || document;
        const voiceBusy = /connecting to voice/i.test(document.body.innerText || "");
        const buttons = [...form.querySelectorAll("button")].filter(visible);
        const states = buttons.map((candidate) => {
          const label = [
            candidate.innerText,
            candidate.getAttribute("aria-label"),
            candidate.title,
            candidate.getAttribute("data-testid"),
            candidate.id,
            candidate.className,
          ].filter(Boolean).join(" ");
          return {
            label,
            disabled: candidate.disabled || candidate.getAttribute("aria-disabled") === "true",
          };
        });
        const button = buttons.find((candidate) => {
          const label = [
            candidate.innerText,
            candidate.getAttribute("aria-label"),
            candidate.title,
            candidate.getAttribute("data-testid"),
            candidate.id,
            candidate.className,
          ].filter(Boolean).join(" ");
          if (/dictation|voice|talk|microphone|audio/i.test(label)) return false;
          const looksLikeSend = /send|submit/i.test(label)
            || candidate.getAttribute("data-testid") === "send-button"
            || candidate.id === "composer-submit-button"
            || String(candidate.className || "").includes("composer-submit");
          return looksLikeSend && !candidate.disabled && candidate.getAttribute("aria-disabled") !== "true";
        });
        if (voiceBusy || !button) return { clicked: false, voiceBusy, states };
        const r = button.getBoundingClientRect();
        button.click();
        return {
          clicked: true,
          voiceBusy,
          method: "dom-button",
          label: [button.innerText, button.getAttribute("aria-label"), button.getAttribute("data-testid")].filter(Boolean).join(" "),
          x: Math.round(r.left + r.width / 2),
          y: Math.round(r.top + r.height / 2),
          states,
        };
      })()`,
    );
    lastButtonState = result?.states || null;
    if (result?.clicked) return result;
    await sleep(100);
  }
  return { clicked: false, states: lastButtonState };
}

export async function waitForSubmission(cdp, { initialUserCount, beforeSnapshot, prompt, timeoutMs = 20_000 }) {
  const startedAt = now();
  let lastProbe = null;
  while (now() - startedAt < timeoutMs) {
    lastProbe = await pageProbe(cdp);
    if(beforeSnapshot && typeof prompt==='string'){
      const match=findNewUserMessage(beforeSnapshot,await snapshotConversationMessages(cdp),prompt);
      if(match?.isNew && ['exact','exact_with_attachment'].includes(match.promptEchoVerification))return {submitted:true,probe:lastProbe,echo:'exact_new_turn'};
      if(match?.isNew && match.promptEchoVerification==='partial')await expandUserMessage(cdp,match.message.ordinal);
    }else if (lastProbe.userTurns.length > initialUserCount) return { submitted: true, probe: lastProbe,echo:'count_only_requires_independent_exact_echo' };
    await sleep(250);
  }
  return { submitted: false, probe: lastProbe };
}

export async function submitPrompt(cdp, { composer, initialUserCount, responseToken = "", attempts = 3, beforeSnapshot, prompt }) {
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
    const acknowledged = await waitForSubmission(cdp, { initialUserCount, beforeSnapshot, prompt });
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
}

export async function waitForReadyProbe(cdp, timeoutMs = 20_000) {
  const startedAt = now();
  let lastError = null;
  while (now() - startedAt < timeoutMs) {
    try {
      const probe = await pageProbe(cdp);
      if (probe.isLoggedOut || probe.composer) return probe;
    } catch (error) {
      lastError = error;
    }
    await sleep(250);
  }
  throw new Error(`Timed out waiting for ChatGPT page readiness: ${lastError?.message || "not ready"}`);
}

export async function waitForTokenOutput(cdp, responseToken, initialAssistantCount, timeoutMs) {
  const startedAt = now();
  let lastProbe = null;
  while (now() - startedAt < timeoutMs) {
    const probe = await pageProbe(cdp);
    lastProbe = probe;
    const newAssistantTurns = probe.assistantTurns.slice(initialAssistantCount);
    const tokenTurn = findExactTokenTurn(newAssistantTurns, responseToken);
    if (tokenTurn) {
      await sleep(1000);
      const stableProbe = await pageProbe(cdp);
      const stableAssistantTurns = stableProbe.assistantTurns.slice(initialAssistantCount);
      const stableTokenTurn = findExactTokenTurn(stableAssistantTurns, responseToken);
      if (stableTokenTurn) return { probe: stableProbe, exactAssistantText: stableTokenTurn.trim() };
    }
    await sleep(750);
  }
  const error = new Error(`Timed out waiting for assistant response token ${responseToken}.`);
  error.errorCode = "chatgpt.response_timeout";
  error.details = {
    timeoutMs,
    observedAssistantTurnCount: lastProbe?.assistantTurns?.length ?? null,
    observedUserTurnCount: lastProbe?.userTurns?.length ?? null,
    bodyTextLength: lastProbe?.bodyText?.length ?? null,
  };
  throw error;
}

function cleanAssistantText(text) {
  const progressLine = /^(pro thinking|reading documents|thinking|reasoning|working|show more|show less)$/i;
  return String(text || "")
    .split(/\n+/)
    .map((line) => line.trim())
    .filter((line) => line && !progressLine.test(line))
    .join("\n")
    .trim();
}

function isProgressPlaceholder(text) {
  return !cleanAssistantText(text) && /pro thinking|reading documents|thinking|reasoning|working/i.test(String(text || ""));
}

async function generationState(cdp) {
  return evaluate(cdp, `(() => {
    const visible = (el) => { const r=el.getBoundingClientRect(); const s=getComputedStyle(el); return r.width>0 && r.height>0 && s.visibility!=="hidden" && s.display!=="none"; };
    const buttons = [...document.querySelectorAll('button')].filter(visible);
    const labels = buttons.map(b => [b.innerText, b.getAttribute('aria-label'), b.title, b.getAttribute('data-testid')].filter(Boolean).join(' ').trim());
    const thinking = [...document.querySelectorAll('div, span, p')].filter(visible).some(el => /^(pro thinking|reading documents|thinking|working)$/i.test((el.innerText||'').trim()));
    const active = thinking || labels.some(label => /stop answering|stop generating|interrupt|cancel response|stop streaming/i.test(label));
    const assistants = (${conversationMessageNodes.toString()})().filter(e => (e.getAttribute('data-message-author-role') || (e.hasAttribute('data-user-message-bubble') ? 'user' : 'assistant')) === 'assistant');
    const latest = assistants.at(-1);
    const turn = latest?.closest('article') || latest?.parentElement?.parentElement || null;
    const finalActions = turn ? [...turn.querySelectorAll('button')].filter(visible).map(b => [b.getAttribute('aria-label'), b.getAttribute('data-testid'), b.title].filter(Boolean).join(' ')) : [];
    const terminal = finalActions.some(label => /copy.turn|copy.turn.action|copy response|regenerate response|thumbs.up|thumbs.down/i.test(label));
    return { active, terminal, labels: labels.filter(x => /stop|interrupt|thinking|reading documents/i.test(x)) };
  })()`);
}

export async function waitForAssistantResponse(cdp, initialAssistantCount, {
  timeoutMs = 240_000,
  stableMs = 4_000,
} = {}) {
  const startedAt = now();
  let lastProbe = null;
  let lastText = "";
  let changedAt = now();

  while (now() - startedAt < timeoutMs) {
    const probe = await pageProbe(cdp);
    lastProbe = probe;
    const newAssistantTurns = probe.assistantTurns.slice(initialAssistantCount);
    const rawText = (newAssistantTurns.at(-1) || "").trim();
    const text = cleanAssistantText(rawText);
    if (text && text !== lastText) {
      lastText = text;
      changedAt = now();
    }

    const generating = await generationState(cdp).catch(() => ({ active: null }));
    const stableFor = now() - changedAt;
    if (isProgressPlaceholder(rawText)) {
      await sleep(750);
      continue;
    }
    if (lastText && generating.active === false && stableFor >= stableMs) {
      return {
        probe,
        assistantText: lastText,
        stableMs: Math.round(stableFor),
        finishDetectedBy: "stop_button_gone",
      };
    }
    if (lastText && generating.active === null && stableFor >= stableMs * 2) {
      return {
        probe,
        assistantText: lastText,
        stableMs: Math.round(stableFor),
        finishDetectedBy: "dom_stable",
      };
    }

    await sleep(750);
  }

  const error = new Error("Timed out waiting for assistant response.");
  error.errorCode = "chatgpt.response_timeout";
  error.details = {
    timeoutMs,
    observedAssistantTurnCount: lastProbe?.assistantTurns?.length ?? null,
    observedUserTurnCount: lastProbe?.userTurns?.length ?? null,
    bodyTextLength: lastProbe?.bodyText?.length ?? null,
    partialAssistantTextLength: lastText.length,
  };
  throw error;
}

export async function waitForAssistantResponseAfterUser(cdp, userMessage, {
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
}
