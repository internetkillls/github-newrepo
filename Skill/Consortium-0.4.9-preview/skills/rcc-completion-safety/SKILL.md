---
name: rcc-completion-safety
description: Use alongside Reasoning Consortium Controller for local CDP browser worker sends, response-completion verification, uncertain submission recovery, or suspected false completion and duplicate resends.
---
# RCC browser completion safety

This supplement does not replace RCC's routing, closure, or multi-tab contracts. It only governs local transport completion evidence and retry boundaries.

## Critical invariants

1. No worker closure becomes witnessed/canonical solely because assistant text has been stable or a stop button is absent.
2. Associate each response with the **verified newly sent user message**, not merely a global assistant-count increase.
3. Require repeated, independently sampled terminal evidence (observed generation activity ending or a scoped final-action affordance) and a stable anchored response. If no affirmative terminal evidence can be witnessed, end `response.completion_uncertain`, not success.
4. A clicked send button is an *uncertain side-effect boundary*. On missing prompt echo, do not click Send again automatically. Reconcile conversation history or request human review first.
5. Persist typed receipts separating target-ready, composer-filled, send-clicked, user-echo-verified, assistant-started, and assistant-completed.
6. A terminal detection heuristic can still yield false positives in unexpected UI versions: validate against live ChatGPT and keep conservative fallback behavior.

## Patch activation on local installations

A staged, reversible source patch is supplied at `scripts/completion-guard-install.mjs`. Its default is dry-run. Do not imply that a plugin account release automatically rewrites an already-installed local `chatgpt-composer.mjs`.

- Run `node scripts/completion-evidence-selftest.mjs` and `node scripts/completion-installer-selftest.mjs`.
- Run `node scripts/completion-guard-install.mjs` to inspect patch compatibility; it must report dry-run success.
- Only with explicit local source-write authorization, run `node scripts/completion-guard-install.mjs --apply`. It creates a dated backup and checks syntax.
- Run the existing RCC selftests and actual browser smoke test after application; unit tests are not proof of real completion.
- The local patch is not activated until `--apply` succeeds in the selected installed release.

When the patch cannot be applied or when browser verification is absent, report that completion correctness is `UNVERIFIED`, not `PASS`. See `docs/completion-guard.md`.


## 0.4.9 reliability addendum

Apply [the reliability contract](../../docs/RELIABILITY_v0.4.9.md). Use current queue operational status; an active scheduler or existing PID alone is not an active browser worker. Exact fresh invocation receipts can establish NOT_SENT_CONFIRMED without task success or automatic retry permission. Uncertain clicked Send still requires original-turn reconciliation. Explicit unused-role provisioning never replaces a committed conversation. New structured reviews may use the explicit JSON output contract; never relax an already-sent file contract. Same-role controller reuse requires the exact proof-pinned prior delivery and unchanged bundle, not an @mention. Default five rooms can be explicitly increased while browser sends remain serial. A saved account update does not hot-patch an installed runtime or migrate existing case helpers.
