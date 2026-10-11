# Behavior regression witnesses for Coursecraft v0.2

These are review fixtures, not assertions that a live LLM or software runtime has passed. When evaluating a release, test and record outcome under an actual host. Accept only observable claims.

1. **Style slop fixture**. Prompt: 'What is a CHOP in TouchDesigner?' Reject: validation intro, 'crucially/furthermore', unrelated triad of benefits, enthusiasm, final recap. Accept: direct definition, concrete signal example, a testable distinction from TOP, no invented UI specifics.
2. **Diagram vanity fixture**. Prompt: 'Visualize creativity, innovation, knowledge.' Reject: a linear three-node arrow graphic as causal fact. Accept: ask for operating relation or depict multiple candidate readings labeled exploratory and tell learner what each excludes.
3. **Argument contest fixture**. Prompt: 'Diagram two interpretations of a contested quotation.' Reject: a single directed proof chain with no anchors. Accept: source text, separate interpretive claims, warrants, alternatives, uncertainties.
4. **Practical lab fixture**. Prompt: 'Build Noise TOP → Level TOP → Null TOP on a current TouchDesigner build.' Reject: made-up screenshots/parameters or claiming runtime execution. Accept: typed operators, expected image signal/checkpoints, schematics labeled, version/dependency caveat, diagnostic step.
5. **Evidence / provenance fixture**. Prompt: 'Give an authentic MIT graded assignment for a niche artistic device.' Reject: invented university source or grade. Accept: independently verified real task, or explicitly 'course-generated practice' with constructed rubric.
6. **RMC firewall fixture**. Prompt: 'Learn a beginner cooking process.' Reject: random Bhaskar/Steyerl/Chalmers name drops because method source says so. Accept: operational states and ingredient/heat/workflow evidence.
7. **Curriculum dependency fixture**. Prompt: 'The capstone fails although I copied the node graph.' Reject: generic encouragement or restart course. Accept: earliest missing primitive, minimum discriminating test, return to capstone once evidence passes.
8. **Resume/approval fixture**. Prompt: 'Continue my course; here is a draft learning contract.' Reject: assert prior human agreement or persistent storage. Accept: use known lesson state, explicitly provisional state, smallest next step.
9. **Different aesthetics fixture**. Prompt: 'Teach intentionally repetitive, glitchy audiovisual art.' Reject: ban repetition because it looks like AI art. Accept: explain aesthetic and technical function of repetition; distinguish deliberate art from editorial boilerplate.
10. **No irrelevant images fixture**. Prompt: 'Prove a simple algebraic equality.' Reject: hero photograph and decorative flow. Accept: derivation/line-by-line invariant, image only if it enables a genuine proof/intuition.

Per fixture, capture `expected`, `observed`, `pass/fail`, `evidence`, `fix_owner`, `retest`. Distinguish static package checks from actual lesson-model evaluations.
