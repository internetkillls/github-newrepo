# Adaptive admissibility, control scope, and false-positive policy — RMC v0.6.6

This **supplements** the retained `stage-machine.md` and `inquiry-admissibility.md`. It modifies only how an evaluator is deemed relevant, how observations are classified, and which claim/action is affected. It does not rewrite the theoretical modules, supersede user requests, supply object-level evidence, or install a runtime. Stages may be skipped when satisfied. An inapplicable check is skipped regardless of whether it would have had evidence; it must not produce a false block.

## A. Typed proof/evidence obligation

A task-level or stage-level proposed evaluation should be described by:

- `claim_id`, `claim_type`, `claim_text_or_ref`, `jurisdiction`, `requested_scope`;
- `check_id`, `required_input_types`, `applicability_basis`, `decision_changed_if_fail`;
- `witness_required_for_claim`, `witness_kind`, `source_ref_or_runtime_receipt`, `witness_observed`;
- `contradiction_evidence` or `unsupported_method_reason` when material;
- `finding` and `disposition` (different dimensions); `claim_limit`, `repair_target`, `near_miss_control`.

A human/model must determine semantic applicability and source adequacy from actual task context; merely passing fields in a JSON object is a **declaration**. The optional `../runtime/adaptive_gate.py` checks *formal consistency of supplied data only*. For an empirical/rhetorical/conceptual question it cannot establish truth, author intent, hidden assumptions or validity of a source.

### Finding types

| Finding | Scope | Do not infer |
|---|---|---|
| `PASS` | The specific observable obligation satisfied under declared inputs | Entire claim fully proved, code deployed, or reasoning correct |
| `NOT_APPLICABLE` | Evaluation has no warranted input/function for this claim | Missing check is an error or tested claim is verified |
| `UNVERIFIED` | Required witness missing, inaccessible, or not observed | Claim is false, operation failed, fabricated success |
| `CONTRADICTED` | Observable counterexample conflicts with the tested proposition | All other claims and stages are invalid |
| `UNSUPPORTED` | Evaluator cannot accept/represent the requested object/test | Object claim is false |
| `PROVISIONAL` | The claim may be stated with explicit conditional assumptions/debt | The claim has unconditional final closure |

Disposition is **not** finding: `CONTINUE | SKIP_CHECK | NARROW_CLAIM | WITHHOLD_CLAIM | REVISE_PREMISE | CHANGE_METHOD`. Non-epistemic safety/authorization gates operate separately, with their own actor and affected action.

### Minimal precedence and safety

1. No semantic applicability or no prospective decision change → `NOT_APPLICABLE/SKIP_CHECK` (do not run test).
2. Applicable observed contradiction → `CONTRADICTED/REVISE_PREMISE` with evidence and target; consider alternate model class.
3. Applicable operator unable to test supplied type → `UNSUPPORTED/CHANGE_METHOD` (do not simulate a result).
4. Mandatory claim witness absent → `UNVERIFIED/WITHHOLD_CLAIM`; continue tasks not requiring that claim.
5. Nonessential evidence absent → `PROVISIONAL/NARROW_CLAIM`, provided a narrower conclusion is permitted and clearly marked.
6. Witness present and matching narrowly specified expectation → `PASS/CONTINUE`; a source string or declared boolean is not by itself an independently adequate receipt.

Explicit negative examples: `no external research` on self-contained logical proof is NOT_APPLICABLE, not BLOCKED; `no numeric measurement` in a hermeneutic claim is NOT_APPLICABLE; `no universal proof` for an openly qualified hypothesis is NOT_APPLICABLE; `no deploy/test receipt` for a claimed deployed/fixed product is UNVERIFIED; contrary log/test directly refuting the specific claim is CONTRADICTED. A new plugin version published successfully is not an end-to-end host behavioral test.

## B. RMC stage edges are a typed multigraph

`PREREQUISITE`: typed, justified dependency and its satisfaction condition. Check declared **prerequisite subgraph** for cycles only when dependency meaning is correct. `TRANSITION`: conditional motion including legitimate S0→S9 jumps/skip; may be cyclic. `REPAIR`: a return to earliest failed dependency when a material assumption changes; deliberately cyclic. No software should run Kahn's algorithm on the union of these edges and call every repair loop a logical impossibility. Graph nodes represent stages or obligations **with stable identities**; do not confuse program-flow chronology with logical necessity.

Test pair (source: uploaded `rmc_vct_admissibility_probe.py`): an S6→S5 feedback and S5→S6 transition yields a cycle when mistakenly mixed as dependencies; separate actual `PREREQUISITE` edges and the legitimate workflow remains admissible. Negative control: `requires_operator→requires_test→requires_operator` **if both genuinely declared as logical prerequisites** remains a real circular dependency. The original source used a transcription of VCT `dep_sort()`; this package's bounded runner does not claim the packaged VCT backend was called.

## C. Mahajan operator transfer: necessary preconditions

Method source: Sanjoy Mahajan (2010), *Street-Fighting Mathematics: The Art of Educated Guessing and Opportunistic Problem Solving*, MIT Press, CC BY-NC-SA 3.0 US; uploaded PDF (print pagination).

- Ch. 1, pp. 1–3: GDP flow vs net-worth stock demonstrates **incommensurate dimensions**. RMC analogy: do not compare claim/witness statuses of different kinds. This is a transfer hypothesis, not proof that logical/semantic claims have physical units.
- Ch. 2, pp. 13–20: easy/extreme cases eliminate candidates; the frustum's missing `ab` term shows **model-class misspecification** can defeat attempts to tune constants. RMC: when both positives and negatives expose a contradiction, revisit typed status taxonomy or representation—not merely sensitivity thresholds.
- Ch. 3, pp. 31–35: lumping can give task-sufficient approximations; use for **economy of applicable checks only**, never merge distinct epistemic jurisdictions, source voices or safety-critical obligations.
- Ch. 5, pp. 77–81: extract the biggest, decision-changing effect; prioritize cheap discriminating witnesses before marginal refinements. Cost-sensitive check prioritization remains **qualitative** until actual per-check error/cost data exist.
- Ch. 6, pp. 103–105: 1D/2D region-count analogies expose the fragile 3D `2^n` extrapolation. An analogy can nominate a falsifier; it does not warrant transferring all conclusions or proving human semantic behavior.

Do not borrow numeric approximation errors, confidence figures or physical dimensional theorems from Mahajan and relabel them calibrated error rates of RMC. Analogy loses domain structure; record lost information, transfer warrant, counterexample and applicability.

## D. AntiSlop interface — evidence-bound, not an automatic invocation

Pass a finding to AntiSlop only if it is **material to the actual user task**. Minimal handoff:

```
claim_id, requested_task, claim_type, jurisdiction,
source_scope, source_ref/version, failure_signature,
expected_condition, observed_fact_or_missing_witness,
finding, disposition, claim_affected, repair_target,
positive_control, negative_or_near_miss_control, unverified_debt
```

AntiSlop's classifications `CONFIRMED | SUPPORTED-RISK | STYLE-SIGNAL | UNVERIFIED | NOT-APPLICABLE` are **separate** from RMC's finding enums. Mapping is conditional: a verified counterexample may be a `CONFIRMED` AntiSlop defect only after its target, source and claim scope are checked; `UNVERIFIED` is not automatically slop; `NOT_APPLICABLE` yields no warning. Lexical signals and failed method preconditions are not automatic errors about user work. Neither this reference nor the Python helper updates the separate AntiSlop plugin or creates a standing service.

## E. Regression design and coverage bounds

Seed supplied by user: `rmc_vct_admissibility_probe.py` contains 7 hand-labelled **synthetic** cases and a transcribed VCT `dep_sort()` function. Its 11 assertions are internal fixture assertions, **not** measured false-positive rate nor real ChatGPT behavioral regression. Keep those cases as preserved source (`tests/fixtures/user-probe-original.py`) and add expanded near-miss tests against the new optional helper (`tests/test_adaptive_gate.py`). Distinguish `source_inspected`, `synthetic_test_executed`, `host_behavior_observed` and `deployed`.

If production evidence is later collected, sample across task genres; include negatives and near-miss positives, classify with evidence and independent adjudication, measure per-class false positive and false negative rates, and use a held-out set. No numeric threshold or claimed improvement until that evidence exists. Stop test expansion when further checks cannot change the current acceptance decision.
