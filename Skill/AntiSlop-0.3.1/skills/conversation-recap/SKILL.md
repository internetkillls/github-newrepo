---
name: conversation-recap
description: Reconstruct the available chat when the user requests all-chat recap, wants previous decisions, reports assistant drift, updates a long project, or needs a reliable context checkpoint before anti-slop testing.
---

# Conversation self-recap

Read `../../references/self-recap-method.md`; follow it rather than unconstrained summarization. A chat summary is a compact **decision-state reconstruction**, not a story about themes or a dump of every turn. Access is conditional: inspect only actual visible current messages, user-provided transcript exports, or tool-authorized retrieved context; mark which missing intervals cannot be reconstructed.

## First resolve scope

Make a `scope_manifest`: requested thread range, visible/retrieved ranges, missing intervals, source identities, evidence reliability. If incomplete, explicitly write `partial`; do not ask the user to repeat context already accessible. No fabricated message indexes or cross-chat access.

## Pass 1: event extraction

Scan relevant turns in order. Extract only decisions, controlling questions, corrections, material claims, tests, rejected proposals, term-sense changes, constraints, deliverables and open debts. For each event keep a turn anchor/short quote and **actor** plus **origin** (quoted vs authored vs assistant). Never convert user questions into user beliefs or assistant proposals into accepted decisions. Mark implied acceptance as unresolved unless a direct user action can reasonably witness it.

## Pass 2: reconcile

Construct `question register`, `decision/claim register`, `term-sense register` (only inference-bearing shifts), and `open-debt/test register`. A state transition is supported by a dated turn/source, not mere salience. On conflicts, preserve both and explain who asserted which; current explicit user correction wins as an instruction for the present task without rewriting historical facts. Supersession needs an evidenced link. Detect question substitution and source/stance laundering.

## Pass 3: self-audit the recap

Challenge omission of late corrections, false user adoption, unmarked question switch, equivocation, merged source voices, summary compression losing the test/result, and repeated unchanged explanation after rejection. Require at least one negative control: a historical assistant suggestion that **remains proposed**. If none exists, note no such proposal seen; do not fabricate one.

## Emit a portable checkpoint

Default compact format: `scope & coverage`, `governing question`, `user-approved constraints`, `assistant proposals not adopted`, `superseded/rejected`, `known tests with observed results`, `open debts`, `next action`. When user explicitly wants machine-readable state, use `references/ledger-schema.json` and optional `assets/cli/antislop.py` to validate. Do not store data externally by default; do not claim persistent state without a saved artifact. Re-run **delta recap** on material changes rather than recomputing full corpus every turn.

## Executable preflight (when transcript supplied as normalized JSONL)

Read `../../references/transcript-import.md`. Run `python assets/cli/antislop.py index-transcript PATH.jsonl` to build an inspectable index. Never claim this has read inaccessible chats, attachments, nested export objects, or private model reasoning. Next extract material events from indexed messages, then check that each proposed `adopted_by` points to a user adoption event specifically targeting that proposal (`target_event_id`). Preserve independent scopes; mark changed governing questions with justified `replaces` links, and targeted corrections with `corrects`. If those edges are not supported, preserve ambiguity instead of deciding by recency or fluent similarity.

`recap` is an evidence ledger summarizer, not a transcript summarizer. Its active-question result is only as good as extracted events and their explicit edges. Treat any manual classification as defeasible and challenge it against original turns.
