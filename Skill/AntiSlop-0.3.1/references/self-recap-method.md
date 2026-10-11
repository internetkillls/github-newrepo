# Reconstruct a conversation without laundering authority

## 0. Decide whether to recap

Trigger on: user explicitly asks a recap or continuation; a past instruction may override a current suggestion; thread contains multiple materially distinct goals; user has corrected the assistant; named prior decision is being reused; cross-turn concept meaning affects inference; potential repetition/question drift. Otherwise keep only a task-local checkpoint. No universal every-N-turns recap: length alone is insufficient.

## 1. Coverage manifest

```yaml
scope_id: conversation-or-user-supplied-export
requested: "all chat relevant to present AntiSlop work"
accessible:
  - type: visible_chat | provided_export | retrieved_user_context | supplied_file
    range: "accurate message locators; no guessed spans"
    source_ref: "actual source identifier"
missing: ["unknown or inaccessible history, if any"]
coverage: complete_for_requested_range | partial | unknown
confidence_basis: source-anchored | indirect-report | unresolved
```

If no complete export is available, label partial. A summary model's memory is not an archived verbatim transcript, and "recently discussed" is not a verified quote. Mark confidence by evidence, not by eloquent certainty.

## 2. Extract event candidates with attribution

For each material turn or paragraph, parse candidate records with actor, origin, stance, proposition, exact anchor, relation to question, material date/version, affected task and dependency. The actor is whoever said the message; the origin can still be a quote, uploaded draft, prior assistant or external source. Presence in a user's message does not make its contents user-authored or adopted.

Use the JSONL example in `ledger-schema.json`; the supplied CLI checks structure, not the semantic fidelity of extraction. Avoid hidden private chain-of-thought or a personality ledger. Granularity: one material state transition per record; not every sentence or chat turn.

## 3. Four canonical registers

**Question register:** `question_id`, formulation, introducer, first seen, status `active|proposed|superseded|rejected`, scope, prior question replaced, explicit reframe authorization and evidence locator. Where many questions coexist, distinguish branches; do not force a single global question.

**Claim / decision register:** content, speaker, origin/stance, state (`stated|proposed|accepted|rejected|superseded|unresolved`), user acceptance evidence, hard/soft constraint, dependencies and supersession link. An assistant-originated proposal is proposed by default. An assistant can assert facts, not make user's commitment.

**Sense register:** inference-bearing term, sense-id, origin, working definition, affected claim, when/why shift was introduced; multiple simultaneous senses can be legitimate if indexed. Do not automatically flag polysemy.

**Debt / test register:** unresolved question, missing source, failed probe, expected vs observed, responsibility/next reversible step, stop/reopen condition. A planned test is not an executed test; a summary of someone's alleged test is `reported`, not `observed`.

## 4. Reconciliation invariants

1. Every authoritative decision is traceable to the user's direct statement/action, or is explicitly marked as a provisional working assumption.
2. When a user correction contradicts an assistant proposal, preserve the correction and mark the proposal rejected or superseded within the relevant scope, not globally or retroactively.
3. Each superseded decision links to a replacement; if no new authority is known, status `unresolved`.
4. A question reframe must identify what problem made it necessary, who authorized or merely proposed it, and whether it actually answers the prior question.
5. A finding's source role must be retained: a paper about a teaching *method* is not evidence about a lesson's *subject*.
6. Term-sense conflicts are material only when they change an inference, test, source set, or commitment.
7. No closure after test failure without reproduction, changed requirement, or explicit limitation.
8. A recap's omissions and coverage are first-class evidence debts.

## 5. Self-critique (second pass, different question)

Do NOT ask merely "is this summary correct?" Instead run disconfirming checks:
- Find an assistant proposal the user never accepted; ensure it is *not* recorded as accepted.
- Find the most recent material correction; verify it affects the active acceptance criteria.
- Find an old question that looks like the latest question; compare their required outputs; flag drift if the later one displaced the former without authority.
- Find a source cited as substantive proof only because it appears in a methodology document.
- Find an accepted claim whose evidence anchor points to a third-party quote, not user's explicit stance.
- Find a term with more than one sense and check whether substitution changes validity.
- Find an executed test vs promised test; don't promote intentions into results.

Record `pass|fail|unknown` with source anchors. Failure in extraction returns to the corresponding turn/attachment, not stylistic rewriting. No mandatory external adversarial worker; use independent review when stakes warrant it.

## 6. Delta-recapping and refresh

Keep a small warm checkpoint only when explicitly produced or provided (not assumed stored). Next turn: compare newly visible events with active question/constraints; append an event for user change, rejected suggestion, new test, or reframe; mark dependent conclusions stale. No recomputation of unrelated history. An unavailable earlier ledger is unknown, not empty.

## 7. Minimal response sample

> **Scope:** 14 visible relevant turns, one attachment; other historical sessions not available. **Current question:** repair TD rendering, not rebuild geometry. **Approved:** raster diagnostic first. **Proposed only:** switch engine. **Test:** screenshot shows blur, but source texture size not measured. **Next:** compare source TOP resolution and viewer scaling. **Debt:** screen capture resolution unknown.

This is a schematic example, **not** a statement about the user's actual TouchDesigner session or a verified test.

## v0.3 protocol clarification: decision-edge witness

The recap now distinguishes: (i) source coverage/index completeness, (ii) extraction accuracy, (iii) directed decision relations, and (iv) domain-specific quality. A successful syntax/schema check establishes (ii) neither automatically nor completely. Use the index command only on normalized supplied JSONL; never treat line counts as evidence that all account conversations were loaded.

A user response that says *continue* can authorize the **next bounded task** without accepting unrelated architectural proposals. To accept proposal A, the adoption record must target A specifically. To replace question Q1, Q2 must have a supported `replaces: Q1` relationship. Two unanswered questions can coexist when their scopes differ. Without target links, the result should be `ambiguous` rather than a fabricated canon.

When correcting decision D1, record the correction pointing at D1. Omit D1 from effective accepted commitments, but keep it in the audit history as `corrected_prior_events`, rather than deleting contrary history. Corrections without an explicit target remain visible with an unresolved warning.

Near-miss negative controls: an assistant makes two proposals and user accepts only one; a user quotes a policy but rejects it; a later question extends rather than replaces the first; a correction changes *quality of raster* but not scene geometry; a formal proof is sound but the formalized theorem is not the intended specification. A good detector should refuse premature acceptance, preserve parallel questions, and avoid a style-only rewrite for semantic failure.
