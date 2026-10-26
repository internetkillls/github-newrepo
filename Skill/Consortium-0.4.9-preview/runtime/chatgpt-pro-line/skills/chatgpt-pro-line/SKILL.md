---
name: chatgpt-pro-line
description: Operate the bundled local ChatGPT room and Chrome CDP transport only when explicitly requested by the user. Not a cloud browser tool.
---

# ChatGPT Pro Line — bundled local transport

This is a **local Codex transport**, bundled by Reasoning Consortium Controller (RCC). It is not a remotely hosted MCP server. Run with Node.js 20+ in a user-controlled terminal and a dedicated Chrome profile; the user completes login manually. Never read cookies, passwords, session storage, OTPs, or hidden reasoning.

Use `node <plugin-root>/runtime/chatgpt-pro-line/bin/chatgpt-pro init` to initialize project-local room metadata and install this skill into a project. The command may write `.devspace/state/chatgpt-project.json`, canonical session registry state, and `.codex/skills/chatgpt-pro-line/SKILL.md` in the selected project; run it only with authorization and from the intended project directory. It does not launch an MCP service.

Useful local commands (replace the command prefix with your CLI installation where appropriate):

```text
chatgpt-pro doctor --warm
chatgpt-pro doctor --live
chatgpt-pro status --alias=main
chatgpt-pro rooms new --alias=critic
chatgpt-pro rooms rebind --alias=spec
chatgpt-pro rooms repair --alias=main
chatgpt-pro call --alias=main --prompt-file=packet.md
chatgpt-pro read --alias=main
```

All write/send operations require the user's authorization and respect the global browser-profile lock. Maintain **serial-safe** operation unless stronger concurrency is independently verified. Readback receipts, room bindings, selected model/effort, and submitted messages are separate states; do not infer completion from tab creation or upload filenames. Never automatically resend an ambiguous submission. Rebind missing rooms explicitly instead of duplicating tabs. Source code belongs in the bundled `src/` and `scripts/` tree, not in this skill.
