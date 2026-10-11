---
name: studio-visual-pipeline
description: "Plan venue generative visuals from a brief to measurable specifications, target adapters and delivery. Use for Bali restaurant/clubhouse portfolio or multi-screen loop projects."
---

# Visual studio pipeline

Read [references/personal-context.md](references/personal-context.md) for this user's confirmed requirements and draft assumptions. The context is editable data, not universal restrictions; a new user request takes precedence.

## DAG and exit evidence
Brief -> design cues/ideation -> measurable spec -> feasibility probe -> engine adapter -> preview -> creative decision -> render -> media QA -> Resolume package -> venue playback -> catalog.
TD may be the first implemented portfolio step while upstream brief/spec nodes remain explicit draft inputs. Record each node's input hashes, version, status, output and exit evidence. Re-run only descendants of a changed input.

1. Confirm the goal, venue/theme, content mode, screen dimensions, player and constraints; preserve known facts. Separate unknowns and proposals from approved values.
2. Use `studio-visual-ideation` for contrasting concepts and personal cues. Compare concepts against brand fit, seams, motion, technical cost and daily variation.
3. Use [assets/project.example.json](assets/project.example.json) and [references/contract.md](references/contract.md) for a compact intermediate contract. Include seed, timing, coordinates, color, asset rights, targets, physical mapping and acceptance evidence. Do not silently change 1800 to 1920.
4. Probe at reduced resolution in one chosen engine before branching. A nominal pixel count is not a GPU benchmark. Record application build, license, plugin/server version and measured export/playback behavior.
5. Use `studio-visual-targets` for adapters; the output may be sibling interpretations rather than pixel-identical renders. Encode target-specific differences explicitly.
6. Use `studio-visual-qa`, then `studio-resolume-show`. Preserve project spec, decision log, source, hashes, preview, render manifest and actual test results.

Offline helper: `python scripts/studio.py validate <spec.json>`; `plan <spec.json> --out <directory>` generates a deterministic build manifest, not live app mutations; `cue <spec.json> --at <timezone-aware-ISO-time>` computes a read-only proposed session; `catalog <manifest.json> --db <project.sqlite>` stores a local project record. Read [references/tooling.md](references/tooling.md) before connecting applications or extending the catalog.

Check saved contracts before asking for information. Skill installation does not connect TD, Blender or Resolume, create API credentials, or certify their runtime. No automatic show scheduling is set up by this package.
