# VCT v0.8 — signed-policy autonomy, bounded canary and trust gates

## Owner and goal
This reference derives from user-provided `VCT_Autonomous_Patcher_Implementation_Plan(1).md` (P00–P11). It adds a **tested local canary** as a first execution milestone. It is not production release authorization. RMC's inference status is separate from permission to mutate.

## Operations that actually exist

- `runtime/autopatcher_core.py`: inspect a pinned commit of an **operator-registered local Git repository**, require clean HEAD, reject linked/special archive entries, materialize regular files in ephemeral directory, and run a narrowly typed **non-executing JSON fixture** on the snapshot before and after a SHA-bound replacement.
- `runtime/autopatcher_control.py`: persist jobs/event-chain and receipts in SQLite, enforce gateway HMAC assertions for submit/read/cancel, and require a second independently signed patch grant for work in the ephemeral snapshot.
- `runtime/autopatcher_math_bridge.py`: delegate mathematical admissibility to existing v0.7 Python `heuristic_dispatcher`, preserving model-class refutation, underdetermination, conditional refinement and AREX candidate-only states. Mathematical output **does not sign grants**.
- `runtime/autopatcher_cli.py`: operator-only CLI. Gateway/Patch signing keys are supplied outside the package via environment. The CLI does **not** mint either authority.
- Existing `local_apply.py` is legacy and MUST NOT be described as a trusted checkout or fail-before proof, even though it retains its original scoped uses.

## Invariant and evidence ceiling
A bug-fix claim requires an actual relevant baseline failure and a later pass on the **same immutable test identity**, with comparable environment and no regression. The canary only enforces this on an operator-declared JSON equality predicate, not on target code. A green baseline returns `BASELINE_NOT_REPRODUCED`. The positive case returns `CANARY_RED_GREEN`, never `PATCH_TESTED_IN_ISOLATION`. A one-test canary must never be promoted into passing the full project suite or a deployment.

The policy grant is signed with an operator-owned HMAC key and binds job, repo identifier, original commit SHA, exact diff digest, allowed paths, expiry, operation and nonce. A trusted gateway signature independently binds actor, repo, requested action and payload hash. Neither issuer is an MCP tool. A user-provided `approved` boolean is not an authorization credential.

The Git identity checked here is **local registry path + commit**; remote provider repository ID, signed commits and installation ownership are **not independently established**. The ephemeral source is created from `git archive` rather than a production `git worktree`; this avoids checkout filters/hooks but does not provide a production sandbox. Target code is never imported or executed by the canary.

The SQLite chain detects simple modifications under the assumption the original trusted signing/storage environment and its canonical serializer are intact; it is not a remote append-only/WORM audit ledger. The job can be read after restart, but running worker leases and in-progress resumability are not yet implemented.

## Ready/remaining milestones
- P00 source inspected and old baseline tested on uploaded zip: **locally verified**.
- P01 operator policy and signed grants: **canary implemented + tested**; not a remote identity provider.
- P02 durable jobs and retrieval: **local SQLite implemented + tested**; no MCP v2 host handshake.
- P03 Git source verification and ephemeral snapshot: **synthetic local Git tested**; not container sandbox or provider attestation.
- P04 red baseline fixture: **implemented + tested** for JSON predicate only.
- P05 VCT/AREX math bridge: **read-only Python integration tested**; real donor code remains unverified.
- P06 isolated exact patch: **canary JSON fixture implemented**; no general test-runner or production patch.
- P07 target suite: **not implemented**; requires independent container/microVM isolation, per-job immutable runner attestation, limits, scoped credentials, and signed test receipts.
- P08 Git push/PR/CI: **not implemented**; requires GitHub App installation grant and protected branch checks.
- P09 staging and rollback: **not implemented**; requires CI runner and environment attestation.
- P10 production: **explicitly DENIED**, pending separate authorization.
- P11 plugin packaging: local package tested; live host observation and deployed MCP not yet verified.

## Next separate security implementation
1. Provision an independent authenticated gateway to mint scoped assertions with trusted actor identity. Do not place signing key inside model prompts or plugin assets.
2. Run official MCP Python SDK v2 in an isolated service, provision private authenticated transport and test real tool discovery/roundtrip; the packaged `mcp_server.py` only adds a **read-only capabilities** tool.
3. Provision disposable sandbox worker (container/microVM, egress deny, no secrets, CPU/memory/time quotas). Bind worker attestation to source SHA, tests, environment image digest, test spec and result receipt. The fixed JSON fixture does not substitute for this.
4. Add worker lease, heartbeats, crash reconciliation, idempotent external side-effect protocol and quarantine on partial failures.
5. Add GitHub App per-installation permissions, PR lifecycle tied to head SHA, independent CI, staging deploy/canary and separately authorized rollback.

**References for framework behavior:** https://py.sdk.modelcontextprotocol.io/run/ (MCP SDK v2 streamable-http), https://docs.github.com/en/rest/pulls/pulls (GitHub PR permission). Neither reference provides an observed live connection here.
