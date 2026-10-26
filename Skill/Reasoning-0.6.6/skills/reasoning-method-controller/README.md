# Reasoning Method Controller v0.6.0

v0.6.0 changes the controller's top-level abstraction from **operator-first dispatch** to **route → stage → operator → exit test → repair**.

The change borrows a useful architectural lesson from explicit reasoning protocols: a method is easier to execute when procedure, guardrails, and completion conditions are separated. RMC keeps its broader generality by making the stages conditional rather than forcing one fixed protocol on every task.

Core changes:
- adds seven route families: reconstruct/audit, research/discovery, design/debug, compare/decide, formalize/measure, theory/concept, and mixed;
- adds a canonical S0–S9 stage machine with entry gates, operations, guardrails, exit tests, and handoffs;
- makes `operator-index.md` a **stage-local subrouter** selected by failure signature rather than the whole workflow;
- allows a stage to be skipped only when its exit condition is already satisfied;
- adds explicit discriminating-test/probe behavior before closure;
- adds repair-to-earliest-failed-dependency rather than polishing downstream output;
- adds a closure change-condition: what specific evidence/result would reopen or flip the conclusion;
- keeps visible worklogs as observability over the method, never as private chain-of-thought;
- preserves semantic descent, orientation-bundle/umbrella mapping, source provenance, transport validity, interaction discipline, world-remap, formalization gates, dual closure, and APA controls.

Detailed runtime control lives in `references/stage-machine.md`.
