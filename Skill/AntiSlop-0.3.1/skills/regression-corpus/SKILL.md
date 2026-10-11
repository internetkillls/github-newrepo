---
name: regression-corpus
description: Curate new or user-reported slop into verified regression cases, add negative controls, test false-positive and miss rates, and control threshold changes in AntiSlop.
---

# Regression corpus

Read `../../references/regression-method.md`. Corpus rows separate `reported`, `observed`, `reproduced`, `adjudicated`, and `resolved`. A reported example is valuable, but does not become measured evidence by inclusion. Use real source refs and turn locations when authorized; do not invent transcripts or attach hidden chain-of-thought.

For every confirmed failure save: input/task contract, output excerpt with locator, expected behavior, actual behavior, reproduction/probe, affected class, *root dependency*, minimal repair and retest. Always add at least one close non-failing case for a new rule. Preserve diverse genres and Indonesian linguistic cases in separate sets; keep original text and source role labels.

Calibration loop: labelled gold set → blinded adjudication where needed → precision/recall and classwise false-positive review → select thresholds for deployment context → frozen holdout/regression → versioned updates. Do not optimize on the same examples reported as final performance. When independent reviewers disagree, report disagreement without forcing a consensus. Keep `UNKNOWN`/abstention separate from detector failures.

Output includes reproducible test fixtures, a changed-behavior claim backed by test results, the limits of the test set, and `REOPEN` conditions. Never claim automatic continuous monitoring without an actual scheduled or hooked runtime.
