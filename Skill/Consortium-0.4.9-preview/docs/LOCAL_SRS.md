# RCC local-first minimal SRS (build scope)

| ID | Requirement | Acceptance witness |
| --- | --- | --- |
| L-01 | Exact worktree root + gitDir + HEAD | Inspect two separate Git worktrees |
| L-02 | Stable machine-readable Git status | Parse porcelain-v2 -z including renames/untracked filenames |
| L-03 | Context acquisition decision, not duplicated flatten | Native-by-default plan; portable task and complete AIF paths |
| L-04 | External flattener as explicit optional adapter | Preview without execution, output outside repository, explicit --execute |
| L-05 | Local Git change requires approval and preimage match | Reject dirty target, stale plan, wrong approval |
| L-06 | No implicit destructive Git mutations | No stage, commit, reset, file deletion or rename |
| L-07 | No silent change to existing browser behavior | v0.3 distribution suite passes |
| L-08 | Honest evidence boundaries | Receipts do not claim compilation or semantic correctness |

Deferred: MCP tools, browser extension, AST index, database, token profiling, concurrent source mutation guarantees, support for advanced Git binary/rename patches.
