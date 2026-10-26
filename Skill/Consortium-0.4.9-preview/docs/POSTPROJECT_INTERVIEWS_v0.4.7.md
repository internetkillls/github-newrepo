# Post-project worker interviews as an evidence method

This method was exercised on Paperfold's existing W1–W10 rooms. It gathers retrospective explanations from AI workers and tests their claims against artifacts. It does not turn AI workers into human participants or replace actual user observation.

## Start with the decision the retrospective must improve

The question is not “did the workers do a good job?” It is “which workflow, handoff, design assumption or verification gap should change in the next project, given what actually happened?” In Paperfold, the material questions included source-to-writing continuity, artifact delivery, fixture/native evidence boundaries and the cost of manual orchestration recovery.

Freeze the source revision, role map, current release status and accessible evidence. Read the user's present evaluation rules. Record when those rules were introduced; do not backdate them into prior workers' instructions. Keep original state, events, responses and negative evidence immutable. Run interviews in a separate namespace so they cannot advance the production queue.

## Reuse role memory, but declare dependence

Use the original role-owned rooms. Do not create an invented “expert” claiming the old worker's memory. If a room is inaccessible, preserve a missing interview rather than substituting a newly created persona. Reopening a target for a known conversation is a browser-binding repair, not a new worker.

These interviews are **I0 retrospective self-reports**. A worker has already seen its own work, the project discussion and any supplied outcome summary. This dependence is useful for explaining intent but weak for independent certification. An independent host check can corroborate a specific artifact claim; ten agreeing interviews cannot certify runtime behavior or user benefit.

For Paperfold, the host supplied a clearly labeled current-result summary so workers could critique the outcome. They were instructed not to claim they personally observed those host tests. Several explicitly reported that final source, receipts, previews or original method files were inaccessible in their rooms. That is evidence about context limitations and should remain in the synthesis.

## The bounded interview packet

Each packet contains:

- interview/case/worker IDs and known room identity;
- role-specific responsibilities and concrete probe;
- causal user scenario and current evaluation criteria;
- historical artifact anchors available to that role;
- clearly labeled host-supplied result summary;
- AntiSlop and RMC requirements, including provenance, strongest rival, falsifier and truthful closure;
- output size/format, no implementation, no extra workers, no invented tests or human feedback;
- eight prompts: purpose, human situation, decision/rival/tradeoff, evidence, own weakness, handoff critique, next experiment, RCC improvement;
- stop after the retrospective response.

Use open questions before supplying disputed explanations when minimizing anchoring is critical. This Paperfold exercise intentionally supplied narrow role probes based on known incidents. It is therefore a **prompted retrospective**, not an unbiased discovery of all possible failures. A future two-pass version can collect unprompted reflection first, then challenge contradictions with evidence.

## Transport and completion gate

Limit active generations to the authorized cap; Paperfold used three. Serialize browser mutations. Before sending, verify the exact room, idle state, authenticated composer, empty draft and model/effort readback. Persist the uncertain-send boundary before the click. Store prompt identity and exact echo; use affirmative anchored terminal evidence across repeated observations before capturing completion.

If a send is uncertain, reserve its slot, inspect the exact conversation/turn and never automatically resend. If a selector fails **before any send**, preserve the failure and permit one bounded retry after proving the draft is empty, the token is absent and the room is idle. Do not clear a live lock or edit a healthy runner's state.

For this review, the initial collector had a DOM snapshot string-escaping defect and the composer adapter did not always recognize the new user turn. The host preserved the events, verified exact prompt echoes and resumed observation with no repeated submissions. Two model-selector readiness failures occurred before send; their retry evidence must be retained separately. These are collector/recovery defects, not evidence that the workers failed to answer.

## From testimony to a finding

Use claim records with this minimum shape:

```json
{
  "worker": "W8",
  "interviewRef": "interviews/w8-response.md",
  "claim": "Initial fixture checks missed a native contrast defect",
  "origin": "WORKER_SELF_REPORT",
  "scope": "initial fixture versus repaired native candidate",
  "evidenceRefs": ["EVIDENCE/native/control-colors-before.json", "EVIDENCE/native/native-contrast-after.json"],
  "assessment": "CORROBORATED_FOR_NAMED_SCOPE",
  "counterevidence": [],
  "nextExperiment": "exercise final enabled-control states in actual extension",
  "reopenCondition": "same source hash fails a required contrast state"
}
```

Do not require a numerical confidence score. Useful assessments are corroborated, contradicted, self-report only, proposal or unavailable. A report count discrepancy can be confirmed against two records without claiming all tests were rerun. A proposed 20% time reduction is an unvalidated target, not measured improvement. A generic complaint without an anchor remains a hypothesis.

For a supported improvement, preserve **failure → cause hypothesis → minimal method change → negative control → acceptance → owner**. For example, a PASS-only gate blocked honest W10 delivery; split transport, artifact completion, runtime verification and release fields; test a hash-valid artifact with a BLOCKED release so it must be retained without rerunning integration.

## Produce two outputs

**Project output:** a readable story about decisions, consequences and limits, linked to a worker matrix, interview transcripts, verification evidence and actual source identity. Include a human-task validation debt where appropriate.

**RCC output:** a reusable skill/method, a case packet with source/material index and interview findings, and narrowly defined candidate regressions. Preserve plugin identity, audience and runtime configuration. Record the saved release and verify changed files. Saving an account plugin update does not hot-patch an installed local runtime.

Do not upload daily browser profiles, cookies, tokens, real user records or hidden model reasoning. Paperfold's portable material consists of project documents, public-facing response text, synthetic-test evidence references and checksums. Full cold binary artifacts stay in the local archive with an explicit retention index.

## Closure and negative controls

The retrospective is complete when each requested role is answered or explicitly unavailable, material claims are corroborated or labeled, the project narrative is source-linked, and reusable changes are saved with actual receipts. It need not finish every new UI experiment it proposes.

Required negative controls: mock success cannot become native PASS; host-supplied results cannot become worker observations; an incomplete interview cannot become ANSWERED; a proposed metric cannot become an achieved result; a hash-valid BLOCKED release cannot become failed transport; and an uncertain send cannot cause a second click.

## What to put in the next prompt

“Run post-project interviews in the original rooms against this frozen revision and user-goal contract. Apply AntiSlop/RMC; label I0 testimony and host-supplied context. Corroborate material claims, preserve contradictions, and produce project stories plus RCC improvements with negative controls. Record missing access, exact send/completion receipts and concrete reopen conditions.”
