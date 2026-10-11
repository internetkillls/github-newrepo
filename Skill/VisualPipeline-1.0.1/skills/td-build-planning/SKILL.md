---
name: td-build-planning
description: "Plan and reconcile TouchDesigner builds with stable ownership, dependency stages, retry recovery and output checks. Use before multi-operator builds."
---

# Plan a repeatable TD build

1. Inspect project root, build/capabilities, operators, connections and errors. Save a project snapshot before changing an existing network.
2. Persist a build manifest: project/build ID, owned parent path, stable logical node ID/name, operator type, parameter values, connection/input order, source hashes and previous accepted output.
3. Query live operator help; allocate positions from measured dimensions. Build inner COMP input/output nodes before connecting the outer COMP. Choose explicit frame/phase for loop exports.
4. Reconcile: matching owned name/type -> update intended differences; absent -> create; unowned or wrong type -> report a collision and choose a separate owned location. Never accept TD's numbered suffix as successful reconciliation.
5. Execute dependency stages in bounded batches. Validate each stage before advancing. Use a server batch tool only if available; it does not guarantee rollback.
6. After a partial failure inspect actual persisted state. Reconcile the manifest before retry. Restore the previous saved project or remove only newly created owned objects whose creation was recorded. Limit unchanged retries to two, then diagnose a new cause or report the actual blocker.
7. Verify errors, topology and output, then run layout cleanup. Re-run the same spec once: no duplicate nodes, orphan files or changed output contract. Record changed parameters separately from layout edits.
8. Finish with editable exposed parameters, relative bundled assets, stable outputs, manifest and runtime evidence. Export/show QA is separate.

Build identity covers canonical spec, asset hashes, template/adapter versions and engine build. Runtime nondeterminism and hardware behavior still need empirical checks. Read [technical-guide.md](technical-guide.md) only for additional operator details; these retry rules govern this package.

TD-derived adaptation attributed to Derivative Inc.; [license](../../LICENSE-TDMCP.md).
