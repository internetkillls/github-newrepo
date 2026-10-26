# Build an anti-slop regression set without pretending it is already validated

## Candidate life cycle

`reported` (narrative complaint) → `observed` (artifact/source excerpt) → `reproduced` (same relevant conditions and expected/observed mismatch) → `adjudicated` (root cause and intended contract established) → `resolved` (repair passes same probe + near-miss control). Do not advance merely because the same story appears in multiple recaps.

For academic arguments and sense-making, experimental reproduction may be replaced with independently checkable premise/definition/locator analysis. Different tasks demand different warrants.

## JSONL case shape

```json
{"case_id":"C-01","class":"C","status":"reported","origin":"user-supplied-draft","problem":"constant response despite a signal the specification says matters","original_source_ref":"source-draft-v0.1.md#C-01","witness":null,"expected_relation":null,"observed":null,"root_dependency":null,"negative_control":null,"repair":null,"retest":null,"split":"unassigned"}
```

Use `origin` and `status` separately, record source/source role, expected input-output relation and observed output, user acceptance criterion, actual repair and retest. Unknown fields must stay null rather than fabricated. A record may be useful while still `reported`.

## Calibrate scientifically

Choose positive and negative cases from similar genres and difficulty. Separate development and held-out sets by *case or project* to prevent near-duplicate leakage. Report per-class precision, recall, abstention rate, and serious error rate with raw counts. Surface false positives in authentic prose and valid metaphors; surface false negatives in structurally correct but causally idle code. If there are too few labeled examples, state not calibrated.

A change to a rule/model/prompt must be tested on the same frozen regression set, and on new holdout where practicable. Thresholds that shift false positives require explicit reviewer signoff. Any resource in the source draft is a *lead* until retrieved and validated; star count is neither proof nor warrant.

## v0.3 regression objectives

Tests must include both a true positive and a near miss for each new directed-edge rule:
- `adopted_by` with matching explicit target should pass; unrelated target should fail; generic `go on` should not blanket-authorize proposals.
- explicitly replaced old question should disappear from the active set; simultaneous scoped questions should survive; two same-scope questions without a reframe link should stay visible with an ambiguity warning.
- corrected accepted decisions should be recorded historically and omitted from *effective* accepted decisions; corrections without target must not silently change the prior record.
- transcript indexing should preserve role/count/locator and abstain from declaring account-wide coverage or inferred commitments.

The Python unit suite is a **structural regression suite**, not a semantic benchmark. Semantic precision/recall can only be measured after blind human labels on raw source passages plus adjudication.
