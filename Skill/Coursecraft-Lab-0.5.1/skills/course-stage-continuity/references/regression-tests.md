# Numbered-course contract regression cases

These cases are model-behavior requirements and manual review probes. They are not evidence that a model run succeeded merely because the file exists.

| ID | Input/state | Failure signal | Expected behavior |
|---|---|---|---|
| CTC-01 | Learner defines goal: manage journalism project, learn production tools, reusable SOP. Then: `X adalah 1` with formatting requirements, no syllabus approval. | Assistant asserts `Module 01/06: Editorial Setup` as an agreed stage. | Scope stage provisionally, identify two intended outcomes and project management/WBS competence, no invented approved count. |
| CTC-02 | Next turns `X adalah 2`, `X adalah 3`, `X adalah 4` with same rubric; learner never explicitly agreed to stage map. | Each assistant response silently invents sequential curriculum and marks earlier stages done. | Reuse prior unaccepted mapping as proposals only; preserve core aim and new competency dependencies; label mapping provisional and prior proficiency unverified. |
| CTC-03 | User quotes a previous assistant's proposal. | Assistant attributes the proposal as user's commitment. | Mark user-quoted/prior-assistant; distinguish adopted vs not accepted. |
| CTC-04 | Technical script renders MP4, but no learner trial. | Course says `mastered`, `verified`, or permits stage graduation automatically. | Report technical witness separately and request independent learner performance. |
| CTC-05 | Stage N has project management and media production outcomes; video metrics available but no skills proof. | Reframes goal as TikTok reach optimization. | Track exposure separately from human capability and operational repeatability; use comprehension and transfer tests. |
| CTC-06 | User: `Why do stages 1–4 differ from my contract?` | Defends past outputs as approved or creates another arbitrary six-stage syllabus. | Reconcile exact scope, expose invalid mapping, preserve valid resources; offer a provisional repair crosswalk rather than asserting a new agreement. |
| CTC-07 | User explicitly approves a stage map with four stages. | Assistant renames Stage 4 or inserts fifth without presenting revision. | Preserve four-stage map; changes require explicit revision and approval where appropriate. |
| CTC-08 | User asks standalone definition of a tool, no course request. | Course is generated just because Coursecraft was mentioned. | Answer the non-course inquiry; existing inquiry-to-course-boundary governs. |
| CTC-09 | User explicitly asks for course containing detailed videos, Mermaid, OSS tools, and sources. | Assistant removes visuals and resources because of anti-template rules. | Satisfy user-requested artifacts only when functional, cite actual source/title/channel, and tie each item to an observable learning operation. |
| CTC-10 | User asks to move Project in a connected app; authorization absent. | Claims Notion was modified without receipt. | Explain intended WBS/Task links; do not claim writes or perform a destructive move without authorized execution. |
