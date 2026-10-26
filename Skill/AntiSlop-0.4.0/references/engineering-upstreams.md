# Engineering source map — retrieved 2026-10-15

These are **source-grounded integrations**, not the full downloaded/vendor copies of five projects. Their documentation was inspected using an authorized GitHub connector. In this run, remote repository cloning from the file container was unavailable (DNS resolution), so no external code is packaged or claimed to have executed. Each project is independently installed only when a local coding runtime and operator approval are available. Any new local code here was written for this plugin and has distinct behavior and separate tests.

| Source | Inspected file and Git blob SHA | License seen | Adopted boundary |
|---|---|---|---|
| [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop) | [README](https://github.com/dmmulroy/anti-slop/blob/main/README.md), `e272d7bf026b122bb4d022a02415bf96629acbe5` | MIT | Optional Oxlint AST/static checks; vendored upstream plugin belongs in target TS/JS repository, not this skills-only package. Evaluate opinionated rules individually. |
| [nferna26/anti-slop](https://github.com/nferna26/anti-slop) | [agent claim verification](https://github.com/nferna26/anti-slop/blob/main/docs/agent-claim-verification.md), `2b426f91cf7f35e42bee3ce8ef43c17d133a8ccf`; [README](https://github.com/nferna26/anti-slop/blob/main/README.md) `c16ff3004287f9a353242358db4537607ff9abbd` | Apache-2.0 | Adopt checkable file/test/command receipt distinction. Optional CLI can be installed externally from pinned `anti-slop-receipts-v0.1.1`; our gate supports only a subset of the receipt schema. |
| [OWASP/Agent-Security-Regression-Harness](https://github.com/OWASP/Agent-Security-Regression-Harness) | [scenario specification](https://github.com/OWASP/Agent-Security-Regression-Harness/blob/main/docs/scenario-spec.md), `817dddfec7e91fe85843029fe84cc5b84c1a1861`; [README](https://github.com/OWASP/Agent-Security-Regression-Harness/blob/main/README.md), `aad6df13a49a77a16b149bade8c1b83895b3d542` | Apache-2.0 | Adopt expected goal, tool allow/deny assertions and security regression scenarios; our trace checker supports JSON subset only, not the complete upstream harness. |
| [zansxart/anti-slop](https://github.com/zansxart/anti-slop) | [GUIDE](https://github.com/zansxart/anti-slop/blob/main/GUIDE.md), `5d12244eeed4b5c138936eb116caa631afcc5bdc`; [README](https://github.com/zansxart/anti-slop/blob/main/README.md), `f573e56f94e988e7ae82f24e2025cda97647feac` | MIT | Adopt UI/copy checks as purpose-sensitive optional review; no automatic injection of their 39 rules into unrelated engineering workflows. |
| [openai/codex](https://github.com/openai/codex) | [README](https://github.com/openai/codex/blob/main/README.md), `06b02fced7db972084bf0188cb03f60375b51c1c` | Apache-2.0 | Codex is a distinct local engineering agent; integrate via scoped `AGENTS.md` contract, repo tests, and explicit runtime receipts. The upstream root `AGENTS.md` was **not found** in the inspected checkout: never cite it as an existing file. |

## Operator-dependent integrations (instructions, not installed)

```bash
# TypeScript/JavaScript repository, after inspecting source rules and lockfile
npx skills add dmmulroy/anti-slop --skill install-anti-slop

# Optional upstream evidence CLI: pinned source, requires Python/git/network
python -m pip install 'anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1'
anti-slop-run -- npm test
anti-slop-claims --root . --receipts .anti-slop/receipts --report AGENT_FINAL_REPORT.md

# Optional standalone OWASP test harness; in its cloned repository
python -m pip install -e .
agent-harness validate scenarios/goal_hijack/basic.yaml
agent-harness run scenarios/goal_hijack/basic.yaml --trace-file examples/traces/denied_tool_call.json --exit-on-fail

# Optional UI/copy skill; evaluate local style policies before applying
npx skills add zansxart/anti-slop
```

These commands require an actual target repository, dependencies and execution authorization. An optional installer changing a user's repository must not be run implicitly merely because this plugin is installed. Pin third-party dependencies to appropriate reviewed commit/tag before production use; inspect licenses if vendoring.

## Provenance boundaries

- Source docs are evidence of *what an upstream project claims it implements*, not proof that it behaves correctly in the user's environment.
- No external code, source README, banners or assets are copied into this release. The five source URLs and abbreviated SHA values may be independently rechecked.
- Local engineering_gate.py is a small offline verification adjunct, **not** an implementation or fork of upstream tools.
- An installed skills-only ChatGPT plugin does not run Oxlint, npm, pytest, OWASP harness or a live browser by itself.
