# Independent Discovery Query Lab — transferable, ethical research dorking

## Contract
Whenever matching venues, tasks, external standards, competing literature, project opportunities or monetization eligibility, output a **copyable discovery packet**: one question; the target evidence; 3–6 engine-appropriate literal queries; what the operators mean; source quality check; an exclusion/negative test; an update query; and a search log. Teach user how to reproduce and adjust queries without assistant access. Do not call a search successful until a relevant page is opened and checked. Prefer CURRENT OFFICIAL author/policy/project documentation for eligibility, fees, deadlines and claims.

Search-engine qualifiers are NOT universal or guaranteed: `site:`, `intitle:`, `filetype:`, quoted phrases and minus often work on major search engines but vary by engine; `after:`/`before:` support differs. The native GitHub issue/PR search has its own `repo:`, `is:`, `label:`, `author:` syntax. If a query returns zero, broaden term, remove operator, try official site navigation, or query language variant; never infer that the topic or opportunity does not exist.

## Method: semantic widening without source laundering
1. Start with target question, not a famous author or publisher name by default.
2. Identify construct synonyms in both English and Indonesian, target evidence type and venue.
3. One broad orientation query, one site-restricted official query, one competing or negative query, one exact author-policy query, one fee/eligibility query as needed.
4. Open and validate each candidate: exact scope, date, policies, author/institution, source category; record disagreements and stale versions.
5. If the search misses known positive controls, repair the query; only compare results obtained under clearly described scope and date.
6. Produce own research log: `date | engine | literal query | clicked URL | source role | page date | verified claim | open question | next mutation`.

## Copyable templates, replace [TOPIC], [JOURNAL], [YEAR], [USERNAME]
**Journal discovery**
- `"[TOPIC]" "aims and scope" "journal"`
- `"[TOPIC]" "instructions for authors" site:academic.oup.com`
- `"[TOPIC]" "journal" site:link.springer.com/journal`
- `"[TOPIC]" "submission" site:degruyterbrill.com`
- `"[TOPIC]" "journal" site:direct.mit.edu`
- `"[JOURNAL]" "article types" "word limit"`
- `"[JOURNAL]" "article processing charge" OR "publication fee"`
- `"[JOURNAL]" "preprint" "AI" "authors"`
- `"[TOPIC]" "systematic review" OR "critical review" -advertisement`
- `"[JOURNAL]" site:thinkchecksubmit.org` (if no result, open the general journal checklist directly; lack of result is not disqualification)
Check actual official venue URL; publisher-site indexes and path structures can move. Search scholarly papers, NOT just publisher policy. Use trusted citation indexes and verified manuscript pages where appropriate.

**Professional exposure and media**
- `"[TOPIC]" "research implications" site:linkedin.com/posts/`
- `"[TOPIC]" "visualization" site:instagram.com`
- `"[TOPIC]" "explain" site:tiktok.com`
- `"[TOPIC]" "creative technologist" "portfolio"`
These public indexing searches reveal **examples**, not reach or private analytics. Copyright and quotation apply; don't replicate a creator's creative work without permission.

**Open-source opportunities and contribution proofs** (GitHub's own search box; not Google)
- `is:issue is:open label:"good first issue" "documentation"`
- `repo:OWNER/REPO is:issue is:open label:"help wanted"`
- `is:pr is:merged author:[USERNAME]`
- `repo:OWNER/REPO is:pr is:open review:required`
Verify repo README, CONTRIBUTING.md, scope, issue status and PR review in actual pages. A Google `site:github.com "good first issue" "[LANGUAGE]"` query is a broad locator, not live issue state.

**Monetization and eligibility**
- `"[PROGRAM]" "eligibility" "Indonesia" site:[OFFICIAL-DOMAIN]`
- `"[PLATFORM]" "creator" "monetization" "requirements" site:[OFFICIAL-DOMAIN]`
- `"[SERVICE]" "freelance" "scope of work" "rate card"` (secondary market signal, not validated actual income)
- `"[FORMAT]" "copyright" "commercial use" site:[OFFICIAL-DOMAIN]`
Keep all numerical results linked to official sources or real actual contracts; refuse to extrapolate an individual's income from vanity metrics.

**Adversarial checking**
- `"[CLAIM]" "replication" OR "failed"`
- `"[CLAIM]" "limitation" OR "criticism"`
- `"[TOPIC]" "retraction" OR "correction"`
Treat search results as leads. Verify identities, scholarly versions and context before drawing conclusions.

## Independence challenge
After showing one example search with results, ask the learner to modify ONE dimension (year, theory, journal, format or disagreement), predict how results change, run it, and identify one authoritative result and one false positive. Assess the learned technique by their demonstrated retrieval/verification, not by their ability to restate an operator list.

## Ethical boundaries
Only public/authorized sources. Never teach queries to find leaked passwords, tokens, personal addresses, health records, gated manuscript copies, private messages or login bypass. Do not scrape platforms in breach of terms or bulk-harvest personal data. Use privacy-respecting discovery, official APIs or public indexes where permitted. Record source URL and access conditions; honor author rights.
