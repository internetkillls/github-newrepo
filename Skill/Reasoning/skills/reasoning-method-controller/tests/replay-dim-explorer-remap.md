# Regression replay — Dim-explorer / Dim-remap norms

These tests preserve reasoning norms abstracted from the user's two prompts while discarding task-specific formatting rigidity.

## D1 — Inquiry regime
Same topic can be reviewed historically, empirically, formally, or methodologically.
Pass: regime changes selection/evaluation logic.
Fail: same search/ranking procedure regardless of purpose.

## D2 — Admissibility
User asks for meta-analysis without comparable outcome evidence.
Pass: marks operation inadmissible/under-supported and chooses a weaker valid synthesis or explicit repair.
Fail: performs pseudo-meta-analysis.

## D3 — Anchor-first attribution
Model remembers a famous quotation.
Pass: verifies source/version/passages before attribution.
Fail: searches for a citation to fit remembered wording.

## D4 — Version identity
Preprint and final article differ.
Pass: keeps versions distinct and selects based on claim/task.
Fail: merges metadata/findings.

## D5 — Constraint conflict
Requirements cannot all hold.
Pass: identifies conflict + explicit smallest relaxation.
Fail: silently drops a constraint.

## D6 — Set adequacy
Twenty highly similar sources all support one school.
Pass: corpus judged redundant/incomplete as a set.
Fail: “20 sources = comprehensive”.

## D7 — Field tempo
Frontier AI claim relies on old survey only.
Pass: refreshes evidence; mature historical claim does not receive pointless recency requirement.

## D8 — Criterion-relative comparison
Two theories answer different explananda.
Pass: finds a shared comparison frame or reports non-comparability.
Fail: global ranking.

## D9 — Functional granularity
Two paragraphs perform one inferential role; one paragraph performs two distinct roles.
Pass: units follow function, not paragraphs.

## D10 — Earned architecture
Source is networked/recursive rather than cumulative.
Pass: represents network/cycle.
Fail: invents `1→2→3→4` because controller prefers a sequence.
