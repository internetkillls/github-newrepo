# VibeCode Transducer v0.4.0 — Model Admissibility & Heuristic Inference

V0.4 adds a Python-executable, evidence-gated layer for typed unit/representation adequacy, normalization, sparse-data model comparisons, decision-preserving approximation, and conditional deductive counterexamples. Existing static engineering runtime, v0.2 router, v0.3 Python executor and optional MCP source remain preserved. The update does not automatically deploy cloud Python.

Read `skills/vibecode-engineer/references/representation-heuristic-inference.md` and `docs/MODEL_ADMISSIBILITY_VERIFICATION.md`. Examples: `heuristic_regions_underdetermined.json` and `heuristic_lexical_noninjective.json`. New MCP tool source `vibecode_heuristic_execute` requires a separately configured server.

# VibeCode Transducer v0.2.0 — mathematical mental models + engineering

This is an additive update to the existing USER/PRIVATE **VibeCode Transducer** plugin. It preserves the original v0.1 static Python code-analysis transducer, local guarded patch support and optional MCP adapter source; it does not automatically run a remote server, patch a repository, or prove any target behavior.

## What's new in v0.2.0

- `skills/vibecode-engineer/references/math_foundations_review.md` and `math_001_099_registry.csv`: the earlier broad open-access mathematics review and 99-entry index.
- `math_heuristic_literature_review.md`, `math_001_100_crosswalk.csv`: Toulmin–Mahajan–Rice synthesis and Co-Domain case-indexed crosswalk, with proposed MATH-100 marked clearly.
- `math_task_graph.yaml` and `math-model-derivation.md`: conditional task graph T00–T17; typed observation→model→warrant→engineering handoff; limits of inverse reasoning, causal inference and semantic proxies.
- `runtime/math_model_router.py`: a new standard-library-only read-only problem-to-operator candidate and task DAG selector. It checks **declared** feature gates; it does not calculate linguistic metrics, model statistics, or run a proof checker.
- `runtime/vct_math_cli.py`: optional combined CLI using `math_problem` and optionally the existing `engineering_spec` (for existing `vibe_transducer.transduce`).
- `tests/test_math_model_router.py`: 15 tests for typed routing, dependency cycles, namespaces, claim boundaries, and owner approval. No code writes.

## Run locally

From plugin root (containing `skills/vibecode-engineer`):

```bash
python -m unittest discover -s skills/vibecode-engineer/tests -v
python skills/vibecode-engineer/runtime/math_model_router.py --spec skills/vibecode-engineer/examples/second_order_model_problem.json
python skills/vibecode-engineer/runtime/math_model_router.py --spec skills/vibecode-engineer/examples/semantic_claim_blocked.json
python skills/vibecode-engineer/runtime/vibe_transducer.py --spec skills/vibecode-engineer/examples/duplicate_selection.json
```

The combined CLI takes a JSON envelope:

```json
{
  "math_problem": {
    "goal": "Audit whether a lexical count establishes a rhetorical claim",
    "claim_type": "semantic",
    "observation_kind": "lexical_spans",
    "features": {"sentence_bounded_tokens": true, "annotated_propositions": false}
  },
  "engineering_spec": {
    "task_kind": "review",
    "goal": "Inspect bounded code snapshots; do not infer behavior from lexical similarity"
  }
}
```

Use with:

```bash
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec combined.json
```

This emits candidate route/task plan and, if the envelope includes `engineering_spec`, the legacy static-analysis report. It **does not execute a task graph, perform source writes, or turn user-declared features into verified evidence**. It does not create a functioning MDE DSL, symbolic backend, statistical testing engine, formal proof assistant, causal estimator or general solution to inverse problems.

## Boundaries and provenance

Read `skills/vibecode-engineer/references/math-model-derivation.md` for operator gates, human rhetorical annotation requirements, root schema preservation, and mathematical/coding namespace distinctions. `MATH-001..099` are inherited review records, `MATH-100` proposed; `ATLAS-031..080` are separate. Most Atlas methods remain reference-only; the narrow v0.1 implementations cover parts of Jaccard 034, MAD 055 and toposort 058. Do not use code keyword matches to assert semantic equivalence.

Mahajan's book is referenced and cited, but the full PDF is **not bundled** because source accessibility and redistribution permission differ. This package keeps research syntheses separate from runtime proof/results. The user's `SECOND_ORDER_MODELS_v1.3.md` is used as a bounded requirements source, not overwritten.

## Previous v0.1 capabilities retained

Python AST parse, lexical donor prefilter, declared dependency order, basic attempt-isolated trace checking, numeric median/MAD, SHA-bound patch preview, negative test planning, and `runtime/local_apply.py` as a separate owner-gated local-only patch utility. The source for an optional SDK-v2-compatible MCP adapter remains but needs independent installation, hosting, authentication and host handshake; no live ChatGPT MCP runtime or tunnel is implied.

Refer to `docs/VERIFICATION.md` for historical v0.1 test witnesses and `docs/MATH_MODEL_UPDATE_VERIFICATION.md` for new 15-case tests and remaining unknowns.

## v0.3.0 — mandatory Python computation inside reasoning

Corrects v0.2.0's **plan-only** mathematical router: `vct_math_cli.py` now calls `cloud_math_executor.execute()` for each supplied `math_problem`, so a typed observation payload is computed in Python before its numerical/structural output can inform a decision. `math_python_execution` records `EXECUTED`, `NO_OBSERVATION_PAYLOAD`, or `UNSUPPORTED_COMPUTATION`; hash-bound results and `next_tasks` are returned. The goal is **tool-augmented reasoning**, not just packaging mathematical methods.

Run in an available Python workspace (including a ChatGPT Python/cloud environment **when these package files have been made available**):

```
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_lexical.json
python skills/vibecode-engineer/runtime/vct_math_cli.py --spec skills/vibecode-engineer/examples/python_cloud_linear_inverse.json
python -m unittest discover -s skills/vibecode-engineer/tests -v
```

Implemented bounded execution: α/β-style descriptive lexical observations, descriptive statistics, graph components/DAG cycles, exact finite matrix linear inference, and simple polygon point classification. A matching read-only `vibecode_math_execute` MCP tool is included in source for an **independently hosted** Python server; no cloud endpoint is deployed here. These are not the entire mathematical registry, automatic proof, or a production semantic classifier. Read `references/cloud-python-decision-contract.md`. The plugin skill requests a Python tool call on any mathematical reasoning turn but **cannot guarantee host tool availability or cloud-service execution by merely being installed**.
