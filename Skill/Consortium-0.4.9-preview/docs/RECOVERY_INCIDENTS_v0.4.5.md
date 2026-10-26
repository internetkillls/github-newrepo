# Durable recovery incident outbox — 0.4.5-preview

This local module persists structured diagnostics when bounded connection discovery or binding reconciliation cannot establish a healthy worker. It does not contact ChatGPT, execute returned code, restart Chrome, change bindings, clear locks or dispatch jobs.

## Executable commands

```text
node bin/rcc-recovery incident --state=<case-state.json> --case=<id> --root=<workspace> [--port=9222] [--goal-ref=<reference>]
node bin/rcc-recovery resume-observation --state=<same-state.json> --root=<workspace> --incident=<incident-id> --decision-file=<decision.json> [--port=9222]
```

The first command performs up to three bounded discovery attempts, then persists a failure packet under `.devspace/rcc/recovery-incidents/<id>/`. Exit 2 means unresolved local diagnostic, not successful message delivery. A healthy unique bound worker is not escalated. New observation metadata is retained without creating another incident for the same case/checkpoint/signature/endpoint. No raw prompt or chat content is collected.

Records are immutable, hashed envelopes. Complete temporary files are fsynced before an exclusive hard-link commit; a competing writer cannot overwrite another claim. Unsupported filesystems fail rather than silently weaken this contract. Partial temporary files are not committed records. This provides local process-crash evidence, not proof of Windows power-loss durability or authentication against a writer able to rewrite the entire history.

## Checkpoint-bound decision

```json
{
  "schema":"rcc.recovery.decision.v1",
  "decisionId":"64-lowercase-hex-unique-id",
  "incidentId":"64-lowercase-hex-incident-id",
  "checkpointHash":"hash-from-persisted-incident",
  "expiresAt":"ISO-8601-future-time",
  "decision":"REOBSERVE",
  "action":{"kind":"RECONNECT_READ_ONLY","parameters":{}}
}
```

Only read-only discovery is executable in this increment. The incident, endpoint, current input state hash, expiry and allowlisted action must match. Other actions and parameters are refused. A ChatGPT answer is data, not authority for arbitrary code or external mutations. A changed checkpoint requires a fresh diagnostic/decision; no cached reply can resume a changed job.

Each decision has an exclusive immutable claim. A live or indeterminate PID owner blocks a concurrent observer. Completed observation results are returned from cache. If an observer is proven dead, the same still-valid decision may launch the next read-only attempt, up to three total process attempts. No ambiguous side effect is replayed because this API has no dispatch capability. PID reuse is treated conservatively as possibly live; process-incarnation supervision remains work to complete.

An observation returning is not task completion or repaired browser state. Inspect its nested report: ENDPOINT_UNAVAILABLE, missing conversations and ambiguous matches remain unresolved. `sendAllowed` remains false throughout. A stale or corrupt record is retained and rejected rather than overwritten.

## Emergency re-engagement boundary

The packet includes goal reference, case/worker/job metadata, checkpoint fingerprint, expected/observed state, attempts, signature, runtime identity, unverified root-cause marker, available capabilities and forbidden repetitions. Its delivery state is always PERSISTED_LOCAL_NOT_DELIVERED. No service, API key, automated chat route or acknowledgment is invented.

A future authorized integration can transport this exact packet and return a typed decision. That transport needs its own durable delivery intent, deduplication and acknowledgment. Existing Codex deferred wake is opt-in and cannot be treated as proof of emergency-message delivery. Current commands let an agent diagnose available evidence or safely repeat local observation without altering the task queue.

## Executed evidence

Tests cover diagnostic deduplication, healthy negative control, observation-result caching, expired/wrong/stale/unsafe decisions, concurrent live owner exclusion, corrupt record rejection, a real interrupted child observer resumed on attempt 2, and the actual CLI against an HTTP loopback discovery fixture. The fixture is not ChatGPT or Chrome. No worker prompt was sent.

The incident API itself only resumes read-only observation. The separate opt-in automatic review path is documented in AUTOMATIC_REVIEW_v0.4.5.md. Automatic browser restart, an installed independent supervisor, external diagnostic delivery and software self-modification are not implemented here.
