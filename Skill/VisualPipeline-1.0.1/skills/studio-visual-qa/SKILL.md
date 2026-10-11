---
name: studio-visual-qa
description: "Verify generated visual specifications, seamless cube loops, exported media and catalog provenance. Use before presenting a portfolio clip or handing content to Resolume."
---

# Evidence for a deliverable

Read [references/acceptance.md](references/acceptance.md). Keep four levels distinct: contract valid, source built, render checked, venue playback accepted. A static validator proves only the first level plus its explicitly reported mathematical checks.

1. Validate dimensions, fps, integer frame count, clock/seed, parameter bounds, asset references and declared coordinate/color model.
2. Repeat the build with identical inputs; compare owned state and manifests. No suffix nodes, missing assets or uncontrolled seed drift.
3. Inspect first/middle/last frames and a played loop, including exact face seams A-B/B-C/C-D/D-A. Probe analytic frame N against frame 0, export only 0..N-1, then inspect the last-to-first playback transition.
4. Probe actual media metadata and decode representative frames: width/height, fps, duration/frame count, codec/container, alpha and color/range. Compare all four faces' transport phase. Numerical checks complement viewing.
5. Relocate the delivery folder and reopen with relative assets. Test the encoded master in Resolume with the actual mapping and hardware. Record sustained playback/storage/thermal behavior for the intended show duration; a short preview cannot certify six hours.
6. Record theme/session IDs, spec/asset/adapter hashes, tools/builds, actual results, known limitations and output paths. Use the pipeline helper catalog for a small local SQLite index; keep JSON/source/media as the portable truth.

Fail the relevant stage on a material mismatch and repair only that stage's dependencies. Do not label an unrendered plan production-ready. Preserve an accepted fallback loop for show operation.
