# AntiSlop v0.4.0

A private skills-only plugin for evidence-driven conversation-state reconstruction and scoped audits of nine kinds of AI-output failure. Includes an **optional local Python 3.10+ standard-library CLI**; ChatGPT plugin skills do not automatically execute it, retrieve full account history, access private local source code, or upload conversational content.

## Main workflow (unchanged)

1. **Scope**: distinguish visible chat, supplied export, retrieved authorized context and inaccessible history.
2. **Index** (when a transcript is supplied): verify source IDs, roles and locators; do not infer commitments solely from role.
3. **Self-recap**: preserve active question, user-accepted decisions, explicit corrections, term senses, tests, open debts and directed acceptance/replacement links.
4. **Audit** only the relevant Q/W/L/S/I/N/C/A/M domain detectors.
5. **Repair and regress** at earliest demonstrably failed dependency; keep plausible near-miss controls and residual unknowns.

## Engineering audit (new in v0.4.0)

`skills/engineering-audit/SKILL.md` adds evidence-first software engineering guidance for Codex and GPT-6 workflows: code quality and static lint, exact command receipts, agent goal and tool-boundary checks, runtime probes, UI/accessibility checks, queue duplicate-send and false-completion checks. The new `assets/cli/engineering_gate.py` runs a limited **offline structural verifier**. It does not install Oxlint, Codex, a browser automation server or OWASP harness, and it cannot prove semantic correctness. Full provenance and optional operator-dependent installation steps for five inspected GitHub projects appear in `references/engineering-upstreams.md`.

```bash
python assets/cli/engineering_gate.py contract engineering-contract.json --root .
python assets/cli/engineering_gate.py agent-trace agent-trace.json policy.json
python assets/cli/engineering_gate.py queue-trace queue-trace.json
python -m unittest discover -s tests -v
```

## Existing optional CLI (retained)

```bash
python assets/cli/antislop.py index-transcript examples/chat.jsonl
python assets/cli/antislop.py validate-ledger events.jsonl
python assets/cli/antislop.py verify-anchors events.jsonl --transcript examples/chat.jsonl
python assets/cli/antislop.py recap events.jsonl --coverage coverage.json
python assets/cli/antislop.py validate-findings findings.jsonl
python assets/cli/antislop.py audit-text paper.txt
```

`index-transcript` handles only **normalized JSON Lines** with `message_id`, `role`, and string `content`; it does not auto-import all raw ChatGPT export formats or establish account-wide coverage. Read `references/transcript-import.md`, `references/ledger-schema.json`, and `references/evidence-contract.md`. Style checks produce STYLE-SIGNAL, not claims of AI authorship. JSON validators validate structure, not truth.

## Provenance, testing and limits

The original v0.1 research draft remains unchanged at `references/source-draft-v0.1.md`; the historical v0.3 files remain in the existing plugin release unless explicitly changed. New code is independent of upstream projects and does not vendor their source. New tests cover only executable evidence/trace/queue invariants, not model reliability, production deployment, browser runtime, or semantic correctness. No calibrated external performance score is claimed. Optional local execution requires an accessible checkout and actual tool execution, neither of which is automatically provided by the ChatGPT plugin.
