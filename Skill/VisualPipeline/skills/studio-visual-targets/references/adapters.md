# Adapter contract
Shared: recipe semantics, frame/phase, normalized coordinates, seed/asset identity, parameters, safe region, palette intent and composition.
Target-specific: node/object IDs, API/build, shader language/boilerplate, sampling, camera/material model, color transform, raster dimensions and export API.
TD analytic field: GLSL TOP with explicit uPhase; compute face=floor(x*4), u=fract(x*4) for linear atlas, v from pixel coordinates; for grid explicitly decode tile index. Read the installed TD GLSL docs before uniforms/sampler boilerplate. Do not reuse TD-specific APIs in Blender/p5 code.
Blender: for a 2D ribbon rendition, evaluate analytic centerlines as curves/meshes with orthographic camera and opaque background; distinguish emission palette from lit PBR. Explicitly set frames, resolution and color-management settings verified against installed API. Curves require sample-density QA at corners.
p5.js: explicit density=1, canvas or per-face dimensions, frame index/phase and deterministic math; transform bottom-up v to canvas-down y. Canvas color/alpha behavior must be recorded. Capture numbered frames without browser-time dependence, then encode and inspect actual video metadata.
Declare output fidelity as semantic_sibling until measured equivalence supports a stricter promise. A format bridge is not a universal compiler; implement and test recipes one at a time.
Primary docs: https://docs.derivative.ca/GLSL_TOP ; https://docs.blender.org/api/current/ ; https://p5js.org/reference/ . Fetch version-matched pages before implementation.
