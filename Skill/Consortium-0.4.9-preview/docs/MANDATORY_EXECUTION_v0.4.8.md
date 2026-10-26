# Mandatory RCC execution contract — 0.4.8 preview

RCC now requires Reasoning Method Controller and AntiSlop **instructions** on every orchestrator decision, worker task, follow-up, correction and merge. A plugin mention is not an invocation and a worker's “applied” assertion is not evidence of compliance. This release combines a mandatory skill procedure, pinned actual instruction sources, packet compilation and fail-closed public CLI preflight.

The user authorized compiling the Paperfold evaluation into execution requirements. The rules below generalize supported findings; experimental percentages, a universal UI layout, ten workers and Chrome testing for unrelated research are not made universal requirements. User/system authority remains higher than skill policy.

## Controller ownership and loading

- **RCC** controls dependency partition, roles/rooms, independence, exact ownership, active limits, handoff, merge and reopening.
- **RMC** controls task-intent/provenance, inquiry routing, conditional stages, operator suitability, falsifying tests and closure. Do not create a worker for each RMC stage or force every stage on every task.
- **AntiSlop** checks accessible scope and commitments first, then evidence-backed defects, negative controls, smallest repair and residual uncertainty. It is not a style scrubber or sole LLM quality score.

The primary skill must read `skills/rcc-execution-contract/SKILL.md` before substantive orchestration. Read current live companion skills when available. Otherwise the package carries **pinned snapshots** in `policies/RCC-REQUIRED-CONTROLLERS.zip`: RMC package 0.6.5 and AntiSlop package 0.4.0 (its router text identifies itself as v0.3.0). `policies/required-controllers.json` records every source path/hash and the bundle identity. These supply instructions, not remote plugin/tool activation. A source-version change requires deliberate review and re-pinning, not silent drift.

If live companion versions differ from the pinned snapshots, record that drift and reconcile/update the pin before representing the newer policy as delivered to workers. Do not silently mix version claims.

The 74-file instruction library retains canonical skill/reference modules, not all historical corpora or executable companion tooling. Optional tools absent from the snapshot must be reported unavailable; never claim they ran. If mandatory core instructions themselves are absent or corrupt, delegation is BLOCKED. Do not silently downgrade to names or a homemade replacement.

## Mandatory lifecycle gates

| Gate | Required behavior | Failure handling |
|---|---|---|
| Intake | Freeze user request, source revision, general story and concrete episode; label observed/user-reported/scenario; preserve the desired outcome and domain identities. | Repair wrong intent/source before design. Do not backdate later criteria. |
| Function framing | Map atomic action, state/data owner, smallest usable representation and relevant precedent or explicit reason none applies. | Avoid a framework/dashboard chosen before the problem. |
| Decision | Record chosen mechanism, strongest rival, tradeoff and falsifier. | Preserve a serious rejected alternative through later handoffs. |
| WBS/ownership | Each role has a persistent room, independence class, exact deliverable, exit test, forbidden moves and nonoverlapping case-correct paths. | Reopen the responsible boundary; no silent eleventh specialist or unowned edit. |
| Dependency receipt | Read complete required artifact bytes; verify path/length/SHA256, scope, receiver and critical sections. | Hold canonical planning on missing/truncated input; do not substitute a summary or inherited PASS. |
| Packet | Every task/follow-up/repair/merge contains the canonical controller preamble, pinned bundle digest and case/role context. Supply actual source library. | Reject names-only packets before sending. |
| Transport | Verify role/room/model/readiness, serialize mutations, obey active cap, persist uncertain-send boundary and exact prompt/turn/terminal evidence. Probe artifact transfer early; obtain receiver ACK. | Reconcile uncertainty, never resend; check PID/lock and finite recovery budget before recovery. |
| Cross-owner behavior | Record selectors/events or equivalent data interface, owners, allowed transition, forbidden mutation, negative control and evidence/debt. Inspect inherited handlers. | A new dialog does not remove old listeners; independently passing files do not establish a working interaction. |
| Native vertical journey | For software/UI, test one risky end-to-end native journey before a broad fixture matrix or successful behavior closure. Include relevant cancel/ACK/stale/abort/dedup/reload/permission/focus/theme/accessibility controls. | Missing native evidence stays unverified. Honest artifact completion can still close with explicit debts; do not reintegrate to obtain a green label. |
| Evidence and outcome | Bind claims to scope/environment/source identity. Distinguish spec, source, fixture, native, human and self-report. Predeclare before/after measurement or retain a debt. | Fixture cannot fulfill native/human criteria; targets cannot become measured results; heterogeneous test counts are not a quality score. |
| Merge | Parent reviews evidence against RMC/AntiSlop requirements for every role. Require actual finding/negative control/residual and artifact anchor, not “used both plugins.” | Repair earliest unsupported dependency; do not merge by vote or confidence. |
| Retrospective | At completed consortium boundaries, interview original roles within authorized worker communications; record I0 self-report, actual access, defects, falsifiers and improvements. | If authority/tools/history are absent, record unavailable/partial and reason; never impersonate workers or invent human feedback. |
| Retain/deliver | Preserve source, reports, failed/negative evidence, public-response receipts, hash index, ownership and reopen conditions; derive counters from actual job records. Finish with future experiment/prompt requirements. | Separate transport, artifact, behavior and release. Preserve original material; do not modify daily profiles or deploy because UI work finished. |

For non-UI/research tasks, use the corresponding source/argument/formal witness. Explicitly document inapplicability; do not require Chrome or UI controls as a ritual. Missing human outcome data blocks claims of measured human improvement, not an honestly scoped technical report.

## Local CLI workflow

From the selected release directory, use its full CLI path while working in the project:

```text
node <RCC>/bin/rcc-consortium execution init --case=CASE
# Fill .devspace/rcc/CASE/execution-contract.json with actual task/context/evidence.
node <RCC>/bin/rcc-consortium execution packet --case=CASE --role=ROLE --input-file=owned-task.md --output=packet.md
node <RCC>/bin/rcc-consortium execution check --case=CASE
node <RCC>/bin/rcc-consortium worker send --case=CASE --role=ROLE --prompt-file=packet.md
```

`execution init` creates a deliberately incomplete DRAFT and refuses overwrite. Template shape is `assets/execution-contract.template.json`. Role objects contain `role`, `room`, `independence`, `deliverable`, `exitTest`, `forbiddenMoves`, `ownedPaths`. Function objects contain `id`, `action`, `dataOwner`, `states`, `representation`, `precedentOrReason`. The example in `tests/execution-fixture.mjs` is synthetic test data, not a real execution contract or native evidence.

`execution packet` preserves the owned task under the exact canonical preamble and current case context. It writes a new file and reports the fingerprint; it does not send. `worker send` checks that exact prefix and source-bundle checksum, then automatically uploads the pinned library along with user artifacts. Original compiled prompt bytes remain unchanged for queue/receipt hash binding. Compile each changed follow-up; a changed causal context invalidates old compiled prefixes. Do not compile and resend an already uncertain submission.

Dependencies declare `kind: source|closure`, `requiredBy`, `receivedBy`, `requiredSections`, `sectionAck`, exact file proof and `evidenceScope`. Packets include only the role's declared dependencies. I2 blind packets omit producer decisions, selected representations and other workers' closures; the guard rejects a closure dependency assigned to an I2 role. Parent authors must also keep shared context and owned task text free of undisclosed producer answers; no lexical filter can prove complete epistemic blindness.

`queue run` preflights its pending task before changing it to DISPATCHING. `deferred prepare/arm/tick/run` require the case contract; their actual worker sends use the same guarded wrapper. `--execution-contract=PATH` is supported by direct send/queue/check/packet; deferred uses the canonical per-case path. Read-only doctor/status/list/read operations remain available for recovery without an execution contract.

Use `execution check --stage=matrix` before broad UI matrix work, `--stage=closure` for scoped final handoff and `--stage=release` for declared release readiness. Closure requires per-role controller review artifacts, I0 interview status, retained material identity, debts and reopen condition. An actual deploy/publish operation still requires its own user authority and tooling.

## Parent wake and emergency diagnosis

Deferred parent wake and explicitly authorized emergency diagnosis also carry actual pinned core RMC/AntiSlop instruction text. The core is checksum-verified before claiming a new outbound action; missing sources block it. These local Codex messages use stdin, including parent wake, to avoid Windows command-line length limits. Diagnosis remains tool/action restricted and schema constrained; controller text does not expand its authority or permit resending. Referenced unavailable evidence stays unresolved.

## What is enforced and what still needs review

The official local CLI checks required shape, pinned instruction delivery, exact packet prefix, declared cap/uncertain roles, ownership collisions, full artifact hashes/sections, evidence-class consistency and stage prerequisites. Existing transport retains real locking, completion and uncertainty checks. The gate does not independently verify every assertion in a JSON receipt or prove a worker actually read or understood instructions. Its success status is deliberately `STRUCTURAL_PRECONDITIONS_MET_REVIEW_REQUIRED`.

Cloud/account execution follows the mandatory skill procedure; it has no host process to run the Node checker. Custom runners, direct library imports, vendored transport or unrelated agents can bypass the public CLI mechanically. They remain subject to the policy and must call `assertExecution`/provide equivalent evidence; this release does not claim a universal unbypassable sandbox. A role cap declared in a case contract is not independent live browser telemetry. Official C0 transport continues to serialize active calls; general C1 concurrency is not newly certified.

Mandatory instruction delivery + evidence gates + parent review is the practical control loop. It cannot guarantee 100% internal LLM obedience, zero bugs, deterministic private reasoning or user benefit. Never ask for hidden chain-of-thought as a substitute for receipts.

## Migration and activation

This is a deliberate fail-closed change: old public CLI send/run commands lacking an execution contract now stop before delegation. Keep existing prompts and receipts; prepare a new contract and compile only genuinely new, reconciled tasks. Never edit a healthy legacy runner's state, erase its lock, restart it casually, or treat this update as authorization to resend.

A saved account release does not hot-patch the currently installed local cache or any active process. Use the tested new package, or update/reload the managed plugin through its supported host flow. Do not overwrite a managed cache to imply activation. Existing chats may retain old instructions until refreshed; apply the current procedure explicitly during that transition.

## Traceability from the evaluation

| Paperfold evidence | Mandatory consequence |
|---|---|
| F01 silent fixture insertion; F06 legacy Capture listener | Preview/confirm/cancel data invariant and cross-owner negative control |
| F02 41-versus-42 narrative mismatch | Receipt/version-bound counts and artifact identity; parent evidence review |
| F03 Library-first rival | Decision–Rival–Falsifier retained across build |
| F04 broad/shallow fixture coverage; F07 native contrast failure | Native vertical boundary first; state-specific scope/evidence; no fixture promotion |
| F05 incomplete W5 predecessor | Full byte/section/receiver gate before canonical planning |
| F08 chunk49/receiver knowledge gap; 52-part transport | Early deliverability probe, pinned sources, receiver ACK, delivery/release separation |
| F09 proposed 20%/25%/90% targets | Before/after plan and claim-origin separation, no invented measured benefit |
| Repeated manual continue/check; stale 13-task counter versus 17 jobs | Finite recovery, actual runner ownership, derived counters and actionable status |
| W6 PARTIAL; other roles lack later native records | I0/access-aware interviews, no host-report or human-feedback laundering |
| Notion causal story/function/representation/WBS criteria | Causal intake, atomic data/state map, simple representation, exact WBS and measured outcome/debt |

Source corpus and original interviews remain in `docs/cases/paperfold-20261019/PAPERFOLD-POSTPROJECT-MATERIALS.zip`. The historical 0.4.7 case is preserved; this document supersedes its description of improvements as merely optional policy proposals for future RCC execution.
