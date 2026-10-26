---
name: vibecode-engineer
description: Use for vibe coding, mathematical mental-model selection, evidence-gated engineering task derivation, MDE/KRR modeling, donor search, source inspection, bug reproduction, and guarded fixes.
---

# VibeCode Transducer — engineering + mathematical model derivation (skill v0.8.0 (bounded policy-authorized canary orchestration))

**Identity:** VibeCode Transducer (VCT), not KTA/KAT. Preserve the user's task and observed behavior. Skill instructions are not automatic tool calls, and a saved plugin does not provide cloud hosting; a live Python tool invocation is REQUIRED for mathematics-dependent decisions in an available ChatGPT Python/cloud runtime. If unavailable, explicitly block the computational claim. This does not connect MCP, modify code, or certify mathematical correctness by itself. Read the original `references/atlas-and-routing.md` for the existing narrowly implemented static Atlas operators and `references/donor-map.md` for donor policy.

## Governing contract and controller order

1. **Task intent:** determine request, observable target, source provenance, constraints, non-change surfaces, permitted code access, current branch/revision, programming language and target runtime. Do not silently convert lexical diction analysis into complete rhetorical/causal analysis.
2. **RMC:** materialize entities, phenomena, relations and measures; distinguish empirical observation from its symbolic/numeric representation; choose route/claim regime; select operator only after type/precondition and representation warrant checks; revisit earliest failed assumption on a counterexample. Read `references/math-model-derivation.md` when the task involves modelling, mathematics, inference, proof, inverse reconstruction, statistics, graph, topology, or heuristics.
3. **AntiSlop:** test unsupported promotion of claims, false code/test/scope assertions, missing provenance, mismatched mathematical assumptions, fabricated proof/behavior, and task substitution. Demand smallest discriminating counterexample plus near-miss positive control.
4. **VCT:** choose `debug | donor | refactor | migrate | trace | performance | design | test | review`, scope state transitions and ownership, use only legitimate code and math operators, preserve donor licensing/compatibility, produce an evidence-bound task graph and optional patch preview. No unauthorized write.

## Mandatory Python-in-the-reasoning-loop for mathematical decisions

**Corrected hard requirement:** Every VCT decision depending materially on mathematical modelling, quantitative evidence, symbolic/graph calculation or data manipulation must **invoke a real Python tool during the current reasoning turn**, consume the computed values and failure signatures, and revise operator/task selection accordingly. Merely generating a router report, formula, plan, code snippet, or a DAG is **insufficient**. In the same turn, state which Python runtime/tool was actually invoked. Do NOT say an installed skill runs Python automatically; plugin assets are not necessarily mounted in a cloud Python sandbox. If a callable Python runtime or source data are absent, mark the computational decision `PYTHON_EXECUTION_UNAVAILABLE`/`PYTHON_COMPUTATION_REQUIRED`; do not simulate a receipt. Never equate `EXECUTED` with a proved theorem or target-code fix. Read `references/cloud-python-decision-contract.md` first for exact supported modes and gates.

On an eligible cloud Python environment, use the actual runtime implementation when accessible:

```bash
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_lexical.json
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_linear_inverse.json
```

The Python-backed combined CLI now returns `math_python_execution`, `decision_gate`, `computed_findings` and `next_tasks`. `NO_OBSERVATION_PAYLOAD` and `UNSUPPORTED_COMPUTATION` mean **no mathematical computation occurred**. If an operation needs a specialized uninstalled package or unsupported kernel, leave it unexecuted; do not invent an execution result. Use the Python cloud calculator for falsifying numerical probes, source-backed measurements, and recomputation as appropriate; no obligation to run all 100 mathematical registry items.

## Mathematical mental-model path (model selection conditional; computational execution mandatory when decision-relevant)

Before operator selection:
- Identify the **claim type**: lexical/descriptive, semantic/interpretive, argumentative, statistical, causal, inverse, deductive, or engineering-only.
- Identify the **observation type**: token spans, numeric samples, graph edges, matrices, geometry, symbolic formulae, code state, or unknown; units and measurement domains; masks and denominators; sampling dependence/censoring.
- State the **representation map** from phenomenon/empirical relations to formal objects. One numeric feature, a dimensionless ratio, and a unidimensional latent construct are **three different propositions**; neither dimensional analysis nor a lexeme count proves rhetorical meaning.
- Write competing **forward model** and **inverse conjecture** where relevant. Test existence, uniqueness, stability, equivariance/invariants, and loss under the representation. If many sources yield the same observation, return a candidate class or `UNIDENTIFIABLE`, not one alleged recovered truth.
- Map a candidate math operator to explicit typed preconditions, warrant, limitation, falsifier, status (`ELIGIBLE_AS_METHOD`, `NEEDS_EVIDENCE`, `NOT_APPLICABLE`) and tasks, and distinguish declared predicates from observed runtime witnesses.
- Use Toulmin claim/data/warrant/backing/qualifier/rebuttal to audit inferential bridges; Mahajan dimensions/easy cases/lumping/analogy for *heuristic conjecture*; Rice instance-feature/algorithm-set/performance distinction for method selection. None independently proves program behavior or semantic interpretation.
- Build a **conditional DAG** of bounded tasks; task execution is not implied by DAG generation. A falsifier invokes revision T17 and invalidates downstream evidence rather than merely tuning a coefficient.

Read `references/math-model-derivation.md`, `references/math_heuristic_literature_review.md`, and `references/math_001_100_crosswalk.csv` selectively according to the claim. `math_001_099_registry.csv` is the original 99-item inventory, `MATH-100` is a flagged **proposed** Buckingham-Π addition in the crosswalk, and `ATLAS-031..080` refers to a DIFFERENT method catalog; never conflate IDs. The registry is **reference data, not 100 implemented executors**. `references/math_task_graph.yaml` is a conceptual 18-task model; the current Python module selects and orders a bounded subset, not a complete MDE/KRR compiler.

## Case boundary: Co-Domain v1.3 pattern extraction

In `SECOND_ORDER_MODELS_v1.3.md` α anchored-context windows `W3` and `W5` overlap, their ratios are descriptive and not independent hypothesis tests, absent B endpoints are `lag=null` censored, and the sample of evaluated anchors is bounded by 80. β observed lexical gaps and X→Y silence are not semantic absence. δ/ε/φ/γ are surface candidate gates, not validated proposition parsing, causal attribution, formal proof, or morphological parsing. Sections `03` (measurement), `04` (user-selected evidence-bound task candidates), and `05` (human steering) retain different owners. The `corpus-to-codomain/unified-1.1` snapshot root remains unchanged. See `references/math-model-derivation.md` for Toulmin evidence and counterexamples.

## Additional bounded analysis commands

The v0.1 transducer remains available, unchanged, for bounded static code analysis, Python AST inspection, 034/Jaccard donor prefilter, 055/MAD, 058/topological ordering on supplied edges, trace chronology and SHA-bound patch preview. These do not prove target behavior:

```bash
python -m unittest discover -s skills/vibecode-engineer/tests -v
python skills/vibecode-engineer/runtime/vibe_transducer.py --spec skills/vibecode-engineer/examples/duplicate_selection.json
```

Legacy v0.2 standalone **read-only mathematical selector** (stdlib, plan-only):

```bash
python skills/vibecode-engineer/runtime/math_model_router.py --spec skills/vibecode-engineer/examples/second_order_model_problem.json
python skills/vibecode-engineer/runtime/math_model_router.py --spec skills/vibecode-engineer/examples/semantic_claim_blocked.json
```

Updated **combined** CLI now performs actual Python observation computations when `observation_payload` is supplied; also uses `math_problem` plus an optional independent v0.1 `engineering_spec`; it does not write code:

```bash
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec path/to/combined.json
```

Input keys are `goal`, `claim_type`, `observation_kind`, optional `source_id`, and explicit boolean `features`; labels are **user declarations** and must not be treated as independently validated findings. See `references/math-model-derivation.md` for accepted enum values, scope, and example. The standalone CLI produces a conditional task dependency order, mathematical method candidates, missing evidence, forbidden claim promotions and revision trigger. A CLI `exit=0` means the analysis serialized; check `math_python_execution.python_execution.state` to know if a computation ran. It does **not** automatically mean that it performed an inferential statistical test, mathematical proof, runtime validation or repository patch. No host MCP endpoint or local repository auto-access is packaged.


## v0.4 Model Admissibility & Heuristic Inference — execution and claim gates

READ `references/representation-heuristic-inference.md` whenever a task involves **choosing a unit or mathematical representation, dimensionless/formal assignment, an approximation from sparse data, normalization, or abductive/inductive/deductive claims**. The v0.3 router is insufficient by itself: it only checks declared boolean flags. V0.4 introduces an actual bounded Python kernel `runtime/heuristic_inference.py` and optional separately deployed MCP tool `vibecode_heuristic_execute`. Use it when Python access/source is actually present, never simulate receipts.

For modelling-dependent decisions: (a) individuate entities/events and boundary/identity; (b) specify relations, preserved transformations, measurement scale, domain/unit and provenance; (c) keep **representational warrant** separate from **task-relative adequacy**; (d) keep dimensionless scalar separate from one-dimensional latent construct; (e) choose *only* scale-licensed operations and normalization, with null denominator semantics; (f) retain explicit rivals from abduction, do finite inductive diagnostics without unjustified generalization, and derive only conditional logical/model consequences; (g) test easy/boundary cases, non-injectivity, decision-robust bounds, revising the model family (not just coefficients) when all candidates fail; (h) route H01–H07 planned tasks to conditional original T00–T17 tasks and reopen the earliest failed assumption on falsification.

Examples (from an **actually available** Python environment with these package files):

```bash
python -m unittest discover -s skills/vibecode-engineer/tests -v
python - <<'PYRUN'
import json,sys
sys.path.insert(0,'skills/vibecode-engineer/runtime')
from heuristic_inference import execute
with open('skills/vibecode-engineer/examples/heuristic_regions_underdetermined.json') as f:
    print(json.dumps(execute(json.load(f)),indent=2))
PYRUN
```

The bounded initial candidate grammar supports only `pow2` and `regions3`, `exposure_rate`, declared interval-threshold decisions, a known Gaussian-lumping example, and a 2-witness noninjectivity counterexample. It does NOT autonomously validate empirical ontology, select all mathematics, infer rhetorical meaning, produce confidence intervals, or prove arbitrary propositions. When the user's target is beyond these domains, return `UNSUPPORTED_COMPUTATION` or a precise evidence/task gap; do not pretend to have a general heuristic oracle. Executed mathematics remains conditional decision evidence, not target code verification.


## v0.7 Mahajan-inspired full-loop dispatcher / depatcher

For requests needing *which model should be used and how it is falsified, refined, routed to AREX and handed to engineering*, READ `references/heuristic-depatcher-loop.md`. Use `runtime/heuristic_dispatcher.py` or `runtime/heuristic_dispatcher_cli.py` to execute typed bounded Python probes. Mahajan's methods: dimensions, easy cases, lumping, pictorial proof/interpretation, taking out the big part, analogy. Executable scope: v0.6 probe families, bounded Euler/periodic graph refinement, frustum exact cross-term polynomial derivation and Gaussian-lumping error comparison. Other methods remain heuristic guidance, **not** general-purpose executable provers.

The loop retains initial failed receipts even if a refined variant passes; distinguishes synthetic numerical testing from formal/empirical validation; and never elevates AREX metadata to verified donor behavior. When a concrete AREX query is present, it uses the existing sibling `arex-repository-intelligence/runtime/arex_router.py`. Read `../arex-repository-intelligence/references/depatcher-discovery-contract.md`. `D00–D08` task graph states are PLANNED, even after Python computational evidence is produced. Code modification requires the separate, authorized `local_apply.py` pathway and a trusted checkout with fail-before/pass-after testing. `REPAIR` feedback is not a logical prerequisite cycle. No automatic unlimited retry, auto-installation, donor execution, or hosted MCP is implied.

```bash
python skills/vibecode-engineer/runtime/heuristic_dispatcher_cli.py --spec skills/vibecode-engineer/examples/dispatcher_euler_refinement.json
python skills/vibecode-engineer/runtime/heuristic_dispatcher_cli.py --spec skills/vibecode-engineer/examples/dispatcher_inverse_blocked.json
```

## Donor, patch and result integrity

Inspect code, tests and permitted revision before any concrete bug diagnosis. Compare donors by behavior, license, dependencies, interface, state ownership and runtime tests, not only lexical overlap. Present minimal diff and a fail-before/pass-after reproducer with close negative control. `runtime/local_apply.py` is a **local-only** guarded patch tool; do not expose through remote MCP; require explicit owner approval, write enablement, trusted isolated checkout, and owner-supplied test runner. Preserve `SUBMITTED`, `ACKNOWLEDGED`, `COMMITTED`, `COMPLETED` as distinct queue states and retries by attempt. `BLOCKED` only follows a contradicted declared prerequisite; absent runtime confirmation is `INCOMPLETE/UNVERIFIED`.

The Python MCP adapter `runtime/mcp_server.py` is an *optional source component*: only a deployed, SDK-compatible authenticated endpoint and verified handshake would create callable tools in ChatGPT. Installed skill or sandbox Python != hosted service. Read `references/cloud-venv-and-mcp.md` before proposing a connection. Avoid secrets in source submissions.

## Required handoff output

State (a) problem and observation type, target claim, mathematical representation and evidence ceiling; (b) candidate models and falsifying rival; (c) operator eligibility with unmet preconditions; (d) conditional task graph and branch triggers; (e) actual source snapshot/commands/receipts and explicitly unverified claims; (f) smallest warranted engineering change/test. A report with missing evidence is legitimate; never invent proof, completion, or deployment.

## Cloud execution guarantee limit

The code packaged here can be executed in a real Python tool when the source and corpus are made available. The skill cannot control the host tool availability or turn an installed package into an always-on cloud service; if no Python tool is accessible the requested computational contribution must remain unresolved, rather than silently falling back to a text-only router. The MCP adapter now offers read-only `vibecode_math_execute` for a separately deployed service, but **is not** an automatically deployed cloud Python service.

## v0.6 Cross-representation modelling and mathematical evidence (MANDATORY WHEN MATERIAL)

Read `references/cross-representation-execution.md` for tasks involving **multiple models of one phenomenon; discrete↔continuum; graph↔continuum; hidden-state reverse engineering; identifiability; coupled multi-scale models; bidirectional transformations; noise-vs-discretization; or proof obligations for approximations**. This is the actual Python-backed continuation of the v0.4 Model Admissibility and Mahajan heuristic path, not an instruction-only framework. It is not an unconditional step for all coding tasks.

- **Materialize:** declare domain entity, individuated unit, measurement scale, observation map, dimensions (including explicit dimensionless type), source provenance, state and assumptions. Reject unsupported conversion of lexical counts to semantics, graph degrees to unique connectivity, or algebraic precision to empirical fidelity.
- **Relationalize:** instantiate at least two typed model contracts when alternatives matter; name bridge operation, invariant/preserved behavior and **lost or unverified information**; a bridge is *not* automatically an exact inverse. A source-to-view lens requires consistency laws, and a hybrid model requires a coupling/clock/synchronization contract.
- **Choose candidate operator by evidence** using `references/registry_99_multimodel_audit.csv` (99 original IDs, annotated) and `references/oa_multimodel_source_ledger.csv` (22 inherited OA references). These are literature mappings, NOT 99 executed algorithms nor 22 independently checked source proofs. `MATH-100` remains separate PROPOSED crosswalk and `ATLAS-*` remains unrelated to MATH IDs.
- **Execute** in real Python using `runtime/multimodel_engine.py` and `runtime/multimodel_kernel.py`, or `vct_math_cli.combine` with `multimodel_problem`. The optional `vibecode_multimodel_execute` MCP handler works only if the MCP server is actually hosted/connected. Never imply the skill automatically mounts files or hosts Python.
- **Read results**: `probe_receipts`, `source_sha256`, `decision_gate`, `proof_obligations` and conditional M00–M11 tasks. An executed numerical witness may refute a narrowly specified universal/reconstruction assertion; passing finite synthetic probes NEVER proves full model equivalence, convergence or runtime behavior. Distinguish observations, abductive rivals, induction from finite refinements, conditional deduction, symbolic proof, empirical validation, and software tests.
- **Repair** at the earliest representation or assumption contradicted. A false *model class* must be expanded (frustum interaction term `ab`), not just a coefficient refit. A failure of numeric tolerance may require a smaller step, changed method, or changed measurement—not an unfounded physics claim.
- **Handoff** through conditional DAG with only actual prerequisite edges. Feedback revisions are conditional repair edges and may cycle without invalidating the prerequisite DAG. Do not equate `PASS` for a bounded calculation with certification of all models or with successful target software deployment.

Execute directly (if installed source and Python exist):

```bash
python skills/vibecode-engineer/runtime/multimodel_cli.py --spec skills/vibecode-engineer/examples/multimodel_discrete_continuum.json
python -m unittest discover -s skills/vibecode-engineer/tests -p 'test_multimodel*.py' -v
```

`runtime/multimodel_kernel.py` contains only bounded declared examples (Euler survival, one periodic graph spectrum, simple two-state observability, a parameter symmetry, a noise perturbation, two Datalog rules, and a projection lens). It does not perform arbitrary PDE solving, formal theorem proving, topology inference, general multi-model optimization or real empirical validation. Unsupported domains must return explicit limitations and an evidence-backed task, not a guessed output.


## v0.8 autonomy boundary: trusted snapshot and fail-before checks

For requests to execute autonomous patching, read `references/autopatcher-trust-and-control.md` and use the **actual** `runtime/autopatcher_core.py` and `runtime/autopatcher_control.py` in a Python runtime. This local beta is a strictly bounded **canary**, not arbitrary repository execution. It verifies an operator-registered Git source at pinned SHA, obtains an operator-signed HMAC grant bound to job/repo/commit/diff/path, evaluates a non-executing JSON regression fixture before and after an exact patch to an ephemeral Git archive snapshot, and stores an evidence-scoped receipt in SQLite. It may report `CANARY_RED_GREEN` without claiming target production tests, repository mutation or deployment. It refuses invalid/expired/mismatched grants, green baseline, dirty/stale repo and protected paths. Gateway assertions require separate operator-owned trust; no token issuer is exposed over MCP. Legacy `local_apply.py` is **not** a trusted Git checkout or fail-before guard.

Production prerequisites remain **UNVERIFIED**: SDK v2 live handshake, externally authenticated MCP control plane, durable sandbox worker for untrusted project tests, repository provider attestation, PR/CI integration, staged deploy/rollback. `CANARY_RED_GREEN` is not `PATCH_TESTED_IN_ISOLATION` or `DEPLOYED`. Production/push remains denied in the packaged source. See `docs/AUTOPATCHER_PHASE1_VERIFICATION.md` for exact test scope.
