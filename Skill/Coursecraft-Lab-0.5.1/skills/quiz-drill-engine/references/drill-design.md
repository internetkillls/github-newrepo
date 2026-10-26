# Quiz Drill Design Contract — Coursecraft Lab

## Objects and separation

`SourceRecord` (e.g. user-owned SM-20) → `EvidenceLink` (explicit retrieved span, locator and verification status) → `QuizItem` (authored, validated assessment) → `Attempt` (learner answer, hint use, timestamp) → `BlockScore` (first attempt across fixed 50) → `Progress` (portable next-session state) → `Remediation` (unmet prerequisites).

A record is not automatically a question. A citation validates a historical claim only if directly inspected. An answer key is not validated by a plausible paragraph. Do not confuse a historical fact's truth with the quiz item's independent correctness.

## Default JSONL item

Each UTF-8 line is a JSON object. Important fields:

```
{"schema":"coursecraft.quiz-item/v1", "id":"C01-M01-Q001", "course_id":"C01", "module_id":"M01", "subject":"Mathematics", "skill_id":"modulo", "difficulty":1, "origin":"course-generated", "prompt":"17 mod 5?", "format":"single_choice", "options":["2","3","4","1"], "answer":"2", "hints":["Find the largest multiple of 5 no greater than 17."], "explanation":{"reason":"17 = 5 × 3 + 2; the remainder is 2.","common_error":"The quotient is 3, not the remainder.","transfer":"Indexing repeated cycles."}, "history":{"claim":"Euclid treats greatest common measures in Elements VII.2.","person":"Euclid","year":"Ancient Greece","title":"Euclid, Elements VII.2","url":"https://www.perseus.tufts.edu/hopper/text?doc=Euc.+7&fromdoc=Perseus%3Atext%3A1999.01.0086","source_locator":"Book VII, Proposition 2"}, "tip":"Subtract complete groups before reporting remainder.","contribution":"Modular reasoning supports periodic indexing.","applied_activities":["Scheduling repeating cycles"],"visual":{"type":"remainder","steps":["5×3=15","17−15=2"],"description":"15 of 17 objects grouped into threes of 5, with 2 remaining."},"source":{"kind":"course-generated-practice","title":"Coursecraft authored exercise","url":null,"verified":"generated"},"retrieval":{"bank":"SM-20","source_ids":[],"status":"not-linked"}}
```

Schema does not declare actual SM-20 keys or semantics, and does not require using it. For open-ended responses, code, formal proofs and oral answers, provide an appropriate separate assessor or human review rather than auto-grading arbitrary natural language via exact string equality.

## Session/progress invariants

- Bank has exactly 100 unique stable IDs for 2 × 50 scoring; each question and required field passes local validation.
- First submitted answer counts as assessment. Store `answer`, `correct`, `hintsUsed`, `questionId`, `completedAt`. Corrections belong in new attempts, not rewritten first attempts.
- Score I is correct answers in 1..50 divided by 50; score II is correct answers in 51..100 divided by 50. If a block is incomplete, show numerator AND answered count, never percentage as if all attempted.
- Block-boundary export/import to tomorrow/next session uses `schema:coursecraft.quiz-progress/v1`, `bankFingerprint`, `pos`, `attempts`, `hints`, `linked`, `startedSecondBlock`. Import refuses wrong bank identity; preserves first-answer record.
- At least one repair task must revisit each error family with a changed input/case, while historical score remains frozen. Repeated trivia is supplemental reading, not tested mastery by mere exposure.
- No invented scheduler: "tomorrow" is user intent to return, not permission to create a reminder. No automatic sync absent explicit connected permission.

## Instructional interaction

`Question → learner predicts → choice → submit → feedback (first score) → progressive derivation → historical fact with source → application/tip → next item.`

Visual state types (examples): `remainder`, `number_steps`, `code_trace`, `logic_gate`, `stock_flow`, `timeline`, `argument_map`. All labels clarify state and causal vs inferential arrow. Minimum human-readable still text. Animated states must have manual previous/next controls, pause and reduced-motion behavior. Do not falsely imply a mathematical animation itself establishes theorem validity.

For visual assets: the *Visual Pipeline* contributes cue discipline (intent, state transition, reversible playback, QA), not its venue/cube-face theme, Resolume codecs or default palettes. For external media verify accuracy, licensing, attribution, rights. Simulated diagrams are labeled generated explanatory visuals.

## Question-family coverage examples beyond mathematics

- Programming: predict code trace, diagnose a failing test, specification vs execution.
- Engineering: calculate stock-flow-state, anticipate feedback and delays, set acceptance conditions.
- Philosophy: locate an unsupported premise, give a counterexample, separate model and physical attribution.
- Historical humanities: source-context chronology, rival interpretation, document provenance.
- Creative coding/art: compare perceptual outputs under one control variable, source image rights, composition changes.
- Natural sciences: observable prediction, experiment design, measurement error, model validation.

Do not require numerical scoring for subjective reflection unless a transparent assessor and review process exists.
