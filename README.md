# Human–AI Workbench

A modular toolkit for human–AI work: problem framing, evidence-grounded reasoning, learning design, output review, collaborative analysis, and visual and audio production.

Many problems need interpretation, concept clarification, or ideation before a person and a model can work on them together. This repository brings together skill packages and local scripts that support those tasks. The tools structure and inspect work; they do not guarantee that a model's answer is correct or unbiased.

## Focus

- **Frame:** clarify a request, its concepts, assumptions, constraints, and success criteria.
- **Reason:** organize evidence, provenance, rival explanations, tests, and repair steps.
- **Teach and interact:** create source-grounded courses and make interpretations easier to inspect through visual or practical work.
- **Review:** reconstruct conversation state, audit outputs, and maintain regression examples for recurring failures.
- **Coordinate:** divide complex work into bounded roles and merge results using explicit criteria.
- **Build visual work:** plan, validate, and package creative visual projects for supported workflows.
- **Build audio work:** compose and validate structured music projects, export MIDI, and prepare audio-to-visual handoffs.

These are research directions and design aims, not claims that the packages eliminate model bias or guarantee correct answers.

## Packages in this snapshot

| Archive | Role in the collection |
| --- | --- |
| `Skill/Reasoning-0.6.1/` | Reasoning Method Controller (0.6.1): staged task framing, evidence and provenance controls, source lookup, discriminating tests, and repair. Its `source_lookup.py` lists, searches, and reads the bundled source corpus offline. |
| `Skill/Coursecraft-Lab-0.4.1/` | Coursecraft Lab (0.4.1): course design, source scouting, lessons, and learner-evidence workflows. `build_research_links.py` creates public search links from a subject term and outcome; it does not fetch or verify results. |
| `Skill/AntiSlop-0.3.1/` | AntiSlop (0.3.1): conversation reconstruction, scoped output audits, and regression checks. Its optional Python CLI indexes a supplied normalized JSONL transcript, validates evidence-ledger/findings structures, verifies anchors, builds recaps, and emits text-audit signals. It does not query models or establish truth. |
| `Skill/Consortium-0.2.0/` | Reasoning Consortium Controller (0.2.0): worker roles, persistent-room orchestration, bounded context, status, read/send operations, and closure/merge rules. The optional Node.js CLI delegates to a vendored ChatGPT browser transport; the package contains extensive self-tests. Runtime execution requires its documented local environment and authentication. |
| `Skill/VisualPipeline-1.0.1/` | Visual Pipeline (1.0.1): visual ideation, TouchDesigner guidance, and handoffs to Blender and p5.js. `studio.py` validates project specifications and can generate build plans, calculate show cues, and maintain a local SQLite catalog. It is an offline helper, not a renderer or show player. |
| `Skill/AudioMusicPipeline-2.1.0/` | AudioMusicPipeline (2.1.0): music and audio production skills, a portable project contract, validated offline MIDI export, and a local MCP server. The included Ableton, Max, JUCE, and visual handoff tools require their documented host environments for live use; the MCP capability report does not claim a live DAW connection. |

Together, the packages cover framing, reasoning, learning, output review, coordination, and visual and audio project workflows. The Visual Pipeline and AudioMusicPipeline apply those ideas in creative-production domains; neither by itself validates general claims about human–AI reasoning.

## Repository state

This repository stores the package files in folders so individual documents, scripts, tests, and references can be reviewed and versioned. Each package's own README describes its intended use and requirements. The tools are not all wired into one application, and this repository does not claim that every package has been installed or runtime-tested from here.

Before unpacking or redistributing a package, read its own README, attribution, and license files. The packages contain distinct licensing and attribution terms; this repository does not add a blanket license over their contents. In particular, the public `Reasoning.zip` snapshot includes reference and conversation-derived materials. Check individual rights and privacy before making future releases or repackaging it.

## Suggested review path

1. Read this overview and the README inside the package folder you plan to use.
2. Check its requirements, limitations, attribution, and license.
3. Treat generated or model-produced interpretations as proposals until checked against the original question and relevant evidence.
4. Record changes in Git with a short commit message that explains what changed.

## Name

`human-ai-workbench` describes the shared functions while leaving room for additional human–AI workflows.

