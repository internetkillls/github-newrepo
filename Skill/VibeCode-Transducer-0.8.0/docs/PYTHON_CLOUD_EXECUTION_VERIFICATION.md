# VCT 0.3.0 — Cloud-Python decision loop implementation and audit

## Corrected task contract

The user's correction requires *actual Python computation during active mathematical reasoning and data manipulation* to support ChatGPT decision-making. A static mathematical eligibility router alone is insufficient.

Implemented additive source changes:
- `skills/vibecode-engineer/runtime/cloud_math_executor.py`: actual typed Python functions, deterministic data SHA-256, result hashes, computed findings, conditional next tasks, and epistemic claim gates. No eval/exec/subprocess/network/remote repository access.
- `skills/vibecode-engineer/runtime/vct_math_cli.py`: existing combined entrypoint now ALWAYS invokes Python math evidence kernel; missing payload returns `PYTHON_COMPUTATION_REQUIRED` instead of presenting planning as computation. Old output fields remain.
- `skills/vibecode-engineer/runtime/mcp_server.py`: optional **read-only** `vibecode_math_execute` MCP tool source, for future *separately hosted* Python cloud backend; unchanged local-only security binding.
- `skills/vibecode-engineer/SKILL.md`, `references/cloud-python-decision-contract.md`: mandatory in-turn Python-tool-use policy when mathematical decisions are material, execution/revision gates and clear boundaries when unavailable.
- Added real-data examples and `tests/test_cloud_math_executor.py`.

## Local Python execution witnesses (2026-10-23)

Environment: CPython **3.13.5**, ephemeral sandbox Linux (not hosted plugin MCP).

```
python -m unittest discover -s skills/vibecode-engineer/tests -v
# 30 tests PASS, exit code 0 (15 new execution tests + 15 pre-existing mathematical-router tests)
python -m compileall -q skills/vibecode-engineer/runtime skills/vibecode-engineer/tests
# exit code 0
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_lexical.json
# PYTHON_EVIDENCE_AVAILABLE; 2 anchors, 2 censored endpoints;
# OBSERVATION_ONLY_HIGHER_CLAIM_UNVERIFIED
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_linear_inverse.json
# rank=1, nullity=1, solution_class=AFFINE_FAMILY; task to obtain additional independent constraints
```

Observed example SHA-256 payload fingerprints:
- lexical: `119fdb4c65d516cc98352dcffe8aff6cdaa3835813373a9ae8c55344e1634f93`
- inverse: `3a5fa44a51e77729d1f32ae8625b9bd9f2d9e949fb30dbfaacb8fbc8660f2c79`

## What this does NOT establish

- The **29 previous original v0.1 engineering tests** were not rerun locally in this partial overlay; unchanged original runtime/tests are retained in the account plugin on update.
- The `mcp` SDK 2.x was **not present** in the sandbox (`ImportError: No module named 'mcp'`); `mcp_server.py` syntax compilation succeeded but MCP handshake and actual ChatGPT-origin tool calls **UNVERIFIED**.
- A Plugin Creator package cannot deploy a persistent cloud Python process or guarantee that every ChatGPT host supplies a Python execution tool. When unavailable, the skill requires explicit `PYTHON_EXECUTION_UNAVAILABLE` rather than an invented receipt.
- Only five bounded observation kinds execute: lexical spans, numeric sample descriptions, declared graph edges, finite linear matrices and point-in-polygon. Other entries in mathematical registry 1–100 remain references or candidate models until independently implemented/tested.
- Lexical α/β is an independently implemented bounded measurement variant; no equivalence to the original Co-Domain JS application is claimed. Semantic, causal, statistical population and deductive proof claims remain guarded.

## Negative and close controls

Missing observations never become EXECUTED; unsupported symbolic kind never pretends to solve; lexical phrase crossing sentence boundary is not a match; missing B is censored, not zero; graph cycles reject a topological ordering; rank-deficient consistent matrix generates affine solution family; inconsistent linear system generates no solution; floating invalid numeric inputs are rejected; geometry boundary is not classified as inside/outside by default; input kind mismatch is rejected; source payload mutation is forbidden.

## Reopen criteria

A host with Python tool fails to invoke it for material math decisions; new data changes model selection; missing payload is labelled executed; an arithmetic result is represented as a semantic/casual proof; MCP tool not visible after an actual authenticated deployment; older runtime tests regress; unsupported registry entry is falsely advertised as implemented; SDK v2 differs from expected interface.
