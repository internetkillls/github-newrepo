# Critical diagram translation — visual epistemology over decoration

Diagram design is an act of modeling and interpretation, not a magical translation from prose into truth. Adapt concerns in Johanna Drucker's *Humanities Approaches to Graphical Display* (2011), D'Ignazio & Klein's *Data Feminism* (2020), Hito Steyerl's *Mean Images* (2023), and Markelj & Kemper's analysis of the operational aesthetics of AI slop (2026). These works inform critique; they do not prescribe this exact template. Consult critical-sources.md.

## Pre-diagram semantic gate

1. **Object / question:** What does the learner need to distinguish, predict, do, or critique? State an observable outcome.
2. **Units and relation:** List node meanings, what edges assert (data flow, control, time, dependence, argument support, contested influence, material continuity, spatial adjacency). Do not use arrows merely for association. For a causal claim, require source, intervention, or uncertainty label.
3. **Epistemic status:** Is each node/edge measured, source-documented, convention, interpretation, hypothetical, generated, or unknown? If ambiguous, show alternatives/qualified links rather than solid arrows. A graph is not evidence of its own arrows.
4. **Type and scale:** Respect physical units, UI operator classes, temporal scales, directionality, aggregation, modality (actual/possible/normative), and the learner's tool/version. Verify labels.
5. **Exclusions:** Which actors, alternatives, values, bodies, sensory experiences, or contexts have been abstracted away? Expose omissions when they change inference.
6. **Test:** Which observation or counterexample could make a connection fail? Can a reader reconstruct the claimed relation from the picture without relying on decorative labels?

## Choose only the visual form that fits the epistemic function

- **Process/state change**: flowchart with actual inputs, typed operators, checkpoints and direction; distinguish algorithmic order from causation.
- **Software or creative-code network**: node graph with actual operator/data types, wires, units, parameter mapping and a runnable target state. Diagram does not prove runtime behavior.
- **Argument or historical dispute**: claim–evidence–warrant–objection map; show rival interpretations and textual anchors. No false definitive arrow between disputed ideas.
- **Comparative taxonomy**: matrix with explicit distinction principle; do not impose a decorative Venn diagram when intersection cannot be justified.
- **Time**: timeline only where order/duration is established; alternative chronologies or uncertain dates labeled.
- **Spatial practice/performance**: mapped positions, relative scale, orientation, performer/screen relation; annotate viewpoint, projection, audience position where meaningful.
- **Quantitative relation**: chart only with real/synthetic status, units, denominator, intervals, source, aggregation and appropriate uncertainty. Never create fabricated numbers to give a lesson gravitas.
- **Phenomenology/interpretive multiplicity**: annotated scenes, juxtaposition, layered readings, reversible relations, ambiguity boundary; avoid treating contested meanings as a single causal process.
- **No diagram**: if prose/code/source picture is already more exact or no relation needs display, use no diagram. A source photograph is not always a technical schematic.

## Diagram specification / contract (compact)

`question; object; nodes/types; edges/relation labels; direction; scale/units; evidence anchors; interpretation flags; exclusions; expected observation; counterexample; caption; alt text; available format`.

Caption MUST say what is seen and what claim is being made; distinguish documentation vs analytic schematic vs speculative interpretation. Alt text MUST identify the same instructional relations, not simply 'diagram of X'. Images sourced from web must be verified and rights respected. For artistic abstraction, intelligibility may be deliberately withheld, but explicitly locate the pedagogic purpose of ambiguity rather than calling it a technical fact.

## Example: weak vs functional diagram

Reject: `Creativity → Technology → Knowledge` with featureless circles. Arrow semantics, object and test are undefined.

For a beginner TouchDesigner lesson:
`Noise TOP (image 256×256) --image pixels--> Level TOP (image 256×256) --image pixels--> Null TOP (output preview)`.
What to see: Level TOP brightness changed from default. Verify TOP family, operator names and build version before claiming exact parameters. Use a separate dashed parameter-control edge from a CHOP when a verified mapping is actually introduced. Mark any unrun graph as a **schematic**, not an executed project.

For interpretive humanities: Instead of `Author A → Influenced → Author B` without evidence, map `Passage P → reading X (argued by source S1)` and `Passage P → reading Y (argued by source S2)`; use question mark on disputed textual connection and tell learner what quoted passage could discriminate.

## Quality and anti-slop witness

1. Remove the entire diagram. Which novel and necessary insight is lost? If nothing: remove it.
2. Strip its aesthetic styling. Are labels and relations still correct? If not: rewrite content first.
3. Reverse or remove one arrow. Would the claim change? If no: edge is not explanatory.
4. Ask an informed skeptic for a counterexample; expose ambiguity where it persists.
5. Re-express diagram as two sentences and compare. If picture adds no spatial/relational insight, present text.
6. For source images, inspect the actual picture; never claim a website image depicts an operator or production workflow merely because the search query says so.

## v0.4 UI delivery addendum
A semantically valid diagram can still be unusable. Check readable type, scale, co-located explanations, keyboard-operable detail inspection when made interactive, long text alternative, mobile reflow, reduced-motion/still-frame alternatives, and context restoration for question-by-click. Use `visual-experience-router.md` and `lesson-ui-ux-contract.md`; they do not replace the semantic/provenance gate above.
