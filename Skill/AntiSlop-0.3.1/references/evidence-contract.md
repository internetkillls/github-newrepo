# Evidence types, finding states and repair contract

## Evidence hierarchy (not a numerical truth score)

- `observed_runtime`: exact version, command, input, expected relation, observed output, test artifact/trace and environment; may support confirmed runtime failure.
- `formal_check`: target statement, assumptions, exact formalization and checker output; distinguishes proof success from spec accuracy.
- `source_witness`: accessible source URI/file/page/line and claim matched to source role, provenance and date; may support documented contradiction.
- `conversation_anchor`: turn id, actor, exact short quote/text locator and scope; supports dialogue/commitment findings.
- `structured_argument`: explicit premise/warrant/defeater reconstruction grounded in text. Strong analytical evidence, but not made deterministic by JSON shape.
- `heuristic_scan`: regex, lexicon, semantic similarity, LLM label, score. Signals requiring review; not proof of slop or AI authorship.
- `unavailable`: claimed evidence absent/inaccessible; return UNKNOWN.

## Findings fields

```json
{
  "finding_id": "F01",
  "class": "L",
  "status": "CONFIRMED",
  "severity": "major",
  "failure_signature": "Assistant proposal represented as user-approved",
  "scope": "thread-a",
  "artifact_anchor": {"source_id": "export-1", "locator": "turn-14", "actor": "assistant", "quote": "I suggest switching tools"},
  "expectation": "Unaccepted suggestions remain proposed",
  "actual": "Summary lists switch as approved",
  "proof_type": "conversation_anchor",
  "proof_anchor": {"source_id": "export-1", "locator": "turn-15"},
  "test": "Compare decision ledger and user acceptance anchors",
  "root_dependency": "stance attribution at recap pass 1",
  "repair": "Re-mark as proposed and redo dependent conclusion",
  "retest": "Check no user-only decisions lack user anchor",
  "known_limit": "Assumes export includes all relevant response turns"
}
```

This is a **schema illustration** with hypothetical data, not an observed finding. The auxiliary CLI validates only structural sufficiency of the chosen state and anchor, not source truth.

## State labels

- `CONFIRMED`: decisive, witnessed violation *within a stated scope*. Only with proof and explicit expected-vs-actual.
- `SUPPORTED-RISK`: material defeasible analysis, but no decisive test or incomplete source set.
- `STYLE-SIGNAL`: surface pattern; must not be used as evidence of AI authorship or factual failure.
- `UNVERIFIED`: missing inputs, inaccessible sources or unavailable runtime; abstain.
- `NOT-APPLICABLE`: class does not apply to this artifact.

Severity is independent of state: `blocker|major|minor|signal`. A severe suspected failure can remain unverified. Never confuse a numerical risk score with truth. Decision: fix confirmed high-impact root failures first, surface supported risks, give user control of stylistic preferences.

## Independence and closure

When reviewers are independent, record `shared`, `closure-only`, `blind`, `adversarial`, `witness` scope. They do not settle factual disagreement by majority vote. Merge by comparing evidence/provenance and actual test conditions; unresolved contradictions remain open. If new evidence invalidates a premise, mark descendant repairs stale and re-open earliest affected inference.

## Reproducibility

Keep source/version hashes when readily available. A model with a fixed temperature and schema is *not* a guaranteed deterministic extractor. Use paired positive/negative samples, exact scope of test, and distinguish test plan from test execution. Do not claim regression tests passed until they run, with results.
