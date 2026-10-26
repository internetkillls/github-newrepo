# RCC completion safety — staged 0.4.1-preview patch

## Source inspection and scope

Runtime: `runtime/chatgpt-pro-line/src/chatgpt-composer.mjs` and `scripts/chatgpt-call.mjs`.

Existing RCC already verifies a new user-message echo and links assistant messages to that user-message anchor. Preserve these guards. Two concrete risks remain in inspected version 0.4.0-preview:

1. `waitForAssistantResponseAfterUser()` previously returned success when anchored text stayed stable and `generationState.active === false`. A missing stop indicator can be a UI false-negative; the `active === null` DOM-stability fallback also produced completion without positive terminal evidence.
2. `submitPrompt()` attempted another click after a successful button click when user-message observation was delayed. A successful first submission with lagging DOM could be duplicated by the retry.

## Contained change

This release adds `completion-evidence.mjs` and a dry-run-first patch installer. It applies two remedies to the *existing local installed file*: (a) repeated anchored completion evidence requiring active-to-inactive lifecycle or scoped final-action controls, and (b) no repeat click after a click whose acknowledgment is uncertain. A missing positive terminal signal results in `response.completion_uncertain`; an unacknowledged click results in `send.submission_uncertain`. Both are bounded failures, not success or implicit retry.

This is a **staged local repair**, not a claim that the account plugin automatically updated the local vendored transport. The installer must be run from the plugin root and only after local write authorization.

## Apply and verify

```bash
node scripts/completion-evidence-selftest.mjs
node scripts/completion-installer-selftest.mjs
node scripts/completion-guard-install.mjs
node scripts/completion-guard-install.mjs --apply
node scripts/runtime-selftest.mjs
```

Apply creates a `chatgpt-composer.mjs.backup-<UTC timestamp>` file. If a syntax check fails, the installer restores the backup. A local browser E2E using the dedicated logged-in Chrome CDP session is still required before declaring real ChatGPT completion robust. Check response hooks and selectors against the deployed UI.

## Known limits

DOM-based terminal controls and stop-button presence are heuristic. A fast response without a detected active phase or final-action control will be reported as uncertain. The unanchored legacy waiter is not part of RCC `worker send`'s anchored path and has not been migrated by this staged repair. Release tests here exercise synthetic signals and the installer's transformation, not a live account.

## Negative controls

- Stable partial text while the stop control is missing must not auto-complete without lifecycle or terminal witness.
- A clicked send without visible user echo must not be clicked again.
- A paused, stale, or different room must not receive a handoff merely because a global idle event was observed.
