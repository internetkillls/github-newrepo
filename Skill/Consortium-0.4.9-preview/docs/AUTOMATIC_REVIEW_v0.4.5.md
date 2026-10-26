# Opt-in automatic response and output review — 0.4.5-preview

This increment connects the queue, live reviewer, required-output gate and existing deferred runner. It does not certify reasoning quality, deploy a product, automatically restart Chrome, send diagnostic messages, or resend uncertain prompts.

## Opt in once per prepared queue

Create an output contract, then pin it when adding each job:

```json
{"schema":"rcc.output-contract.v1","mode":"files","required":["result.md","tests.json"]}
```

For a task whose whole deliverable is its response, declare `{"schema":"rcc.output-contract.v1","mode":"response"}`. Do not use response mode to bypass file requirements. Jobs without a contract retain the original manual review path.

```text
node bin/rcc-queue queue add --case=<case> --role=<role> --prompt-file=<packet.md> --output-contract=<contract.json>
node bin/rcc-deferred handoff prepare --case=<case> --session=<existing-session-uuid> --auto-review
```

Use the existing trusted arm/Stop-hook workflow and run the prepared handoff. `--auto-review` permits machine evidence review; it does not add permission for sending tasks, waking Codex, or deployment. `--auto-resume` remains a separate existing opt-in. Manual invocation of `node bin/rcc-queue queue verify --case=<case> --job=<job-id>` performs the same review without submitting a prompt.

The producer packet must request transferable bytes in supported response code blocks: `rcc_delivery: "v1"` files with relative `path`, canonical `content_base64`, and SHA-256; or complete numbered `rcc.file-chunk.v1` records. Existing `paperfold.file-chunk.v1` records are also understood. A link or file name alone does not establish delivery. The verifier does not execute code, extract ZIPs or invent missing output.

## Evidence path

1. Queue invocation binds the child transport receipt to the exact job ID and payload hash. The wrapper captures a fresh nonce-scoped structured receipt and a committed conversation reference.
2. The reviewer requires the expected case/role/project, pinned input hash, exact prompt echo, response-to-user anchoring and an unchanged receipt fingerprint. Partial echoes are not enough.
3. Under the browser-operation lock, it discovers one matching authorized conversation and independently re-observes the raw anchored response. Ordinals, hashes, assistant identity, visible Stop and scoped terminal controls must agree repeatedly and on a final readback. Hidden selected message nodes and ambiguous/missing targets fail closed. Display-cleaned response hashes are not substituted for the raw anchored-run hash.
4. The output gate decodes hash-verified bytes, rejects path traversal, Windows device/stream paths, conflicting chunks, duplicate files and missing required files, and writes only to the job-owned verified-output directory. Existing conflicting bytes are not overwritten.
5. An immutable machine-review artifact is committed before REVIEWED_WITNESS. Every later deferred reconciliation rechecks this artifact and required file hashes before another worker or READY transition. The summary preserves machine versus operator provenance and never claims task quality.

Three unresolved verification attempts exhaust the persisted job budget and create a local RCC_RECOVERY_ESCALATION packet. The runner returns REVIEW_ESCALATED; no diagnostic delivery or prompt resend is implied. Ambiguous transport remains UNCERTAIN and is not automatically promoted through this path.

## Verified scope

Unit/fixture tests exercise automatic two-job progression, missing required bytes, post-review file changes, uncertain transport, contract conflicts and legacy manual behavior. A real Chrome intercepted fixture exercises the default browser reviewer, raw message/code-block extraction, required-byte capture and progression to the second fixture dispatch callback. No ChatGPT prompt is submitted by that test; transport callbacks and the receipt are fixtures. Production ChatGPT UI completion and actual child-message delivery are not thereby certified.

Queue journals bootstrap existing cases on the next normal write. Use a single current runtime per adopted case; older direct-edit scripts do not understand the authoritative journal. Existing live worker processes are not hot-patched by an account release.
