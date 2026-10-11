# Reasoning Consortium Controller v0.2.0

RCC is the orchestration companion to Reasoning Method Controller (RMC).

- **RMC** disciplines reasoning inside a bounded worker job.
- **RCC** partitions work, assigns epistemically distinct workers, controls what each worker may see, caches closures, adjudicates merge/invalidation, and optionally maps worker roles to persistent ChatGPT browser tabs.

## Two execution surfaces

### ChatGPT Web / account plugin
The skill/policy works normally. It can design the consortium, worker packets, closures, and merge plan. The web-hosted skill alone cannot execute local Chrome automation.

### Local Codex plugin
The bundled `rcc-consortium` CLI uses a dedicated logged-in Chrome profile through CDP. It can physically create and bind multiple persistent ChatGPT tabs/rooms. v0.2 keeps all active send/read operations **C0 serial-safe** using the inherited global browser lock. Parallel generation (`C1`) is intentionally not claimed yet.

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
node bin/rcc-consortium worker send --case=demo --role=constructor --prompt-file=constructor.md
```

The browser tabs persist. RCC state is stored under `.devspace/rcc/<case>/state.json`; the vendored transport keeps its own receipts/transcripts under `.devspace/runs/`.

## Important boundary

`workers spawn` really creates ChatGPT CDP targets/tabs when the local browser runtime is running. It does **not** make the account-hosted ChatGPT Web plugin able to control the user's ordinary browser tabs. Local execution is required.

See `skills/reasoning-consortium/references/browser-runtime.md` for the runtime contract and `browser-multitab.md` for the C0→C1→C2 concurrency roadmap.
