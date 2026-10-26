# Browser multi-tab / multi-room design — v0.2

v0.2 moves this design from policy-only to **C0 executable** for local Codex. It vendors the user-supplied ChatGPT Pro Line transport and adds RCC case/worker mapping.

## Executable mapping

```text
ROOM constructor   ↔ TARGET T1
ROOM independent   ↔ TARGET T2
ROOM skeptic       ↔ TARGET T3
ROOM verifier      ↔ TARGET T4
ROOM merge         ↔ TARGET T5
```

Each RCC case record keeps, at minimum:

```text
CASE-ID
ROLE
ROOM ALIAS
TARGET-ID
CONVERSATION-URL
STATUS
LAST-SEND / LAST-READ ARTIFACT
```

The underlying transport additionally records its own room lineage and run receipts.

## Current locking behavior

v0.2 deliberately inherits the upstream **global browser-profile lock** for active browser operations. This means:

- creating several persistent tabs is supported;
- sending/reading to those tabs is deterministic and room-bound;
- active browser calls serialize;
- parallel generation is not yet claimed.

This is `C0 SERIAL-SAFE`.

## C1 roadmap

The intended next mode is:

```text
PROFILE-MUTATION-LOCK
short-lived; login/tab lifecycle/global UI state only

TARGET-LOCK(Tn)
per worker tab for send/read/verify
```

Before C1 is enabled, verify all of the following in the user's environment:

1. simultaneous send to T1/T2 never cross-posts;
2. response extraction anchors the correct newest assistant message per target;
3. model/intelligence selection is page-local or otherwise isolated;
4. uploads remain target-bound;
5. reload/close in one target does not corrupt another room;
6. new-chat creation is serialized under profile mutation lock;
7. login/CAPTCHA remains human-only;
8. receipts reconstruct exact worker → target lineage;
9. ChatGPT site rate/interaction behavior tolerates simultaneous target activity without ambiguous completion states.

If any test fails, keep affected operations C0 or move the workers to C2.

## C2 roadmap

`C2 MULTI-PROFILE-ISOLATED` uses separate Chrome profile pools for strong browser/model state isolation. It costs more resources but is preferred when page-level model choices or site state are demonstrably profile-global.

## Room policy

Persistent tabs are worker rooms, not disposable RPC calls. Create a fresh tab when:
- an I2 blind reconstruction must not inherit prior context;
- role context is contaminated;
- model/profile isolation requires replacement;
- the closure contract explicitly demands a fresh witness.

Do not infer epistemic independence from tab separation alone. Independence is controlled by packets and allowed evidence.
