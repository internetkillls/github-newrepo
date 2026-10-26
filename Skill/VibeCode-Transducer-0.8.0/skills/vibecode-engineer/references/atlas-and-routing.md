# Atlas-to-VibeCoding transduction: task-indexed operators

Source scope: user-uploaded lateral atlas batches 004/005/006/007/008, units 031–080. This registry is a **reference inventory**, not an executable library. Unit records carry source file names, SHA-256 hashes, and original links in `atlas_registry.json`. Historical KTA audit claims 61 units 020–080, but units 020–030 were not supplied as batch source here. Do not invent them.

| Coding failure signature or objective | Atlas method | Input & output | Local runtime status | Mandatory non-claim |
|---|---|---|---|---|
| Candidate donor source retrieval | 034 Jaccard | Source-token sets → candidate similarity | **RUN** only when target and distinct donor files supplied | Score ≠ behavioral equivalence or functional donor |
| Very large code candidate universe | 045 MinHash | Set signatures → approximate overlap | PLAN_ONLY | No MinHash implementation shipped |
| Declared file/dependency order | 058 Topological Sorting | Directed prerequisite pairs → order or cycle | **RUN** with supplied edges | Does not resolve JS imports, runtime ownership, or safe migration |
| Code constraints & refactor compatibility | 050 AC-3 | Typed domains/binary constraints → arc-consistency | PLAN_ONLY | Local arc consistency ≠ global satisfiability; no bundled AC-3 here |
| Benchmarks with extreme values | 055 MAD | Numeric values → median and raw MAD | **RUN** when samples supplied | Outlier threshold, regressions and causes require independent tests |
| Event choreography | 040 Allen interval relations | Start/end intervals → qualitative relations | PLAN_ONLY; a *separate* basic timestamp trace checker exists | Timestamps and event order ≠ external commit or queue completion |
| Baseline drift in response latency | 036 CUSUM | Measurements + baseline → accumulation | PLAN_ONLY | Alarm ≠ root cause |
| Repeated failure/performance patterns | 041 Matrix Profile | Time-series subsequences → motifs/discords | PLAN_ONLY | Discord ≠ error diagnosis |
| Performance distribution drift | 068 Wasserstein-1 | 1D distributions → distance | PLAN_ONLY | Distance ≠ product impact or statistical significance |
| Multiple significant regression tests | 069 Benjamini–Hochberg | p-values → FDR procedure | PLAN_ONLY | No statistical test execution bundled |
| Async/event log structure | 052 ACF / 078 Permutation Entropy | numeric, evenly sampled traces → regularities | PLAN_ONLY | No causal attribution |
| Ownership hotspot in dependency graph | 060 Articulation points / 035 k-core | graph → candidate fragile nodes/core | PLAN_ONLY | Structural prominence ≠ architecture responsibility |
| JSON/media upload safety | 039 Magic Bytes | byte header → format candidate | PLAN_ONLY | Signature ≠ full parser validity or file safety |
| Incremental asset sync | 047 FastCDC | byte content → stable chunks | PLAN_ONLY | Shared chunks ≠ entire content integrity |
| Visual regression & screenshot shifts | 031 pHash / 072 phase cross-correlation | images → similarity or shift | PLAN_ONLY | Pixel similarity ≠ UX functional correctness |
| Canvas hitboxes | 065 STRtree / 037 point-in-polygon | 2D geometry → candidate/intersection | PLAN_ONLY | Bounding-box candidate ≠ true shape hit |
| Complex UI matching | 076 Linear Sum Assignment | cost matrix → optimal one-to-one matching | PLAN_ONLY | Optimality only relative to supplied costs |
| Ranking implementation alternatives | 046 Pareto / 077 Borda | typed objectives or rankings → alternatives | PLAN_ONLY | Ranking rules ≠ acceptance or preference truth |

Prefer ordinary regression tests when they more directly answer the issue. Do not load mathematical machinery because it sounds sophisticated. Select an operator only when its object model and measured quantity match a necessary aspect of the user's task.

For each transfer, record source domain, target data type, representation mapping, loss, candidate transfer warrant and counterexample. Example: a Jaccard score over lexical function names may prioritize inspection, but it **drops order, type binding, mutation, async happens-before and invariants**; for actual donor selection require behavioral tests and interface scrutiny. An instruction to fix a UI selection bug cannot be discharged by a lexical similarity score alone.

`RUN` in static report means a narrow implemented operation was performed on supplied inputs. `PLAN_ONLY` is a design suggestion. Future optional libraries (Tree-sitter, ast-grep, STUMPY, SciPy) must be actually installed, versioned and tested before status changes.
