---
name: reasoning-consortium
metadata:
  version: "0.2.0"
description: Use when a complex task should be split across independent or adversarial reasoning workers, browser rooms, model/context variants, or staged closures, especially when Reasoning Method Controller is also available. In local Codex, use the bundled browser runtime when the user explicitly wants visible persistent ChatGPT worker tabs. Do not use merely to create more agents; use when partition, independence, cached closure, handoff, or merge can materially improve correctness.
---

# Reasoning Consortium Controller v0.2

RCC is the **orchestration layer**, not the primary epistemic-quality controller.

```text
RMC = local reasoning policy inside a worker or merge gate
RCC = partition / assignment / independence / closure / handoff / merge / room policy
```

When running locally in Codex, RCC also has an **optional executable browser transport**:

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

When RMC is available, append only the relevant RMC constraints, not the entire RMC corpus.

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

v0.2 supports **C0 SERIAL-SAFE execution with visible multiple tabs**. The vendored transport serializes active browser operations under its global lock. Tabs persist, but worker generations are not yet claimed to execute concurrently.

```text
C0 SERIAL-SAFE             executable in v0.2
C1 MULTI-TARGET-COOPERATIVE design/test target; not yet verified
C2 MULTI-PROFILE-ISOLATED   future stronger-isolation mode
```

Never describe v0.2 as parallel multi-agent browsing unless C1 tests actually pass in the user's environment.

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

Read `references/rmc-coexistence.md` when RMC is installed.

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
