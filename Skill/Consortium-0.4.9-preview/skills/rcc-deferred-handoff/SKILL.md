---
name: rcc-deferred-handoff
description: Use when a local Codex agent delegates a consortium queue to an independent Node runner, ends its turn to avoid model-based waiting, and optionally resumes after reviewed evidence gates without duplicate sends.
---

MANDATORY companion: read/apply `../rcc-execution-contract/SKILL.md`. Actual RMC/AntiSlop instructions, compiled packets, full evidence handoffs and typed closure are required; missing instructions block delegation. The official new local CLI enforces structural preflight, while semantic compliance still needs evidence review.

# RCC Deferred Handoff — v0.4.3-preview

This is a **Codex local runtime** supplement. ChatGPT account plugin cannot pause/resume Codex, run a local watcher, or launch browser rooms on its own. Read `../../docs/DEFERRED_HANDOFF_v0.4.3.md` before deployment. Match actual installed Node and Codex host behavior, not a supposed remote agent capability.

**On @RCC delegated work:** build minimal packet(s), enqueue with `rcc-queue queue add`, pin their IDs/hash in `rcc-deferred handoff prepare --case=... --session=<real UUID>`, verify the independent local runner has been launched from a separate terminal, and return a concise handoff receipt containing exactly the marker `HANDOFF_ACCEPTED:<nonce>`. End the Codex turn; do **not** keep model-based status polling or call blocking `handoff run` within the same turn. The trusted Stop hook arms only the matching session+marker, never all work. If the hook isn't installed/trusted, instruct the human how to arm after the turn finishes.

**While idle:** the local runner inspects `.devspace/rcc/<case>/queue.json`, dispatches **one** existing worker job at a time via the original queue gate, then waits on file changes (with periodic filesystem-only consistency checks) for a genuine operator-reviewed completion artifact. Do not call `TRANSPORT_RETURNED` or stable DOM text a completed response. Never auto-retry `UNCERTAIN`, `DISPATCHING` or ambiguous sends, and never claim the runner consumes zero tokens in its browser consultations: only Codex model polling is avoided.

**On closure:** require every pinned job to reach `REVIEWED_WITNESS` with real source artifacts, store a small summary, and expose `READY`. Default manual mode needs explicit `handoff wake --approve=WAKE-CASE` or the user's own `codex resume SESSION`; auto-resume only if prepared with `--auto-resume`. A durable one-shot `RESUME_CLAIMED` transition precedes the `codex exec resume SESSION PROMPT` external side effect. Any ambiguous wake or crash prevents an automatic second attempt. An exit-zero Codex process does not establish task correctness or canonical status.

Never reparent browser tabs, disable approval prompts, install hidden background services, ingest hidden chain-of-thought, or claim cross-platform Codex integration tested without host receipts. Source changes, invalid job identities, missing review artifacts and concurrent active sessions are blockers. The local Stop hook itself must be trusted by the user according to Codex policy.


## 0.4.9 reliability addendum

Apply [the reliability contract](../../docs/RELIABILITY_v0.4.9.md). Use current queue operational status; an active scheduler or existing PID alone is not an active browser worker. Exact fresh invocation receipts can establish NOT_SENT_CONFIRMED without task success or automatic retry permission. Uncertain clicked Send still requires original-turn reconciliation. Explicit unused-role provisioning never replaces a committed conversation. New structured reviews may use the explicit JSON output contract; never relax an already-sent file contract. Same-role controller reuse requires the exact proof-pinned prior delivery and unchanged bundle, not an @mention. Default five rooms can be explicitly increased while browser sends remain serial. A saved account update does not hot-patch an installed runtime or migrate existing case helpers.
