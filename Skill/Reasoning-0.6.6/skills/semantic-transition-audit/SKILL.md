---
name: semantic-transition-audit
description: Use alongside Reasoning Method Controller only when a material intra-turn or inter-turn shift in meaning, referent, scope, modality, pragmatic force, inferential warrant, or metaphor threatens the answer; also for user-requested Irrationality Saccade analysis, typo-aware reconstruction, verbal-dispute tests, and ambiguity in digital/new-media art. Skip ordinary questions and harmless topic changes.
---

# Semantic transition diagnostic subrouter — RMC adjunct v0.6.4

This conditional skill is a **behavioral policy**, not an inference about GPT-6 internals, a psychological assessment, or a standalone reasoning route. The provisional shorthand *Irrationality Saccade (IS)* names a candidate **discourse transition** only; never label a user irrational. Entry is a demonstrated consequential transition, not a trigger word or incidental typo. Existing RMC stages S0–S9 and the primary route retain authority. Use `../reasoning-method-controller/references/stage-machine.md` and `../reasoning-method-controller/references/operator-index.md` where relevant. Keep all internal identifiers out of ordinary user-facing prose.

## Conditional entry and fast exit

1. At S0/S2 establish exact user request, conversational force and source/origin. Ask whether any real competing reading changes the answer, action, inferential validity, or evidence regime. If **no**, answer directly and stop; do not run this skill merely because language is abstract, Indonesian/English code-mixed, artistic, or unfamiliar.
2. At S3 preserve the *verbatim original*, turn/speaker locator, quotation versus endorsement, corrections, present topic, admissible contextual history, and inferentially relevant referents/senses/modality. Do not infer an absent past conversation or internal psychological state.
3. If a material discontinuity is plausible, compare the smallest needed hypotheses: ordinary topic shift, valid ellipsis, typo/transcription noise, source quotation, intentional conceptual/metaphorical transfer, constructive art ambiguity, unlicensed bridge, and actual same-context contradiction. Do not enumerate all alternatives by ritual.
4. Run a **forward pass** from explicit/recoverable premises to licensed consequences and a **reverse pass** from apparent conclusion to the minimum bridge it would require. Label each premise `EXPLICIT`, `CONTEXTUAL`, `SOURCE`, `MODEL-HYPOTHESIS`, or `UNSUPPORTED`. Never attribute model-added bridges to the speaker.
5. Choose the *existing* RMC operator matching the earliest live failure: FORCE-CHECK; CONTEXT-STATE; SEMANTIC-DESCENT; ELIMINATE/BRACKET TERM; WARRANT-EXPOSE; COMMITMENT-CONSEQUENCE; TYPE-CHECK; ONTIC/EPISTEMIC AUDIT; STRUCTURAL-ALIGN; PROVENANCE-TRACE. No new global operator or mandatory stage.
6. At S5 attempt a **discriminating negative control**: Does a plausible ellipsis, scope, quotation, permitted framework change, typo, or aesthetic intention dissolve the apparent contradiction? Conversely, does genuine inconsistency survive these charitable repairs? A diagnostic must be capable of changing the interpretation.
7. At S8 exit by one of: `NO_MATERIAL_ISSUE` (normal answer), `QUALIFIED_RECONSTRUCTION` (answer with bounded bridge), `EXACT_INFERENTIAL_DEFECT` (briefly explain the invalid step), `MATERIAL_UNRESOLVED` (one decisive clarification or clearly conditional answer), `FACTUAL_EVIDENCE_DEBT` (check source/runtime). Complexity should scale to the smallest **semantic grain** that discriminates the relevant outputs; never perform a full G0–G7 sequence by default.

## Conservative language repair

Do not silently normalize personal names, author names, philosophical technical vocabulary, mathematics, source quotations, artistic neologisms, repository IDs, code symbols, or user-defined terminology. Nonconsequential errors can be understood silently. For consequential alternate readings, preserve original and present a precise hypothetical correction or one question. Indonesian dialect, Javanese-influenced phrasing and multilingual code-switching are **not defects**. Do not call grammatical oddity irrationality.

## Figurative, conceptual and artistic distinctions

- In metaphor, separate source-domain features, transported structural relation, target-domain claims and excluded transfers. Figurative coherence does not establish literal entailment.
- In New Media Art, do not eliminate productive semantic instability when multiple readings are intentional and technically compatible. Distinguish *interpretation*, *interaction design*, *critique*, *creative generation*, and *fact verification* as different warrants.
- In verbal disputes, bracket a load-bearing term and restate each side's claims. If incompatible nonterminological claims remain, retain the substantive dispute; if none remains, note the explanatory contribution of terminology without universalizing the diagnosis.
- For a demonstrated incompatible pair of commitments under the same actor, force, referent, time, scope, and conditions, name the precise conflict without mind-reading, flattering away the contradiction, or accusing a person of irrationality.

## Admissibility, reference activation and limits

Read `references/rule-contract.md` for typed rules and counterexamples; `references/evidence-matrix.md` when external method warrants materially influence a disputed operation; `tests/paired-cases.jsonl` when auditing or evaluating the diagnostic. These are scoped to research- or error-bearing tasks, **not mandatory citations in every response**. Preserve OBJECT / METHOD / ENGINEERING / MODEL-HYPOTHESIS / TEST-EVIDENCE distinctions. These references have been inspected for the declared use, but do not establish an experimental improvement for GPT-6. Never claim the bundled cases were run as model tests unless responses were actually elicited, independently scored and logged.

The new subrouter's added value is **admission and exit control** across existing operators. An optional local static fixture validator `tests/check_fixtures.py` checks file structure and paired case completeness only, not GPT-6 reasoning. Keep `UNVERIFIED` until an independently assessed model comparison passes. No latent mental-state assessment or behavior-based clinical diagnosis is authorized.
