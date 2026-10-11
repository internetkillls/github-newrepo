---
name: td-network-cleanup
description: "Organize TD positions, sizes, colors and owned annotations without changing functional topology. Use after builds or for an explicit layout cleanup."
---

# Clean layout without changing behavior

Read `td-node-layout`; survey actual positions, sizes, connections and annotations. Preserve manual annotations and functional operators. Update only annotations recorded as owned by this workflow, using stable IDs. Create a missing owned annotation only when the tools support it; do not delete all annotations.

Group related operators and calculate bounds with room for headers. Batch reposition through dedicated tools. Check containment, spacing and overlapping boxes; use body text for explanations, short titles, restrained colors.

Layout cleanup does not change signal parameters, create select operators, replace long wires, alter flags controlling cooking, or rewire topology. A requested structural refactor is a separate change with before/after topology and `td-review-network` validation.

Run cleanup twice: no annotation multiplication or functional change. Record a topology/parameter comparison alongside a readable layout preview. Use live tool signatures for annotation properties and parameters.

TD-derived adaptation attributed to Derivative Inc.; [license](../../LICENSE-TDMCP.md).
