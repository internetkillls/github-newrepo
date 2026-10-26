# RCC v0.3.0 — corrected distribution validation (2026-10-13)

**Release candidate:** 0.3.0 (updated packaging, local transport initialization and worker-binding guards). No real Chrome session or ChatGPT web UI was driven in this sandbox.

## Corrected defects

1. The vendored `chatgpt-pro init` previously read an **unpackaged** `.codex/skills/chatgpt-pro-line/SKILL.md`, leading to `ENOENT` and false portability claims. A dedicated bundled runtime skill now lives at `runtime/chatgpt-pro-line/skills/chatgpt-pro-line/SKILL.md`, and `init` copies it to the user project's expected path only on explicit invocation.
2. `workers spawn` previously returned `BOUND` with a null CDP target. It now requires an actual target ID, persists `PROVISIONING` **before** attempting external tab creation, and refuses blind retry of an ambiguous result. `worker send/read` requires a verified BOUND state.
3. RCC state writes are now atomic (using the vendored `writeJsonAtomic`, including its Windows-compatible fsync mode). Reserved `.`/`..` case and role identifiers are neutralized. CSV export neutralizes spreadsheet formulas.
4. Removed local `.devspace/state/` material containing sandbox-specific absolute paths from the distributed package. Aligned version text in skill, CLI, README, and package. Included a target-specific historical note for the earlier blocked backend identity.

## Test evidence

- **14/14 distribution checks PASS** with `npm run test:distribution`. This includes synthetic positive and negative worker binding tests, flag forwarding, initialization, room lifecycle, IR transduction, loopback server and transport guards.
- **25/28 vendored upstream selftests PASS** when run from `runtime/chatgpt-pro-line/` checkout location.
- The remaining **3 FAIL** are *upstream source checkout / marketplace packaging assertions*: `package-surface-selftest.mjs`, `plugin-package-selftest.mjs`, and `v1-readiness-selftest.mjs`. They require upstream files (`.agents/plugins/marketplace.json`, `.codex/config.toml`, upstream README and package metadata), which are intentionally **not** bundled as a second plugin/marketplace. They are not valid acceptance tests for the vendored transport artifact. Their guarantees are not claimed as verified in this distribution.

## Deferred real-host acceptance

- Live CDP/Chrome connection (including Windows/macOS), room creation, model/effort UI readback, upload readiness, and multi-tab sender behavior remain unverified. Run dedicated-profile smoke tests on the real device before claiming operational browser automation.
- Cloud-account plugin **only provides routing policy/skills**. Plugin upload/readback proves distribution, not local execution.
- Historical parser error on `plugins_6ac4c3fb114881919f3f0a9c9ddf5706` (0.2.0) is a separate backend issue, not repaired by this candidate. The v0.2.3 source accessible plugin `plugins_6ac4cc829a748191a2531c47e7be2838` is the upgrade target; never create a third RCC identity as a workaround.
