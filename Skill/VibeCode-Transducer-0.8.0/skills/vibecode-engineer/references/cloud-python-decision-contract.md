# Python-first cloud decision contract — VCT 0.3.0

## Governing correction

The mathematical router is **not** merely a static model selector. For every VCT task where a mathematical model materially informs an engineering or reasoning decision, run a real calculation using the available Python tool **inside the active reasoning turn**, inspect its result and provenance, test an alternative/falsifier, and feed the results back into the operator choice and task graph. The model's numerical answers without a witnessed tool run are NOT Python execution receipts.

**Invariant:** `MATH_DECISION_READY => PYTHON_EXECUTED & TYPED_INPUT & INSPECTED_RESULT & CLAIM_GATE_CHECKED`. The converse does not hold: execution alone does not establish a mathematical theorem, semantic/causal interpretation, or target software behavior.

## Execution modes and boundaries

1. **ChatGPT-hosted Python tool (cloud session):** when a Python/Code runtime is available in the current host, invoke it in that turn using explicit bounded data, the actual `cloud_math_executor.py` (if files can be made available) and the `math_model_router.py` with its `math_001_100_crosswalk.csv` beside it. Record tool invocation and results. Do not infer that plugin assets are auto-mounted; load or materialize the actual source only by supported tool access. If the packaged files cannot be mounted, a bounded, independently inspectable Python calculation can be run directly with the Python tool but it must be labeled an *ad hoc* computation rather than a VCT backend run.
2. **Deployed Python MCP backend:** optional persistent service if explicitly deployed and connected. An explicit read-only `vibecode_math_execute` tool is supplied in `runtime/mcp_server.py` (MCP SDK v2); supply typed JSON, not Python source code. Source files are not deployment. No live MCP endpoint, hosted executor, persistent Python process or guaranteed always-on tool call is provided by Plugin Creator. Do not claim one.
3. **No Python tool present:** return `PYTHON_EXECUTION_UNAVAILABLE` with data/assumption debt and a safe execution recipe. Do not conclude mathematical eligibility as empirically tested and do not fabricate calculations. General conceptual reasoning may still be given, labeled uncomputed.

The mandatory nature concerns reasoning tasks needing mathematical operations, not arbitrary non-mathematical tasks. Operator-specific computation is conditional: never run all 100 registry entries; choose from problem types, evidence and preconditions. Unsupported operators must be marked `UNSUPPORTED_COMPUTATION`, not silently approximated.

## Computational cycle

```
Observed problem & claim + source fingerprint
    -> materialize entities, types, units, relations, sampling/censoring
    -> nominate rival mathematical models (Mahajan, Rice; no proof)
    -> select eligible operator by preconditions and measurement contract
    -> CALL PYTHON with observed data, do not simulate output
    -> inspect computed values, lost information, counterexample controls
    -> adjust instance signature / model / tasks where warranted
    -> halt as VERIFIED_OBSERVATION_ONLY, INCOMPLETE or BLOCKED
    -> report source hash, actual tool, calculated output and claim ceiling
```

`cloud_math_executor.execute(spec)` takes `math_problem` compatible with v0.2 plus `observation_payload`. The combined `vct_math_cli.combine(spec)` now always calls that Python evidence kernel and returns `math_python_execution`; absent payload yields `PYTHON_COMPUTATION_REQUIRED`. `vct_math_cli.py` retains the prior independent engineering static analysis output for compatibility.

## Implemented Python calculations (stdlib only)

- `lexical_spans`: corpus tokenization bounded by sentence, W3/W5 backward window counts/rates, <=80 evaluated anchors, censoring of unseen boundary, lexical gap series. Descriptive only, not true semantic extraction. One input is treated as one document. This is a bounded independent implementation of α/β measurement, not byte-for-byte Co-Domain JS equivalence.
- `numeric_samples`: sample size, mean, median, raw median absolute deviation and sample standard deviation. Descriptive only; no inference distribution, iid or p-value.
- `graph_edges`: weak connected components, topological ordering iff directed acyclic; graph isomorphism and ownership unverified.
- `matrix`: exact rational Gaussian elimination up to 12x12, rank, nullity, consistency and uniqueness of a finite linear equation system; no noisy/general inverse solver or numerical conditioning certificate.
- `geometry`: point-in-polygon via ray crossing with explicit boundary result for bounded floating inputs; polygon validity, robust computational geometry and coordinate transformations unverified.

`symbolic`, `code_state`, `unknown`, persistent homology, Bayesian modeling, algebraic topology, causal discovery, general theorem proof, and 100 individual registry implementations remain NOT IMPLEMENTED in this kernel. Use specialized Python libraries only when actually available and exercised with independent tests (SciPy, SymPy, NetworkX, Gudhi, Z3, etc.).

## Outcome states

- `EXECUTED` = function called in Python with typed payload; not proof or semantic identification.
- `NO_OBSERVATION_PAYLOAD` = no data; cannot say the model has run.
- `UNSUPPORTED_COMPUTATION` = no implemented operator for observation kind; cannot say the 100 catalogued mathematics were executed.
- `DESCRIPTIVE_RESULT_INFERENCE_UNVERIFIED` = statistics calculated; no population inference warranted.
- `OBSERVATION_ONLY_HIGHER_CLAIM_UNVERIFIED` = numeric/lexical measurement cannot prove semantics, causality, deduction or full inverse reconstruction.
- `COMPUTED_OBSERVATION_REVIEW_REQUIRED` = measured observable only, inspect against data and independent control.

## Specific source contract: SECOND_ORDER_MODELS_v1.3

Keep Section 03 descriptive measurement, Section 04 candidate editorial tasks, Section 05 human steering. Anchor matches cannot bridge sentences, W3 and W5 share paragraphs, and `B=null` censoring cannot be treated as zero lag. Empty lexical counts do not imply semantic absence; delta/epsilon/phi/gamma are marker candidates only. Toulmin warrants require proposition-level annotation with provenance before rhetorical claims. Null is not a probability estimate. Source immutable and exclusion settings modify a *measured view*, not the raw source.

## Required small audit/decision trace in user-facing engineering answer

1. Input type and claim; source revision/hash.
2. Exact Python tool actually invoked and status, no implied background worker.
3. Computed values and at least one boundary/negative test affecting the decision.
4. Operator/model chosen or rejected and the inference ceiling.
5. Updated dependency tasks, problems still untested, earliest premise to revisit.

This is an execution policy and kernel contract, not authorization to mutate a project or a live MCP connection.
