---
name: quiz-drill-engine
description: Build, validate, teach, and resume Coursecraft Lab interactive quiz drills from source-grounded JSONL across mathematics, programming, philosophy, engineering, science, arts, and other subjects. Use for 100-question banks, 50+50 scored checkpoints, learner-paced animated diagrams, historical trivia and applications, or retrieval from user-owned SM-20 JSONL source banks.
---

# Coursecraft Lab — Quiz Drill Engine v1

This skill extends, and does NOT replace, Coursecraft Lab's course-orchestrator. It applies to **any discipline**, not mathematics alone. Work within the governing course/module outcomes; use the domain's actual epistemic standards and discipline terms. Read `../course-orchestrator/references/learning-contract.md`, `../course-orchestrator/references/lesson-ui-ux-contract.md`, `../course-orchestrator/references/assessment-provenance.md`, and `references/drill-design.md` before a substantive drill.

## Dispatch and truthfulness

- `/drill`, `/quiz`, `/bank100`, `/quiz-session`, `/quiz-retrieve-sm20`, `/quiz-resume` and natural language equivalents select this workflow. Ordinary conceptual questions are answered directly; invoking Coursecraft alone never authorizes 100 questions.
- If user requests **100 questions**, prepare exactly **100 distinct scored items** for the defined lesson/session, in a **UTF-8 JSONL/NDJSON** bank, with stable question IDs, schema version, source status and valid answers. If 100 defensible non-duplicate questions cannot be authored with verified criteria, deliver a smaller explicit pilot and state the remaining authoring debt; never pad the bank with trivial numerical substitutions while claiming authentic variety.
- **Default sequence:** Drill I = 1–50, checkpoint score; Drill II = 51–100, checkpoint score; exact block index saved. User can continue now, tomorrow, or the next session. Do not infer the next day's completion from a date.
- Every scored item must include: `prompt`, `answer`, `options` or appropriate response validator, progressive `hints`, a precise `explanation` with warrant and misconception, a **historical fact/trivia** with named source URL/locator or an explicitly pending fact not allowed into scored release, a practical `tip`, `contribution` (disciplinary contribution, properly bounded), `applied_activities`, and an **instructional visual contract** (`type`, meaningful steps/states, description and static fallback). Include `origin` to distinguish institutional prompt, user-authored prompt, retrieved artifact, or generated practice.
- Historical trivia must be relevant to the concept, not random entertainment; one fact per question can be reused if contextually justified. Never attribute generated questions to MIT, other universities, or the SM-20 bank unless verifiable source IDs document that origin. “Verified history source” does not imply “verified question answer”.
- **Different subjects need different witnesses:** numerical derivation, code execution/trace, system state update, historical chronology with primary-source location, philosophical argument/counterexample, art/design perceptual comparison, source-critical interpretation. A multiple-choice answer alone is not independent understanding. Use a follow-up transfer item after errors.

## Generation and quality gates

1. Collect course ID, `module_id`, target action, prerequisites, language, time/pressure constraints, source corpus, and actual SM-20 availability. Preserve agreed vs provisional states.
2. Derive question family and concept coverage, mixing recognition/recall/application/error diagnosis/transfer in pedagogically appropriate proportions, **not a universal fixed ratio**. `question_count=100` is a delivery contract rather than a reason to fabricate provenance.
3. Retrieve candidate sources from original documents or authorized banks; preserve exact source IDs, loci, authors, rights, and uncertainty. SM-20 is an **opaque user-supplied source-bank identifier**; do not invent what "SM-20" means or claim access without file/tool evidence.
4. Author and independently validate each keyed answer, correct type/units/assumptions, distinct options, explanation, failure case, link, animation claims, and retrieval provenance. Run subject-specific mathematical/code witnesses where feasible, and strongest opposing arguments for philosophical items.
5. Attach one **instructional visual** when perception/state transition requires it: staged remainder bars/groups, typed state graph, argument map, code trace, source timeline, animated geometry, an annotated real media fragment if its rights are resolved. Visual transitions show meaningful state, not decorative animation; support reduced motion, pause and static text. When no informative animation exists, use a static visual contract rather than inventing movement.
6. Implement one attempt at a time. Predict before reveal, allow progressive hint, register first submitted answer, show verified/corrective reasoning and source-backed trivia after submission. Correct-with-hint is **assisted**, not unassisted mastery.
7. After items 1–50 and 51–100 compute score as `first-attempt-correct / 50`; display unanswered as such. Preserve mistakes as remediation work; retries do not overwrite the first-attempt score. Do not invent institution pass marks or psychological conclusions from speed/accuracy.
8. On pause, export/import progress capsule with bank identity, item/attempt ID, question positions, scores, hint usage, incorrect concepts, next exact action, source anchors and actual date. Browser local storage is not cloud persistence. Use portable JSON with explicit export if no connected storage was authorized. Integrate with current Learning Contract, but don't mutate a user's Notion Journal or Critique and Reflection without genuine activity/evidence.

## SM-20 / retrieval adapter

`SM-20` is a separate retrieval corpus; do NOT silently turn its rows into scored questions. When a user provides an SM-20 JSONL file, the adapter should:

- Validate each line as JSON and retain **the complete original record**, row number, bank identifier, original ID where present, and source date/URL if present. If no ID exists, assign a local content hash labeled generated, never a fake original ID.
- Support a **best-effort lexical first-stage search** over available JSON fields, preserve query and retrieved record IDs, allow source review and explicit link to a question. No claiming vector/semantic retrieval without actual embedding/index infrastructure. Never quietly claim the bank was read when unavailable.
- Preserve the existing bank's unknown schema and avoid writing back to it without a separate mapping agreement. Field-name guessing is restricted to read-only display (`id`, `source_id`, `title`, `text`, `content`, `body`, `excerpt`, `tags`). Emit a mapping report with unmapped fields.
- Retrieval citations and historical facts are separate objects; a matching record does not verify the fact or answer. Attach loci and `source_verified` state, use authentic publication URLs where verified.
- If a file is missing, generate a **schema adapter and a pending link**, not imaginary retrieval results. See `references/drill-design.md` and bundled `scripts/sm20_retrieve.py`.

## UI and deployment contract

Native chat controls support a small ephemeral quiz; they do **not** guarantee 100-item navigation, autoplay, browser localStorage, multi-session persistence, or file uploads in every host. The bundled offline HTML demo supports browser-local progress, deliberate JSON import/export, 50+50 scoring, staged visuals and SM-20 lexical file retrieval. It is not a hosted service or synchronized LMS; test its runtime and report host-specific results accurately.

Do not impose severe timers, surprise animation, confetti or autoplay on the learner. Pressure training is optional and should only follow basic accuracy and demonstrated recovery. Give an actionable next step if the learner loses track of a procedure.

## Files and examples

- `references/drill-design.md`: content, schema and interaction invariants.
- `references/quiz-item.schema.json`: JSON Schema for a scored single-choice bank item; other response kinds require separately validated assessors.
- `../../scripts/sm20_retrieve.py`: read-only JSONL SM-20 importer and lexical retriever.
- Offline browser prototype and the 100-question cross-disciplinary demonstration bank are companion **local artifacts**, not automatically served to all plugin clients; provide them when user asks for working prototype/source.
