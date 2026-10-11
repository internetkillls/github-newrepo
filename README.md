# Human–AI Reasoning Lab

An experimental collection for studying how people and language models can interpret, frame, and solve problems together.

Many problems are not fully formed when a person first describes them. They may need interpretation, concept clarification, or ideation before they can be expressed as a shared problem. This repository collects tools that explore those steps and the limits of treating a fluent model response as a reliable problem-solving result.

## Focus

- **Reasoning and problem framing:** surface ambiguous concepts, assumptions, evidence, and the consequences of inference before relying on an answer as a basis for action.
- **Learning and interaction:** explore visual, interactive, and course-based ways to help people inspect a model's interpretation and compare it with their own intent.
- **Output quality:** develop explicit checks and regression examples for recurring AI output failures, including unsupported claims, question drift, and unhelpful prose.
- **Collaborative reasoning:** experiment with bounded independent analyses, evidence checks, and explicit synthesis for problems where one pass is not enough.

These are research directions and design aims, not claims that the packages eliminate model bias or guarantee correct answers.

## Packages in this snapshot

| Archive | Role in the collection |
| --- | --- |
| `Skill/Reasoning.zip` | Reasoning Method Controller: routes complex tasks through staged framing, evidence, testing, provenance, and repair. |
| `Skill/Coursecraft Lab.zip` | Course design and tutoring with source-grounded examples, practical learning, and learner evidence. |
| `Skill/AntiSlop (2).zip` | Conversation reconstruction, scoped output audits, and regression checks for recurring failure patterns. |
| `Skill/Consortium.zip` | Reasoning Consortium Controller: partitions complex work into bounded roles and defines closure and merge rules. |
| `Skill/VisualPipeline (2).zip` | Visual ideation and production workflows; included as an adjacent experiment in making intent and outcomes inspectable through visual work. |

The collection's conceptual core is reasoning, learning interaction, and output auditing. Consortium orchestration supports independent checking. Visual Pipeline is an adjacent domain package, not evidence for general claims about human–AI reasoning.

## Repository state

This repository currently preserves the packages as ZIP archives. The table above describes their intended roles from the included package metadata and READMEs. It does not claim that every package has been installed or tested from this repository.

Before unpacking or redistributing a package, read its own README, attribution, and license files. The packages contain distinct licensing and attribution terms; this repository does not add a blanket license over their contents. In particular, the public `Reasoning.zip` snapshot includes reference and conversation-derived materials. Check individual rights and privacy before making future releases or repackaging it.

## Suggested review path

1. Read this overview and the README inside the archive you plan to use.
2. Check its requirements, limitations, attribution, and license.
3. Treat generated or model-produced interpretations as proposals until checked against the original question and relevant evidence.
4. Record changes in Git with a short commit message that explains what changed.

## Name

`human-ai-reasoning-lab` describes the collection's central concern while leaving room for experiments in problem framing, teaching, interaction, and evaluation.
