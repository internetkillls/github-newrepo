# Handler policy — 0.4.5 candidate

This document describes executable candidate guards. It does not establish production ChatGPT recovery, Windows protocol registration, emergency message delivery, or full crash/restart supervision.

## Conversation identity

`runtime/chatgpt-pro-line/src/conversation-url.mjs` is the shared grammar for recovery, vendor conversation IDs, live witness and binding receipt validation. HTTPS exact hosts chatgpt.com and chat.openai.com are recognized; legacy references are observable but a legacy live target cannot qualify the dispatch resolver or a new verified transport binding. Host substrings, subdomains, userinfo (including empty userinfo), non-default ports, encoded path segments, dot segments and extra path suffixes are rejected.

Supported committed paths are `/c/<id>` and `/g/<scope>/c/<id>`, with optional trailing slash. ID and scope use case-sensitive ASCII letters, digits, hyphens or underscores, each 1..256 characters. Raw URL input is capped at 8,192 JavaScript code units. These bounds are conservative grammar limits, not empirically calibrated service format guarantees. Unknown future routes produce unsupported identity, not a permissive fallback. Query/fragment do not establish conversation identity. A change of scope invalidates identity even with an equal ID.

Homepage and `/g/<scope>` are uncommitted. They can only continue through the same live, still-uncommitted target. If the saved homepage has become a committed conversation without a saved receipt, reconciliation is required; the resolver cannot replace it with a new blank chat.

Duplicate matching conversation targets are ambiguous in automatic resolution, including when the saved target ID matches one. Explicit user target selection in alias/rebind tooling can identify a specific live target; this is distinct from trusting a stale saved target hint automatically. Metadata resolution remains separate from exact-turn and action-authority checks.

Tab creation uses one PUT. A failed or lost acknowledgment is marked outcome unknown with automaticRetryAllowed=false. There is no fallback GET that could create a second tab. Existing RCC provisioning claims continue to prevent a new spawn after an unresolved prior provision. New/open metadata is not task completion.

## Response observation budget

`lib/control-policy.mjs` exposes a versioned, hashed effective review policy. Defaults: timeout 20,000 ms, stable window 4,000 ms, poll 1,000 ms, individual DOM observation timeout 2,000 ms, at least three terminal candidate polls and a minimum candidate span of 1,000 ms. Terminal-only observations require twice the stable window through the completion detector. These are bounded implementation defaults, not production-calibrated latency targets.

Policy inputs are integers with explicit ranges. Unknown keys and infeasible combinations are rejected before sampling. The conservative feasibility guard accounts for twice the stable window, candidate polls/span, and two observation budgets. Sample capacity is derived from total timeout/poll interval; the accepted 60,000/100 ms combination no longer silently hits a fixed 100-sample limit at ten seconds.

Each DOM read, including final readback, receives min(2,000 ms or overridden sample budget, remaining review time) as its CDP command deadline and an AbortSignal. A timer also bounds an observer that ignores cancellation. Late observations cannot qualify a witness. Cancellation removes pending CDP command bookkeeping; it does not prove that a remote side effect failed. Observation is read-only and cannot resend.

The review budget starts at `reviewAnchoredResponse`. Browser-lock acquisition (10 seconds), target discovery (5 seconds default) and WebSocket connection (10 seconds default) are separately bounded preparation phases; they are not hidden inside that 20-second promise. This increment does not impose a hard OS scheduling/disk-I/O deadline or a single persisted incident-wide elapsed budget.

Every returned witness/unverified outcome carries the effective review policy and hash. A pinned per-job policy migration mechanism remains a separate gate; the presence of a policy hash in evidence does not establish that all older jobs adopted it.

## Receipt compatibility

The transport producer builds sessionTarget with the shared `sessionTargetReceipt()` helper, whose canonical identifier field is targetId. The RCC binding consumer accepts targetId and the older id alias, rejects conflicts when both are present, and validates invocation token, alias, project, prompt hash and committed modern URL before saving the worker binding. Tests use the actual producer helper and an isolated wrapper fixture using targetId.

## Remaining controller and Windows work

Capacity limits retain distinct purposes: DOM user/assistant length is 2,000,000 UTF-16 code units each; output decoding has separate encoded-block and decoded-byte caps. The decoder's 32 MiB cap is not a promise that a 32 MiB artifact fits in a single browser response. Streaming artifact transport, unified cross-stage capacity admission and calibration remain incomplete.

There is no Windows MSIX/custom-protocol activation adapter in this package. A URI adapter would only deliver a durable, deduplicated inspection intent to the owning controller instance; it cannot itself acknowledge agent reasoning or waive recovery authority. Full Windows cold/warm/crash/ACK contracts and Emergency routing are design artifacts in the authoring audit, not implemented host functionality.
