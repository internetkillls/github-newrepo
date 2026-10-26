---
name: reasoning-consortium
metadata:
  version: "0.4.9-preview"
description: Use when a complex task should be split across independent or adversarial reasoning workers, browser rooms, model/context variants, or staged closures, especially when Reasoning Method Controller is also available. In local Codex, use the bundled browser runtime when the user explicitly wants visible persistent ChatGPT worker tabs. Do not use merely to create more agents; use when partition, independence, cached closure, handoff, or merge can materially improve correctness.
---

# Reasoning Consortium Controller v0.4.9 preview

For connection loss or stale tab bindings, use the `rcc-deterministic-recovery` companion. Version 0.4.4 added CDP cleanup/deadlines and read-only recovery inspection. Version 0.4.5 adds a queue commit journal, local diagnostic outbox, verified receipt binding, and opt-in automatic response/output review; see `../../docs/RELEASE_v0.4.5.md` and `../../docs/HANDLER_POLICY_v0.4.5.md`. These capabilities do not install browser restart supervision, a Windows URI adapter, or diagnostic delivery, and never authorize resending uncertain submissions.

The 0.4.6 local candidate adds incident-wide recovery budgets and an opt-in explicit-session CLI diagnostic route; see `../../docs/EMERGENCY_v0.4.6.md`. A real CLI resume of an app-owned chat was rejected by an active-writer conflict. Never assume an idle app chat is available to a separate CLI writer. Real-agent ACK and one observation were verified separately through an authorized parent-chat app-tool harness. That harness is not autonomous RCC-to-app delivery. No release, local activation, production worker recovery, or independent supervisor is implied.

MANDATORY: Before substantive orchestration, read/apply `../rcc-execution-contract/SKILL.md` and `../../docs/MANDATORY_EXECUTION_v0.4.8.md`. RMC and AntiSlop instruction sources are required for the orchestrator, every worker/follow-up, and merge. Missing mandatory source instructions block delegation; an @mention is insufficient. Use the pinned source library when current companion skills cannot be loaded.

RCC is the **orchestration layer**, not the primary epistemic-quality controller.

```text
RMC = local reasoning policy inside a worker or merge gate
RCC = partition / assignment / independence / closure / handoff / merge / room policy
```

When running locally in Codex, RCC also has an **optional executable browser transport**; browser tabs cannot be created by the account plugin itself:

```text
RCC policy
   ↓
rcc-consortium CLI
   ↓
dedicated logged-in Chrome profile via CDP
   ↓
persistent ChatGPT worker tabs/rooms
```

The account/web plugin and the local runtime are different execution surfaces. **Never claim that a browser tab was opened unless the local runtime actually returned a target/tab binding.**

## 1. Segment by dependency, not by stage number

Never create one worker per RMC stage. Infer problem topology first.

Useful partitions include:
- independent reconstructions of the same object;
- constructor versus adversarial defeater;
- source/evidence verification versus interpretation;
- formal modeller versus formalism-applicability auditor;
- coding/runtime witness versus architecture proposal;
- historian/philologist versus hermeneutic/theoretical synthesis;
- provenance audit versus claim generation.

Use a consortium only when the split creates useful informational or evaluative independence.

## 2. Consortium primitives

```text
CASE        entire user problem
SLICE       bounded subproblem with explicit dependencies
WORKER      isolated reasoning role
ROOM        persistent conversation/browser context owned by one worker role
TARGET      concrete browser tab/CDP target when local runtime is attached
PACKET      bounded input delivered to a worker
CLOSURE     typed result artifact produced by a worker/consortium
MERGE       adjudication over closures, not concatenation
CANONICAL   closure accepted for downstream dependency
STALE       once-canonical closure affected by new evidence
INVALID     closure withdrawn after a failed dependency
REOPEN      rerun earliest responsible slice
```

## 3. Worker packet

Every worker receives only the minimum context needed for its role.

```text
WORKER-ID
ROLE
PROBLEM-SLICE
PARENT-CLOSURES
ALLOWED-EVIDENCE
HIDDEN-FROM-WORKER
TOOLS
OBJECTIVE
FORBIDDEN-MOVES
OUTPUT-SCHEMA
ACCEPTANCE-CRITERIA
STOP-CONDITION
```

RMC and AntiSlop are mandatory companions. Supply actual pinned source instructions and the canonical controller preamble in every packet, then select relevant modules. If required sources are missing, stop delegation as BLOCKED; never substitute a name-only reminder.

## 4. Independence classes

```text
I0 SHARED       sees producer reasoning/context
I1 CLOSURE-ONLY sees result + evidence anchors, not producer narration
I2 BLIND        sees source/problem independently, not producer result
I3 ADVERSARIAL  sees target closure and is tasked to defeat unsupported edges
I4 WITNESS      may only test named claims against source/runtime/formal criteria
```

A merge MUST know the independence class of every contributing closure.

## 5. Closure packet

A closure is not a summary. It is a cached epistemic boundary.

```text
CLOSURE-ID
CASE-ID
SLICE-ID
WORKER-ID / CONSORTIUM-ID
STATUS: DRAFT | WITNESSED | CROSS-CHECKED | CANONICAL | STALE | INVALID
INPUT-REFS
ESTABLISHED
REJECTED
INVARIANTS
PROVENANCE-DELTA
OPEN-DEBTS
INVALIDATED-PATHS
RESIDUALS
SCOPE
DEPENDENCIES
REOPEN-CONDITION
NEXT-ENTRY-CONTRACT
ARTIFACT-REFS
```

Do not transport hidden chain-of-thought. Transport evidence, decisions, invariants, provenance, debts, and tests.

## 6. Cache model

```text
HOT   active worker context and live alternatives
WARM  canonical closures, invariants, provenance graph, open debts
COLD  raw sources, full transcripts, discarded branches, screenshots, old closure versions
```

A successor normally receives WARM state plus selected COLD anchors, never the whole history by default.

## 7. Merge is adjudication

Classify closure relations before synthesis:

```text
AGREE
COMPATIBLE-BUT-DIFFERENT-JURISDICTION
GENUINE-CONTRADICTION
DIFFERENT-QUESTION
DIFFERENT-SENSE
DIFFERENT-EVIDENCE-BASE
ONE-DEFEATS-OTHER
NON-COMPARABLE
```

A merge worker should preferably be unable to originate a new theory unless the merge contract explicitly permits it.

## 8. Invalidation

```text
new evidence
→ identify affected closure edge
→ mark closure STALE/INVALID
→ propagate only to descendants
→ REOPEN earliest responsible slice
```

Do not rerun the whole case unless root dependencies changed.

## 9. Browser execution modes

Read `references/browser-runtime.md` and `references/browser-multitab.md` when the user wants visible ChatGPT worker tabs.

### Web/account mode
Policy only. You MAY define rooms/packets/closures, but MUST NOT claim local browser automation occurred.

### Local Codex mode
The bundled CLI is executable with Node.js 20+:

```text
node <PLUGIN_ROOT>/bin/rcc-consortium browser warm
node <PLUGIN_ROOT>/bin/rcc-consortium browser doctor
node <PLUGIN_ROOT>/bin/rcc-consortium workers spawn --case=<id>
node <PLUGIN_ROOT>/bin/rcc-consortium worker send --case=<id> --role=<role> --prompt-file=<packet.md>
```

`workers spawn` maps one persistent worker role to one ChatGPT room/target and creates real tabs through CDP when the dedicated browser is running.

Default worker rooms:

```text
constructor
independent
skeptic
verifier
merge
```

These are defaults, not mandatory topology.

## 10. Concurrency contract

v0.3 supports **C0 SERIAL-SAFE execution with visible multiple tabs**. The vendored transport serializes active browser operations under its global lock. Tabs persist, but worker generations are not yet claimed to execute concurrently.

```text
C0 SERIAL-SAFE             executable locally in v0.3
C1 MULTI-TARGET-COOPERATIVE design/test target; not yet verified
C2 MULTI-PROFILE-ISOLATED   future stronger-isolation mode
```

Never describe v0.3 as parallel multi-agent browsing unless C1 tests actually pass in the user's environment.

## 11. Browser-room ownership

Default mapping:

```text
one WORKER ROLE ↔ one persistent ROOM ↔ one browser TARGET/tab
```

Do not open a new tab for every micro-call. Reuse a role-owned room until context contamination, explicit blindness, or a fresh independent reconstruction requires replacement.

The runtime writes RCC case state under:

```text
.devspace/rcc/<case>/state.json
```

The transport writes receipts/transcripts separately under its run artifacts. Target IDs and room aliases are execution witnesses; prose claims are not.

## 12. RMC coexistence contract

Read `references/rmc-coexistence.md` and the mandatory execution companion. Load actual RMC/AntiSlop instructions or pinned verified snapshots; do not silently omit them.

Rules:
1. RCC owns routing and state boundaries.
2. RMC owns reasoning discipline inside each bounded job.
3. RCC MUST NOT turn RMC's stages into worker topology.
4. RMC MUST NOT silently rewrite RCC's worker role or evidence boundary.
5. Merge gates can apply RMC to the closures they adjudicate.
6. A worker may challenge the partition itself; this becomes routing-debt.

## 13. Visible trace

Show orchestration-relevant events only:

```text
Partitioned the problem into three independent slices.
Opened five persistent worker rooms in the local CDP browser.  # only with runtime witness
Assigned a blind reconstruction and an adversarial audit.
Canonicalized closure C7 after source witness passed.
Invalidated C4 because its source dependency failed.
```

Do not expose private chain-of-thought.

## 14. Stop condition

A consortium run stops when:
- all decision-driving slices have canonical or explicitly unresolved closures;
- merge criteria have been applied;
- no invalidated ancestor remains upstream of the final result;
- residual disagreements are typed;
- the result can be returned without transporting unnecessary worker history.

## Release integrity and submission evidence

Before browser work, run selftest from the selected plugin release. If bin/runtime files are absent, resolve the incomplete installation; do not silently fall back to an older cached release. Read `../../docs/windows-browser-repair-2026-10-12.md` for recovery and negative tests (path is relative to this skill directory).

Pass exact requested UI labels with `worker send --model=<label> --level=<label>` and repeat `--upload-file=<path>` for each authorized artifact. Confirm model/effort readback before submission. Distinguish target created, attachments ready, prompt submitted, and response captured. Never report a consultation complete from attachment or tab evidence alone.

## 15. Local-first transducer, portable observability and anti-drift (v0.3)

**Mandatory method companions**: Apply actual Reasoning Method Controller and AntiSlop instruction sources at intake, in all task/follow-up packets, and at merge; missing required sources block delegation. The router cannot summon unavailable tools or force all sessions to load other plugins. Preserve task-intent boundaries, especially before producing courses, speculative code or independent worker claims.

Use `references/local-first-ir-runtime.md` for the full IR-to-prompt-patch protocol, privacy/recovery gates, Node CLI on Windows/macOS/Linux, browser DOM extraction, ASCII loopback process view, JSON/CSV citation/snippet export and token-estimate receipts. For code/vibecoding, prefer canonical machine-readable IR schemas, module boundaries, minimal patches and executable test reports instead of long code ideation prose.

The cloud plugin is a **policy/router**, not a process manager. The user must explicitly launch the CLI on their local computer; never claim cloud plugin saved a host service, accessed Chrome or harvested hidden reasoning. Model/effort data require visible, verifiable receipts; do not export private chain-of-thought. Use bounded recoverability, not limitless endurance or unsafe automatic resends. A second-AI postmortem is prepared as a packet, not executed unless tool capability and permission exist.

## Local context acquisition and Git boundary (v0.4 preview)

For local coding agents, prefer existing native Git/file/search tools. The CLI has optional `local` commands for worktree inspection, acquisition planning, AIFFolderFlatten delegation and explicit approval-gated text patch application. These do not open browser tabs or install MCP. Read `references/local-context-and-git.md` before Git write operations. Never imply local Git authority inside the cloud account plugin.

## Post-project interviews and reusable learning (v0.4.8 preview)

When a user requests a project evaluation, portfolio process story or original-worker interviews, apply `../rcc-postproject-interview/SKILL.md`. Reuse role-owned rooms with explicit authorization, preserve the active-worker cap, and declare I0 retrospective self-report. Freeze source/evidence identities; corroborate claims against actual artifacts; preserve missing access and production debts. Never request hidden chain-of-thought or equate worker agreement with human feedback. Save a Decision–Rival–Falsifier and boundary-evidence record; propose repeatable routing/acceptance rules rather than deterministic model thought. The companion is policy, not an automatically installed interview runner.


## Mandatory execution supersession (v0.4.8)

The 0.4.8 execution contract supersedes earlier optional/when-requested application of the Paperfold-derived evaluation and interview gates. Every run applies the lifecycle with explicit scope and debts. CLI sends require compiled pinned controller packets; all final merges require evidence-backed per-role RMC/AntiSlop review and authorized original-role retrospective or an explicit unavailable reason. See `../rcc-execution-contract/SKILL.md`. This is not a guarantee of hidden model compliance or local cache activation.


## 0.4.9 reliability addendum

Apply [the reliability contract](../../docs/RELIABILITY_v0.4.9.md). Use current queue operational status; an active scheduler or existing PID alone is not an active browser worker. Exact fresh invocation receipts can establish NOT_SENT_CONFIRMED without task success or automatic retry permission. Uncertain clicked Send still requires original-turn reconciliation. Explicit unused-role provisioning never replaces a committed conversation. New structured reviews may use the explicit JSON output contract; never relax an already-sent file contract. Same-role controller reuse requires the exact proof-pinned prior delivery and unchanged bundle, not an @mention. Default five rooms can be explicitly increased while browser sends remain serial. A saved account update does not hot-patch an installed runtime or migrate existing case helpers.
