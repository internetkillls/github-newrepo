# RCC 0.4.4-preview — connection cleanup and recovery inspection

This incremental release addresses a reproduced defect: closed CDP sockets previously left pending request promises unresolved. It does not replace queue completion gates or claim general PC control.

## Executable changes

- Preserve the two fixes already present in this computer's 0.4.3 runtime: the bundled completion guard (no re-click after uncertain Send, affirmative anchored completion evidence) and skipping an unavailable effort slider when exact effort is already selected. The previous account archive did not contain these local fixes. They are included here to avoid reverting them on refresh; unknown UI versions still require live validation.

- Close, error and explicit session close reject every pending command and clear its timer and cancellation listener.
- Connection deadline defaults to 10 seconds; command deadline to 120 seconds; target discovery to 5 seconds. Callers may provide bounded deadlines. A long intentional Runtime.evaluate can override the command deadline through send's third options argument.
- Optional AbortSignal cancels connection setup or a command; late replies are ignored. No command is automatically replayed. Transport errors carry errorCode, remoteOutcome=unknown and automaticResendAllowed=false.
- `node bin/rcc-recovery inspect --state=<case-state.json> [--port=9222] [--output=<new-report.json>]` probes loopback discovery up to three times with 250/500 ms backoff and 3-second request deadlines. It records a state fingerprint and attempts, and classifies saved bindings by verified conversation URL metadata. Multiple candidates are ambiguous, even if one target ID matches.
- Inspector does not read chat content, access cookies, send, navigate, reopen tabs, restart browsers, update worker bindings, clear locks or advance a queue. Output is a diagnostic report, not an execution checkpoint or completion witness.

## Verification

`npm run test:recovery` covers healthy responses, close/error cleanup, cancellation before and after send, deadlines and late replies, send exceptions, connection timeout, actual loopback WebSocket disconnect, moved targets, wrong conversations, duplicate candidates and bounded discovery. The network test uses a local test server, not Chrome. Existing queue/deferred/completion tests remain separate gates. Live Chrome metadata inspection is narrower evidence than live crash/restart recovery.

## Next increments

1. Phase-aware operation receipts and a machine-verified completion review adapter, preserving exact user/assistant anchoring and output integrity.
2. One-owner action journal and checkpoint reconciliation across queue, worker binding and handoff. Record possible side effects before Send; retain uncertainty after interrupted submission.
3. Authorized browser restart and supervisor recovery only after process-incarnation/lease validation. Do not steal a lock from a possibly live owner.
4. Durable diagnostic outbox and opt-in ChatGPT/Codex re-engagement with incident/checkpoint-bound decisions. No arbitrary returned code execution or stale decision application.

These remain unimplemented here. Existing registries and atomic queue persistence are retained. A new database or always-on service is not introduced without evidence that the narrower extensions are insufficient.

## Installation boundary

A saved account release does not rewrite an already-running or cached local runtime. Use the updated release through the host's supported refresh/install flow. Keep local runtime-only patches separate; do not overwrite customized installations with an older archive. A new process can run this staged source directly for validation. Do not hot-patch the installed cache or interrupt active worker jobs to demonstrate this release.
