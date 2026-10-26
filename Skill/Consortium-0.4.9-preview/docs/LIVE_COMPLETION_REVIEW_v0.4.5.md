# Read-only completion re-observation — 0.4.5-preview

`lib/live-completion-review.mjs` provides `sampleBoundTurn` and `reviewAnchoredResponse`. It observes exact pinned conversation, user ordinal/bytes, assistant identity/bytes and scoped final controls across repeated samples. Changed turns, unrelated controls, active generation, wrong bytes, missing anchors and renewed generation at final readback cannot qualify.

The result RESPONSE_UI_WITNESSED means only that the exact response UI and bytes passed this observation contract. It does not certify file delivery, content correctness, task completion or handoff. The module cannot send a prompt, adopt a target or advance a queue. The separate queue-owned integration additionally enforces a pinned output contract and immutable proof; see AUTOMATIC_REVIEW_v0.4.5.md.

Unit tests exercise the decision logic and its near-miss controls. A separate smoke test used actual Chrome on a newly created HTTP loopback fixture tab, confirmed exact DOM selection, visible Stop detection and scoped control rejection, then closed that fixture tab. It did not submit a ChatGPT message, change existing tabs or verify production ChatGPT markup end to end. Packaged proof scope is in verification-0.4.5.json; detailed local audit receipts remain in the authoring workspace.

## Persisting committed conversation identity

The worker wrapper now requests a structured receipt sidecar from its exact child invocation. A fresh random invocation token, alias, project root, original prompt hash, committed conversation URL and unchanged target identity must match before the case worker binding is updated. Prose stdout is never parsed as instructions or as a trusted binding receipt. Capture failure is recorded as unavailable/unverified and is not task completion. A changed target still requires reconciliation.

This repairs a concrete case-registry gap for future sends: the older wrapper recorded send/output timestamps but did not copy the final conversation URL back to the RCC worker record. A current read-only audit found three live committed conversations lacking this reference among four inspected workers. This is not proof that all session state was lost: the vendored transport has a separate canonical alias registry.

Tests cover the binding helper and the real wrapper with an isolated fake transport. Actual ChatGPT first-send capture remains an integration gate. Automatic review was exercised through a real Chrome intercepted fixture with simulated transport receipts/callbacks, not through new ChatGPT messages. No running worker or existing state file was hot-patched.
