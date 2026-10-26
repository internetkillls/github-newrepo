# Provenance of AntiSlop design inputs (snapshot: 2026-10-09)

**Primary design artifact:** `source-draft-v0.1.md` (the user-supplied Anti-Slop Spec compiled 2026-10-09). Its interaction/coding errors are reported signatures, not measured transcript incidents. Its repository table is a research lead; no reproduction was provided in the attachment.

**Reasoning controllers:** Current installed RMC v0.6.0 guidance: task route → conditional stage → failure-signature operator → exit-test/repair; maintain origin-vs-stance and term senses, distinguish METHOD from OBJECT sources. Current installed RCC v0.2.0 guidance: workers are dependency slices, independence classes I0–I4, source-anchored closure, invalidate descendants, never claim browser workers ran without receipts. AntiSlop adds failure-audit specialization; does not fork those runtimes.

**External spot checks** (project documentation consulted for design limits; not claiming their benchmarks independently reproduced):
- LongMemEval, https://github.com/xiaowu0162/LongMemEval — long interactive memory benchmark; motivates anchored multi-session memory checks, not magical access to arbitrary chats.
- awesome-slop, https://github.com/hwajongpark/awesome-slop — multilingual collection; language lists are leads not validated Indonesian slop corpus.
- Auto-Antislop, https://github.com/sam-paech/auto-antislop — methodology for profiling model-specific repeated patterns; needs representative baselines.
- AI-SLOP-Detector, https://github.com/flamehaven01/AI-SLOP-Detector — offline deterministic structural code signals; README explicitly disclaims runtime correctness guarantee.

The plugin does not vendor these repositories, copy their code, imply a collaboration, or depend on them at runtime. It does not implement their statistical model, AST detector, transformer, LLM judge, or formal solver. The bundled optional CLI is a small, independent standard-library validator and heuristic scanner.
