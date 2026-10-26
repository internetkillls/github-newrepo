# GitHub contribution detector — no inflated reputation claims

## Input and access
Require user-authorized profile/repo, specific PR/commit/issue URL or connected GitHub tools. Public search may locate candidates; never infer account ownership from a similar name. No scraping private repos, token collection or use of sensitive data. GitHub contribution graph visibility ≠ full history and is subject to branch/email/repo rules (https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference).

## Contribution candidates and evidence
- `documented project` — repository, user ownership, README, license, examples/test or demonstrable output. A repo exists but usage is unknown.
- `reported problem` — issue URL with repro, issue triage evidence, author attribution. Issue opened ≠ fix merged.
- `proposed change` — PR URL; commits; tests; named behavior and diff; PR status. PR opened ≠ accepted.
- `reviewed/helped` — comment/review or merged maintainer-contribution with durable URL. A review is not a code merge.
- `accepted change` — merged PR or maintainer-confirmed docs/code accepted; include merged date and repo ownership. Merged alone doesn't prove end-user value.
- `adopted/useful work` — documented release, dependency use, user report or measured deployment; harder evidence, do not infer from stars.
- `sustainable open-source role` — repeated high-quality contributions / maintainers trust / issue resolution, sourced, not a number guessed from squares.

## Inspect when possible
1. Identify repo license and `CONTRIBUTING.md` / code of conduct; avoid projects requiring confidential information.
2. Locate matching `good first issue`, `help wanted`, or docs/test gap; ensure issue still open and scoped.
3. Read existing maintainer discussion, issue context and tests; reproduce or outline a safe documentation improvement.
4. Make smallest independent change with user approval, explain test and expected diff; do not auto-create PR or publish secrets.
5. Compare actual PR checks, feedback, merge or closure to stated criterion; label progress `candidate / attempted / PR-open / revised / merged / impact-observed`.
6. Create career-facing evidence: concise CAR (context, action, result) paragraph with links, accurate ownership, peer feedback, no inflated metric.

## Legitimate search syntax
Search issues/PR on GitHub using native search qualifiers, e.g. `is:issue is:open label:"good first issue" Python` or `repo:OWNER/REPO is:issue is:open label:"help wanted"`, and public contributions `is:pr is:merged author:USERNAME`. Syntax and searchable indexed data can change; confirm against https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests. For queries without results, adjust syntax, label and repo choice; do not claim no opportunities globally.

## Detector output
`evidence links | author verified? | contribution type | actual stage | reproducible quality witness | maintainer acceptance evidence | career relevance | unresolved risk | one independent next operation | optionally: no action`.
