# VCT v0.7 heuristic dispatcher – build, test, limitations

Current deliverable: partial overlay update to existing VCT v0.6 (which retains AREX v0.5). Additive Python bounded dispatcher and AREX metadata handoff; no claim of hosted MCP or autonomous target-repository patching.

## Executed local tests

- `python -m unittest discover -s vibecode-transducer/skills/vibecode-engineer/tests -q` → 151 tests, OK, including 23 new dispatcher tests. This is a reconstructed locally available subset of legacy test modules and supplied v0.6 update; not a complete installed-production environment.
- `heuristic_dispatcher_cli.py --spec examples/dispatcher_euler_refinement.json` → original `REFUTED_BY_WITNESS`, two iterations, refined variant tolerance met, original model claim remains refuted.
- `heuristic_dispatcher_cli.py --spec examples/dispatcher_inverse_blocked.json` → `MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE`, no fake refinement.
- `vct_math_cli.combine({'heuristic_dispatcher': ...})` → dispatch outcome returned under `DISPATCH_*` decision namespace, consumes Python execution results.
- Independent SymPy 1.14.0 check `integrate(h*(a+(b-a)*t)**2, t=0..1)-h*(a²+ab+b²)/3` → exact symbolic zero. Conditional on similar parallel square sections, not arbitrary shape.

## AREX verification ceiling

The currently installed plugin inventory shows `skills/arex-repository-intelligence/runtime/arex_router.py`, `references/arex-index.json`, and `SKILL.md`. Their tool/source contracts were inspected through Plugin Creator. The local partial-update workspace does not include the full AREX source; dispatch with `arex_query` appropriately yields `DONOR_METADATA_UNAVAILABLE`. A temporary *test double* of `arex_router.py` verified the dynamic import, metadata-only receipt and D07 handoff (`PASS`), then was removed. This is **not** a live test of AREX routing semantics. In the installed plugin archive, the dynamic sibling import is designed to call `route(query, load_index(), top=5)`. This integration was **not** executed against the full 1,000-entry AREX index in the local test; treat as `UNVERIFIED` until a live local or hosted installed-plugin test is run.

## Proof vs test

- `REFUTED_BY_WITNESS` is sufficient to disprove a **precisely scoped universal/uniqueness claim** under the declared forward model; not a general empirical claim of how nature works.
- Euler/periodic graph tolerance is a single or finite family test. `ORIGINAL_CLAIM_REFUTED_REFINED_VARIANT_PASSES` does not erase the original failure.
- Frustum polynomial identity is formal algebra for the stated geometry; it does not prove source data/source classification, program correctness, or all geometry.
- Mahajan dimensions/easy cases/lumping/pictorial proofs/taking big part/analogy are selected heuristics. Only enumerated operators are actual executors.
- No target repository, preimage SHA, permission, test runner, or deployed MCP handshake were supplied. `PATCH_APPLIED`, `PRODUCTION_VERIFIED`, and `AREX_DONOR_TESTED` must remain `UNVERIFIED`.

## Safety and acceptance

No arbitrary user Python, shell commands, external fetches, donor installs, or file writes occur in `dispatch`. `allow_writes=false` is compulsory. Repair budgets finite `0..6`. Conditional `REPAIR` cycles are separate from `PREREQUISITE` DAG edges. D00–D08 task graph is planning data, not executed patch evidence. Separate `local_apply.py` remains the only explicitly guarded local mutation route.
