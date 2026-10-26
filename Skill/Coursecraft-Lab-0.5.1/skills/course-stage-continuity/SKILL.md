---
name: course-stage-continuity
description: Use with Coursecraft Lab whenever a learner says Tahap X, X adalah N, Stage N, Lesson N, continue a previously numbered course, compares lesson content with a contract, or asks to repair drift across a multi-turn curriculum. Recover the course contract before assigning topics or claiming progress.
---

# Course stage continuity and contract integrity

This skill supplements `../course-orchestrator/SKILL.md` and `../inquiry-to-course-boundary/SKILL.md`; do not replace their pedagogy or override current explicit user instructions. Activate **before** composing a numbered stage/lesson, or when the user reports inconsistent stages. Its job is to keep governing goals, syllabus authority, capability evidence, and cross-stage dependencies consistent—not to supply an automatic syllabus.

## 1. Source-of-authority gate (mandatory for staged follow-ups)

Reconstruct from the **actually accessible** conversation and approved learning contract:

- learner's governing goal and intended competencies, including multiple outcomes (e.g., project management capability AND a media publication), their intended relationship, available skills/tool constraints, and exact user-provided stage or ordinal;
- original approved course syllabus or WBS/course crosswalk, if any, including stage count, stable IDs, prerequisite edges, and status `AGREED`;
- current requested stage and evidence the previous stage's competency was demonstrated; explicitly distinguish `not_started`, `mirrored`, `modified`, `transferred`, `verified`;
- prior assistant-proposed syllabus/stage labels and artifacts not adopted by the learner;
- accessible sources and verified external claims vs unverified or generated examples.

`X adalah 4` names an **index**, not automatically the content of Stage 4 and not acceptance of whatever the assistant last called Stages 1–3. Repetition of a formatting prompt or clicking to request the next stage does not, by itself, approve a proposed syllabus or demonstrate mastery. Distinguish an agreed label, provisional mapping, proposed replacement and user correction. Do not fabricate prior approval, hidden learning evidence, or access to absent lessons. Use existing shared state; do not ask the user to repeat facts already available.

When there is no agreed syllabus, **never infer an agreed course size, stage names or stage-to-competency mapping**. Give the requested stage only with a visible `PROVISIONAL` mapping grounded in the real goal and prior dependencies, or offer a concise syllabus crosswalk when that is the actual current request. Continue usefully, but do not lock in an invented six-stage map. Do not relabel earlier content as user-approved. If a new user correction changes the goal, update the working mapping and preserve prior material as reusable resources where relevant.

## 2. Two-layer curriculum contract

**Course level** (may be DRAFT/PROVISIONAL until accepted): governing learner goal; separately named publication/artifact outcome and human capability outcome; success evidence for each; named modules and stage map; stage count only if supplied/agreed; prerequisite DAG; intended practice setting/tools; reusable WBS/project linkage when an operational project exists.

**Stage level**: stable stage ID and crosswalk to course goal/WBS; explicit input states and prerequisite evidence; ONE primary new learner capability with optional secondary capability; concrete operations `observe → predict → execute → compare → diagnose → correct`; actual tool installation/setup where needed; evidence-based media, video and articles when requested; checks that discriminate learner understanding from working software; handoff to next stage or exact dependency repair.

If stages contain multiple technical areas, preserve one coherent workflow: `input data [type/provenance] → transfer/manipulation [specific tool/operation] → observable artifact [format] → human skill test → reusable method`. A tool list, fabricated screenshot, code block or 'PASS' log is not evidence of learning. For free/open-source preference, label open-source vs proprietary free-tier and name paywalls/dependencies when material. Video tutorials: inspect/verifiably ground URL, title, channel/publisher and exact pedagogical focus; do not invent timestamps.

**Project-based course invariants:** distinguish deliverable-oriented WBS, executable Tasks, skills and assessment artifacts, and operational SOP/logs. Do not replace a project-management curriculum with an exclusively media-production syllabus merely because one pilot produces videos. Reuse existing Project–Task relationships rather than silently creating a new database or pretending to have synchronized a remote workspace.

## 3. Entry/exit before a numbered stage

Preflight before answering:
1. Resolve course identity, contract status, exact ordinal and source of stage label. If any of these are unresolved, keep that field explicit and provisional.
2. Check the intended stage's dependency on the goal, previous stages, and existing WBS. If Stage N's topic was assistant-proposed and not accepted, do not assert it as the learner's established map.
3. Identify the *difference* from the previous stage: new capability, new primitive, new operation, and new independently testable artifact. Do not repeat the same task with a different stage title.
4. Validate each requested medium against the learner operation. Prefer genuine video walkthrough / functional schematic / official docs; never use purely decorative image queries to tick an illustration quota.
5. Label demonstration/simulation/reference vs observed learner execution. A local script passing its test is only a software witness.

Stage exits when deliverables are **specified and taught**. Learner proficiency advances only after learner-provided evidence and a discrimination/transfer test; do not claim verified proficiency from a generated artifact or checklist. When evidence is missing, offer a prerequisite branch or simulated lab but keep mastery status unknown.

## 4. Drift detection and repair

Trigger a contract-drift audit when (a) learner asks why stages differ from contract, (b) a later stage changes the governing objective, (c) module counts or labels were invented, (d) stages repeat without new capability, or (e) platform reach metrics are conflated with independent learning.

Compare `USER-AGREED → ASSISTANT-PROPOSED → OUTPUT PRODUCED → LEARNER EVIDENCE`. Mark deviations precisely. Repair the **earliest invalid assumption** (usually an unapproved syllabus) before regenerating another lesson. Keep valid sources, code, and media as resources; do not claim previous work was worthless or automatically completed. If the learner asks only for an audit, do not mutate the course or plugin. If they explicitly want a course revision, show the old-to-new stage/WBS mapping and preserve verified progression.

## 5. Portable delta contract (extend—not replace—Coursecraft Learning Contract v1)

If an ongoing course would otherwise drift across turns, append a lightweight state block rather than inventing a memory backend:

```yaml
course_governance:
  syllabus_status: DRAFT  # DRAFT | AGREED | REVISION_PROPOSED
  governing_goal: ''
  editorial_or_project_output: ''
  human_capability_output: ''
  stage_count: null          # null unless agreed
  approved_stage_map: []    # stage_id, title, new_competency, prerequisites, WBS_link
  assistant_proposals_pending: []
  requested_stage: null
  prior_stage_learner_evidence: unknown
  current_stage_wbs_link: null
  known_curriculum_drift: []
```

Only add populated fields whose provenance is known. On successive `X=N` turns, check against this block and the actual conversation. Do not claim external storage or automatic updates. Cross-check source labels; a quoted assistant syllabus is not user approval. A stage may be delivered provisionally without asking clarification when the goal is clear, but must stay marked provisional.

## 6. Regression probes

Before delivering a new staged course, test against the cases in [references/regression-tests.md](references/regression-tests.md). Each case has a failure signal and expected observable behavior. Do not claim the test *ran* unless executed; these are authoring and review prompts, not a hidden autonomous worker.
