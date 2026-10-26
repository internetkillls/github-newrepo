# RMC v0.6.6 — scoped refinement verification

## Provenance
- Based on inspected Plugin Creator current RMC v0.6.5 (`pluginrel_6acff5a70edc8191b9270017b5aecaf4`). Only selected overlay files are included; all omitted existing plugin files/assets are intended to remain unchanged.
- User-provided `rmc_vct_admissibility_probe.py` SHA-256: `e265420470e0e9bfe7ddfbf8267d8b2bcf7ae5090d16300a03d7b18b5f0a7c0c`; original verbatim copy at `skills/reasoning-method-controller/tests/user_probe_original.py`. Its `dep_sort()` is a source-faithful VCT transcription and **not a live packaged VCT backend call**. Its seven labels are synthetic fixture declarations.
- User-provided *Street-Fighting Mathematics* PDF SHA-256: `3073d7a06bdd3fa2abb06ec52e0dcc7504522c4ffd490bf528983ff84ee53bf4`. Its contents are NOT bundled in this update; only a short sourced methodology mapping is recorded in `references/adaptive-admissibility.md`.

## Local verification
- Executed `python /mnt/data/rmc_vct_admissibility_probe.py`: 11 original synthetic assertions passed.
- Executed `python -m unittest discover -s /mnt/data/rmc_refine_0_6_6/skills/reasoning-method-controller/tests -p 'test_adaptive_gate.py' -v`: 11 unittest methods passed, including original synthetic cases, graph-type controls, applicability, provisional and unverified states, and false-positive controls. Subtests are grouped under unittest methods.
- These checks exercise `runtime/adaptive_gate.py` on declared JSON-style inputs. They do NOT verify actual ChatGPT reasoning behavior, independent semantic validity, existing RMC test suites, anti-slop runtime, or inter-plugin deployment.

## Scope / risk
- **Changed** existing root/compat manifests (version 0.6.6) and the main RMC `SKILL.md` (condensed with adaptive controls); **added** new reference, optional Python checker, local regression tests, this ledger and preserved original probe.
- **Unchanged** canonical `stage-machine.md`, user task-intent skill, older RMC references, corpus, PDFs, icons, other plugins. These retained files are not in the update ZIP and rely on documented overlay preservation.
- The instruction-level rule is not an enforcement hook. A runtime invocation is necessary to claim an executable test was run.
- If a future test shows lost nuance due to the condensed RMC main skill, repair the offending section or revert via the preserved previous plugin release, rather than silently reinterpreting user decisions.
