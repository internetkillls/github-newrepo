# VCT v0.8 — local-canary implementation verification

**Task:** execute the previously uploaded P00–P11 plan as far as available source/runtime and authorization permit. This document records scoped receipts from the current assistant execution, not a report of cloud deployment.

**Input baseline:** user-uploaded `plugin (4).zip`, VCT v0.7.0. The baseline archive was checked and 180 VCT and 8 AREX tests executed; both pass. New code is released as a partial overlay to preserve original modules.

**Implemented:** Signed policy control, local Git pinned snapshot, strict patch scope, before/after JSON test, durable SQLite job/event hash-chain, idempotent submission, preflight gates, separate actor gateway assertion, read-only VCT/AREX mathematical bridge. No arbitrary target code is evaluated, no branch is published, no deployment performed.

**Security note:** HMAC signatures are meaningful only when key issuance and gateway actor identity are independently secured. The packaged functions used to sign a grant are operator-side helpers, not remote MCP tools. SQLite event chain is tamper-evident under current trust boundary but not guaranteed append-only under an adversary with DB write access. Sandboxing is NOT provided by this package.

**Counterexamples required:** prior already-green baseline must never be considered fixed; dirty repo, stale commit, unsafe symlink, wrong grant scope, expired/replayed grants and protected paths deny. Mathematical counterexamples do not become permissions. Receipts and exact raw commands are saved in the attached local execution artifact.

**Remaining debt:** MCP SDK absent in the runtime used; therefore HTTP transport, real ChatGPT connection, worker isolation, real target pytest/unittest execution, GitHub PR/CI, environment deployment/rollback and production behavior are UNVERIFIED / NOT IMPLEMENTED.

## Executed integration receipt

- Input plugin zip: `plugin (4).zip`; v0.7.0 baseline.
- Legacy VCT: `python -m unittest discover -s plugin_full/skills/vibecode-engineer/tests -v` → 180 PASS.
- Legacy AREX: `python -m unittest discover -s plugin_full/skills/arex-repository-intelligence/tests -v` → 8 PASS.
- Combined updated source: `python -m unittest discover -s staging_full/skills/vibecode-engineer/tests -v` → 225 PASS (180 legacy + 45 new).
- AREX against updated package → 8 PASS.
- CLI canary integration script (local operator-owned synthetic Git repo): signed `submit` → grant verification → pinned Git archive snapshot → red before → green after → chained event/receipt; source unchanged.
- VCT mathematical bridge invoked Python `heuristic_dispatcher.dispatch()` with existing Euler refinement fixture, returned `CONTRADICTED/REVISE_PREMISE`, and cannot mint write authorization.
- MCP transport v2 live run: NOT EXECUTED (SDK absent). Static `py_compile` only.
- Source repository real hosted identity, full target test suite, PR, CI, cloud tunnel, staging and production: NOT EXECUTED.

See `CANARY_EXECUTION_RECEIPT.json` in the separate user-facing execution package.

Observed demo source Git commit: `4f27663f4f3795c443164a578f325f7af64f6afa`. Receipt hash: `cbe1fe39ecc1eb5211e03ae363aefdbefa99753f048b0f098a01b0c9ed81222b`. Ledger integrity and source unchanged both verified.
