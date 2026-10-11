---
name: antislop-router
description: Entry point when the user asks for AntiSlop, self-audit of a chat, answer quality, coherence/routing review, unsupported commitments, or cross-domain slop detection and repair. Start with context coverage and conversation-state reconciliation before any substantive detector.
---

# AntiSlop router v0.3.0

## Task definition

Detect and repair output that is locally plausible yet fails the user's task, evidence, conceptual commitments, or operative tests. This is a **quality and warrant audit**, not an AI-authorship detector, stylistic humanizer, or automatic deletion system. The term "slop" is an evaluative working category, not a claim of model provenance.

## Priority order — never reverse this

1. **ACCESS / SCOPE** — identify which turns, files, sources, tools, versions and outcomes are actually accessible. Distinguish `current-turn`, `visible-chat`, `user-export`, `retrieved-previous`, `unavailable`. The phrase "all the chat" means **all demonstrably accessible relevant turns**, with an explicit coverage statement, not an invented complete account history.
2. **SELF-RECAP GATE** — decide if a contextual reconstruction is necessary. Required for explicit recap, prior-decision claims, material user correction, long/multi-task threads, updates to existing projects, or suspected question/commitment drift. Otherwise use 2–4 sentence current-task recap, no ledger dump. Read `../conversation-recap/SKILL.md` and `../../references/self-recap-method.md` when gate fires.
3. **TASK CONTRACT** — derive present governing question, exact requested artifact, acceptance criterion, constraints, role of citations, source provenance, explicit user decisions, unaccepted assistant proposals, material open debt. Explicit current instructions outrank inferred history.
4. **RISK ROUTING** — route to the few relevant detectors among Q/W/L/S/I/N/C/A/M from `../slop-audit/SKILL.md`. `L` is cross-cutting interaction integrity, normally adjudicated in step 2. Never run all nine by habit.
5. **EVIDENCE / TEST** — a cheap linter may flag patterns; only witnessed contradiction, source check, test output, or warranted inferential analysis can establish substantive failure. No LLM-as-judge sole PASS/FAIL. Use an independent adversarial check only if a live unresolved interpretation affects the outcome.
6. **REPAIR** — locate the earliest failed dependency: wrong user question → reframe; false source → retrieve/withdraw; unmet runtime contract → minimal failing probe; diction problem → rewrite from claim. Do not repair by synonym swapping.
7. **REGRESSION / CLOSURE** — archive confirmed errors with evidence, include a near-miss negative control, rerun affected test; mark pending when no evidence. State residual unknowns. Use `../regression-corpus/SKILL.md` when corpus building is asked or a confirmed reusable case exists.

## Dispatch and priority

- `conversation drift | who agreed | previous decisions | summarize all chat` → RECAP priority.
- `output incorrect | code doesn't work | hallucinated reference` → contract + verification priority.
- `academic paper | argument | proof` → A/M/S and Q only when retrieval is material.
- `writing in Indonesian` → W/I plus semantic coverage; register preference ≠ correctness.
- `codebase | names | architecture` → C/N/L with runtime witness when available.
- `search quality | dorking | citations` → Q + evidence roles before writing.
- mixed requests → separate jurisdiction-specific tests, one coherent closure; do not average scores.

## Coexistence boundaries

- If Reasoning Method Controller is present: use its conditional stages and failure operators to test local inferences; AntiSlop supplies witnessed failure signatures, not a replacement reasoning theory. METHOD sources never become evidence about the user's subject.
- If Reasoning Consortium Controller is present: delegate genuine independent source/runtime verification only when it would change a decision. Preserve I0–I4 independence class; do not claim worker tabs, parallelism or browser execution without execution receipts. AntiSlop consumes typed closures; RCC owns worker topology and invalidation propagation.
- Absent either controller: use equivalent minimal checks locally; never claim they were invoked.

## Finding output contract

In ordinary conversation do not expose the full audit machinery. When an audit is explicitly requested, show: `(1) available scope`, `(2) current question/accepted decisions vs proposed`, `(3) each material issue with anchor and type`, `(4) a repair and discriminating retest`, `(5) remaining uncertainty`. Use `CONFIRMED`, `SUPPORTED-RISK`, `STYLE-SIGNAL`, `UNVERIFIED`, `NOT-APPLICABLE`; no invented precision/confidence. User receives the substantive corrected answer or artifact, not just diagnostic lists.

## Stop criteria

Stop after the smallest adequate test set passes, or state an exact evidence debt and narrow any conclusions. Do not manufacture new defects, obligatory objections, terminal summaries, or research hunts. Current user authority and safety constraints override prior assistant artifacts.

## v0.3 transcript-input branch

If a chat export is supplied, start by confirming whether it is a normalized JSONL transcript (see `../../references/transcript-import.md`). If it is not, normalize *only through explicitly supported access to the source*, or state the import limitation. Index first, extract event candidates second, validate directed acceptance/replacement/correction links third. Do not present the CLI's structural success as proof that a past user decision occurred. For short current-chat continuations, no file conversion is required; the same provenance and target-link rules still apply.
