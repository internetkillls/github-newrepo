# RMC semantic transition rules — conditional, typed, falsifiable

## Epistemic separation

- `EMPIRICALLY SUPPORTED`: specific published empirical observation within its examined population/models, **not** GPT-6 behavior.
- `THEORETICALLY MOTIVATED`: philosophical, cognitive or formal argument motivating a testable method.
- `DESIGN HYPOTHESIS`: an RMC policy proposed from those warrants.
- `OBSERVED IN TEST`: a result tied to an actually executed named test; static validation cannot promote behavioral correctness.
- `UNVERIFIED`: behavior or claim cannot currently be tested.

## Global protocol

`INPUT → S0 context and force → S1 route → S2 governing question → S3 material transition and competing readings → S4 licensed existing operator → S5 discriminating test → S6 evidence only when needed → S7 synthesis → S8 smallest sufficient closure → S9 answer.`

State is an externally assessable design contract, **not a computation trace**. Exact rule fields are listed on each row. All rules require (i) a material interpretive consequence, (ii) sufficient context for the proposed intervention, (iii) an intermediate result that could change interpretation, (iv) a discriminating test, (v) no disproportionate overhead. No mandatory granularity sequence or keyword-only classifier.

| RULE_ID | PROBLEM_CLASS | TRIGGER_CONDITION | REQUIRED_INPUT | ADMISSIBILITY_GATE | SEMANTIC_OPERATION | EXPECTED_INTERMEDIATE_RESULT | OBSERVABLE_EXIT_TEST | COUNTEREXAMPLE | FAILURE_SIGNATURE | REPAIR_PATH | SOURCE_PROVENANCE | IMPLEMENTATION_LOCATION | REGRESSION_TEST_ID | EPISTEMIC_STATUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ST-01 | force/context/commitment | apparent incompatible turns or lost correction | speaker, turn, source, force, chronology | same person endorses both? | FORCE-CHECK + CONTEXT-STATE | effective commitments and attribution | quote/hypothesis/correction not counted as assertion; actual same-condition contradiction survives | user merely quotes conflicting sentence | IS-07/08 | repair earliest attribution | Anikina et al. 2025; ISO 24617-2:2020; RMC interaction module | semantic-transition-audit/SKILL.md S0–S3 | T07,T09,T12 | DESIGN HYPOTHESIS |
| ST-02 | sense/referent | load-bearing term/referent shifts | original wording + local senses | output materially differs | SEMANTIC-DESCENT, USE-CLUSTER, CONTEXT-STATE | sense-indexed rival readings | each alternative changes at least one licensed inference | unrelated polysemy in a recipe | IS-01/09 | narrow term or ask one question | Chalmers 2011; RMC semantic descent; LAmP implementation precedent | semantic-transition-audit/SKILL.md S3–S5 | T04,T05,T10 | DESIGN HYPOTHESIS |
| ST-03 | scope/modal/category | apparent leap possible→certain; some→all | quantified and modal claims | premises/relevant domain identifiable | WARRANT-EXPOSE + TYPE-CHECK | normalized scope + missing warrant | corrected inference or qualified claim | explicit valid universal premise | IS-02/03 | expose scope or condition | Toulmin; RMC stage S3/S5 | semantic-transition-audit/SKILL.md S4 | T01,T02 | DESIGN HYPOTHESIS |
| ST-04 | explanatory bridge | descriptive→normative, knowing→being, correlation→causation | premises and claim jurisdictions | real cross-level transfer alleged | WARRANT-EXPOSE + ONTIC/EPISTEMIC AUDIT | typed bridge with provenance | reason validates bridge or explicit gap named | explicit independent normative premise given | IS-04/05/10 | correct inferred step, do not diagnose person | RMC provenance and argumentation schemes | semantic-transition-audit/SKILL.md S4/S5 | T01,T02,T07 | DESIGN HYPOTHESIS |
| ST-05 | metaphor/aesthetic | figurative transfer can be mistaken for literal mechanism | source domain, target, art context | transfer affects interpretation or factual claim | STRUCTURAL-ALIGN + semantic source/target separation | licensed relation and excluded properties | interpretation preserved; invented mechanism rejected | literal technical specification | IS-06 / aesthetic overnormalization | retain productive ambiguity | Gaver et al. 2003; Meta4XNLI 2026 | semantic-transition-audit/SKILL.md S3/S5 | T03,T08 | DESIGN HYPOTHESIS |
| ST-06 | noisy input | typo/transcription might invert key inference | verbatim input, language variety, technical terms | material alternative supported by context | noise-hypothesis → contextual test → existing operator | bounded candidate corrections | exact term left intact or targeted question; clean code-mixing untouched | proper name or deliberate coinage | typo-induced false contradiction | abstain or ask local clarification | ROBIN engineering precedent (not typo metric); RMC interaction | semantic-transition-audit/SKILL.md language repair | T06,T11,T10 | DESIGN HYPOTHESIS |
| ST-07 | task burden | heavy analysis gives no material decision gain | user's ask and candidate answer | simple determinate response possible | stage-exit shortcut | answer without operator jargon | answer satisfies request directly | actual incompatible interpretive alternatives | false complexity | bypass S3–S7 after earned exits | RMC stage-machine v0.6.0; Li et al. 2025 risk of overthinking | semantic-transition-audit/SKILL.md fast exit | T10,T12 | DESIGN HYPOTHESIS |

## Granularity / stopping

`G0 force`, `G1 context`, `G2 sense`, `G3 constitutive relation`, `G4 inferential warrant`, `G5 modal/epistemic qualification`, `G6 realization`, `G7 test/closure` are *diagnostic resolutions*, not required stages. Select the smallest G that distinguishes competing actions, interpretations or conclusions. Cost gate: unless a deeper level promises an outcome-changing contrast, stop.

## Forward/reverse reconstruction

Forward: user-stated premises and context → defeasible consequences. Reverse: later conclusion → required minimum bridge and presuppositions. Compare both against participant stance, time, quote/endorsement and sources. Label the source of each bridge and refrain from attributing reconstructed premises to the speaker. An underdetermined hypothesis is not proof of inconsistency.

## IS signature consolidation

- IS-01/09: SEMANTIC-REFERENCE (ST-02) because both concern unstable inferential targets, distinguish sense from entity only at the local witness.
- IS-02/03: MODAL-SCOPE (ST-03) because quantifier and modal overreach share warrant testing, but keep their distinct test data.
- IS-04/05/10: BRIDGE/JURISDICTION (ST-04); different cross-jurisdiction warrants remain individually testable.
- IS-06: FIGURATIVE/ART (ST-05), *not* irrationality by default.
- IS-07/08: COMMITMENT/FORCE (ST-01), distinguish wrong attribution from genuine contradiction.
- Typo-noise and unnecessary complexity are independent diagnostic controls ST-06/ST-07, not claims that every typo is irrational.

## Negative controls and non-equivalence

A clean prompt with philosophical vocabulary ≠ need for semantic descent. A metaphor ≠ literal falsehood. A concession ≠ contradiction. A changed topic ≠ dropped commitment. An online repository ≠ test evidence. Research done on older models ≠ GPT-6 benchmark. Static fixture PASS ≠ improved model behavior. Never use one aggregate score across these different constructs.
