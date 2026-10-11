# Lesson UI/UX contract — actionable, accessible and recoverable

This is a **design/specification contract**, not an installed LMS or proof the current chat UI implements every affordance. Use real host components only when supported. A static screenshot of a button must not be presented as working interactivity. Keep a plain text/button-query fallback when there is no custom UI runtime.

## Default lesson viewport / information hierarchy

1. **Where am I?** Small stable `course_id / module / lesson / current goal` and a meaningful state such as `provisional`, `attempted` or `verified`. Never show fabricated mastery percentages. Keep progress secondary to task.
2. **What am I trying to see/do?** An operational target or question + one reference outcome, preferably beside it.
3. **What is the object?** Exactly situated instructional visual or source passage/code with labels, source status, and alt. Minimal terms in field language. Link definitions contextually, not as pop-up overload.
4. **What do I do next?** One primary action: `Predict`, `Try`, `Compare`, `Run` (ONLY if executable), `Explain`, or `Check`. Other actions remain discoverable: `Why?`, `Show a hint`, `View source`, `See another example`, `Report mismatch`.
5. **What happened?** Feedback on the learner's action with observable evidence, failed condition, and concrete next attempt; do not confuse a selected option with demonstrated independent competence.
6. **How do I come back?** Retain a return pointer and portable recovery capsule at lesson transitions. No fake automated cloud save.

No mandatory card grid or sidebar. On narrow screens stack media, action, then feedback in reading order; for desktop pair media with only its closest explanation/action. Where columns become inaccessible, prefer the linear version. Avoid persistent overlays that cover source, controls or keyboard focus.

## Interaction taxonomy and click semantics

- `EXPLORE_OBJECT`: an anchored hotspot/term reveals *what/where/role* and returns to same task. Hotspot only if exact location is known. Accessible label and keyboard equivalent mandatory in a real app.
- `ASK_WHY`: include a selected concept/object ID and question; respond in local context, preserve current lesson state. No global-context-less 'Why?' action.
- `SHOW_STEPS`: reveal necessary substeps with checkpoints, not an unverified application clone.
- `PREDICT`: collect expectation *before* revealing outcome; explain the discriminating variable.
- `MODIFY`: alter one controlled variable where a real simulation/code runner exists; otherwise instruct external action and ask for observation.
- `HINT`: progressive hint sequence; don't jump to the complete answer by default; always let the learner request an explicit solution when appropriate.
- `COMPARE`: show reference and observed result with differences linked to causes and version assumptions.
- `REPAIR`: route to first missing prerequisite; offer a reversible return to original lesson.
- `VIEW_SOURCE`: show original author/URL, license and what claim it supports; don't drop the learner into a random search result.
- `RESUME`: show actual last verified work, unresolved blocker, and next exact action using provided state.

Every visible interactive control must have an advertised meaningful action and immediate status feedback when supported. Disable or omit unavailable actions instead of inert decorative buttons. Do not auto-trigger new chat turns merely from changing a visual selection. Distinguish `navigation` from `assessment`: click-through and familiarity prove neither recall nor transfer.

### Portable context envelope

```
course_id | course_revision | lesson_id | element_id | intent
learner_choice_or_question | last_observed_output | source_anchor
return_to | attempt_status | verified_evidence_ref | unresolved_blocker
```

Send only fields actually known and necessary, avoid sensitive data and fabricated timestamps. Make lesson/element IDs stable, allow a question to return to its point of origin. Cross-session persistence exists only when a real file, connected store or user-supplied contract provides it. Treat generated capsules as export suggestions until saved.

## Accessibility test: apply when building a real interface

- Conform to applicable WCAG 2.2 success criteria at the requested target level (typically AA for course web apps). Text contrast 4.5:1, large text 3:1, non-text UI states 3:1 where applicable; verify actual colors, don't assert compliance from naming a palette. WCAG 2.2 AA 2.5.8 pointer targets have at least 24 x 24 CSS px *or a documented exception*. Prefer larger comfortable targets when feasible; do not misstate 44 px as the AA minimum.
- Controls keyboard navigable with meaningful labels, logical focus order, visible/non-obscured focus. No color-only success/error indication. Help/action available without hover-only affordance.
- Informative image: concise alt. Complex diagram: short identification AND substantial text description of nodes, relations, order, caveats; source image with text may need transcription. Decorative imagery is ordinarily avoidable here. Source image and generated images have clear provenance.
- Motion: learner-paced media; pause/stop/hide auto-motion when WCAG requires; support reduced motion for nonessential interaction animation. Offer still-frame/text equivalence where appropriate. Do not invent UI pause controls in a skill-only response.
- Use straightforward labels in learner/discipline language; accessible mathematical notation and meaningful reading order. Code exercise feedback not limited to red/green.
- Interaction modes can vary: clicking, keyboard, text answer, narrated explanation or artifact submission when available. Equivalent *access* need not imply identical assessment: record what evidence each mode actually establishes.

Reference: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/tutorials/images/complex/ ; https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

## Progressive disclosure without pedagogical withholding

First show primary target, current visual and action. Optional depth via contextual `Why?`, `Compare rival`, `Open glossary`, `Show sources`, `Detailed derivation`. Do not hide a safety-relevant step, crucial premise, feedback, assessment rule, or help needed by a learner with access barriers. Do not make the learner chase many 'More' clicks just to understand the base task. Honor explicit requests for full detail rather than impose endless micro-steps. NN/g principle: https://www.nngroup.com/articles/progressive-disclosure/

## Feedback microinteraction contract

`trigger → state acknowledged → evidence/results → meaningful next choice`.

Use statuses `not_started`, `attempted`, `mirrored`, `modified`, `transferred`, `verified`, `blocked`; map to original contract fields, not new mandatory backend states. Invalid answer gets actionable correction, not decorative confetti. Inform user when an action navigates away, exports a file, or requests new external execution. Respect reversible exploration: going back does not erase work.

## Host levels / honest implementation

- **Level T (text-native)**: interleaved source, static diagrams, code, useful links, direct answer, portable progress packet. Available broadly.
- **Level C (chat controls)**: supported buttons, selectable answers, ask-by-click context handoff when actual host offers controls; ephemeral local state does not equal permanent storage.
- **Level E (external executor)**: validated embedded live editor/simulation/real tool, runtime test, explicit permissions, file artifacts; only claim what was executed.
- **Level P (persistent course platform)**: connected backend/authorized storage, account/session/progress sync, migration/revision, accessible navigation; NOT automatically supplied by the skill.

Before promising a component check host capabilities. If unavailable, downgrade gracefully to Level T rather than fabricate UI.

## Methods, not course-object sources

- Jakob Nielsen, 'Progressive Disclosure': https://www.nngroup.com/articles/progressive-disclosure/
- NN/g, '10 Usability Heuristics': https://www.nngroup.com/articles/ten-usability-heuristics/
- CAST, UDL 3.0: https://udlguidelines.cast.org/more/about-guidelines-3-0/
- W3C WCAG 2.2 and image alternatives: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/tutorials/images/complex/
- H5P Branching Scenario, *example pattern not an integration*: https://h5p.org/branching-scenario

These guide UI design; they do not belong in a TouchDesigner/math/history syllabus unless UX/design itself is the subject.
