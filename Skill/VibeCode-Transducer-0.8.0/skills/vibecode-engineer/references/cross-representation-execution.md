# VCT v0.6 — Cross-representation mathematical execution (evidence-bound)

## Purpose / provenance

Operational extension of the *user-supplied* `VCT_Math_Multimodel_AntiSlop_Audit.zip` and original `math_dsl_operator_registry.csv`, combined with the inherited VCT v0.4 representation-admissibility and heuristics layer. It is a scoped synthesis of existing mathematical methods, **not** a new theorem, certified theorem prover or a claim that every source has been independently checked in the present update.

Canonical artifact crosswalk:
- `registry_99_multimodel_audit.csv`: 99 unchanged `MATH-001..099` IDs + research annotations; the source's original `S01..S37` IDs remain **unresolved** without their referenced bibliography; this file is **not a correctness certificate**.
- `oa_multimodel_source_ledger.csv`: 22 OA literature candidates carried forward from the user's previous audit. `oa_linkage_status = DOMAIN_CONTEXT_ONLY_NOT_THEOREM_VERIFIED` is a valid limit; a domain-level reference cannot prove a particular theorem or code implementation.
- `multimodel_review_and_test_report.md`: previous research analysis and fixture report, not a live production receipt.
- `multimodel_dsl_contract_proposal.json`: research proposal, not implemented DSL compiler.
- `multimodel_kernel.py`: bounded Python mathematical examples (executed only upon actual CLI or Python call), not general PDE solver.

## Governing decision contracts

**Model identity:** `M = (Domain, State, Operation, Parameters, Assumptions, ObservationMap, Evidence, Goal)`. Representation change is a typed bridge `B_{ij}` with explicit **preserved structure** and **lost/unverified structure**. A similarity score or low norm difference by itself does not prove model or system identity.

**Admissibility:** representation witness and task-relative adequacy are independent tests. A count may be valid as a dimensionless observed rate but insufficient for inferring semantic claims. Check physical dimension and *measurement scale*, units versus entities, conservation/monotonicity/invariance, sampling and censoring, granularity and dependence, observability and identification. Unknown validity is `UNVERIFIED`, not `CONTRADICTED`.

**Abduction/induction/deduction:** preserve multiple competing forward models and candidate explanations; finite agreement only supports scoped empirical/inductive diagnostics; derive a consequence only under explicit assumptions, and distinguish analytical proof from checking finite points. A counterexample to a *specific universal claim* can be dispositive even though successful finite tests cannot establish that universal claim.

**Discrete to continuum:** specify grid, time step, boundary conditions, topology, stability regime, truncation error, convergence mode, and interpretation. `euler_decay` is a fixed-rate survival discretization, not automatic CTMC equivalence. For deterministic Euler positivity/stability a distinct condition might be appropriate; in this **probability** model `r*h <= 1` is required.

**Graph to continuum:** specify point domain, weight/degree normalization, operator scaling, boundary geometry, and target convergence (spectral, strong operator, Γ, etc.). `periodic_graph` checks only 1D periodic nearest-neighbor eigenvalues; do not infer topology for arbitrary network graphs.

**Inverse:** require forward map, observational quotient/symmetries, noise assumptions, identifiability and stability. `inverse_ambiguity` exhibits two different parameterizations with equal output. Two observations with same values do not prove all trajectories share a distribution; in this declared algebraic model gain and x0 enter only by their product.

**Validation & verification:** `numerical approximation` → numerical accuracy diagnostics; `software verification` → exact code behavior under tested fixtures; `mathematical proof` → sound derivation under domain assumptions; `empirical validation` → evidence the model is fit for its intended real-world use. These categories are not substitutable.

## Actual Python entry points

- `runtime/multimodel_cli.py --spec examples/multimodel_discrete_continuum.json`: isolated read-only evaluation of a typed contract.
- `runtime/vct_math_cli.py --spec path/to/combined.json`: may contain `multimodel_problem` alone or with `math_problem`, `heuristic_problem`, `engineering_spec`; results separated in `cross_representation_execution`. Existing math/heuristic paths remain supported.
- `runtime/mcp_server.py`: optional new `vibecode_multimodel_execute(multimodel_json)` tool if a real MCP server is hosted and connected; source presence alone is not deployment.
- Never evaluate arbitrary submitted Python, perform source mutation, return a global PASS based on one probe, or manufacture cloud execution receipts.

## Probe contract

Top-level object has `goal`, `target_claim`, `source_id`, `representation` (`entity, unit, measurement_scale, observation_map, dimensionless`), `models` (id/domain/operator/assumptions), `bridges` (from/to/kind/preserved/lost_or_unverified), `probes` (id/type/parameters/model_ids), optional `decision.error_tolerance`.

Supported bounded probe types:

| Type | Mathematical intent | Warrant ceiling |
|---|---|---|
| `euler_decay` | finite Euler/continuous decay comparison | finite-time numeric match only |
| `periodic_graph` | scaled periodic graph eigenvalues | one constructed graph family |
| `inverse_ambiguity` | non-injective hidden parameter witness | refute uniqueness for declared map |
| `graph_degrees` | graph degree-versus-connectivity counterexample | refute degree-based unique reconstruction |
| `observability_linear` | 2x2 LTI rank heuristic | tolerance-sensitive numeric rank only |
| `noisy_derivative` | discretization/noise perturbation | deterministic adversarial noise example |
| `region_candidates` | Mahajan model-family rivals | named candidates only |
| `dimension_check` | exponent-vector compatibility | necessary, never sufficient |
| `interval_decision` | threshold robustness | declared interval only |
| `datalog_reachability` | finite least fixed point with base rule | ground finite edge graph only |
| `lens_laws` | GetPut and PutGet on a projection lens | one declared source/view projection |

Any probe's `state = EXECUTED` means a bounded Python function ran. `CONDITIONAL_PASS` means a specified tolerance was met for that fixture, `REFUTED_BY_WITNESS` means the tested universal/identification claim was contradicted by that witness, `UNDETERMINED` retains rivals. An `INVALID_PROBE` is not `CONTRADICTED` theory; it is an inadmissible implementation input. A missing proof is `UNPROVED_GENERAL_CLAIM`, not false.

## Task graph / nonlinearity

`M00..M06` are prerequisite-bound declarations, computations and separation of evidence classes. Conditional `M07` hidden-state data, `M08` refinement, `M09` discriminating experiment, and `M10` model-class revision lead to `M11` engineering acceptance. Feedback returns to earliest invalidated assumptions as a **REPAIR edge**, never as an asserted acyclic prerequisite. An observation cannot be upgraded to production fix without repository-specific acceptance and runtime receipts.

## Applied mathematics and literature (source roles, not formal-proof licenses)

Inherited OA links (check edition, publication dates, full text and source role before new public citations):

- Brunton, Proctor & Kutz (2016), *PNAS*, sparse dynamics and basis/coordinate assumptions — `OA01`.
- Villaverde et al. (2023), *Bioinformatics*, structural identifiability tools — `OA02`.
- Cilfone, Kirschner & Linderman (2015), *Cellular and Molecular Bioengineering*, coupled discrete-agent/continuous models — `OA03`.
- Chazal & Michel (2021), *Frontiers in Artificial Intelligence*, topology extraction and scale conditions — `OA05`.
- *Formally Verified Architecture Patterns of Hybrid Systems Using Proof and Refinement with Event-B* (2020), research proceeding — `OA06` (NOT a verified journal article).
- Ecological model-selection guide (2021), *Ecology*, goal-relative model selection — `OA07`.
- Mahajan, *Street-Fighting Mathematics* (2010), sections 1–6, is methodology for generating and falsifying approximations; its heuristics do not constitute an automatic mathematical/empirical proof. The three-dimensional frustum example adds interaction term `ab` after boundary-case failure.

## Required adversarial acceptance checks

(1) false unit assignment and correct near-miss; (2) dimension match but false semantics; (3) discrete step outside probability domain; (4) smaller derivative step amplifying measurement noise; (5) same output generated by different latent states; (6) different graphs sharing degree sequence; (7) two candidate families agreeing on short prefix; (8) recursive Datalog missing base rule; (9) projection lens cannot reconstruct hidden state from view; (10) missing tolerance leaves quantitative decision narrower. Record exact test command and scoped PASS only for executed tests.
