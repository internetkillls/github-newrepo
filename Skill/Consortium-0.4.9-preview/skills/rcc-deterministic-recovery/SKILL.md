---
name: rcc-deterministic-recovery
description: Diagnose RCC connection loss and stale browser bindings using bounded local observation before escalating or retrying a worker action.
---

# Deterministic recovery — 0.4.6 local preview

Use the selected release's local runtime. Account invocation does not start a process or provide PC access. Read `../../docs/RECOVERY_v0.4.4.md` before running recovery diagnostics.

Run `node bin/rcc-recovery inspect --state=<existing-case-state.json> --output=<new-report.json>` from the plugin source. This is metadata observation with up to three bounded connection attempts; it never sends, opens tabs, restarts Chrome, modifies bindings or clears locks. Use the authorized loopback port explicitly when it differs from 9222.

Treat MATCHED_HINT_VERIFIED as metadata identity only. A UNIQUE_REBIND_CANDIDATE still requires exact conversation/turn verification before changing a worker binding. AMBIGUOUS, missing conversation references and absent conversations do not authorize replacement with a blank chat.

The CDP transport now rejects pending requests on disconnect/error/caller close, and has bounded connection/command deadlines with optional cancellation. These errors never establish that the remote action did not execute. Do not automatically resend messages after command timeout, cancellation, missing echo or disconnect.

Before escalating, perform available safe liveness, discovery and readiness observations. Preserve the resulting report with the task/job identity, last verified checkpoint, expected/observed state, failure signature, attempts, evidence references, forbidden repetitions and exact decision needed. Persist locally when no authorized ChatGPT route is available. Do not claim an emergency message was delivered without acknowledgment.

The inspection CLI remains read-only. Version 0.4.5 additionally provides a queue commit journal and opt-in machine response/output review; these do not supply automatic browser-binding adoption, a general action journal, Windows URI activation, browser restart supervision, or emergency diagnostic delivery. Keep the distinct queue/completion evidence gates; never equate transport return with task completion.

Version 0.4.5 extension: queue-specific hash-linked committed snapshots and a durable diagnostic outbox. See `../../docs/QUEUE_JOURNAL_v0.4.5.md` and `../../docs/RECOVERY_INCIDENTS_v0.4.5.md`. `rcc-recovery incident` persists a local packet; `resume-observation` accepts only a fresh checkpoint-bound read-only decision and retains a bounded restart budget. Neither command sends diagnostics to ChatGPT or resumes task dispatch. The separate opt-in automatic review path is documented in `../../docs/AUTOMATIC_REVIEW_v0.4.5.md`. Once a case adopts the journal, do not let an older runtime or direct-edit script write that case.

Use `../../docs/HANDLER_POLICY_v0.4.5.md` for the executable URL and review-budget contract. Unsupported routes and duplicate conversations never authorize first-match dispatch. A new-tab request whose acknowledgment is lost must be reconciled before another open; there is no automatic PUT-to-GET replay. Review timeouts cancel observation commands and never permit resending a worker prompt.

Use `../../docs/EMERGENCY_v0.4.6.md` for the new candidate's incident-wide budgets, explicit route setup, durable diagnostic claim and ACK/decision checks. Delivery is opt-in and experimental. An app-owned Codex chat may reject a CLI resume with an active-writer conflict even while idle; do not release its writer, archive it, switch destinations or retry automatically. A real-agent app-tool test is evidence of the protocol only, not an autonomous Node delivery adapter. If a checkpoint cannot be loaded, only diagnostic delivery with a null decision is permitted. A changed checkpoint rejects the old incident. One accepted queue proposal permits at most one extra response/output verification, never another worker send.


## 0.4.9 reliability addendum

Apply [the reliability contract](../../docs/RELIABILITY_v0.4.9.md). Use current queue operational status; an active scheduler or existing PID alone is not an active browser worker. Exact fresh invocation receipts can establish NOT_SENT_CONFIRMED without task success or automatic retry permission. Uncertain clicked Send still requires original-turn reconciliation. Explicit unused-role provisioning never replaces a committed conversation. New structured reviews may use the explicit JSON output contract; never relax an already-sent file contract. Same-role controller reuse requires the exact proof-pinned prior delivery and unchanged bundle, not an @mention. Default five rooms can be explicitly increased while browser sends remain serial. A saved account update does not hot-patch an installed runtime or migrate existing case helpers.
