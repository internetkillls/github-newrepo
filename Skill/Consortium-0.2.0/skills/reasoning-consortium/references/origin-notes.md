# Origin notes

This plugin was designed after inspecting the user-supplied `codex-chatgpt-pro-plugin-main.zip` (MIT-licensed ChatGPT Pro Line project).

Patterns retained conceptually:
- stable conversation aliases/rooms;
- repo/session lineage;
- direct CDP browser control;
- receipts and target verification;
- narrow browser-operator responsibility;
- fail-closed provenance for browser targets.

Patterns intentionally changed for consortium use:
- global serialization is not the final concurrency model;
- room identity becomes worker-role identity;
- worker independence is explicit;
- closures replace verbatim-transcript transport as the main inter-worker payload;
- merge/canonicalization/invalidation become first-class;
- multi-target concurrency must be proven by tests before activation.

No source code from the uploaded project is required by v0.1; this release is a policy/orchestration skill.
