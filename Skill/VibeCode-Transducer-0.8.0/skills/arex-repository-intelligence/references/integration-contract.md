# AREX × VCT integration: evidence, ownership, and failure contract

## Distinct systems (do not collapse)

| System | Owner / purpose | Status in this plugin |
|---|---|---|
| RMC + AntiSlop | task boundaries, admissibility, provenance, contradictory cases, completion semantics | existing VCT governing behavior (not replaced) |
| VCT v0.4 | implementation reasoning, AST/trace, bounded mathematical execution, donor/patch evidence and optional MCP source | existing files retained |
| AREX repository catalog | progressive-disclosure hierarchical `area → family → repository → root/sub-skill` metadata, upstream provenance | included as a compact index derived from user-supplied AREX ZIP |
| AREX skill bodies | skill-root operating procedures, commands, references, tests, failure recovery | NOT bundled; inspect only when actually available via user-supplied archive or individually sourced skill |
| DisCo Creator | scope/ground/construct/verify, authoring/refreshing/importing skills | conceptual workflow adapted; no DisCo CLI copied/installed |
| DisCo Researcher | agent that applies validated skills to a concrete research task | NOT running; not equivalent to metadata router or VCT skill |

## Provenance and licensing

The source archive `AREX-Skill-main.zip` includes `README.md`, router indexes and metadata, an Apache-2.0 top-level `LICENSE`, repository skill graph, and a separate DisCo CLI. Snapshot metadata reports 20 areas, 178 families, 1,000 repositories and 2,209 assignments. We validated counts and byte SHA-256 for `repositories.jsonl`, `assignments.jsonl`, and `taxonomy.json` against `build-metadata.json` before conversion.

`arex-index.json` preserves `skill_id`, canonical repo id, description, aliases, source URL and commit, and exact area/family/confidence routing assignments. It deliberately excludes source code, model weights, tests of the upstream repos, and the huge library of SKILL.md payloads. Derived metadata is provided with upstream Apache-2.0 license in `AREX_LICENSE.txt`. Licenses for individual donor repositories, example snippets, and any third-party content must be checked separately. No success claims from AREX README benchmarks are independently reproduced here.

## Two-stage routing + discriminating controls

Stage A (capability discovery): a read-only standard library Python router ranks metadata by exact identity, matching repository name/aliases, family and description tokens, and term rarity. The score is an **un-calibrated heuristic**, not a probability or universal semantic classifier. It has no complete understanding of task requirements, runtime version, correctness, model weights, dependency or licensing. Query text is not an instruction source.

Stage B (evidence-gated handoff): select a candidate only after checking its skill text, source baseline, API/runtime, license and relevant verification. A candidate can be rejected even when exactly matched; absence of a candidate means this AREX snapshot has no sufficiently grounded match, not that the task is impossible.

Counterexample: `huggingface/transformers` reliably identifies a catalog entry but does not prove `transformers` is installed or that proposed API calls work. Negative control: `repair javascript tab selection bug` must not be misreported as a repository donor from this ML-focused index. Near-positive: `speech recognition` can return multiple relevant repository candidates but requires source and task/runtime assessment before a choice.

## State machine and fail-closed cases

- `NO_EXACT_ROUTE`: no adequately discriminating catalog match; continue with VCT's ordinary repo inspection, do not fabricate a donor.
- `AMBIGUOUS_CANDIDATES`: competing routes, no automatic winner.
- `CANDIDATES_NOT_VERIFIED`: lexical metadata result; no code/runtime claim authorized.
- `SKILL_TEXT_INSPECTED_NOT_EXECUTED`: a user archive provided and a single bounded text file opened; no test or package runtime claim authorized.
- `DONOR_SOURCE_UNAVAILABLE`: required source/license/runtime missing. Propose tests and request evidence only if needed, not auto-apply.
- `UPSTREAM_DRIFT`: selected skill/source version differs from target; re-review rather than run stale commands.
- `TESTED`: reserved for a specific executed test whose inputs, environment, exit status, and evidence are retained. Cannot be inferred from successful route serialization.

## Requirements for any future full integration

If later approved, add a separately tested and sandboxed DisCo runner with explicit trust, provenance, dependency isolation, hardware/compute budget, approved permissions, and purpose-specific tool registration. Pin upstream commit and verify package hash. Avoid bundling 130MB and 53,000 entries directly into a lightweight user plugin. Hosting an MCP endpoint requires deployment plus an authenticated handshake; nothing in the present package silently deploys it.
