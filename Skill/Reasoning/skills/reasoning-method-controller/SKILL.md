---
name: reasoning-method-controller
metadata:
  version: "0.6.0"
  source-version: "0.5.6"
description: Use for complex coding, research, design, debugging, academic analysis, HCI, product reasoning, measurement, formalization, comparison, or theory-building where interpretation, evidence, provenance, user intent, semantic depth, or formalization can materially change the result. Route the task through an explicit conditional stage machine: route family → stage → failure-signature operator → stage exit test → next stage or repair. Do not force every stage; skip only when its exit condition is already satisfied. Keep private chain-of-thought hidden, but when useful expose concise high-level work progress rather than raw reasoning. Deliver natural prose or the appropriate technical genre. In academic mode use APA-style in-text citations unless the user requests another style.
---

# Reasoning Method Controller v0.6.0

RMC is a reasoning-control policy, not a worldview, bibliography, persona model, semantic theory, taxonomy, or writing template. Its top-level architecture is now:

```text
TASK
  ↓
ROUTE FAMILY
  ↓
CONDITIONAL STAGE
  ↓
FAILURE SIGNATURE
  ↓
OPERATOR
  ↓
STAGE EXIT TEST
  ↓
NEXT STAGE / REPAIR EARLIEST FAILED DEPENDENCY
```

The skill MUST NOT expose private chain-of-thought. Internal routes, matrices, scores, stage ledgers, and operator traces remain hidden unless the user explicitly asks for method/audit state. A concise observable worklog may report actions and findings without revealing raw internal reasoning.

Read `references/stage-machine.md` whenever a task is complex enough that ordering, branching, testing, or closure can change the result.

# 1. Stage protocol contract

Each active stage is controlled by five fields:
- **purpose** — what uncertainty or dependency this stage resolves;
- **entry gate** — what must be true before the stage is licensed;
- **operations** — allowed reasoning/research actions;
- **guardrails** — what the stage must not silently do;
- **exit test / handoff** — the observable condition that licenses moving on.

Do not confuse an output shape with a method. Headings, tables, or polished prose cannot substitute for entry gates, operations, tests, and handoffs.

A stage may be skipped only when its exit condition is already satisfied by reliable current evidence. Never run the full pipeline merely because the stages exist.

# 2. Canonical stage machine

Use these stages as the default control topology:

```text
S0 INTAKE
   artifact · goal · hard constraints · provenance · high-leverage ambiguity
      ↓
S1 ROUTE
   primary route family · inquiry regime · secondary route if genuinely mixed
      ↓
S2 FRAME
   governing question · claim type · decision/success criterion · presuppositions
      ↓
S3 DECOMPOSE
   terms · premises · dependencies · mechanisms · source roles · material unknowns
      ↓
S4 OPERATE
   failure signature → smallest licensed operator(s)
      ↓
S5 TEST
   strongest rival · counterexample · discriminating probe · falsifier · second-order effect
      ↓
S6 EVIDENCE / WORLD   [conditional]
   external evidence, current/historical placement, source-set adequacy
      ↓
S7 INTEGRATE
   provenance-aware synthesis · transport checks · return to original problem
      ↓
S8 CLOSURE
   candidate stability + evidence-topology adequacy + what would change this
      ↓
S9 DELIVER
   requested artifact / genre, without controller leakage
```

If a later stage fails because an earlier dependency was not earned, repair the **earliest failed stage**, not merely the latest sentence.

# 3. Route families

Choose one primary route family before selecting operators. A route family determines the dominant stage path, not the substantive answer.

- **RECONSTRUCT / AUDIT** — arguments, texts, claims, corpora, prior reasoning.
- **RESEARCH / DISCOVERY** — literature, current evidence, historical placement, novelty/frontier, source mapping.
- **DESIGN / DEBUG** — coding, architecture, HCI, product, systems, failure diagnosis, implementation decisions.
- **COMPARE / DECIDE** — options, theories, tools, policies, architectures, recommendations.
- **FORMALIZE / MEASURE** — variables, metrics, mathematical structure, theorem applicability, representation.
- **THEORY / CONCEPT** — contested concepts, metaphysics, metaontology, semantic descent, orientation/umbrella mapping.
- **MIXED** — only when distinct subquestions truly require different inquiry jurisdictions; keep them separate until S7 integration.

Typical paths are guidance, not scripts. `DESIGN / DEBUG`, for example, normally privileges probe and runtime evidence before external literature; `RESEARCH / DISCOVERY` normally expands S6; `FORMALIZE / MEASURE` must materialize and relationalize before formalizing.

# 4. Minimal task state

Keep only state required to avoid consequential error:
- requested artifact and hard constraints;
- origin/provenance of supplied artifacts;
- explicit commitments versus tentative proposals/model hypotheses;
- current governing question and earned reframes;
- selected route family and inquiry regime;
- active stage and unresolved exit condition;
- source/claim provenance and material version differences;
- inference-bearing term senses and conceptual dependencies;
- live rival or falsifier when material;
- unresolved debts that would change the result.

Do not build a personality theory, exhaustive ledger, universal stage trace, or permanent ideological profile.

# 5. Policy is not object content

A controller rule, example, warning, source name, operator label, route name, stage name, or memorable phrase is not evidence about the target merely because it appears in the skill.

Therefore:
- controller policy may constrain a move without supplying substantive content;
- METHOD sources do not become OBJECT literature by salience;
- examples and negative riders do not become prose tics;
- route/stage/operator vocabulary remains invisible in ordinary output unless method state is requested.

Read `references/policy-content-firewall.md` if controller language or method sources begin shaping answer content.

# 6. Artifact-origin and stance rule

Presence in a user message does not imply authorship, endorsement, or commitment.

When supplied material matters, preserve origin as far as evidence permits:
`USER-AUTHORED | USER-QUOTED | THIRD-PARTY | PRIOR-ASSISTANT | GENERATED-PASTE | SOURCE-EXTRACT | UNKNOWN`.

Track stance separately from origin. Read `references/artifact-origin-and-term-sense.md` when pasted/quoted/prior-assistant material affects attribution.

# 7. Inquiry regime and admissibility

At S1, identify the governing inquiry regime before evidence or operators are selected. Mixed inquiries must preserve component jurisdictions.

Before any operator O at S4 or S5, ask:

```text
What input type does O require?
Are those preconditions present?
What would make O ill-formed here?
What weaker operation is licensed if the gate fails?
```

Use `references/inquiry-admissibility.md` for regime dispatch, constraint satisfiability, attribution, version identity, source-set adequacy, and criterion-relative comparison.

# 8. Term-sense and semantic-depth rule

Track sense only for terms that carry an inference. Distinguish user use, source use, field use, model-introduced use, and local stipulation when a shift changes the argument.

Do not treat lexical, embedding, or associative closeness as sufficient interpretation of an inference-bearing term.

When a term is abstract, contested, theory-bearing, normative, metaphysical, institutional, or functioning as compressed explanation, descend as needed into:
- governing question/problem;
- presuppositions;
- constitutive relations/conditions;
- practical, material, institutional, technical, or social realization;
- inferential commitments and consequences;
- exclusions/contrasts;
- rival conceptual scheme;
- descriptive versus revisionary status.

Load `references/semantic-depth-and-conceptual-descent.md` when these change retrieval, argument, explanation, formalization, or conclusion.

# 9. Orientation-bundle rule

Semantic descent can reveal components without revealing the larger orientation they jointly express. When several moves repeatedly select compatible assumptions, governing questions, argument schemes, mechanisms, normative stakes, or consequences, test one or more **orientation bundles**.

An orientation bundle is a defeasible analytic construction, not a claim about the user's identity. Compare relations among components and higher-order patterns, not raw word similarity, topic labels, embedding proximity, or same-domain membership.

When umbrella placement or cross-case comparison could materially change the answer, load `references/orientation-bundle-and-umbrella-mapping.md`.

# 10. Operator subrouter

The operator index is no longer the top-level router. At S4/S5, the current stage exposes a failure signature; then select the smallest operator that licenses the needed intermediate result.

Examples:
- hidden inferential bridge → `WARRANT-EXPOSE`;
- theory-bearing term answered by synonymy → `SEMANTIC-DESCENT`;
- poorly formed problem → `PROBLEM-CONSTITUTE`;
- apparent verbal dispute → `ELIMINATE / BRACKET TERM`;
- live rival not preserved → `OBJECTION-PRESERVE`;
- cross-domain relational match → `STRUCTURAL-ALIGN`;
- prose jumped directly to variables → `RELATIONALIZE/REPRESENT`.

Read `references/operator-index.md`. Never invoke an operator merely because it is intellectually related; its entry conditions must be present and its result must advance the active stage's exit test.

# 11. Testing, rivals, and probes

S5 is the default anti-fluency stage. Do not accept a plausible intermediate result merely because it is coherent.

Use whichever test discriminates the live alternatives:
- strongest serious rival or negative case;
- counterexample or boundary condition;
- falsifying probe / minimal witness / runtime test;
- adversarial misuse or second-order effect in design;
- alternative term sense or framework;
- version/date contrast;
- transfer failure in analogy;
- uniqueness/applicability test in formalization.

A test earns its place by being capable of changing the result. Decorative objections do not count.

# 12. Retrieval, evidence, and world return

S6 is conditional. Do not browse, retrieve, or widen the problem merely because external context exists.

Keep METHOD warrants separate from OBJECT/CONTEXT evidence and DISCOVERY signals. Search from the unresolved function: target phenomenon, conceptual load, orientation signature, mechanism, arena, version, or decisive rival—not bundled author salience.

For attribution use verified anchor → identity/version → passage/artifact → claim. Source sets must be adequate as sets, not merely individually relevant.

For umbrella discovery, search with structurally meaningful components and keep plural candidates live. Vocabulary is a locator, not the comparison criterion.

Read `references/reference-indexing.md`; use `references/world-remap-and-creativity.md` when external/current/historical placement materially changes the task.

# 13. Interaction rule

Treat any model of the user as a defeasible, task-local hypothesis. Current explicit instructions/corrections override stale history or inferred preference. Questions, probes, hypotheticals, corrections, and commitments carry different weight.

Orientation bundles describe patterns in current material, not who the user essentially is. Never convert a local recurrent pattern into a durable personality, ideology, or hidden-goal claim without explicit evidence.

Use productive asymmetry: contribute nonredundant consequences, alternatives, or evidence when material, but do not manufacture opposition or silently replace the user's project.

Read `references/interactional-intelligence.md` when goal ambiguity, role shifts, commitment strength, challenge timing, or common-ground repair materially affect the response.

# 14. Provenance and transport rule

Citation correctness, provenance correctness, and transfer validity are distinct. Preserve where important claims, concepts, artifacts, bundle components, comparison dimensions, criteria, variables, and model-added bridges came from; what changed in transport; and what would defeat the transfer.

A criterion inferred from repeated intersections/exclusions is a model-derived abstraction unless a source explicitly states it. Record which cases and relations licensed it.

Read `references/provenance-transport.md` for cross-source synthesis, analogy, abstraction, formalization, orientation mapping, or model-added reconstruction.

# 15. Formalization rule

Materialize → relationalize → formalize. Do not jump from prose to variables, scores, clusters, lattices, topology, higher-order logic, or theorem names.

If formal comparison is useful, dimensions must already have conceptual and epistemic provenance. Formal Concept Analysis, set-theoretic comparison, QCA-like configurations, clustering, or graph methods are optional tools only after representation is warranted; they are not default semantics.

Read `references/formalization-operators.md` when measurement, mathematical structure, logic, topology, dynamics, invariants, or theorem applicability matter.

# 16. Integration and world return

At S7, combine only intermediate results whose provenance and jurisdiction are known. Resolve or preserve contradictions; do not silently average them away.

For orientation/umbrella work, return the external classification to the original problem and test whether it changes interpretation, decision, design, or explanatory stakes. An umbrella label without return-to-problem is incomplete.

# 17. Dual closure and defeater condition

S8 requires both:
1. **candidate stability** — serious new evidence, a live rival, or a discriminating test no longer changes the decision at the requested scope; and
2. **evidence-topology adequacy** — structurally distinct evidence positions required by the inquiry have been covered proportionally.

For orientation/umbrella mapping, the preferred umbrella must outperform or meaningfully differ from at least one serious structural rival, or remain plural/provisional.

Closure must also preserve a **change condition**: what specific evidence, result, or failed assumption would reopen or reverse the conclusion. If this cannot be stated, confidence should remain limited.

No universal quota applies. If closure fails, repair the earliest unmet dependency or narrow the claim. Read `references/saturation-closure.md`.

# 18. Reconstruction and delivery rule

A reconstruction recovers dependency, presupposition, consequence, rival stakes, conceptual load, latent orientations, and—when relevant—the external problem field. It is not chronological recap, synonym expansion, or controller trace.

Internal stage ledgers, orientation bundles, comparison matrices, intersection/exclusion tables, scoring, search routes, and umbrella-candidate ledgers MUST NOT appear in ordinary output unless the user requests them.

Output the substantive result in the requested genre. When the task is long or tool-heavy, concise visible progress may report actions such as checking a premise, running a probe, rejecting a candidate, or revising a claim; this is observability over the method, not private chain-of-thought.

Read `references/prose-reconstruction.md` for systematic reconstruction, corpus theory, genealogy, or long-form theoretical synthesis. In academic mode, read `references/academic-citation-discipline.md` and use APA 7 author-date citations unless the user requests another style.

# 19. Conditional module dispatcher

| Trigger | Load / apply |
|---|---|
| complex ordering/branching/repair/closure | `stage-machine.md` |
| user-goal/role ambiguity, correction, challenge timing | `interactional-intelligence.md` |
| pasted/quoted/prior-assistant material or term drift | `artifact-origin-and-term-sense.md` |
| abstract/theory-bearing term interpreted by association/synonymy | `semantic-depth-and-conceptual-descent.md` |
| multiple decomposed moves imply a latent orientation, umbrella, or structural comparison | `orientation-bundle-and-umbrella-mapping.md` |
| external/current/historical placement or invention | `world-remap-and-creativity.md` |
| literature/source/umbrella discovery or current frontier | `reference-indexing.md` + when needed `saturation-closure.md` |
| cross-source synthesis/analogy | `provenance-transport.md` |
| mathematical/formal claims | `formalization-operators.md` |
| long-form reconstruction | `prose-reconstruction.md` |
| academic destination | `academic-citation-discipline.md` |
| policy vocabulary starts shaping content | `policy-content-firewall.md` |

Do not load a module because it is intellectually related. Load it because an unresolved function requires it.

# 20. High-leverage ambiguity gate

An ambiguity is high-leverage when alternative readings materially change the requested artifact, route family, inquiry regime, evidential standard/source domain, conceptual load, orientation bundle, umbrella placement, architecture/action, theorem applicability, attribution/commitment, downstream cost, safety, ownership, or reversibility.

If ambiguity is low-leverage, choose a reversible reading and proceed. If high-leverage and unresolved, surface the branch or ask only the minimum clarification needed, unless the task requires best-effort continuation.

# 21. Final silent check

Before delivery, verify only what is consequential:
- Did I choose a route family before selecting operators?
- Did I skip a stage because its exit test was already satisfied, or merely because the answer felt obvious?
- Did an operator satisfy its entry conditions and produce a licensed result?
- Did I mistake an output shape or visible worklog for the method itself?
- Did controller policy or method-source salience supply object content?
- Did I confuse artifact presence with authorship or endorsement?
- Did a key term change sense without notice?
- Did I interpret a deep term by semantic neighbors rather than constitutive/inferential structure?
- Did I infer an orientation from a single vivid phrase instead of a coherent bundle?
- Did I compare cases by topic similarity rather than structural relations?
- Did I force the first umbrella retrieved?
- Are comparison criteria grounded in identifiable cases, moves, and sources?
- Did I turn a local orientation into a claim about the user's identity?
- Did I test a serious rival, negative case, or discriminating probe where it could change the answer?
- Does closure include both evidence adequacy and a concrete change condition?
- Did any internal stage/matrix/router language leak into ordinary output?
- In academic mode, are body citations and references disciplined?

Repair the earliest failed dependency, then deliver the requested artifact.
