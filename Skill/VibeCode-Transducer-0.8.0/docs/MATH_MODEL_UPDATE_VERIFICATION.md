# VCT 0.2.0 mathematical model router verification — 2026-10-23

This update is additive and overlays current USER/PRIVATE plugin release `pluginrel_6adb5459214c8191b2ec78ee7a42b566`. The existing `vibe_transducer.py`, `local_apply.py`, `mcp_server.py`, original examples, Atlas registry, and donor mapping are **unchanged and retained**. No plugin audience, App/MCP connection, defaultPrompt string/array, identity, or existing source version is rewritten apart from the plugin manifest/skill version.

## Witnesses

Local CPython 3.13 test execution for **new files only**:

```
python -m unittest discover -s skills/vibecode-engineer/tests -v
```

The added `test_math_model_router.py` contains 15 unit tests covering: full 1–100 crosswalk and proposed 100th entry, namespaced mathematical IDs, lexical bounded feature acceptance, unsupported semantic promotion, conditionally activated statistical/causal/inverse branches, absence of dimensional-analysis promotion without physical quantity matrix, DAG missing-node and cycle rejection, owner-approval + checkout gate for T16, schema flags, non-executed T17, and read-only combined CLI.

Older 29-test suite was **not rerun locally before package upload** because the existing full plugin archive was not retrievable into the local sandbox. Existing runtime functions and tests were not edited. After tool saving, server-side source read-back is required to verify release overlay and retained modules.

## Important limits

- `math_model_router.py` emits *operator eligibility plans*, not measured α/β outputs, statistical estimators, causal effects, theorem proofs, or runnable DSL-generated implementations.
- The selection is a bounded subset of the 100 crosswalk entries; 99 originate in a previous review, and MATH-100 is a separate flagged candidate. The 50 Atlas methods are distinct; only 034, 055, and 058 had narrow v0.1 implementations.
- A user-supplied `features.<flag>=true` is a declaration, not an independent witness. Engine does not parse Co-Domain `index.html` or infer rhetorical intent.
- `math_task_graph.yaml` remains a conceptual 18-task graph; the Python conditional task graph is a smaller executable planning schema. It does not compile MDE/KRR artifacts.
- `vct_math_cli.py` combined CLI is optional and separate from the original CLI; it will call `vibe_transducer.transduce` only when an `engineering_spec` is supplied.
- No live MCP handshake, GitHub repo patch, connected user host runtime, parser integration or actual application behavior was verified.

## Reopen conditions

Invalid release/preservation comparison; import error in combined CLI with engineering spec; actual runtime regression in prior 29 tests; any emitted claim above `METHOD_ELIGIBILITY_ONLY`; T16 issued without both checkout and approval; a false math registry ID; math/Atlas ID conflation; dynamic semantics promoted from lexical counts; trial falsely advertised as full algorithm execution. In each case repair earliest premise and repeat discriminating test plus near-miss control.
