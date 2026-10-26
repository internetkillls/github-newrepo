# Windows and browser transport repair — 0.2.3

## Incident and evidence

The account package selected by Codex was 0.2.2. During the earlier attempt its local cache lacked the executable runtime, and a fallback invoked 0.2.0. Later inspection found the complete 0.2.2 package locally and in Plugin Creator. Why the cache was initially incomplete is not established. There are two separate personal RCC identities; this release updates only `plugins_6ac4cc829a748191a2531c47e7be2838`.

0.2.0 opened the temporary state file read-only and called fsync. A local Windows probe reproduced EPERM with `r` and success with `r+`. 0.2.2 suppressed Windows EPERM; 0.2.3 opens with write access and propagates genuine sync failures, preserving the previous state and removing temporary files.

The Codex browser tool also reported request-header policy failures. That is a separate transport; its internal cause is unknown and this release does not claim to repair it.

After runtime initialization succeeded, the CLI reported no inspectable page. `connectToPage` hid endpoint errors behind the same message and could select an unrelated page. It now requires the requested URL and distinguishes unavailable target from inaccessible endpoint. `warm` fails if target creation fails, rather than returning ok=true.

## Changes

- Forward explicit model, level and repeated upload-file arguments through RCC. Read the model CLI option in the underlying call script.
- Remove ambiguous prefix matching for model/effort options; verify selected state again before uploads or submission.
- Support the observed GPT web model picker with `data-selected-reasoning-effort`, model list, and bounded effort slider. Selection uses page controls and reads their resulting state; unavailable choices stop the call.
- Wait while upload chips say Uploading/Processing, or report failure. Visible filenames alone are insufficient.
- Wait for editor updates to settle before checking prompt text, including after the DOM paste fallback.

## Reproducible checks

From the plugin root, run with Node 20+:

```text
node scripts/runtime-selftest.mjs
node scripts/forwarding-selftest.mjs
node runtime/chatgpt-pro-line/scripts/transport-negative-selftest.mjs
node runtime/chatgpt-pro-line/scripts/doctor-status-selftest.mjs
node runtime/chatgpt-pro-line/scripts/upload-metadata-selftest.mjs
```

All five passed on this Windows host. Negative cases include injected EPERM/EIO preserving the prior file, absent/wrong tab, offline endpoint, refused/invalid target creation, wrong/missing model readback, empty options, absent worker role, busy browser lock, pending/failed/missing attachment. Positive controls cover state writing, target selection, choice readback, forwarding, ready attachment, and upload metadata integrity. Network tests use a local fixture server; they do not send messages.

## Live observations and limits

The dedicated Chrome profile opened successfully; ChatGPT login and composer were observed. GPT-6.1 Sol / high was confirmed by page readback. A deliberately nonexistent model was rejected before message submission. The first real consultation attempt surfaced two attachment chips but failed prompt submission; it was not a successful consultation. Follow-up results are recorded in `live-validation.md`.

A runtime test does not establish every possible ChatGPT UI variant. This adapter supports the observed English controls. Model availability remains account/UI dependent. Request exact labels rather than inventing an alias for “latest”.

## Recovery procedure

Use the selected release's runtime. Run selftest before warm. If its bin/runtime is missing, report incomplete installation and resolve that release; do not silently downgrade to an old cache. Run warm, then doctor, then bind a worker. Login must be completed by the user when requested. Run with exact model/level and verify receipts. A prepared tab, uploaded attachment, submitted prompt and captured answer are separate states.

Source workspace: `C:/Users/joshu/.codex/plugin-workspaces/rcc-repair-0.2.3`. No Josh Interface product source was changed by this repair.
