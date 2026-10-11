# Cross-session Learning Contract v1

Portable, learner-owned state. Never pretend the plugin stores progress by itself; it is skill-only. Generate an updated Markdown/YAML contract after a lesson and invite user to paste it into the next session or store in an authorized linked location. On resume, use provided contract and recent work when available; do not automatically re-teach from the beginning.

```yaml
schema: coursecraft.learning-contract/v1
course_id: ""
subject: ""
project_goal: ""
learner_level:
  baseline: unknown
  demonstrated: []
  not_yet_demonstrated: []
constraints:
  language: "Bahasa Indonesia prose; English technical vocabulary"
  software_versions: {}
  hardware: []
  weekly_budget: null
course_map:
  current_module: 1
  current_lesson: 1
  dependencies_met: []
  dependencies_missing: []
lesson_state:
  lesson_id: ""
  status: not_started # not_started / mirrored / modified / transferred / verified
  core_claim: ""
  artifacts: []
  sources: []
  completed_actions: []
  observed_output: ""
  diagnostics: []
  learner_explanations: []
  authentic_assessment: null
  attempt_feedback: []
  unresolved_blockers: []
  next_exact_action: ""
provenance:
  updated_at: ""
  claims_verified: []
  pending_verification: []
```

Transitions:
`not_started → mirrored → modified → transferred → verified` only after actual evidence. Never advance merely because time elapsed or learner watched a video. Keep baseline and current performance distinct. Lesson navigation is DAG-aware, so if a failed test reveals missing fundamental, branch to the smallest prerequisite lesson then return.

Use stable lesson IDs (`C01-M02-L03`) and target state IDs. When a long conversation approaches limits, provide *recovery capsule*: course ID, current node, what has been proved/done, artifact paths or descriptive handles, software versions, unresolved issue, smallest next action, and one-paragraph recap. Contracts can be exported to Notion/YAML/docs if corresponding tools are available; never claim sync without execution.
