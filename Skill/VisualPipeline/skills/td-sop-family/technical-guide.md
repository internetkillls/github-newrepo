# SOP Networks

CPU-based geometry operators. SOPs are the traditional geometry family — procedural modeling, deformation, boolean operations. For GPU-accelerated point work, prefer POPs (see td-pop-family skill).

## When to Use SOPs vs POPs

- **Choose SOPs or POPs from capability and workload** — check TD build and GPU support; SOPs suit small CPU geometry, POPs suit supported high-volume point work after profiling
- **SOP examples**: boolean operations, UV work, small geometry, and readable prototypes; a POP equivalent is not sufficient reason to replace working SOPs
- For large parametric point fields on supported builds, consider gridPOP → glslPOP; compare with simpler SOP prototypes
- **Geometry COMP source** — select SOP/POP from supported operators, required output and measured cost

## Common Generators

- `gridSOP` — structured grid
- `sphereSOP` — sphere
- `boxSOP` — box
- `tubeSOP` — tube/cylinder
- `circleSOP` — circle/arc/ellipse
- `lineSOP` — line
- `curveSOP` — NURBS/Bezier curves
- `textSOP` — 3D text geometry
- `scriptSOP` — Python-generated geometry

## Common Processing

- `transformSOP` — translate/rotate/scale
- `noiseSOP` — noise displacement
- `facetSOP` — cusp, consolidate, compute normals
- `convertSOP` — between polygon/mesh/NURBS
- `booleanSOP` — union/intersect/subtract
- `copySOP` — copy to template points
- `deleteSOP` — remove primitives/points
- `mergeSOP` — combine geometry
- `switchSOP` — select between inputs
- `nullSOP` — chain endpoint

## SOP to POP Conversion

`soptoPOP` converts SOP geometry into the POP family for GPU processing.

## Pitfalls

- **CPU-bound** — SOPs run on CPU, not GPU. Large meshes are slow
- **Using SOPs where POPs exist** — sphereSOP inside geometryCOMP won't render properly with POP instancing
