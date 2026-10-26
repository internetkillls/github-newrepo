# RCC 0.4.5-preview

This incremental release adds durable queue commits, local recovery incidents, committed conversation references and opt-in automatic response/output review. Original plugin identity, prompts, scope and audience are retained.

It also aligns conversation URL identity across recovery and browser routing, rejects infeasible review policies, bounds every DOM observation/final readback, and fixes the producer/consumer targetId receipt mismatch. [Handler policy](HANDLER_POLICY_v0.4.5.md) specifies units, bounds, behavior and remaining calibration gaps.

Start with [automatic review](AUTOMATIC_REVIEW_v0.4.5.md), [queue journal](QUEUE_JOURNAL_v0.4.5.md) and [recovery incidents](RECOVERY_INCIDENTS_v0.4.5.md). Each describes executable commands, proof scope and remaining gates. See [verification scope](verification-0.4.5.json) for recorded checks.

Automatic review is opt-in for a prepared handoff and requires a pinned output contract for each pending job. Legacy manual review remains available. Existing live cases must have one current writer before adopting the authoritative journal; do not mix older direct-edit runners with the new queue on one case.

The release does not install an always-on service, restart Chrome automatically, deliver diagnostics to ChatGPT, certify content quality, or authorize new worker messages. Interrupted or uncertain sends are never blindly repeated. An account update does not rewrite already-running worker processes.
