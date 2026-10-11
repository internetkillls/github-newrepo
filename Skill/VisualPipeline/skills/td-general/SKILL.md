---
name: td-general
description: "Core TouchDesigner conventions, capability discovery and skill routing. Use first for TD planning, builds, reviews or TDMCP work."
---

# TouchDesigner shared workflow

Support both learning and production. For exploration, use small visible steps and explain their effect. For an authorized build, implement the agreed outcome in bounded batches and verify each batch; do not stop short of completion merely to force more conversation. Ask only for material missing information or actions outside the authorized scope.

## Capability and runtime gate
Discover the connected tools, TouchDesigner build, project root and current errors. The package contains instructions, not a TDMCP server. Tool names below describe expected capabilities; use actual discovered signatures. If no live tools exist, produce a reviewable build plan or source artifact and report the runtime as unverified. Do not invent live nodes or renders.

Choose built-in operators for simple readable effects; use GLSL/Python for custom logic or a measured advantage. POPs require compatible build/GPU support. For deterministic loops drive an explicit frame index or phase; wall-clock/audio/feedback requires a separate reproducibility contract. Avoid automatic viewer activation on every node: enable only needed viewers and measure cooking impact.

## Build SOP
1. Scout: project information, operators, connections and errors; derive the root from live state.
2. Plan: load `td-build-planning` for multiple operators, relevant family skills, and `td-node-layout` for placement. Persist stable IDs, types, parameters and dependencies.
3. Build: inspect existing objects, create only missing owned nodes, update intended state, and verify after each dependency stage. A build call is not an atomic transaction.
4. Review: `td-review-network`, with errors, topology, runtime values and visible output.
5. Cleanup: `td-network-cleanup`, limited to layout/owned annotations. Review again if a separate refactor changes logic.
6. Export: `studio-visual-qa` and `studio-resolume-show` for loop, seam, color, codec and venue playback checks.

## Skills by intent
Planning: `td-build-planning`; layout: `td-node-layout`; collaboration: `td-colab`; implementation choice: `td-working-mode`.
Image/render: `td-top-family`; control/audio: `td-chop-family`; GPU points: `td-pop-family`; CPU geometry: `td-sop-family`; tables/callbacks: `td-dat-family`; materials: `td-mat-family`; custom shaders: `td-glsl-shaders`.
Modules: `td-comp-architecture`; Python lifecycle: `td-python-extension`; instancing: `td-geometry-instancing`; data UI: `td-lister-ui`.
Verification: `td-review-network`, `td-performance-check`, `td-network-cleanup`.

## Fragile details
- Query live operator help for parameter names and menu tokens rather than guessing. For unfamiliar Python APIs use installed build documentation.
- Prefer named null endpoints and explicit in/out operators. Set connector order where supported.
- Relative asset paths are portable inside the project; use absolute paths for filesystem inspection and normalize bundled references before delivery. Use parent shortcuts for cross-COMP expressions when appropriate.
- Verify requested names: TD may append suffixes on collisions. Never overwrite or delete an unowned node to resolve a name conflict.
- Explicitly set a code DAT's language. File sync and extension reload depend on edit route/build; verify reload and preserve required state.
- HTTP/heavy work in callbacks blocks the cook loop. Delaying `run()` does not move execution off the TD thread; use a documented asynchronous operator or external worker and apply TD mutations in its supported context.
- Return errors before opening previews; numerical samples complement a visible preview when composition matters.

Read [technical-guide.md](technical-guide.md) only for remaining naming/API details. The operational rules here supersede older recommendations in source material. TD-derived material: Derivative Inc.; [license](../../LICENSE-TDMCP.md).
