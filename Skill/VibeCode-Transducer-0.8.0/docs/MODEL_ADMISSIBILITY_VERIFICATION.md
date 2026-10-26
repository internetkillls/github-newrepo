# Verification receipt — VCT v0.4.0 (2026-10-23)

## Target change

Add an actual bounded Python kernel to audit representation and task adequacy independently; normalize bounded observations with explicit denominators; compare rival heuristic models on finite data; test decision preservation under declared bounds; and produce conditional deduction/counterexample receipts that inform task derivation. Keep old v0.3 runtime and public identity.

## Executed checks (local Python container, no network)

- `python -m unittest discover -s skills/vibecode-engineer/tests -v` against available v0.2/v0.3 math source plus v0.4 additions: 54 tests PASS (15 preexisting math-router + 15 cloud math + 24 heuristic tests). Legacy v0.1 test files were not in the local partial-update composite; original 29 tests NOT re-executed in this verification environment.
- `python -m compileall -q skills/vibecode-engineer/runtime skills/vibecode-engineer/tests`: source compile success.
- Concrete example: four data points 1,2,4,8 -> UNDERDETERMINED for pow2 vs regions3, discriminating n=4; adding held-out 15 chooses regions3 *within declared candidates*, not proof for all n. Zero denominators and forbidden scales covered by tests.
- New MCP tool decorator syntax compiled, SDK import and ChatGPT-origin call NOT VERIFIED.

## Epistemic / capability limits

- Source code is not a hosted service. Skill installation does not make Python automatic in every ChatGPT chat. Call the real Python runtime or secure separately deployed MCP tool and inspect tool results.
- Representation identity and `preserved_relations` remain user-declared strings, not checked against actual corpus or code. Both warranted and task-adequate states stay conditional; no model of arbitrary semantics or proof engine.
- Abduction means comparison of a finite named model set, not autonomous generation of unlimited novel theories.
- Finite heldout model agreement is conditional evidence and **not** proof of general laws, population-level confidence, causal inference or rhetorical interpretation.
- Unchanged v0.1/VCT patch tool source is retained by remote plugin overlay rather than re-vendored or retested here.
