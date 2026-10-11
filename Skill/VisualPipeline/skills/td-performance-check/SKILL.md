---
name: td-performance-check
description: "TouchDesigner performance — selective cooking, GPU vs CPU, operator-driven animation, avoiding per-frame Python. Use when cooking cost matters or profiling a network."
---

# Td Performance Check

Use this skill for its TD family or workflow, after discovering the installed TD build and available tools. Load `td-general` for shared build and verification rules. User authorization determines scope; do not impose an extra approval for already authorized reversible work.

Read [technical-guide.md](technical-guide.md) when this family or procedure is needed. Read sibling example/reference files only for the relevant pattern. API names and tool signatures in that guide are examples: confirm them against the connected server and installed TD documentation before mutation.

1. Inspect inputs, existing state, capabilities and the intended output.
2. Choose the smallest readable implementation that meets the spec; prefer built-in operators for simple effects, code for custom math, and profile expensive paths.
3. Build in the owned project area with stable names and explicit clock/parameters. Reconcile existing nodes before retrying.
4. Verify errors, connections, values and the visible output. Record actual checks separately from proposed checks.
5. For export/show delivery, hand off to `studio-visual-qa` and `studio-resolume-show`; a healthy network alone does not certify a playable loop.

This TD-derived material is attributed to Derivative Inc. and remains subject to [LICENSE-TDMCP.md](../../LICENSE-TDMCP.md). Use it in conjunction with TouchDesigner; independently authored studio target guidance covers Blender/p5.js.
