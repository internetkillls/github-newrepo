# Semantic Transition RMC adjunct — release & maintenance

Design date 2026-10-15; target plugin 0.6.3, proposed update 0.6.4. This is a conditional additional skill, **not** a replacement of `skills/reasoning-method-controller/SKILL.md`, `operator-index.md`, `stage-machine.md`, historic corpus, or bundled PDFs. No new top-level S-stage or universal IS operator was introduced.

## Change

- Add `semantic-transition-audit` conditional entry/fast-exit; interpret *Irrationality Saccade* as a provisional discourse anomaly, not psychological/clinical judgment.
- Add seven typed rule families ST-01..ST-07 connecting existing operators to forward/reverse reasoning, typo-aware and metaphor-aware reconstruction, context/force/stance, and semantic-grain stopping.
- Add research/evidence crosswalk, 12 positive/negative pairs, 3 adversarial, 3 transfer cases, and offline static fixture validator.
- Preserve all other existing files by overlay update; keep manifest name, owner, description, UI identity, default prompts, icon references, personal scope and permissions.

## Evidence integrity

`python skills/semantic-transition-audit/tests/check_fixtures.py` verifies the **syntactic fixture contract** only. It does not execute the GPT-6 API or independently rate responses. `BEHAVIOR_OBSERVED` and `REGRESSION_CHECKED` (model behavior) remain UNVERIFIED until baseline/patched GPT-6 transcripts are collected under comparable conditions and independently adjudicated. The existing RMC regression replay documents are NOT asserted to have been run; they remain part of the preserved plugin.

## Recommended model evaluation

For each family T01–T12, run at least both variants against the installed baseline RMC 0.6.3 and experimental v0.6.4; record actual model identifier, source release, date, exact conversation history/prompt, sampling constraints when available, output and human assessor rationale. Use a blinded assessor for serious disputes. On a holdout sample also test novice questions (overtrigger rate), long-turn correction, Indonesian code-mixing with consequential typos, art interpretations preserving productive plurality, and coding transfer. If possible ablate this adjunct while holding the rest constant. Report raw outcomes by dimension, not one undifferentiated score.

## Rollback

Revert to `pluginrel_6acbfbff17f4819185066fc1c786f866` (0.6.3) through an authorized Plugin Creator revision/update workflow using its historical archive; do not delete or force-overwrite unrelated plugin files. An overlay update preserves omitted old files. Alternatively disable invocation of `semantic-transition-audit` in task control while leaving old RMC skills untouched. Release IDs must be checked against current storage, not reused blindly.

## Reopen conditions

- Subrouter fires on ordinary questions or harmless typos more often than baseline.
- Apparent contradictions are wrongfully attributed to the user rather than assistant or source quotation.
- Aesthetic ambiguity is unreasonably normalized or operational faults are excused as art.
- Distinct source interpretations get merged, or a reconstructed bridge becomes attributed to its speaker.
- Cross-domain coding/math routing declines, or model reasoning overhead increases without task benefit.
- Primary RMC routing fails to discover this conditional skill when required (integration activation debt).

Changes require source inspection, matched positive/negative tests and a known release ID. Do not claim automatic background monitoring or a GPT-6 internal mechanism.
