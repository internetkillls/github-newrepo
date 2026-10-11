# AntiSlop v0.3.0

A private skills-only plugin for evidence-driven conversation-state reconstruction and scoped audits of nine kinds of AI-output failure. This package includes an **optional local Python 3.10+ standard-library CLI**; ChatGPT plugin skills do not automatically execute it, retrieve your full account history, or upload conversational content.

## Workflow

1. **Scope**: distinguish visible chat, supplied export, retrieved authorized context and inaccessible history.
2. **Index** (if a transcript is provided): check source IDs, role, exact locators; do not infer commitments from message role.
3. **Self-recap**: extract governing questions, proposals/adoptions, explicit corrections, term senses, tests and unresolved debts; preserve exact directed links, independence of branches and source stance.
4. **Audit** only relevant Q/W/L/S/I/N/C/A/M domain detectors, with evidence appropriate to the problem.
5. **Repair and regress** at the earliest failed dependency. Surface failures, near-miss controls and meaningful uncertainties.

The nine classes are query, writing, linear-interaction monolith, sense-making, Indonesian, naming, coding, argument, mathematics. Do not run nine checks on a task merely to fill a grid.

## Optional command-line tools

```bash
python assets/cli/antislop.py index-transcript examples/chat.jsonl
python assets/cli/antislop.py validate-ledger events.jsonl
python assets/cli/antislop.py verify-anchors events.jsonl --transcript examples/chat.jsonl
python assets/cli/antislop.py recap events.jsonl --coverage coverage.json
python assets/cli/antislop.py validate-findings findings.jsonl
python assets/cli/antislop.py audit-text paper.txt
python -m unittest discover -s tests -v
```

`index-transcript` handles **normalized JSON Lines** with `message_id`, `role`, `content` string. It does **not** handle every raw ChatGPT export format, and it does not infer a question, user assent or the completeness of account history. Read `references/transcript-import.md` and `references/ledger-schema.json`. The linter gives style signals only. The JSONL validators verify shape and explicit directed relationships, **not truth**.

## Provenance and limitations

The original v0.1 research/draft is preserved unchanged in `references/source-draft-v0.1.md` as user-supplied material, not as independently reverified citations. Reported incidents remain reported. A standalone skills package cannot instrument model internals, prove the correctness of source extraction, run hidden continuous monitoring, or auto-fetch all past conversations. This release's unit tests check specific functional invariants; no calibrated external reliability score is claimed.
