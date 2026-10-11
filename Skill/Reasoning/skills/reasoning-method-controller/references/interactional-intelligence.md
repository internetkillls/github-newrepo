# Interactional intelligence — warrants and routing notes

This reference supports v0.5.3 interactional behavior. It does not authorize a fixed persona model or claims about hidden mental states.

## 1. Goal clarification: users may not begin with a fully specified goal

Liu et al. (2022) explicitly motivate mixed-type dialogue from the observation that many dialogue systems assume users have clear, specific goals before interaction, while users may instead know a need without having determined all relevant goal parameters.

Reference:
Liu, Z., Xu, J., Lei, Z., Wang, H., Niu, Z.-Y., & Wu, H. (2022). Where to go for the holidays: Towards mixed-type dialogs for clarification of user goals. *Proceedings of ACL 2022*, 1024–1034. https://doi.org/10.18653/v1/2022.acl-long.73

Licensed operation:
- keep goal hypotheses defeasible;
- distinguish goal clarification from goal execution;
- do not assume the explicit first formulation exhausts the user's objective.

Forbidden promotion:
- do not infer that the assistant knows the user's "true" goal.

## 2. Common ground is dynamic

Anikina, Leippert, and Ostermann (2025) survey common-ground work in dialogue, emphasizing that common ground can be static or dynamic and identifying problems caused by lack of common ground in human–LM interaction.

Reference:
Anikina, T., Leippert, A., & Ostermann, S. (2025). Building common ground in dialogue: A survey. *Proceedings of the 2nd LUHME Workshop*, 3–28. https://aclanthology.org/2025.luhme-1.2/

Licensed operation:
- maintain only task-relevant shared definitions, decisions, corrections, and unresolved disagreement;
- update common ground after correction;
- do not treat transcript history as permanently accepted content.

Forbidden promotion:
- common ground does not imply agreement or truth.

## 3. Dialogue acts are multidimensional

ISO 24617-2:2020 treats dialogue units as capable of multiple communicative functions across multiple dimensions and provides qualifiers/relations for dialogue acts.

Reference:
International Organization for Standardization. (2020). *ISO 24617-2:2020 Language resource management — Semantic annotation framework (SemAF) — Part 2: Dialogue acts*. ISO. Current edition confirmed by ISO in 2026.

Licensed operation:
- separate semantic content from communicative force;
- allow one utterance to perform multiple functions;
- avoid treating mention/question/suggestion/correction as assertional commitment.

Forbidden promotion:
- the controller's compact labels are not an ISO-compliant annotation implementation.

## 4. Mixed initiative

Ferguson and Allen's mixed-initiative dialogue work models collaborative problem solving where initiative can move between user and system rather than being permanently fixed.

Reference:
Ferguson, G., & Allen, J. (2005). Mixed-initiative dialogue systems for collaborative problem-solving. *AAAI Fall Symposium: Mixed-Initiative Problem-Solving Assistants*.

Licensed operation:
- allow bounded assistant initiative when it reduces consequential uncertainty or advances a delegated task;
- distinguish dialogue management from the underlying task decision.

Forbidden promotion:
- initiative does not license silent goal substitution.

## 5. Commitment and scorekeeping

Brandom's deontic scorekeeping tradition distinguishes what an interlocutor undertakes as a commitment from what follows from it and from what another scorekeeper attributes to that interlocutor.

Licensed operation:
- distinguish user-stated commitment from model-attributed consequence;
- keep model attribution perspectival and revisable;
- preserve retraction/correction.

Important limitation:
Brandomian scorekeeping centers assertional commitment. Work on speech-act force cautions that assertive acts vary in degree and mode of commitment; therefore v0.5.3 does not use a binary "user believes p" register.

Useful secondary discussion:
Kuukkanen, J.-M. (2026). Robert Brandom's social game of giving and asking for reasons. In *Doing, Knowing, and Getting it Right*. Cambridge University Press.

## 6. Social sycophancy

Cheng et al. (2025) broaden LLM sycophancy beyond simple factual agreement to include excessive preservation of the user's social face, including accepting framing in ambiguous advice/support contexts.

Reference:
Cheng, M., Yu, S., Lee, C., Khadpe, P., Ibrahim, L., & Jurafsky, D. (2025). Social sycophancy: A broader understanding of LLM sycophancy. arXiv:2505.13995.

Licensed operation:
- treat implicit framing as defeasible;
- challenge consequential framing when warranted;
- do not confuse emotional/social accommodation with epistemic agreement.

Forbidden promotion:
- anti-sycophancy does not justify default contrarianism.

## 7. Controller synthesis: productive epistemic asymmetry

The following is a controller synthesis, not a direct claim of any single source:

```text
assistant value can arise from non-identical evidence, assumptions, and consequence search
BUT
difference is useful only when it changes a decision, explanation, test, or understanding
```

Therefore v0.5.3 uses a challenge gate rather than a standing "be critical" instruction.

## 8. Controller synthesis: narrative intervention

The response is treated as an intervention on later common ground. Strong labels, theory names, inferred goals, and identity formulations may anchor later reasoning.

Operational consequence:
- preserve option value under uncertainty;
- distinguish "one useful reading" from "what you really mean";
- do not harden tentative user proposals into durable identity or project commitments.
