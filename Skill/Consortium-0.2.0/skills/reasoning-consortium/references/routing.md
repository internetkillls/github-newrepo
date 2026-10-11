# Routing heuristics

Route by work type and independence need, not by brand/model name.

## Common worker roles

```text
EXPLORER        broad candidate generation
CONSTRUCTOR     strongest supported reconstruction
INDEPENDENT     blind reconstruction from the same object
SKEPTIC         maximize defeaters and unsupported-edge detection
PROVENANCE      trace source/idea/concept/phenomenon transformations
FORMALIZER      construct typed relational/formal model
FORMAL-AUDITOR  test formalism/theorem applicability
RUNTIME-WITNESS execute/reproduce named technical claims
SOURCE-WITNESS  verify exact source/version/locus claims
MERGE-JUDGE     adjudicate supplied closures without inventing new theory
```

## Split triggers

Create separate workers when any of these is material:
- one worker would otherwise audit its own high-stakes output;
- interpretation and source verification require different evidence behavior;
- formalization can anchor the conceptual reconstruction;
- rival frames should be developed independently;
- a fresh context can reduce anchoring/sycophancy;
- technical runtime tests should be insulated from theory preference;
- the problem contains genuinely parallel independent subproblems.

Do not split when:
- the task is small enough to inspect directly;
- workers would all see the same context/objective and add only sampling noise;
- merge cost exceeds likely epistemic gain;
- the dependencies are so tight that partition would destroy necessary context.
