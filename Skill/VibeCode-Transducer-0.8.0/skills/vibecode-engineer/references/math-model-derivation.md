# Model-driven mathematical heuristic selection — VCT v0.2.0

## Governing problem

**How** does an empirically described phenomenon become an admissible mathematical model and then a testable engineering task *without* substituting numeric proximity, algorithm-name similarity, or visual metaphor for a valid inference? This is a normative engineering synthesis (not a discovered theorem, proof assistant, automatic semantic parser, or direct execution of the 100 mathematical records).

Based on user-provided `SECOND_ORDER_MODELS_v1.3.md`, Mahajan's *Street-Fighting Mathematics* (2010), and two inherited research syntheses. See `math_heuristic_literature_review.md` for prose review and references, `math_foundations_review.md` for broader mathematics, the two registry CSVs for concept links, and `math_task_graph.yaml` for the proposed 18-task dependency specification. Original document provenance is research material, not automatic user endorsement of every theoretical proposal.

## Three noninterchangeable kinds of 'dimension'

- **Scalar observed feature:** A token-count rate `r3` is numeric and may be one feature of many; this is NOT proof of an underlying one-dimensional rhetorical construct.
- **Dimensionless mathematical ratio:** `matched_contiguous_spans / eligible_token_positions` is dimensionless in the physical-unit sense but depends on denominator design, tokenizer, sentence boundary and sampling.
- **One-factor latent construct:** An identified single rhetorical variable requires a measurement/construct model, empirical relational invariants, validity evidence and rival tests. Dimensional analysis does not license this interpretation.

Do not use Buckingham Pi for lexical data without separately defined physical quantities, a meaningful dimension matrix, and a transformation principle. Do not confuse graph topological sorting and mathematical topology.

## Inferential junctions

| Evidence stage | Observables / models | Licensed claim | Must not infer |
|---|---|---|---|
| Corpus measurement | exact lexical span, token offsets, `N_m(Wk)`, masks | bounded exact count/rate in the measured view | rhetorical function, author intent, causal success |
| Lexical temporal gap | adjacent `z` positions, complete X→Y windows, censored Y | absence of exact tracked phrase in declared interval | absence of synonym/anaphora, missing endpoint equals zero |
| Toulmin annotation | proposition boundary, support/rebuttal relation, human/validated annotations | qualified interpretive argument relations under codebook | marker itself entails argument |
| Statistical inference | sampling assumptions, dependence, noise/likelihood | model-relative estimate plus uncertainty | overlapping samples are independent; causal intervention |
| Causal/inverse | explicit forward model, domain, identification assumptions | solution set, identified/partial class or justified estimate | unique truth from noninjective feature map |
| Engineering | actual repository/runtime snapshot, test runner, accepted contract | testable requested behavior and potential scoped patch | static success = feature fixed |

### Toulmin operational distinction

`Claim`, `Data`, `Warrant`, `Backing`, `Qualifier`, `Rebuttal` are typed *argument roles*. Example:

- **Data**: Exact phrase appears at offset 55; anchored `r3=0.14`, `r5=0.10` under a specified tokenizer.
- **Candidate observation claim**: `r3 > r5` **on this measured corpus**.
- **Warrant**: the span counting algorithm corresponds to the declared sentence-scoped denominator.
- **Backing**: reproducible source snippet, source/mask fingerprint and numerical recount.
- **Disputed semantic claim**: the phrase constitutes rhetorical synthesis. This is NOT entailed by frequency.
- **Rebuttal**: the phrase may be quoted, negated or serve a contrary discourse function.

The key proposition is **loss of identifiability**: if two documents `d1,d2` have the same lexical measurement `m(d1)=m(d2)` but different rhetorical labels `R(d1)≠R(d2)`, then no deterministic function `g` of *that measurement alone* recovers both labels via `R(d)=g(m(d))`. This is a mathematical counterexample to a sufficient-feature claim, not empirical proof that a particular human interpretation is correct.

### Mahajan / Rice / RMC division of labor

- **Mahajan, chapters 1–3,6**: seek invariants, dimensions, easy and extreme cases, approximate/lump or analogize to formulate *candidate models*. In frustum example (printed pp. 19–20), the candidate polynomial lacking an `ab` term passed some boundary tests but contradicted another; the response was to **expand the model class**, not merely fit coefficients.
- **Rice (1976)**: define instance features, candidate algorithm space, and target performance/quality criterion. A method is selected for typed problem characteristics, not by association or blanket ranking.
- **RMC**: materialize → relationalize → formalize; choose a regime and admissible operation; use a counterexample to revise earliest failed premise.
- **AntiSlop**: distinguish a tool/API being named, installed, run, passing static verification, and empirically solving a user's target behavior.

## A mathematical operator is eligible iff

`TypeMatch(o,p) ∧ Preconditions(o,p) ∧ RepresentationWarrant(p) ∧ SupportsClaimType(o,c) ∧ FalsifierSpecified(o,p,c)`.

This is a **proposed normative gate**, not a proved universal selection theorem. Preconditions can be `true` (declared), `false` (contradicted), or `unknown` (insufficient evidence). In v0.2's strict JSON CLI, `features` uses declared booleans; missing evidence is treated as *not witnessed* without claiming falsity. The router only enforces a bounded subset of this full predicate. `ELIGIBLE_AS_METHOD` means **candidate admitted for further independent validation**, not a proof; a rejected/absent candidate must not be silently replaced by a semantically unrelated operator.

## Case-specific invariants (Co-Domain v1.3)

1. α: `W3(p)={p-2,p-1,p}` and `W5(p)={p-4,...,p}`, each truncated at corpus start. Ratios `r_k(z|a)=c(z,Wk)/N_m(Wk)` only when denominator positive. Windows overlap, are dependent, not independent experimental arms.
2. α: endpoints B searched at most 3 succeeding paragraphs; missing B is **censored null**, never zero gap. Cap 80 evaluated anchors, distinguish full inventory, evaluated, truncated. Summary of complete endpoints is conditional on truncation/censoring.
3. β: same-phrase gap and complete X→Y silence estimate; zero/one z cannot prove recurrence. Missing Y censored and not included in the ratio. Lexical silence ≠ semantic silence.
4. δ,ε,φ,γ: surface markers only; `φ.status=not_formal_proof` mandatory and γ is orthographic suffix, not parsed morphology.
5. Masks change measured view but not raw source, and source fingerprint roles differ. Generation excludes affect user instruction only; do not alter source measurements. Human steering defaults to none. Preserve root schema `corpus-to-codomain/unified-1.1` and section ownership 03/04/05.

## Problem characteristic → operation → handoff

| Observed characteristic | Candidate operation / math anchor | Gate | Task path (conditional) |
|---|---|---|---|
| discrete offsets, legal span positions | finite difference (`MATH-043`) | same sentence, traceable offsets, denominator | T00–T06 → T08 → T13–T15 |
| alleged rhetorical meaning from markers | logic/countermodel (`MATH-001/007/008`), semantic annotation | validated proposition codebook and warrant | T10 → T11 only for argument claims |
| dependent overlapping samples | statistical sampling model, uncertainty (`MATH-044/054`, conditional) | sampling design; cannot assume IID | T09 when statistics requested |
| causal claim from lexical correlation | causal identification (`MATH-090`) | intervention design/identifying assumptions | T12 only on causal request |
| inverse from a lossy measure | Hadamard (`MATH-088`), counterexample (`MATH-007`) | forward model, domain, uniqueness, stability | T12 for inverse request |
| dependencies among tasks | DAG topological ordering (`MATH-061`, distinct `ATLAS-058`) | declared directed edges, no cycle | task scheduling |
| dimensional reduction of physical quantities | proposed Buckingham Π (`MATH-100`) | physical dimensions + matrix | never infer latent rhetoric from lexical scalars |
| code donor similarity | `ATLAS-034` Jaccard | supplied distinct source files | candidate inspection only, never behavioral donor proof |

**Namespace rule:** `MATH-034` (limit/continuity) ≠ `ATLAS-034` (Jaccard); `MATH-061` (mathematical DAG theorem) ≠ `ATLAS-058` (specific partial implementation). `MATH-100` is explicitly a proposed addition. `math_001_100_crosswalk.csv` assigns `CORE/GUARD/CONDITIONAL/NOT_LICENSED` **relative to the Co-Domain case**, not generic proof status. The runtime routes a smaller named subset; do not claim all 100 records have executable algorithms.

## DSL/MDE/KRR modeling contract — proposed schema, NOT implemented language

`Phenomenon(domain, source, observation_unit)`, `Measure(name, codomain, units, normalizer, mask)`, `Claim(kind, proposition, quantifiers, scope)`, `Assumption`, `Operator(id, input_type, output_type, prerequisites, epistemic_ceiling)`, `ModelRevision`, `Warrant(evidence, claim)`, `Falsifier`, `Task(id, depends_on, conditional_gate, evidence_receipt)`, `Evidence(source_hash, actual_command, revision, status)`.

Results should distinguish `HYPOTHESIS`, `DESCRIPTIVE_MEASUREMENT`, `PROVISIONALLY_ESTIMATED`, `MULTI_SOLUTION`, `UNIDENTIFIABLE`, `PROVED_UNDER_ASSUMPTIONS`, and `UNVERIFIED`; current Python CLI only returns method eligibility and task plans. The full mathematical ontology, code synthesis, proof checking, KRR entailment, stochastic learning, graph homology and causal inference are NOT implemented.

## Actual current module behavior

- `runtime/math_model_router.py`: JSON input `goal`, `claim_type` (`lexical|semantic|argument|statistical|causal|inverse|deductive|engineering`), `observation_kind` (`lexical_spans|numeric_samples|graph_edges|matrix|geometry|symbolic|code_state|unknown`), optional boolean `features`, optional `source_id`.
- Validates 100 IDs and proposed `MATH-100` status, selects a **small enumerated method subset** with explicit missing-precondition states, emits conditional DAG and event-triggered T17 (not automatically executed).
- `runtime/vct_math_cli.py` optionally combines a `math_problem` with the old static engineering `engineering_spec` via `vibe_transducer.transduce()`. A combined CLI is an adapter, NOT retroactive modification of the old transducer or an automatically connected MCP tool.
- `tests/test_math_model_router.py` tests 15 conditions including semantic/causal/inverse negative cases, separate namespaces, dependency cycles, and guarded handoff. Local tests do not validate human annotation quality or real target project code.

## References and source authorization

- User input: *SECOND_ORDER_MODELS_v1.3.md* (current conversation). User input: Mahajan, S. (2010). *Street-Fighting Mathematics*. MIT Press, printed ch. 1–3 and 6. Book licensed CC BY-NC-SA 3.0 US; this plugin cites and summarizes, does not redistribute its full text/PDF.
- Toulmin, S. E. (1958/2003). *The Uses of Argument*, Cambridge University Press; use as an argument schema, not lexical NLP proof.
- Rice, J. R. (1976). The algorithm selection problem. *Advances in Computers*, 15, 65–118. Literature anchor for instance features/algorithm space/performance.
- Prior synthesized reports: `math_heuristic_literature_review.md` and `math_foundations_review.md`, research summaries **not** independently re-verified article-by-article in this plugin update.

## Falsifiers for this architecture

- Source has a quoted marker with no synthesis; router MUST NOT emit `PROVED`.
- Window data missing independent sampling, numeric ratio present: no IID confidence test claim.
- Two systems share a degree sequence or lexical feature but differ structurally/semantically: no unique inversion.
- Model changed after failed edge test: invalidate dependent receipts; do not relabel the old proof PASS.
- Approval=true without checkout: no patch handoff T16.
- Static report `exit=0`: never considered deployment, runtime behavior, or proof object.
