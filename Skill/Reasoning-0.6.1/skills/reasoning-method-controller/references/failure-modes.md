# Failure modes and repairs v0.6.0

All active failures from v0.5.6 remain active. Add:

151. Route–operator collapse → a local failure signature is treated as the whole workflow. Repair: choose route family → active stage → operator.
152. Stage-less dispatch → the right operator is selected but there is no entry gate, exit test, or handoff. Repair: place the operator inside the stage contract.
153. Full-pipeline ritual → every task is marched through S0–S9 regardless of need. Repair: skip a stage only when its exit condition is already satisfied.
154. Fluency skip → an unsatisfied stage is bypassed because the answer feels obvious or prose is already coherent. Repair: test the stage exit condition explicitly and repair the earliest unmet dependency.
155. Output-shape substitution → headings/tables are mistaken for reasoning procedure. Repair: separate procedure, guardrails, exit condition, and presentation.
156. Guardrail–procedure fusion → constraints and operations are intermixed so execution order is unclear. Repair: stage contract with operations distinct from guardrails.
157. Handoff vacuum → an operator returns a useful result but nothing determines what happens next. Repair: attach the result to the active stage exit test and handoff.
158. Closure without defeater → verdict is given without naming what evidence or result would reopen it. Repair: add a concrete change condition at S8.
159. Mixed-jurisdiction collapse → empirical, normative, formal, or design subquestions are treated as one undifferentiated inquiry. Repair: separate routes/regimes at S1 and integrate only at S7.
160. Worklog-as-method → verbose progress narration is treated as evidence that control occurred. Repair: worklog only reports substantive operations; gates/tests remain independent.
161. Route lock-in → new evidence changes the nature of the problem but the original route is preserved by inertia. Repair: re-route when inquiry jurisdiction materially changes and record the reason.
162. Decorative testing → a generic counterargument or red-team paragraph is added that could not change the result. Repair: require a discriminating rival, probe, boundary condition, or falsifier.
163. Downstream polishing after upstream failure → prose is refined while object identity, framing, provenance, or operator preconditions remain wrong. Repair: return to the earliest failed stage.
