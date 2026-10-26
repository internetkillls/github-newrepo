# RCC 0.4.9-preview — Paperfold audit repairs

This release repairs the transport and parent-observability failures audited on 2026-10-22. It preserves exact room ownership, invocation binding, canonical byte gates and the rule against repeating an uncertain Send. It does not claim parallel browser generation, a native Paperfold fix, a live ChatGPT reliability guarantee or automatic installation into an already running Codex cache.

## Messages and first-turn identity

The browser adapter now reconciles legacy and modern message nodes in document order. Nested alternate wrappers count once; distinct identical messages remain distinct; sidebar and zero-size hidden intermediate nodes are excluded before reading their text. Snapshot, submission probe and independent completion sampling use the same collector.

New public calls acknowledge the exact newly observed prompt rather than requiring only an increased user count. A collapsed user prompt can be expanded through its scoped visible Show more button; partial echoes are not verified prompts. The acknowledgment budget is 20 seconds. A clicked Send still crosses the uncertain boundary and is never clicked again automatically. The committed conversation identity is recorded immediately after a fully verified first prompt, even when assistant generation later fails. This binding is not a completed-response witness.

## Phase-aware queue result and truthful status

Public queue dispatch assigns an invocation token. The sender records NOT_ATTEMPTED before any Send call and changes it before entering submission. A failed, exact invocation/job/payload/prompt/project-bound receipt can classify a pre-Send failure as NOT_SENT_CONFIRMED. Missing, stale, foreign, signaled or post-Send evidence remains UNCERTAIN. This classification does not authorize a retry or manufacture task success. Existing uncertain histories are not rewritten or reset.

`node <RCC>/bin/rcc-queue queue status --case=CASE` retains the queue fields and adds `operational`: QUEUED, DISPATCHING, BLOCKED, BLOCKED_ORPHANED_DISPATCH, AWAITING_REVIEW or IDLE. Every committed transition writes `.devspace/rcc/CASE/activity.json`. Process existence is reported separately and never establishes browser generation or PID incarnation. A scheduler's ACTIVE setting must not be presented as worker RUNNING. Read current queue status rather than launch-time checkpoint booleans. The public dispatch process timeout is bounded at 12 minutes to accommodate bounded upload plus response deadlines; custom runners must not wrap it in a shorter contradictory timeout.

## Explicit unused-role recovery

For an existing role with a missing temporary blank tab, use only after reconciling its original attempts and granting a bounded provisioning action:

```text
node <RCC>/bin/rcc-consortium worker provision-unused --case=CASE --role=ROLE --approve=PROVISION-CASE-ROLE
```

This action takes the browser and queue locks without clearing any existing lock. It requires an existing pending, compiled task and no send-capable history: only untouched PENDING jobs and reviewed NOT_SENT_CONFIRMED failures are allowed. A committed conversation, active/uncertain/returned/reviewed send, prior run history, changed existing target or unresolved prior provisioning claim blocks replacement. An existing original blank target is retained. A missing original target can be replaced once with the SAME alias and role after a durable claim. Lost new-tab acknowledgment remains UNCERTAIN and is not automatically repeated. No worker role or prompt is created or sent by this command. Preserve old evidence and the original worker's independence class.

## Upload readiness and same-role instruction reuse

Cleanup recognizes current Remove filename attachment controls within the composer; unrelated removal controls are untouched. Readiness errors are scoped to requested filenames rather than unrelated page errors. `CHATGPT_UPLOAD_TIMEOUT_MS` defaults to 120000 and is bounded at 300000. `uploads/UPLOAD-STATE.json` retains exact staged identities and last readiness observation. STAGED_READY_NOT_SENT is not a delivered attachment or source ACK.

An unchanged controller library already delivered in the SAME committed role conversation can be explicitly reused:

```text
node <RCC>/bin/rcc-consortium worker send --case=CASE --role=ROLE --prompt-file=PACKET --reuse-controller-from=PRIOR_RECEIPT --reuse-controller-sha256=EXACT_RECEIPT_SHA256
```

The receipt must show a successful upload of the current exact controller ZIP, matching role alias/project/committed conversation, exact prior prompt echo and bound completed response. The prior receipt is retained before the new call overwrites its current transport sidecar. No cross-role reuse, changed-library reuse, attachment-chip inference, new-upload claim or tool-activation claim is allowed. Source artifacts other than the controller still require their own delivery proofs. Public queue run continues uploading controllers by default; no unreviewed queue rewrite enables reuse implicitly.

## Structured review artifacts without Base64

For a NEW task whose deliverable is the complete structured response, explicitly declare:

```json
{"schema":"rcc.output-contract.v1","mode":"json","path":"review.json","schemaId":"project.review.v1","identity":{"workerId":"W4","phase":"K0"},"maxBytes":12000}
```

Require exactly one complete matching JSON code block. The gate checks schema identity, fixed primitive identity fields, size and output path, then saves the exact returned UTF-8 and computes its NEW local SHA256. This establishes byte completeness/identity, not source understanding or product correctness. Existing files/Base64 contracts remain strict and cannot be silently converted after a failed send; a new review must have explicit supersession identity and authority. Binary/code transfers keep byte/hash gates.

## Larger role sets stay serial

The default remains five roles. Explicit `workers spawn --roles=... --max-roles=12` supports ten workers plus planner/merger in one case, bounded to 32 rooms. An existing case retains its selected limit. `maxActive` and browser operation locks still serialize sends. Do not recreate or migrate the existing linked Paperfold roles merely because the larger cap is now available.

## Verification and remaining debt

The candidate includes new audit regression tests for mixed/duplicate/hidden/sidebar markup, exact send acknowledgment, upload labels and status scoping, phase-bound no-Send records and negative controls, unused-role safety, JSON identity/byte integrity, same-room controller reuse, configurable room counts and operational status. Existing queue/completion/recovery tests remain required.

Unit fixtures do not establish live ChatGPT DOM compatibility, upload latency, a real browser restart journey, a native Windows/macOS pass or ten concurrently active workers. Before production fanout, perform one authorized live exact-room -> context -> single Send -> full anchored response -> exact artifact -> truthful terminal-status round trip. The current account release must be refreshed/reloaded locally before claiming that installed runtime changed; do not edit a managed cache in place or bypass the app-owned chat writer lock.

Legacy receipts may contain ordinals assigned by the old collector. Preserve those receipts. If the new collector cannot match an old ordinal, perform explicit full-prompt reconciliation and retain a typed old/new anchor proof; never silently rewrite historical anchors or redo an already accepted source review.
