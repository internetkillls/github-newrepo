# Conditional stage machine v0.6.0

This module makes RMC procedurally legible without forcing every task through a fixed script.

## 1. Control stack

```text
route family
→ stage
→ failure signature
→ operator
→ exit test
→ handoff
```

A route is a task-level jurisdiction. A stage is a dependency in the workflow. An operator is a local reasoning move. An output shape is presentation. Do not collapse these levels.

## 2. Stage contract

For every active stage record only what is needed:

```text
PURPOSE
ENTRY GATE
OPERATIONS
GUARDRAILS
EXIT TEST
HANDOFF / REPAIR TARGET
```

A stage is skippable only when its EXIT TEST is already satisfied by current evidence. Skipping by intuition, convenience, or fluent prose is not allowed.

## 3. Stages

### S0 — INTAKE
**Purpose:** establish the object and non-negotiable constraints.

**Entry:** task received.

**Operations:** identify requested artifact; hard constraints; artifact origin; current evidence available; high-leverage ambiguity; whether the user asks for execution, evaluation, research, or explanation.

**Guardrails:** presence ≠ authorship; question ≠ commitment; do not invent environment, files, versions, or missing facts.

**Exit:** enough is known to choose a primary route and no unresolved ambiguity would materially change route, evidence jurisdiction, safety, ownership, or reversibility.

**Repair:** return here when later work reveals the wrong object, wrong owner, wrong version, or impossible constraint set.

### S1 — ROUTE
**Purpose:** choose the governing inquiry and dominant workflow.

**Entry:** S0 exit passed.

**Operations:** select one primary route family and inquiry regime; add a secondary route only if a materially distinct subquestion requires it; separate mixed jurisdictions.

**Guardrails:** route families do not supply substantive content; same topic may support different routes; do not use THEORY merely because a philosophical vocabulary appears.

**Exit:** every material subquestion has a known jurisdiction and evidence standard.

**Handoff:** S2 FRAME.

### S2 — FRAME
**Purpose:** make the problem answerable and comparison criteria explicit.

**Entry:** route selected.

**Operations:** state governing question; distinguish descriptive/normative/causal/formal/design claims; identify success/decision criterion; expose presuppositions; test hard-constraint compatibility; backtrack to the question when claims float free of a problem.

**Guardrails:** do not silently reframe the user's project; earned reframes must solve a real dependency.

**Exit:** no live alternative framing would materially change what counts as evidence, success, or a valid answer.

**Handoff:** S3 DECOMPOSE.

### S3 — DECOMPOSE
**Purpose:** expose load-bearing structure before acting on it.

**Entry:** frame stable enough to inspect dependencies.

**Operations:** identify term senses; premises; warrants; mechanisms; causal/functional dependencies; source roles; version identities; material unknowns; candidate orientation components when relevant.

**Guardrails:** do not replace terms with synonyms and call it analysis; do not infer a worldview from one proposition; do not convert prose directly to metrics/formalism.

**Exit:** load-bearing dependencies and unresolved unknowns are visible enough to select a licensed operator or discriminating test.

**Handoff:** S4 OPERATE or directly S5 if the needed operation is itself a test.

### S4 — OPERATE
**Purpose:** perform the smallest reasoning operation licensed by the failure signature.

**Entry:** operator preconditions are present.

**Operations:** choose from `operator-index.md`; apply one or a small composition; record the licensed intermediate result and its provenance.

**Guardrails:** operator names are not explanations; thinker names are warrants/examples, not automatic object content; sophisticated formalism does not increase validity by itself.

**Exit:** the operation has produced an intermediate result that resolves the identified failure or reveals the exact remaining debt.

**Handoff:** S5 TEST, S6 EVIDENCE when external evidence is the unresolved dependency, or S7 when no meaningful test/evidence debt remains.

### S5 — TEST
**Purpose:** try to make the current result fail in a way that discriminates live alternatives.

**Entry:** at least one provisional claim/design/reconstruction exists.

**Operations:** strongest rival; objection preservation; negative case; counterexample; falsifying probe; minimal witness/runtime test; boundary/scaling breakpoint; version contrast; alternative framework; second-order/adversarial effect; uniqueness/applicability check.

**Guardrails:** no straw rivals, generic objections, fake balance, or decorative red-teaming. A test must be capable of changing the result.

**Exit:** the strongest live alternative has been tested enough for the requested scope, and any remaining uncertainty is specific and decision-relevant.

**Handoff:** S6 if evidence is required, otherwise S7.

### S6 — EVIDENCE / WORLD
**Purpose:** obtain external evidence or placement only where an unresolved function requires it.

**Entry:** a source-dependent uncertainty, attribution, current fact, external placement, or evidence-topology gap remains.

**Operations:** anchor-first retrieval; source-role separation; version checking; cross-vocabulary search; structural umbrella discovery; negative/dissent evidence; runtime/community evidence when the claim requires it.

**Guardrails:** do not research for ornament; do not retrieve from author salience alone; METHOD sources do not become OBJECT evidence; do not infer saturation from one vocabulary cluster.

**Exit:** the source set is adequate for the claim's scope, or an explicit research debt is preserved and the claim narrowed accordingly.

**Handoff:** return to S5 when new evidence creates a new discriminating rival/test; otherwise S7.

### S7 — INTEGRATE
**Purpose:** synthesize without laundering provenance or crossing jurisdictions silently.

**Entry:** relevant intermediate results are available.

**Operations:** combine compatible results; preserve contradictions; trace model-added bridges; test transfer; return external umbrella/world mapping to the original problem; identify design/interpretive consequences.

**Guardrails:** do not average incompatible evidence; do not hide transformations; do not let a classification replace explanation.

**Exit:** the synthesis answers the governing question without exceeding source or operator warrants, and the consequences for the original problem are explicit.

**Handoff:** S8 CLOSURE.

### S8 — CLOSURE
**Purpose:** decide whether work may stop at the requested scope.

**Entry:** integrated candidate exists.

**Operations:** test candidate stability; audit evidence-topology adequacy; preserve serious residual rival; state confidence at the proper scope; state what specific evidence/result would reopen or flip the conclusion.

**Guardrails:** no closure from repetition, familiarity, or source count alone; no universal quota; no "final" verdict if a live rival or evidence position remains decision-changing.

**Exit:** candidate stability and evidence-topology adequacy both pass, and a concrete change condition can be named. Otherwise repair the earliest stage whose unmet dependency caused failure.

**Handoff:** S9 DELIVER.

### S9 — DELIVER
**Purpose:** produce the requested artifact in its natural genre.

**Entry:** S8 passed or the answer is explicitly scoped as provisional/debt-bearing.

**Operations:** compose answer/code/design/memo/table/etc.; include sources and uncertainty appropriate to the destination; expose concise action-level work progress only when useful.

**Guardrails:** do not leak private chain-of-thought, internal matrices, stage ledgers, or routing vocabulary into ordinary output; do not over-template natural prose.

**Exit:** requested artifact is complete, constraints are met, and claims are no stronger than earned.

## 4. Route profiles

These are default emphases, not mandatory full paths.

```text
RECONSTRUCT/AUDIT:
S0 → S1 → S2 → S3 → S4 → S5 → [S6] → S7 → S8 → S9

RESEARCH/DISCOVERY:
S0 → S1 → S2 → S3 → S6 ↔ S5 → S7 → S8 → S9

DESIGN/DEBUG:
S0 → S1 → S2 → S3 → S4 → S5(probe/runtime) → [S6] → S7 → S8 → S9

COMPARE/DECIDE:
S0 → S1 → S2(criteria) → S3 → S4 → S5(rival) → [S6] → S7 → S8 → S9

FORMALIZE/MEASURE:
S0 → S1 → S2 → S3(materialize/relationalize) → S4(formalize) → S5(applicability/uniqueness) → [S6] → S7 → S8 → S9

THEORY/CONCEPT:
S0 → S1 → S2 → S3(semantic descent) → S4(orientation if earned) → S5(rival) → [S6 world-remap] → S7 → S8 → S9

MIXED:
separate component routes at S1 → preserve jurisdictions through S6 → merge only at S7
```

## 5. Re-routing

Re-route when new evidence changes the nature of the problem, not merely because a different operator seems interesting. Examples:
- a supposed implementation bug becomes a version/documentation question → DESIGN/DEBUG gains RESEARCH component;
- a conceptual dispute collapses into a verbal dispute → THEORY route remains, but S4 operator changes;
- a recommendation becomes a measurement-validity problem → COMPARE gains FORMALIZE component.

Do not silently re-route. The internal state should record why the jurisdiction changed.

## 6. Observable worklog

For long tasks, user-visible progress can mirror major operations or stage transitions, for example:

```text
Reconstructing the actual deliverables before comparing architectures.
Rejecting the compatibility claim because source inspection cannot establish runtime behavior.
Running a minimal probe against the load-bearing assumption.
Revising the earlier critique after version evidence changes the chronology.
```

The worklog is not the method and must not become a verbose hidden-reasoning transcript.
