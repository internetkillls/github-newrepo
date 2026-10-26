# VCT v0.5.0 — AREX integration verification

## Tested in this build environment (local Python)

Command: `python -m unittest discover -s skills/arex-repository-intelligence/tests -v`.

Test cases: 8 (`snapshot_counts`, `exact_repository`, `name_case_and_alias`, `no_forced_route`, `area_filter`, `empty_query`, `source_not_executed`, `ambiguous_queries_are_not_proof`). Result at package build: 8 passed, 0 failed. Tests cover router behavior and safe one-file ZIP inspection, not upstream package execution. The VCT v0.4 runtime is preserved by overlay (rather than rewritten); its prior regression suite has not been re-executed in this isolated build unless its source is separately mounted.

Provenance cross-check: 1,000 repository IDs unique; 2,209 assignments; 20 areas; 178 families. The `repositories.jsonl`, `assignments.jsonl` and `taxonomy.json` source digests were recomputed in Python and compared to the upstream `build-metadata.json`. New packaged metadata is a derived compact index, not byte-for-byte original JSONL files.

## Not verified and not claimed

No independent quality audit of 5,000+ AREX operating skills; no DisCo TypeScript/npm test run; no LIVE MCP endpoint; no target repository clone/build; no access to the user's application source; no dependency auto-install; no code patch; no proof that future donor recommendations fix user bugs; no host-level activation test before this plugin update is loaded by the ChatGPT host. The source archive's original successful benchmark figures are author claims, not reproduced test outcomes.

## Requirements for future acceptance

Verify plugin readback contains v0.5.0 manifest and new skill files, confirm original `vibecode-engineer` persists and its runtime is preserved, execute a cross-skill end-to-end task with actual target repo source and a fail-before/pass-after test plus negative control, and check licenses/runtime prereqs on the chosen repo before any code import.
