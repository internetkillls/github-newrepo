# Nine class routing: mechanism → trigger → test → repair

| ID | Class | Activation | Signal / candidate | Adjudication gate | Earliest repair |
|---|---|---|---|---|---|
| Q | Browsing queries | Discovery and citation-sensitive answer | Name-only searches, repeated query intent, missing field/role | Compare original question, query diversity by *meaning*, retrieved sources, contradictions and source coverage; no mandatory token novelty or counter-source quota | Rebuild source need then queries |
| W | Writing | Rewriting, editing, long prose | Trite opener, generic closers, contrast clichés, lexical distribution | Has the sentence/paragraph a necessary *rhetorical or evidentiary* role? Claim-density is an indicator, not absolute condition | Restore missing claim or delete/transform filler |
| L | Dialogue drift | Long or updated conversation | Changed question, dropped correction, false adopted proposal | Source-anchored turn/stance comparison | Correct question and decision ledger |
| S | Sense-making | Technical/theoretical terms | Label substituted for mechanism, unmarked equivocation | Define only inference-bearing term, map its effect, instantiate or contrast when needed | Explain relation/case, not synonym |
| I | Indonesian | Indonesian or bilingual writing | English calques, generic formal tone, user-specific banned patterns | Compare with authentic register + genre and user's explicit preferences; no generic style as logical falsity | Revise passage preserving content |
| N | Naming | Codebase/vault identifiers | Synonym soup, same name used across concepts, namespace bloat | Project glossary + scope-aware collision and rename probe; user vault convention is not global code rule | Canonicalize actual concept naming |
| C | Coding | Executable artifacts | Stub, phantom import, constant response to relevant input, unwired path | Build/runtime witness and metamorphic expected-vs-observed tests; static checks as leads | Fix earliest broken input→output layer |
| A | Argument | Debate, essay, academic reasoning | Conclusion without warrant, source meaning lost in transport, hidden is→ought | Reconstruct intended conclusion, premises, warrant, defeater, strongest serious rival; cite each source claim accurately | Rebuild actual inference |
| M | Mathematics | Numeric/symbolic/proof tasks | Unstated domain/assumption, type/units error, wrong problem statement, unchecked rounding | Recompute arithmetically, optional CAS/proof assistant with scope; require intent↔formal-spec agreement | Restate target theorem/model before proving |

## Gate hierarchy

Hard failures are reserved for independently supported contradictions with task constraints, reproducible tests, or source evidence. Source-incomplete or ambiguous cases are **UNKNOWN**, not automatic fail. Style heuristics yield **signals**. User preference can justify a stylistic revision without claiming universal quality laws.

Routing order is **L/scope and task contract first**, then Q/A/S/C/M/N where material, then W/I style. Detector class and route stage are different dimensions: L is a cross-cutting condition, not a tenth RMC stage. For mixed tasks preserve class-specific warrants and jurisdiction; never average a valid proof score with a writing score.

## Important corrections to v0.1

- Pinning temperature/model can aid reproducibility but cannot make LLM interpretation deterministic: extraction must be source-checked and may be non-identical across calls.
- Lexical overlap, discriminating-token novelty, 200-word length, 4-dp rounding and percentage adversarial query share are *not universal pass/fail thresholds*. Apply if specified and calibrated.
- One term can have multiple legitimate senses; fail only on an unmarked inference-bearing shift.
- Descriptive to normative arguments need an explicit justified norm/warrant, but not necessarily a cited normative *source*.
- "A sentence with zero claims" is not invariably slop (narrative, humor, transitions, rhetoric can serve a warranted purpose).
- Formal proof checkers verify the encoded statement, not whether it captures the real problem; execution witnesses verify only their actual scope.
- A name's structure is project-bound; predicate-first bigrams in a note vault cannot silently govern variables in all software.
