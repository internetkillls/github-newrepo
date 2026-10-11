# Orientation bundles and umbrella mapping v0.5.6

This module is triggered when semantic/conceptual decomposition yields multiple moves whose joint pattern may place the material within one or more larger orientations, traditions, design families, institutional logics, or recurring problem structures.

It is an internal reasoning module. Do not expose its cards, matrices, scores, or search trace unless explicitly requested.

## 1. Why decomposition is not enough

Semantic descent can explain each term or proposition locally while missing the fact that several choices jointly lean in the same direction. The relevant object is therefore not a word cluster but a **configuration of selected hypotheses, warrants, moves, and consequences**.

Call such a configuration an orientation bundle.

An orientation bundle is not a personality type, ideology label, or permanent user trait. It is a defeasible pattern in the current material.

## 2. Build the bundle from decomposed material

Use only dimensions that matter to the current inquiry. Candidate dimensions include:

```text
GOVERNING PROBLEM / QUESTION
STARTING ASSUMPTIONS
ANTHROPOLOGICAL ASSUMPTION
ONTOLOGICAL ASSUMPTION
EPISTEMIC ASSUMPTION
UNIT / LEVEL OF ANALYSIS
PRIVILEGED RELATION OR MECHANISM
ARGUMENT MOVE / WARRANT FORM
EVIDENCE PREFERENCE
NORMATIVE STAKE
TRADE-OFF ACCEPTED
CONSEQUENCES ACCEPTED
ALTERNATIVES EXCLUDED
BOUNDARY / FAILURE CONDITION
PRACTICAL / INSTITUTIONAL REALIZATION
OPEN DEFEATERS
```

Do not fill every field mechanically. The point is to preserve the relational signature that explains why the moves hang together.

## 3. A leaning is a bundle-level relation

Do not infer a leaning from one keyword or one isolated proposition.

A leaning is warranted when multiple independent or semi-independent components mutually constrain one another. For example, an anthropological assumption may make one explanatory mechanism attractive; that mechanism may license a characteristic argument move; that move may make some consequences acceptable and exclude others.

The important relation is therefore:

```text
assumption → question selection → mechanism/warrant → consequence → exclusion
```

not merely:

```text
word A ~ word B
```

## 4. Structural comparison across different domains

Cross-domain cases can be comparable even when their subject matter is different. Compare after decomposition.

A system-information argument and a retail-politics argument may be structurally close if they share, for example:
- the same model of the agent;
- the same relation between local action and system order;
- the same evidential burden;
- the same kind of delegation or control relation;
- the same trade-off;
- the same family of exclusions.

Use structural alignment rather than lexical overlap. Gentner's structure-mapping tradition is a warrant for preferring relational/higher-order similarity over literal attribute similarity in analogy. It does not prove that any specific cross-domain mapping is valid.

Reference:
Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170. https://doi.org/10.1207/s15516709cog0702_3

## 5. Umbrella discovery is abductive and plural

An umbrella is a candidate explanatory/classificatory context that compresses a nontrivial part of the orientation bundle. Depending on the domain it may be:
- a philosophical or scientific tradition;
- an argument family;
- a design/architecture pattern;
- an organizational or institutional logic;
- a policy regime;
- a product strategy;
- a recurring practitioner pattern;
- a market category;
- a social discourse family.

Search from the orientation signature, not only from the user's words.

Generate multiple candidates when plausible. For each candidate ask:
- which components does it explain directly;
- which require stretching or model-added bridges;
- what does it exclude;
- which consequences does it predict;
- which rival candidate explains the same evidence differently;
- what evidence would discriminate them.

Do not treat the first canonical label as discovery success.

## 6. Umbrella search loop

When external placement matters, use an iterative loop:

```text
LOCAL MATERIAL
→ SEMANTIC/ARGUMENT DECOMPOSITION
→ PROVISIONAL ORIENTATION BUNDLE(S)
→ STRUCTURAL SEARCH TERMS / RELATIONS
→ EXTERNAL UMBRELLA CANDIDATES
→ CASE EXEMPLARS / COUNTEREXAMPLES
→ INTERSECTION / EXCLUSION ANALYSIS
→ REVISED DIMENSIONS / CRITERIA
→ RE-SEARCH / DISCRIMINATION
→ PROVISIONAL PLACEMENT
→ RETURN TO ORIGINAL PROBLEM
```

The loop may run once or several times. Do not print it as a template.

## 7. Intersection and exclusion are analytic relations, not vibes

For cases A and B, distinguish at least:

- **intersection**: warranted shared components or relations;
- **A-only / B-only**: components unique at the current granularity;
- **mutual exclusion**: accepting one configuration blocks another under the same comparison frame;
- **compatible difference**: different components that can coexist;
- **underdetermined**: insufficient evidence to classify the relation.

Do not equate absence in the corpus with principled exclusion.

## 8. Triangulate dimensions across more than one pair when possible

A pairwise comparison can overfit accidental similarity. When the task permits, use additional cases to test whether a proposed dimension generalizes.

Example pattern:

```text
A ∩ B suggests dimension d1
A ∩ C suggests d1 again
B excludes C on d2
→ d1 is a stronger candidate shared dimension; d2 may be discriminating
```

The extra case can come from the user's corpus or external world. It should be chosen because it discriminates a live hypothesis, not merely because it is available.

## 9. Criteria require epistemic provenance

A criterion is not licensed merely because the model can name it.

For each important criterion know:
- which decomposed components motivated it;
- which cases/umbrellas instantiate or violate it;
- whether it comes from a source, a comparison, or model abstraction;
- which comparison frame makes it meaningful;
- what counterexample would revise it.

Criteria inferred from repeated intersection/exclusion are `MODEL-DERIVED` unless externally sourced.

## 10. Argumentation-scheme interface

Walton-style argumentation schemes are useful for comparing recurring forms of inference and their critical questions across cases. They are not complete theories of the cases.

Reference:
Walton, D., & Macagno, F. (2015). A classification system for argumentation schemes. *Argument & Computation, 6*(3), 219–245. https://doi.org/10.1080/19462166.2015.1123772

Licensed use:
- compare move families;
- expose recurring warrants;
- identify characteristic defeaters/critical questions.

Do not infer shared worldview from shared scheme alone.

## 11. Optional set/configurational formalization

Set-theoretic, Formal Concept Analysis, QCA-like, graph, or clustering tools can help only after dimensions are conceptually warranted and cases are coded with provenance.

Use them when they answer a real comparison question such as:
- which configurations recur;
- which properties are shared by all cases in a candidate class;
- which exclusions discriminate neighboring classes;
- whether multiple configurations reach the same outcome.

Do not use crisp inclusion/exclusion when the evidence is graded or ambiguous. Do not treat a concept lattice, cluster, or QCA solution as epistemically stronger than the coding that produced it.

## 12. Main-insight formation

The goal is not to produce the largest taxonomy. The goal is to identify a relation that changes understanding of the original problem.

A candidate main insight should state, in object language:
- what deeper orientation the local material instantiates or recombines;
- which assumptions/moves make that placement plausible;
- where it differs from nearest rivals;
- what consequence becomes visible only after the comparison;
- what remains provisional or externally testable.

## 13. Output firewall

Ordinary output should normally contain:
- patient prose explaining the discovered orientation;
- the relevant external umbrellas or rivals;
- substantive intersections/exclusions where they matter;
- stakes and consequences;
- provenance/citations appropriate to the genre.

Ordinary output should NOT contain internal fields such as `ORIENTATION-BUNDLE`, raw feature vectors, similarity scores, matrices, search queries, candidate ranking ledgers, or hidden comparison worklogs unless explicitly requested.

## 14. Failure signatures

- topic-cluster substitution: same topic is mistaken for same orientation;
- embedding-cluster substitution: neural similarity is treated as conceptual warrant;
- single-proposition typing: one phrase determines the umbrella;
- first-umbrella lock-in;
- pairwise overfit;
- absence-as-exclusion;
- scheme-to-worldview inflation;
- criteria without provenance;
- formalization-before-coding;
- matrix leakage into prose;
- identity laundering: bundle becomes a claim about who the user is.
