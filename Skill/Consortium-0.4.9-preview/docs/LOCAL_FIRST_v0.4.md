# RCC v0.4 local-first minimal build — 2026-10-14

**Source baseline:** user-supplied `plugin (5).zip` RCC 0.3.0. This is an additive developer preview, NOT a Windows, CDP or hosted plugin deployment receipt.

## Decision and scope

Keep browser C0/worker transport unchanged. Add local Git inspect, context request, optional AIFFolderFlatten delegation, and a preimage-bound patch-apply gate. No always-on server, MCP, new extension, AST dependency index, or token optimizer is introduced. User requested a build following the audited minimal design.

### Layer contract

- The **local agent** retains primary Git/search/test abilities.
- The **AIF CLI** owns complete eligible-source snapshots, task exports, and source verification. RCC never reimplements its scanner.
- The **RCC local CLI** owns acquisition requests, source identity, optional external invocation, and approved Git patch receipts.
- The **browser consortium** retains its v0.3.0 tab routing, independence classes, and closure handling. Local Git operations do not touch Chrome.

## Git commands

On Windows with Node 20+, Git and a checked-out RCC folder:

```powershell
node .\bin\rcc-consortium local git inspect --repo="C:\DEV\Project"
node .\bin\rcc-consortium local context plan --repo="C:\DEV\Project" --task="Inspect an authentication bug"
node .\bin\rcc-consortium local context plan --repo="C:\DEV\Project" --task="Audit all eligible source" --level=complete --portable
node .\bin\rcc-consortium local git plan --repo="C:\DEV\Project" --patch="C:\diffs\change.diff" --output="C:\diffs\change.plan.json"
# Inspect the generated JSON and its approvalId. The next command mutates the worktree ONLY when explicitly entered.
node .\bin\rcc-consortium local git apply --repo="C:\DEV\Project" --plan="C:\diffs\change.plan.json" --approve="APPROVAL_ID_FROM_PLAN" --output="C:\diffs\receipt.json"
```

Only simple text edits/additions via unified diff are permitted; no stage/commit/delete/rename/mode changes. An existing dirty file targeted by a patch is refused, but unrelated dirty source may remain.

## AIF delegation (optional local installation)

```powershell
node .\bin\rcc-consortium local aif task --repo="C:\DEV\Project" --exe="C:\Tools\AIFolderFlatten.exe" --task="Inspect Settings migration" --output="C:\ContextExports"
# Above is a preview only. This one actually starts the executable:
node .\bin\rcc-consortium local aif task --repo="C:\DEV\Project" --exe="C:\Tools\AIFolderFlatten.exe" --task="Inspect Settings migration" --output="C:\ContextExports" --execute --receipt="C:\ContextExports\aif-execution.json"
node .\bin\rcc-consortium local aif complete --repo="C:\DEV\Project" --exe="C:\Tools\AIFolderFlatten.exe" --output="C:\ContextExports" --execute
node .\bin\rcc-consortium local aif verify-task --repo="C:\DEV\Project" --exe="C:\Tools\AIFolderFlatten.exe" --bundle="C:\ContextExports\TASK_FOLDER" --execute
node .\bin\rcc-consortium local aif verify-complete --repo="C:\DEV\Project" --exe="C:\Tools\AIFolderFlatten.exe" --bundle="C:\ContextExports\SNAPSHOT_FOLDER" --execute
```

`aif complete` captures only eligible source under AIF policies; its offline verify does not verify fresh source. Review explicit omissions before external sharing. If the `.exe` is unavailable, RCC cannot run AIF. Portable manual workflow remains possible by running standalone AIF directly then handing over the files.

## Threats and residuals

- The preview treats task text and patch contents as untrusted; patch paths are inspected via Git's numstat parser, restricted to the checked-out worktree and deny-listed high-risk names. The denylist is not a full secret scanner.
- `git apply --check` is an applicability test, not semantic correctness, regression coverage, or a cross-process transaction. Concurrent source editors remain a race risk.
- The Git actor can still write content supplied in a patch; explicit review/approval and tests remain essential.
- Patch approval is a command-line consent handle, not a cryptographic identity or authorization mechanism against malicious local processes.
- Node/CDP was tested in a Linux sandbox; real Windows Git/NTFS and live Chrome tests remain pending.
- Task context source selection still belongs to AIF's lexical selector. We do not claim AST-based dependency closure, token savings, or better agent performance without measured task benchmarks.

## Provenance and test contract

Run `npm run test:local` and `npm run test:distribution` in the extracted RCC root. The original 14 distribution checks must pass without behavior changes; isolated Git fixtures must witness stale-preimage rejection, dirty-file preservation, approval gate, symlink denial and AIF delegation preview. Generated files are separate from source baseline. No worktree or Git state of the user's own Windows machine was modified to produce this build.

The bundled optional `skills/git-controller/SKILL.md` is a narrower Git read/prepare/apply contract grounded in Git's own documentation. It is not a new Git executable or a permission bypass.
