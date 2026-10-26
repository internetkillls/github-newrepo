# Engineering audit: minimum evidence schemas

Use this after `references/evidence-contract.md`; that evidence hierarchy remains authoritative. This module adds local, executable checks for narrowly defined JSON artifacts and documented limitations. None of these checks proves program correctness or production safety.

## 1. Task contract and local evidence references

`python assets/cli/engineering_gate.py contract engineering-contract.json --root .`

Example file, where `proof/browser-witness.json` MUST already exist and describe a real execution:

```json
{
  "task_id": "PRC-send-one",
  "requirements": [{
    "id": "Q1",
    "description": "One send per queue item after an acknowledged UI delivery",
    "risk": "concurrent",
    "verification": ["E1"],
    "negative_controls": ["E2"]
  }],
  "evidence": [
    {
      "id": "E1", "requirement_id": "Q1", "kind": "behavior",
      "path": "proof/browser-witness.json", "observed": true, "outcome": "pass",
      "execution_mode": "live_browser", "input": "send prompt once",
      "expected": "one acknowledged send", "actual": "one acknowledged send"
    },
    {
      "id": "E2", "requirement_id": "Q1", "kind": "behavior",
      "test_role": "negative_control", "path": "proof/retry-witness.json",
      "observed": true, "outcome": "pass", "execution_mode": "live_browser",
      "input": "repeat uncertain send after reconnect",
      "expected": "no duplicate send", "actual": "no duplicate send"
    }
  ]
}
```

`kind: command_receipt` supports limited validation of `anti-slop-command-receipt.v1` (JSON file, argv, exit code, timestamp, and current git HEAD if accessible). It never substitutes for upstream `anti-slop-claims`. The local contract checker refuses evidence paths outside `--root` and only checks that artifacts exist, not their inner semantic claims. Unknown git HEAD is an incomplete receipt freshness check. `kind: review` can confirm a named review artifact was referenced; it does not authenticate the reviewer.

Outcome `EVIDENCE_PRESENT_REVIEW_REQUIRED` is intentionally **not** VERIFIED. `INCOMPLETE` exits nonzero. For concurrency, stateful behavior or security requirements (`risk`), a negative control is required; missing evidence fails. Treat this as an engineering minimum, not a universal requirement for all writing/academic cases.

## 2. Recorded agent policy trace

`python assets/cli/engineering_gate.py agent-trace trace.json policy.json`

Example `policy.json`:

```json
{"expected_goal":"summarize_document","allowed_tools":["read_document"],"denied_tools":["send_email"]}
```

Example `trace.json`:

```json
{"tool_calls":[{"name":"read_document"}],"events":[{"type":"goal","id":"summarize_document"}]}
```

This checks only `no_denied_tool_call` and a strict expected-goal event, inspired by the OWASP scenario scheme. It is not the upstream OWASP harness. Missing goal event is FAIL when required. Trace PASS is conditional on complete and honest instrumentation.

## 3. Queue false completion witness

`python assets/cli/engineering_gate.py queue-trace queue-trace.json`

```json
{"items":[{"id":"prompt-1","events":[{"type":"send_attempted"},{"type":"send_acknowledged"},{"type":"response_completed"},{"type":"complete"}]}]}
```

The recorded event order must be attempted → acknowledged → response completed → complete, without duplicate acknowledgments, duplicate queue IDs, or post-completion state transitions. A timeout, DOM composer fill, or attempted send is insufficient. A duplicate acknowledgment means investigate possible double-send; the tool does not infer deduplication from browser appearance. Without an independent UI witness for event recording, state remains unverified even if the trace shape passes.

## 4. Cross-tool gates

The intended sequence is:

`Source snapshot → Reproducer → Minimal patch → Static lint → Command receipts → Runtime behavior + negative control → Trace assertions → Human review → Delivery`.

A linter PASS does not infer runtime behavior. A command exit code `0` does not establish test relevance. A mock-only test does not establish integration. A local UI witness does not establish production behavior. A model-generated summary is not an independent test result.

For state transitions, preserve initial state, event timestamps or ordering, UI signal source, queue item identity, idempotency key and commit/runtime version where practical. If those signals are absent, abstain rather than claiming a fix.
