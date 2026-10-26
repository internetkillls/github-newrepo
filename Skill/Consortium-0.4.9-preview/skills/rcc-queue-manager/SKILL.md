---
name: rcc-queue-manager
description: Use when orchestrating multiple queued RCC browser-worker messages locally, especially for idempotent dispatch, conservative completion acknowledgement, stale-lock recovery, or preventing duplicate sends after uncertain UI submission.
---

MANDATORY companion: read/apply `../rcc-execution-contract/SKILL.md`. Actual RMC/AntiSlop instructions, compiled packets, full evidence handoffs and typed closure are required; missing instructions block delegation. The official new local CLI enforces structural preflight, while semantic compliance still needs evidence review.

# RCC conservative queue manager (v0.4.2 preview)

Version 0.4.5 adds opt-in machine evidence review. Read `../../docs/AUTOMATIC_REVIEW_v0.4.5.md` before preparing `--auto-review` handoffs. Pin each job's output contract with `queue add --output-contract=<file>`. The default reviewer checks a job-bound transport receipt, independently observes the exact live response, captures all declared file bytes and hashes, and rechecks them before progression. Three failed verification attempts persist an escalation; uncertain sends never retry. REVIEWED_WITNESS still does not certify content quality or canonicalize an RCC closure. Jobs without contracts retain manual review. Queue journal adoption requires one current writer per case; see `../../docs/QUEUE_JOURNAL_v0.4.5.md`.

This skill is a **local** delivery safety supplement for Reasoning Consortium Controller. Do not imply that invoking a ChatGPT account plugin starts the user's Node/Chrome runtime or runs queued jobs. The actual CLI is `node bin/rcc-queue queue ...` from an installed, complete local RCC release; see `docs/QUEUE_MANAGER_v0.4.2.md`.

- `queue add` records a pinned prompt/attachment hash and idempotency key, **does not send**.
- `queue list` reveals unresolved jobs and any active lock.
- `queue run` is an explicitly user-launched, **one-job-only** dispatch through `rcc-consortium worker send`; it preserves C0 serial safety. Nonzero, killed or ambiguous transport never triggers automatic resend.
- Exit-zero transport becomes `TRANSPORT_RETURNED` and **must not be called answer completion**. An explicit evidence review produces `REVIEWED_WITNESS` or `NOT_SENT_CONFIRMED`, neither of which is automatically a canonical RCC closure.
- `queue recover` uses a case-specific approval and refuses to clear a possibly live lock. Stranded `DISPATCHING` becomes `UNCERTAIN`, not `PENDING`.

Retain direct RCC worker/session bindings, explicit model-level readback, the independent `rcc-completion-safety` guard and cross-worker evidence boundaries. The queue cannot guarantee at-most-once submission by agents bypassing it; require one dispatch path per case. Never claim C1 parallel generation, automatic side-effect reconciliation, or live browser completion based solely on these queue tests. Run `npm run test:queue`, `npm run test:completion`, and complete the local CDP/Windows smoke test before production claims.


Deferred runner (v0.4.3 preview): `rcc-deferred` can dispatch the next pinned job only after the previous job reaches `REVIEWED_WITNESS`. Read `skills/rcc-deferred-handoff/SKILL.md` and `docs/DEFERRED_HANDOFF_v0.4.3.md`; the queue's conservative no-resend guard remains authoritative.


## 0.4.9 reliability addendum

Apply [the reliability contract](../../docs/RELIABILITY_v0.4.9.md). Use current queue operational status; an active scheduler or existing PID alone is not an active browser worker. Exact fresh invocation receipts can establish NOT_SENT_CONFIRMED without task success or automatic retry permission. Uncertain clicked Send still requires original-turn reconciliation. Explicit unused-role provisioning never replaces a committed conversation. New structured reviews may use the explicit JSON output contract; never relax an already-sent file contract. Same-role controller reuse requires the exact proof-pinned prior delivery and unchanged bundle, not an @mention. Default five rooms can be explicitly increased while browser sends remain serial. A saved account update does not hot-patch an installed runtime or migrate existing case helpers.
