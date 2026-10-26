# Reasoning Consortium Controller v0.4.9-preview

**0.4.9 reliability repairs:** [Paperfold audit fixes and migration limits](docs/RELIABILITY_v0.4.9.md): unified message detection, invocation-bound pre-Send classification, explicit unused-room provisioning, upload progress/scoping, proof-pinned same-room controller reuse, exact JSON review artifacts, derived operational status and configurable room counts (still serial). Refresh/reload the local installation separately; no active cache is hot-patched.

This preview adds [incident-wide budgets and an opt-in Emergency protocol](docs/EMERGENCY_v0.4.6.md) to the [durable queue/recovery and automatic review](docs/RELEASE_v0.4.5.md). The [URL and review-budget policy](docs/HANDLER_POLICY_v0.4.5.md) remains in force. CLI delivery to an app-owned chat was rejected by an active-writer conflict in the live test; a parent-chat app-tool test separately verified real-agent ACK and one read-only observation. Autonomous app delivery and independent supervision remain unimplemented. Account publication and local activation require separate verification; a saved account release does not hot-patch a local process.

RCC is the orchestration companion to Reasoning Method Controller (RMC).

**Mandatory execution:** read [the 0.4.8 contract](docs/MANDATORY_EXECUTION_v0.4.8.md). Actual RMC and AntiSlop instructions are required for every run, worker/follow-up and merge. New public CLI sends/queue/deferred execution require a filled case contract and compiled pinned controller packet; old name-only prompts fail closed. See [the required companion skill](skills/rcc-execution-contract/SKILL.md). This is instruction delivery plus evidence gating, not guaranteed internal LLM obedience.

- **RMC** disciplines reasoning inside a bounded worker job.
- **RCC** partitions work, assigns epistemically distinct workers, controls what each worker may see, caches closures, adjudicates merge/invalidation, and optionally maps worker roles to persistent ChatGPT browser tabs.

## Two execution surfaces

### ChatGPT Web / account plugin
The skill/policy works normally. It can design the consortium, worker packets, closures, and merge plan. The web-hosted skill alone cannot execute local Chrome automation.

### Local Codex plugin
The bundled `rcc-consortium` CLI uses a dedicated logged-in Chrome profile through CDP. It can physically create and bind multiple persistent ChatGPT tabs/rooms. Active send/read operations remain **C0 serial-safe** using the inherited global browser lock. Parallel generation (`C1`) is not claimed.

## Local quick start

Requirements: Node.js 20+, Google Chrome, Codex local plugin support.

From the plugin directory:

```bash
npm run selftest
node bin/rcc-consortium browser warm
```

A dedicated Chrome window opens. Complete ChatGPT login yourself if needed, then verify:

```bash
node bin/rcc-consortium browser doctor
```

Create a visible five-room consortium:

```bash
node bin/rcc-consortium workers spawn --case=demo
```

Default roles:

```text
constructor
independent
skeptic
verifier
merge
```

Inspect bindings:

```bash
node bin/rcc-consortium workers list --case=demo
node bin/rcc-consortium case status --case=demo
```

Send a bounded worker packet:

```bash
node bin/rcc-consortium execution init --case=demo
# Fill the generated case contract before proceeding.
node bin/rcc-consortium execution packet --case=demo --role=constructor --input-file=constructor.md --output=constructor-packet.md
node bin/rcc-consortium execution check --case=demo
node bin/rcc-consortium worker send --case=demo --role=constructor --prompt-file=constructor-packet.md
```

The browser tabs persist. RCC state is stored under `.devspace/rcc/<case>/state.json`; the vendored transport keeps its own receipts/transcripts under `.devspace/runs/`.

## Important boundary

`workers spawn` really creates ChatGPT CDP targets/tabs when the local browser runtime is running. It does **not** make the account-hosted ChatGPT Web plugin able to control the user's ordinary browser tabs. Local execution is required.

See `skills/reasoning-consortium/references/browser-runtime.md` for the runtime contract and `browser-multitab.md` for the C0→C1→C2 concurrency roadmap.


## v0.3.0 local-first router and portable ASCII process server

This release keeps the existing plugin identity and the optional vendored CDP transport; it does not install services on plugin activation. Node.js >=20 and local Chrome/Chromium are required for browser automation. On Windows use `scripts\rcc.cmd`; on Linux or macOS use `sh scripts/rcc.sh`; no npm install needed.

```sh
node scripts/setup-doctor.mjs
node bin/rcc-consortium transduce --case=demo --input-file=brief.md
node bin/rcc-consortium prompt patch --ir=.devspace/rcc/demo/task-ir.json
node bin/rcc-consortium snippets extract --input=notes.md --case=demo
node bin/rcc-consortium citations export --input=citations.json --format=csv --case=demo
node bin/rcc-consortium server start --case=demo --port=0
# Only on the local machine with a dedicated Chrome CDP profile:
node bin/rcc-consortium browser warm
node bin/rcc-consortium browser doctor
node bin/rcc-consortium browser dom --url-prefix=https://chatgpt.com/c/ACTUAL-ID --case=demo
node bin/rcc-consortium review prepare --case=demo
```

The ASCII network server is a foreground, read-only 127.0.0.1 process-status view (no commands, MCP endpoint or remote access). `doctor`, `repair --apply` and JSONL event receipts provide bounded recovery. Model/effort receipts are not hidden thinking traces. Token counts are estimates. Read `skills/reasoning-consortium/references/local-first-ir-runtime.md`.

## Release verification and unresolved limits

The plugin in ChatGPT is policy-only; local CDP execution must be launched on the user's computer. `worker spawn` will only claim a bound worker when a concrete target ID has been returned. Any ambiguous tab creation leaves a `PROVISIONING` record and requires manual inspection/rebind before retrying.

Run `npm run test:distribution` after extraction to exercise only tests that are meaningful with packaged runtime files. Upstream source-tree/marketplace packaging tests are intentionally not part of this distribution suite; they need an upstream checkout and its build assets. Browser, Windows and host integration require separate live validation.

## v0.4 preview: optional local context & Git controls

`node bin/rcc-consortium local help` lists the new CLI commands. The new commands do **not** require MCP or Chrome. They preserve RCC v0.3 browser transports, defer flattening to optional AIFolderFlatten.exe, and add explicit approval-gated Git patch operations with scope/preimage checks. See `docs/LOCAL_FIRST_v0.4.md` and `docs/LOCAL_SRS.md`. Run `npm run test:local`. No live Windows/browser deployment claim is made.

## Post-project evidence interviews (v0.4.7 preview)

Use `skills/rcc-postproject-interview/SKILL.md` when the user requests a project retrospective, original-worker interviews or a design/engineering case study. It separates worker self-report from human feedback and runtime evidence, preserves decision/rival/falsifier records, and routes supported findings into future experiments. See [the method](docs/POSTPROJECT_INTERVIEWS_v0.4.7.md) and [Paperfold materials](docs/cases/paperfold-20261019/README.md). This is a policy/documentation addition; browser transport and runtime behavior are unchanged.


## Starting a guarded local run

```text
node bin/rcc-consortium execution init --case=demo
# Fill the generated draft with actual context, WBS and evidence.
node bin/rcc-consortium execution packet --case=demo --role=constructor --input-file=task.md --output=packet.md
node bin/rcc-consortium execution check --case=demo
node bin/rcc-consortium worker send --case=demo --role=constructor --prompt-file=packet.md
```

The source library is pinned RMC 0.6.5 and AntiSlop package 0.4.0. No model API or companion tool is invoked merely by these names. The wrapper uploads actual instructions. A checker PASS is structural only; parent review checks claim evidence. Run `npm run test:execution`. Read-only inspection remains available without a contract. Existing live processes/caches are not hot-patched by a saved release.
