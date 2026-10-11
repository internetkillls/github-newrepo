# Open Questions: Project Critique and Problems

This document collects questions for investigation and revision. Questions are not findings, nor claims that a failure has been proven. Answers added later should point to evidence, versions, usage contexts, and conditions that could change the conclusion.

## Repository snapshot

Local snapshot on `2026-10-11`, commit `0800d3a`:

| Package | Version in `plugin.json` | Files in folder |
| --- | ---: | ---: |
| Reasoning Method Controller | 0.6.1 | 491 |
| Coursecraft Lab | 0.4.1 | 23 |
| AntiSlop | 0.3.1 | 24 |
| Reasoning Consortium Controller | 0.2.0 | 88 |
| Visual Pipeline | 1.0.1 | 93 |

File counts include text, code, images, PDFs, tests, and configuration. Versions come from local package metadata; this table does not establish whether they are still current upstream. The source ZIPs remain on the local machine and are excluded from new commits. Earlier Git history still contains the commit that tracked the ZIPs.

## 1. Purpose and problem boundaries

- What user problems should this project help with: interpreting intent, framing a problem, ideation, evaluating a solution, or several of these stages?
- How can the project distinguish a model failure from a problem with the prompt, context, interface, sources, or user expectations?
- What claims can the repository make about model “bias” or “reasoning” without access to the model's internal process?
- What evidence would show that the approach is not helping users formulate or solve problems?
- Which current packages are necessary for the project's core purpose, and what evidence determines whether a package is core or adjacent?

## 2. Interpretation, ideation, and problem framing

- How should a system decide when to ask for clarification and when to present several interpretations for comparison?
- How can it distinguish early ideation, problem definition, constraints, hypotheses, and decisions the user has approved?
- How can users correct a model's interpretation at low cost before it becomes the basis for a recommendation or action?
- How often does a model replace the user's problem with an easier one, and how should that event be recorded?
- What evidence could distinguish helpful clarification from extra questions that only slow the work down?

## 3. Reasoning Method Controller

- For which tasks do stages, evidence checks, and dependency repair improve results, and for which tasks do they add unnecessary work?
- Do checks for rival explanations, negative cases, and conclusion-changing conditions find errors that survive the initial answer?
- How can users inspect the origin of claims and assumptions without receiving lengthy explanations they cannot verify?
- Does “repair the earliest failed dependency” produce better corrections than revising only the final answer?
- What failures remain when a model follows the written procedure but misunderstands the domain or the person's goal?

## 4. Coursecraft Lab and learning interactions

- Do visual or interactive forms help users detect differences between their intent and the model's interpretation? For which tasks and users?
- What performance would demonstrate independent understanding rather than successful imitation of an example?
- How should lessons support people using assistive technology or preferring text explanations?
- How does Coursecraft distinguish field sources, teaching methods, practice examples, and model-generated results?
- Do transfer exercises reveal understanding that persists when the context or tool changes?

## 5. AntiSlop and guardrails

- Which output failures occur most often in real use, and which cause the greatest harm to users?
- How well do explicit rules detect those failures without flagging useful differences in language or style?
- How can regression examples be collected with permission and enough diversity without retaining excessive private conversation data?
- How should false-positive and false-negative rates be measured for each check?
- What happens when a guardrail conflicts with domain needs, language, or a valid user instruction?

## 6. Reasoning Consortium Controller

- Which problems benefit from separate analyses, and when do multiple workers merely repeat the same assumptions or errors?
- How can worker independence be tested rather than simply stated in the task design?
- What criteria should determine whether results are merged, preserved as disagreements, or reopened after new evidence arrives?
- In real use, are the context, time, and orchestration costs justified by better decisions?
- What runtime evidence is needed before claiming parallel execution or isolation between workers?

## 7. Visual Pipeline as an adjacent package

- What relationship can be demonstrated between the visual pipeline and the repository's central goal of human–AI interpretation and problem-solving?
- Does this package provide an example of visual interaction that transfers to other domains, or does it remain a specialized creative workflow?
- Which concepts and artifacts can be shared across packages without treating visual needs as evidence of reasoning quality?
- Should this package remain as an adjacent experiment, move to another repository, or have its relationship explained more specifically?

## 8. Data, evaluation, and updates

- Which unit of analysis is most useful: a conversation turn, a change in user understanding, a decision, the final artifact, or the repair process?
- What dataset could test interpretation, ideation, and problem-solving without equating fluency with correctness?
- How can annotators agree on user intent when a request is genuinely ambiguous or changes during interaction?
- What is a fair comparison: one model's answer, several models, users without assistance, or an alternative workflow?
- How should model and package version changes be recorded so results from older versions are not assumed to apply to newer ones?
- Which measures can be shared, and which aspects should remain assessed through human explanations or artifacts?

## 9. Privacy, licensing, and distribution

- Which materials in each package come from third parties, conversations, or personal context, and what permissions govern public distribution?
- What process should check licenses for PDFs, vendored code, attribution, and conversation examples before a release?
- What information should be redacted or removed before future public versions are made?
- Do the old ZIPs in Git history contain material that should be removed from history, and how would rewriting history affect existing copies or forks?
- How can users report sensitive material or copyright concerns and request a correction?

## 10. Repository structure and governance

- Should package folders remain copied into this repository, or should they point to upstream repositories with pinned versions and checksums?
- How can the repository distinguish upstream copies, local modifications, and added material so that changes remain traceable?
- When should a package change be a local commit, a fork, or an upstream contribution?
- Who decides whether a new package or experiment fits the repository's purpose?
- How should releases, changelogs, and important decisions be recorded without letting administration replace evidence from actual use?

## Closing an investigation

For each question investigated, record the provisional answer, evidence and version, context examined, alternative explanations, limits of the conclusion, and what finding would change the answer. Leave the question open when evidence is insufficient.
