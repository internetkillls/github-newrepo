---
name: intent-substitution-audit
description: Use with AntiSlop to audit cross-plugin question substitution, premature curriculum generation, unapproved niche or business-model choice, hypothetical revenue portrayed as typical income, or UI/presentation replacing evidential work; especially when RMC and Coursecraft are jointly invoked.
---

# AntiSlop intent-substitution and instructional-drift audit v0.3.1

Start with AntiSlop's `../antislop-router/SKILL.md`: scope, recap, governing question, claims and accepted decisions. This module adds a small targeted set of L/S/A/Q failure witnesses; it does not replace the nine-class audit or turn style into a truth test.

## Auditable checks

- Latest user question → primary requested answer type → actual dominant output. Did course design, visual UI, or recommendation displace the inquiry? Anchor the shift to an accessible user and assistant turn. A legitimate explicitly requested course is a negative control.
- Claimed user adoption → exact accepting user event. If none exists, keep micro-agency, affiliate, niche or media-network choices `PROPOSED`, not `AGREED`.
- Revenue estimate → distinguish SYNTHETIC SCENARIO, VERIFIED PROGRAM RULE, OBSERVED TRANSACTION, and EMPIRICAL ESTIMATE. Mathematical consistency does not certify typicality.
- Current country/platform assertions → require date/version-appropriate domain evidence when they determine eligibility. Citation markers without retrievable anchors are not evidence of checking.
- Visual/interaction → identify which relation, uncertainty, observation or operation it enables; an inert selector or revenue calculator can be illustrative but cannot validate assumptions.

Classify findings with `CONFIRMED | SUPPORTED-RISK | STYLE-SIGNAL | UNVERIFIED | NOT-APPLICABLE`. For every claimed confirmed issue provide expected vs observed and an accessible witness; preserve contrary cases. A user-supplied audit without the original turns is material reporting evidence, not independent proof of all factual claims.

## Regression routing

Use the paired examples in `../../tests/fixtures/intent-routing-cases.jsonl`, including negative controls, as reproducible prompts in an actual host. Fixture file presence is not test execution. Do not state PASS or generalization until source-anchored model responses are evaluated. The smallest effective repair is at question identification and plugin handoff, before diagram/source/curriculum embellishment.
