---
name: task-intent-boundary
description: Always apply alongside Reasoning Method Controller when several plugins are invoked, when a user follow-up changes the governing question, when the user asks about business economics or revenue while teaching/course tools are present, or when an answer could substitute a course, design, or recommendation for investigation. This is a small S0-S2 intake and routing preflight, not a replacement for RMC.
---

# Task intent and cross-plugin handoff gate (RMC 0.6.2)

This skill operationalizes RMC's existing S0 INTAKE, S1 ROUTE and S2 FRAME for mixed plugin requests. It has precedence over the output conventions of any co-invoked specialist plugin **only for deciding what task is being answered**. Read the current governing user turn; preserve prior constraints not explicitly revised. Neither an @mention nor a plugin default prompt is evidence that its signature artifact is wanted.

## Required cheap preflight (before designing an output)

1. Write an internal task contract: current question in one sentence; requested deliverable(s); primary inquiry regime (explain, investigate, compare, teach, design, execute, audit); accepted prior decisions versus unaccepted assistant proposals; evidence needed for a correct answer.
2. For follow-ups, check what dimension changed. The latest specific question overrides previous output format when the two conflict; preserve previously accepted constraints otherwise. Do not carry a prior course into an empirical follow-up merely because Coursecraft remains invoked.
3. Attribute roles: RMC decides inference/evidence gates; Coursecraft decides teaching design only where requested or actually needed; AntiSlop audits context, substitution and provenance. Mentioned tool ≠ user instruction to produce that tool's trademark deliverable.
4. Before delegating or producing a curriculum, verify a positive `TEACH/DESIGN-COURSE` signal in the active request or an explicitly agreed dependency. If absent, do not make a curriculum the answer. A concise explanatory example or teaching aid remains permitted when it solves the current question.
5. In mixed requests with distinct deliverables, answer each component under its own evidence standard; mark unsupported comparisons provisional. For commercial mechanism questions: identify who pays whom, payment trigger, eligibility/contract, inputs/costs, relevant uncertainties. Do not infer realistic rates from hypothetical arithmetic.
6. Close with an answer-contract check: would the response satisfy the latest question if all curricula, charts, prompts for niche selection, and UI controls were removed? If not, return to S2 and repair the earliest failure.

## Discriminating tests

- `Buat program Social Media Manager ... dan model revenue` is MIXED: a program is authorized, but micro-agency is not automatically an accepted business model. Show candidate revenue mechanisms with claim status before building the corresponding curriculum.
- `Terus akun meme dan trivia revenue-nya dari mana?` is INVESTIGATE: explain payment flows and evidence first; no week-by-week course without a new teaching request.
- `Sekarang buat kursus 8 minggu dari model yang dipilih` is TEACH if a model has actually been selected; generate the course. If no model was selected, preserve an explicit provisional assumption rather than invent an endorsement.
- `Jelaskan lewat diagram` can authorize a diagram as an explanatory medium; a diagram does not prove profitability.

Do not turn these examples into keyword classifiers; use the actual speech act, object and requested artifact. This skill is an instruction-level guard, not an automatic detector or evidence that earlier model execution passed.
