# VCT 0.4 — Model Admissibility & Heuristic Inference

**Status:** an executable, bounded engineering decision aid. It does not discover an ontology of the world, infer latent constructs, validate natural-language semantics, prove arbitrary laws, or guarantee an always-running cloud Python service.

## Problem and literature anchors

The governing questions are: what legitimately counts as one observation or model unit; which relations survive a representation; which arithmetic operations/normalizations are meaningful; which competing explanations fit limited evidence; which new observation best discriminates them; and which conditional deductions can be verified computationally. Distinguish **representation warrant** from **task-relative adequacy**. Neither is universally binary. Source lineage: Mahajan, *Street-Fighting Mathematics* (2010) 1.3 (formally assigned dimensions in Gaussian integral, print pp.7–10), 2.3 (frustum's missing `ab` interaction term, pp.19–20), 3.2 (lumping / FWHM, pp.33–35), 6.2 (region counting via analogy, pp.103–106); Toulmin (argument warrant vs observation); Rice (instance-feature-dependent algorithm selection). These are sources for modelling ideas, not certificates of software correctness.

**Three non-synonyms:** (a) one countable event, (b) a dimensionless mathematical number, and (c) a unidimensional psychological/semantic latent factor. An observed event count can be legitimate yet inadequate to infer rhetoric. Arbitrarily assigning a formal dimension helps analysis only if its relations are mathematically consistent; it does not establish physical/semantic ontology.

## Executable contract

Runtime `runtime/heuristic_inference.py` has read-only `execute(heuristic_problem)` callable from actual Python, combined CLI (optional `heuristic_problem` plus existing `math_problem`), and MCP source tool `vibecode_heuristic_execute` (only when separately deployed). The module is pure Python stdlib. Every output contains input fingerprint, runtime version, *distinct* representational and task adequacy statuses, normalization receipt, heuristic family comparison, conditional deductive check, and planned task actions H01–H07. It accepts explicit finite JSON only, never evaluates arbitrary expressions.

Minimal input:

```json
{
  "goal":"Is a lexical pattern unit adequate for a lexical frequency task?",
  "claim_type":"lexical",
  "representation": {
    "unit":{"name":"phrase occurrence", "kind":"event", "measurement_scale":"count",
      "dimension_kind":"dimensionless", "identity_rule":"exact phrase under pinned tokenizer",
      "boundary_rule":"one sentence", "source_ref":"corpus#hash"},
    "operations":["frequency"], "required_relations":["token_order"],
    "preserved_relations":["token_order"]
  },
  "normalization":{"method":"exposure_rate","observations":[{"count":2,"exposure":10},{"count":4,"exposure":20}]},
  "approximation":{"method":"none"},
  "deduction":{"rule":"none"}
}
```

`identity_rule`, `boundary_rule`, source identity and preserved relations are **declarations**. Their presence is tested, not their empirical truth. Label a complete representation as `DECLARED_WARRANT_NOT_INDEPENDENTLY_VERIFIED`, never as semantically proved. A dimensionless count is not a validated latent trait. `scale=nominal` cannot license `mean`, `ratio`, `sum`, `order`; `ordinal` cannot license arithmetic mean/ratios; `interval` cannot license meaningful origin-dependent ratios. Physical/formal dimensional check is *necessary*, not *sufficient*. Contradictory vectors block.

## Normalization operator and invariant caution

`exposure_rate` calculates `count / eligible_positions` with binary position assumptions: integer nonnegative, numerator not larger than denominator, denominator 0 -> null/undefined (positive numerator is contradictory). This is not a general count-intensity normalization nor a significance test. Same ratio for 2/10 and 4/20 does not identify semantic role, author intent or statistical independence. To compare nonbinary overlap, multiple hits per exposure, hierarchical data or dependence, specify a new measurement contract and implement a separately tested operator rather than bypassing constraints.

## Three inference jurisdictions (do not linearize by habit)

- **Abduction:** explicitly enumerate rival explanatory model families. `candidate_discrimination` currently supports only `pow2` and `regions3`; no free-form model discovery. On first four instances n=0..3, both fit; propose n=4 as a discriminating instance. Rival in finite set does not span all possible mathematical explanations.
- **Induction:** calculate agreement on finite data and optional held-out observations; even successful holdout can justify only *tested-instance discrimination*, not unrestricted generalization, causal attribution, or numeric population confidence. Data dependencies must be audited externally.
- **Deduction:** evaluate finite consequences **conditional on a specified model**, and use a two-witness counterexample to refute *sufficiency* of a one-valued feature for multiple labels, provided the observations/labels are valid. This is not a natural-language theorem prover.

The finite candidate 3D plane-region model `R(n)=sum(C(n,k) for k<=3)` is mathematically appropriate only when planes are in general position and the task is maximum regions. Without those assumptions it is a hypothesis family, not an observed world law. A model class can be wrong even if all known easy cases pass; choose `REVISE_MODEL_CLASS` when none of the declared candidates fit.

## Approximation / decision preservation

`bounded_decision` supports finite certified-or-asserted intervals `[lower,upper]` and threshold predicates. If the interval straddles the threshold, return `UNDETERMINED`, not an arbitrary midpoint decision. Bounds are inputs, not automatically estimated confidence limits. Gaussian `1/e` and FWHM lumping compute reference approximations for the *known Gaussian integral*, not certificates for arbitrary integrands. A tolerated relative error is task-dependent: an approximation that preserves a coarse yes/no decision can be useful without preserving fine numerical details.

## Model -> decision -> engineering tasks

`H01`: fix type/unit/dimension contradiction; `H02`: obtain identity/provenance/relation witness and higher-order claim warrant; `H03`: test feature nonidentifiability; `H04`: obtain discriminating evidence or revise model class; `H05`: audit out-of-sample extrapolation; `H06`: invalidate an overclaimed sufficient-feature mapping; `H07`: project conditional evidence into actual VCT engineering work. Tasks are ordered with `depends_on`, but status remains `PLANNED_NOT_EXECUTED`; a counterexample can reopen the earliest failed representation assumption.

Conditional integration with older T tasks: H01/H02 belong before T03–T05 operator choice; H03/H04/H05 belong in T08 and T14 tests; H06 is a falsifier that reopens the T17 revision branch; H07 is the handoff to T13/T15/T16. Do not rewrite the historical T IDs or Atlas IDs. Python results are computational witnesses, **not** semantic or empirical-proof certificates.

## Non-trivial negative / close controls

1. Valid unit + source + declared relations -> declared warrant only; absent identity/source -> debt, not false verification.
2. Nominal mean, ordinal ratio, interval ratio, and unequal dimension vectors -> block; numeric-looking inputs are not automatically arithmetic scales.
3. `0 / 0` exposure rate -> null, not zero; positive count / zero exposure -> invalid measurement contract.
4. 1,2,4,8: `pow2` and `regions3` remain rival hypotheses; n=4 with y=15 refutes `pow2` for that instance; y=17 refutes both tested families.
5. Identical scalar feature with different rhetorical roles -> conditional non-injective-feature counterexample, not empirical language classifier proof.
6. Threshold lies within justified bounds -> no decision; entirely one-sided bounds -> robust *conditional* decision.

## Known gaps / tests needed before stronger claim

General typed relational/scale theory, automated ontology alignment, data-driven abductive grammar search, symbolic Buckingham Π solver, formal proof assistant, probabilistic uncertainty inference, Bayes model comparison, semantic/rhetorical annotation validation, arbitrary numerics and full 1–100 registry executors are not implemented here. The Python tool must be actually invoked within a current reasoning turn and its receipt inspected; packaging a plugin alone creates no live Python service. MCP SDK import/remote handshake and host product integration require separate verification.
