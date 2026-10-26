# Local browser runtime contract — v0.2

## Purpose

The browser runtime makes the RCC room abstraction executable without MCP. It is intended for **local Codex use**. It drives a dedicated Chrome profile through Chrome DevTools Protocol (CDP) and never claims to control an ordinary ChatGPT Web tab from the account-hosted skill.

## Provenance

The transport under `runtime/chatgpt-pro-line/` is adapted from the user-supplied ChatGPT Pro Line codebase under its retained MIT license. RCC wraps it rather than re-implementing login/session/message anchoring from scratch.

## Requirements

- Node.js >= 20
- Google Chrome
- local filesystem/process access
- user completes ChatGPT login manually in the visible dedicated browser
- no password, OTP, cookie, or CAPTCHA automation

## Bootstrap

From the installed plugin root:

```bash
node bin/rcc-consortium selftest
node bin/rcc-consortium browser warm
```

Complete login if necessary, then:

```bash
node bin/rcc-consortium browser doctor
```

## Spawn worker tabs

```bash
node bin/rcc-consortium workers spawn --case=my-case
```

Optional custom roles:

```bash
node bin/rcc-consortium workers spawn --case=my-case --roles=historian,hermeneutic,formalizer,critic,merge
```

Every successful live spawn records an alias and CDP target in `.devspace/rcc/<case>/state.json`.

## Send bounded packets

```bash
node bin/rcc-consortium worker send --case=my-case --role=critic --prompt-file=critic-packet.md
```

The transport is blocking and C0 serial-safe in v0.2. It activates the role-owned room, sends text, waits for a stable assistant response, and preserves transport receipts/transcripts.

## Read/status

```bash
node bin/rcc-consortium workers list --case=my-case
node bin/rcc-consortium case status --case=my-case
node bin/rcc-consortium worker read --case=my-case --role=critic
```

## Runtime truth rule

Only claim a worker tab exists if state contains a live-created target/room binding. A planned or dry-run worker is not a browser tab.

Only claim concurrency if environment-specific C1 tests pass. Multiple visible tabs alone do not prove parallel execution or epistemic independence.
