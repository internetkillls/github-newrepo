# VCT–AREX full-loop heuristic dispatcher v0.7.0

**Scope:** a bounded, actual Python computation and decision-cycle for supplied typed models. It is not a general theorem prover, universal inverse-model oracle, autonomous code mutation engine, or deployed cloud MCP endpoint. 'Depatcher' here means task dispatcher/re-evaluator; patch operations remain guarded, local-only, and separately authorized.

## Governing source vs engineering synthesis

Sanjoy Mahajan, *Street-Fighting Mathematics* (MIT Press 2010), supplied PDF: **1 Dimensions** (printed pp.1–12); **2 Easy cases** (13–30, frustum pp.17–20); **3 Lumping** (31–55); **4 Pictorial proofs** (57–76); **5 Taking out the big part** (77–98); **6 Analogy** (99–121). The chapters supply heuristic techniques, not formal licenses to promote guesses to theorem or empirically correct models. The dispatcher, schemas and task phases below are VCT engineering synthesis, not Mahajan's own software design.

## Admissibility-first loop

1. **SCOPE / CHARACTERIZE**: identify phenomenon, observed data, measurement scale, unit, source ID (declared provenance != verified source), target claim, inference type, acceptable error, data rights, and behavior/repository boundary.
2. **MODEL / RIVALS**: build typed model set with explicit domains, assumptions, bridges and loss statements; choose a plausible rival, distinguish data conditioning from ontological truth.
3. **HEURISTIC SELECTION**: Dimensions (comparability and dimensionless groups); Easy cases (extremes, trivial, structural counterexample); Lumping (what information is lost); Pictorial proofs (visual structural explanation, not proof by image alone); Taking out big part (largest decision-changing uncertainty); Analogy (transport requires preserved relation and defeater). Select only if the mathematical object is appropriate.
4. **EXECUTE PYTHON**: use `runtime/heuristic_dispatcher.py` on typed user-supplied data and `runtime/multimodel_engine.py` probes; attach input SHA, real result, and named finite-test scope. Nothing is inferred merely by a token keyword.
5. **TEST / REFUTE**: finite counterexample (`REFUTED_BY_WITNESS`), multiple surviving hypotheses (`UNDETERMINED`), invalid probe (`UNSUPPORTED`), exact polynomial identity with assumptions, or bounded numerical tolerance (`CONDITIONAL_PASS`). Positive finite tests are not general proof.
6. **REPAIR / REFINE**: for declared tolerance failures of `euler_decay` or `periodic_graph` only, refine step or graph size with bounded iterations and actual re-execution. Store the original failed receipt: a refined success is *not* retroactive success of the original claim. For noninjective inverse maps, request independent observation or return equivalence class; finer time step does not repair identifiability. For all models refuted, revise model *class* (frustum interaction term) rather than arbitrarily refit coefficients. Reject uncontrolled recursive repair loops.
7. **AREX HANDOFF (conditional)**: `arex_query` calls existing sibling `arex_router.py` via local Python when present. Metadata candidates stay `METADATA_CANDIDATE_ONLY`: source skill, dependency, license, commit and target runtime must be separately inspected. `NO_EXACT_ROUTE` and unavailable AREX are legal outcomes. No donor code is downloaded, installed, or executed automatically.
8. **TASK GRAPH**: produce M00–M11 domain tasks and D00–D08 dispatcher tasks. Directed `prerequisites` form an acyclic DAG; `REPAIR` feedback is a separate typed edge, *not* a circular prerequisite.
9. **PATCH / VERIFY / HANDOFF**: optional `engineering_spec` generates a legacy read-only transducer result if available. Guarded `local_apply.py` remains separate, with human approval, checkout, preimage SHA, fail-before / pass-after and target-runtime receipts. Reopening after a failing test requires a fresh evidence record; task graph generation does not execute target code.

## Running

From the installed plugin's root (with Python and the files actually present):

```sh
python skills/vibecode-engineer/runtime/heuristic_dispatcher_cli.py --spec skills/vibecode-engineer/examples/dispatcher_euler_refinement.json
python skills/vibecode-engineer/runtime/heuristic_dispatcher_cli.py --spec skills/vibecode-engineer/examples/dispatcher_inverse_blocked.json
python -m unittest discover -s skills/vibecode-engineer/tests -v
```

`vct_math_cli.py` accepts top-level `heuristic_dispatcher` alongside existing `math_problem` and `multimodel_problem`. The optional MCP `vibecode_dispatch_execute` is source only until securely hosted and connected.

## Contract

Required input: `allow_writes=false`, `multimodel_problem` (v0.6 typed schema). Optional: `max_refinements` (integer 0..6), `arex_query` (specific capability, not generic keywords), `mahajan_case` (`frustum_model_revision` or `gaussian_lumping`), `engineering_spec` (existing static VCT schema). Arbitrary shell commands, donor code, and mutation arguments are *not* accepted. If unsupported object or absent observation, return a typed evidence gap rather than fabricated PASS.

`input_sha256` fingerprints serialized declarations, **not independently verified real-world data**. `refinement.input_hash` fingerprints each amended numerical configuration. Evidence states and dispositions must be scoped to claims, not the project overall. Any numerical proof is limited to the tested instance; formal identity from the frustum case relies on the stated linear-square-section geometry and is independent of data provenance.

## Cases / falsifiers

- Euler decay: error exceeds tolerance at coarse step, rerun at smaller steps; expected `ORIGINAL_CLAIM_REFUTED_REFINED_VARIANT_PASSES`, with retained initial counterexample.
- Inverse decay: two different `(gain, x0)` produce same observations; expected `MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE`, not a fake refinement.
- Regions from first four terms 1,2,4,8: rival models still fit; expected `NEEDS_DISCRIMINATING_OBSERVATION`, not predicted `n=4` as observed data.
- Mahajan frustum pp.17–20: old class `h(a²+b²)/2` fails pyramid; interaction `h(a²+ab+b²)/3` satisfies exact polynomial integration given geometry. A coordinate proof is not empirical validation of unrelated building geometry.
- Gaussian lumping: 1/e and FWHM estimates can have different known errors; this does not imply that FWHM always wins for arbitrary functions.
- AREX absent or no appropriate donor: bounded `DONOR_METADATA_UNAVAILABLE` or `NO_EXACT_ROUTE`, without blocking all mathematical reasoning.

## Source and verification limits

Existing v0.6 multimodel studies and OA references in `registry_99_multimodel_audit.csv`, `oa_multimodel_source_ledger.csv`, and `multimodel_review_and_test_report.md` remain inherited context. Their per-entry provenance is not freshly reverified by dispatcher. Neither these docs nor 151 synthetic tests prove end-to-end production patch execution. Full cloud-hosted MCP and donor code verification require separate integration/authorization.
