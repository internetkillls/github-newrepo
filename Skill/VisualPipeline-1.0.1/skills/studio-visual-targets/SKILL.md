---
name: studio-visual-targets
description: "Translate a shared visual specification into TouchDesigner, Blender or p5.js implementation plans/source while preserving coordinates, timing and declared fidelity. Use for engine branching or target compilation."
---

# Compile the visual contract into targets

Read the project spec and [references/adapters.md](references/adapters.md). First classify the recipe: shared analytic geometry, shader field, simulation, 3D scene or input-reactive behavior. A shared specification does not make arbitrary engine projects interchangeable.

Create a target manifest with contract hash, recipe/adapter versions, engine build, assets, seed, frame interval, coordinate/color interpretation, capabilities and unresolved checks. The offline `studio-visual-pipeline` planner can generate this manifest. Implement each adapter only after its relevant APIs have been checked against installed/current official documentation.

For the pilot, read [references/perimeter-ribbons.md](references/perimeter-ribbons.md). It specifies an independently authored analytic ribbon field over four cube faces, including D-to-A and time-periodic closure. Use frame 0..N-1 for export and frame N only as a closure probe. Pixel-center edge samples need not be identical to each other; test the shared analytic boundary and rendered continuity separately.

- TD: use `td-general`, relevant family skills and version-matched shader boilerplate; expose frame/phase, dimensions and recipe controls. Apply TD-derived material only to TD.
- Blender: independently build geometry/camera/material/source from the studio contract. Use explicit frame/time settings, supported rendering API and deliberate color management. Choose 2D orthographic output for semantic parity; 3D lighting requires a new declared rendition.
- p5.js: independently author a sketch with explicit frame index, fixed pixel density, explicit canvas dimensions and offline export/capture procedure. A real-time browser preview is not a verified constant-rate video export.

Compare silhouettes, composition, palette intent, motion period and seams at matching phases. Declare antialiasing/color/render differences; do not promise pixel parity without a measured test. Live audio, stateful physics and feedback require captured inputs/warmup and a separate loop strategy.

Deliver editable source, preview, manifest and execution evidence. If a target cannot run here, deliver its source/plan and report that specific runtime as pending.
