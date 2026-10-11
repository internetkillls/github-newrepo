# Universal provenance and transport protocol v0.5.6

## 1. Provenance-bearing units

Track provenance for any unit whose transformation can change the conclusion: source, author-attribution, idea, concept, argument, school, group, fact, phenomenon, observation, dataset, thematic code, orientation-bundle component, comparison dimension, criterion, model, variable, formal object, theorem-use, software artifact.

## 2. Transport card

```text
EPISTEMIC UNIT:
IDENTITY:
VERSION / STATE / DATE:
ORIGIN:
ORIGINAL JURISDICTION:
ORIGINAL WARRANT:
NATIVE ROLE:
HOST-ASSIGNED ROLE:
MODEL-ASSIGNED ROLE:
CURRENT LENS:
TRANSFORMATION:
PRESERVED:
ALTERED:
DROPPED / ABSTRACTED AWAY:
MODEL-ADDED:
DESTINATION JURISDICTION:
TRANSFER WARRANT:
DEFEATER:
```

Use only fields that matter, but never omit a transformation that carries decision-making weight.

## 3. Transport classes

```text
quotation
paraphrase
translation
interpretive reconstruction
thematic coding
classification
abstraction
generalization
specialization
analogy
orientation bundling
structural alignment
intersection/exclusion inference
criterion induction
measurement/quantification
formalization
cross-domain mapping
causal reconstruction
synthesis
```

Each class has a different burden. A correct citation only proves identity/provenance; it does not prove that the next transformation is licensed.

## 4. Native / host / model distinction

Example:

```text
Author A states X.
Author B uses A's X as support for Y.
MODEL uses B's use of A to propose Z.
```

Do not write Z as though A or B stated it. Keep each derivation edge explicit.

## 5. Bundle and criterion provenance

If the model groups several moves into an orientation bundle, record which observed/source-supported moves enter the bundle and which relation is model-added.

If repeated comparisons suggest a criterion, preserve:
- contributing cases;
- shared/excluded relations;
- comparison frame;
- source-derived versus model-derived status;
- counterexample or defeater.

A useful criterion is still an inference. Repetition across cases strengthens a pattern claim only to the extent that the cases and coding are independently warranted.

## 6. Facts and phenomena

A phenomenon can be mis-coded before any author appears. Example:

```text
observed interaction
→ coded as delegation
→ reconstructed as control transfer
→ formalized as D:A→B
```

Each arrow needs its own warrant. Competing codes are defeaters until discriminated.

## 7. W3C-PROV structural analogy

When useful, model provenance with a lightweight analogue of Entity/Activity/Agent. This is bookkeeping, not a claim that philosophical warrant reduces to PROV-O.
