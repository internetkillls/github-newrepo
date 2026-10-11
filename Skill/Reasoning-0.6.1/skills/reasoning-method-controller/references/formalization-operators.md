# Formalization and operative-mathematics protocol

## 1. No variable leap

Before assigning a symbol to a prose item, state whether it denotes an entity, relation, property, function, set/class, state, event, parameter, distribution, operator, or residual. A symbol is not a model merely because it abbreviates a word.

## 2. Relational system first

When measurement/formal representation is intended, construct the relevant system:

```text
E = <domain, relations, operations/orders/equivalences>
```

Then state a representation map to a formal system `F` and which relations must be preserved. When relevant, state the admissible transformations under which alternative representations count as equivalent (uniqueness class).

## 3. Formalism selection

Use the target structure, not prestige:
- logic: consequence, quantification, type/scope;
- algebra: operations and composition laws;
- calculus: local/continuous change;
- geometry: configuration, metric, incidence, symmetry;
- topology: continuity/connectivity/deformation invariants;
- graph/network: ties/paths/relational positions;
- dynamical systems: trajectories, attractors, stability, bifurcations;
- probability/statistics: stochastic variables/distributions/uncertainty.

Hybrid formalisms require a bridge between their primitives.

## 4. Pólya discovery operators

```text
SPECIALIZE
GENERALIZE
ANALOGIZE
INTRODUCE AUXILIARY
WORK BACKWARD
CHECK SPECIAL CASE / BOUNDARY CASE
```

These generate or reshape hypotheses. They do not prove the resulting claim.

## 5. Klein invariance operator

When classification under transformations is material:
1. define admissible transformation group/class;
2. define equivalence induced by transformations;
3. identify properties invariant under them;
4. classify only relative to that transformation regime.

Do not call something “topologically/geometrically invariant” without specifying the relevant transformation/equivalence.

## 6. Logic-order and metalanguage gates

### FOL/SOL/HOL
Escalate order only when the target requires quantification over properties/relations/functions/types not representable under the accepted first-order/sorted representation. Do not escalate because the prose feels abstract.

### Tarski gate
When a truth/semantic predicate or self-reference is at issue, distinguish object language from metalanguage before inventing a new logical order.

### Gödel gate
Before theorem-level use ask:
- Is there a formal system `F` with syntactically defined proof?
- Is it effectively/recursively axiomatized in the relevant sense?
- Is sufficient arithmetic representable/interpretable?
- Is the conclusion about incompleteness, undecidability, consistency, or something else?
If not, downgrade to analogy/heuristic.

## 7. Morphodynamic operator

Use state-space/morphodynamic modelling only when the target has warranted structure such as forms/patterns, continuous or qualitative transitions, stability, attractors, singularities, bifurcations, or categorical transitions. Thom/Petitot vocabulary is not a generic synonym for “complex”.

## 8. Relational identity operator

Before fixing nodes/entities, test whether identities/roles are stabilized or produced by relational positions, switching, control, or network processes. If so, model relation/formation jointly rather than assigning fixed identities first.

## 9. Residual δ

Every residual must be typed. `δ` is forbidden as an unexplained bucket. Distinguish:
- error/noise;
- latent mechanism;
- contextual dependence;
- semantic remainder;
- mediation between levels;
- stochastic variation;
- deliberately unmodelled material;
- currently non-formalized but conceptually specified content.
