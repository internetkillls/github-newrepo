---
name: course-source-scout
description: Search and audit subject-specific teaching materials, graduate capability profiles, official syllabi, professor sites/blogs, specialist critical blogs, GitHub repositories, primary sources, assignments, practice artifacts, and one-click research links before compiling or revising a Coursecraft Lab curriculum. Uses field vocabulary and evidence/provenance checks; method bibliography never becomes lesson content by mere mention.
---

# Coursecraft Source Scout: outcome-first discipline search

Aim: find **recognized topic names**, direct teaching/working materials, counterexamples and grading evidence matched to an approved or provisional graduate/portfolio performance. Act as the Coursecraft browsing adapter; do not replace its teaching runtime. Default to a short verified *source dossier*, not a list of search results.

Read `../course-orchestrator/references/method-content-separation.md` first. For contested or extensive research read `../course-orchestrator/references/source-method-validity.md`. For source-criticism QA read `../course-orchestrator/references/anti-slop-source-review.md`. The user's uploaded files may be inspected by available file tools; never treat their names as proof of contents. This skill does NOT create a persistent scraper, background web crawler, or account-access connection. Search only via available web and connected tools.

## Dispatch and gates

`/discover` (`/resource-search`, `/professor`, `/critical`, `/github`, `/syllabus`, `/graduates`, `/dork`) routes to this skill. Natural equivalents also trigger. If the learner has not approved a graduate profile, use a **provisional** performance statement and invite correction only when it materially affects source choice.

1. **Outcome gate:** identify field, learner's desired action, output artifact, quality test, context/level, operating constraints. If missing details are nonessential, proceed with stated assumptions.
2. **Topic-naming gate:** search actual disciplinary syllabi, textbooks, authoritative docs and professional standards. Extract canonical field expressions and their exact sources. No invented experimental terms; a genuinely emerging research term requires author/source and provisional label.
3. **Query-family gate:** produce multiple independent route families below. Translate same concept into its established synonyms or competing schools only if field sources warrant. A professor's personal site might be `~username`, institutional directory, custom domain linked from faculty page or GitHub profile; verify identity. 'Critical blog' is discovered from the field's argumentative ecology, not curated solely for agreeing with the user's view.
4. **Verification gate:** open original page, inspect exact course title, person, date, level, files, licensing and whether an assessment really exists. GitHub or directory list is a discovery lead. Treat results from search snippets as unverified until opened. Links may be stale or require login.
5. **Rival/independence gate:** gather one substantive alternative account when it can change lesson sequence, concept definition or example. Avoid duplicated mirrors as independent corroboration. For a domain-specific tool instruction, official docs may suffice; for controversial normative/historical propositions seek substantive disagreement.
6. **Output gate:** deliver a prioritized source dossier, an **accepted/rejected term register**, source-to-competency map, missing evidence, and up to 4 high-value next clickable queries. For a subsequent `/course`, hand off stable source anchors and a dependency proposal. Do not add subject facts from method sources.

## Source families and search templates

Use supported browser/search operations, not unsupported scraping. Search expressions below are plain templates; substitute the *canonical* subject phrase, official institution or actual author name. Restrict `site:` to appropriate sources; it is not itself a certificate of credibility.

- Department/degree profile: `"<discipline>" "student outcomes" university`, `"<program>" curriculum prerequisite capstone`, `"<professional outcome>" accreditation`. Check actual program and country.
- University syllabus: `site:ocw.mit.edu "<term>" "syllabus"`, `site:edu "<term>" "course" "assignments"`, `site:ac.uk "<term>" "module handbook"`, faculty official course subdirectory. These domains are *search filters*, not automatic quality indicators.
- Professor's primary teaching material: `"<person>" "<term>" lecture notes`, `"<person>" course problem set`, `"<person>" blog critique`, institutional directory → verified personal page → course notes/tutorial/blog/GitHub → exact resource. Do not infer affiliation from social profiles alone.
- Critical/disputing source: `"<term>" criticism peer-reviewed`, `"<term>" debate limitations case study`, `"<term>" alternative model`; seek specific documented claims, not antagonism for show.
- Repository source: `"<term>" language:python tutorial`, `"<term>" assignment repo`, `"<framework>" example official`, GitHub code/repositories search. Check LICENSE, README, last commit, version, example runs/issue reports. Stars are popularity signals, not truth.
- Primary papers/book chapters: `"<term>" DOI`, `"<term>" site:arxiv.org` when preprints pertinent; publisher/journal and institutional repositories; distinguish preprint from peer-reviewed text.
- Art/humanities: named work/artist/curator and exhibition catalog or institution → contemporary critical response → primary work documentation/artist statement → alternative interpretation. Never use decorative visual search as sufficient conceptual evidence.

**Search-dorking boundary:** only ordinary public indexed materials, no credential exposures, private files, leaked lecture portals, paywall bypass, robots-evasion, account scraping or bulk unauthorized downloads. Useful supported operators include exact phrase `"..."`, `site:`, `filetype:pdf`, `after:`, `before:`; not guaranteed exhaustive. Official Google documentation: https://developers.google.com/search/docs/monitor-debug/search-operators and https://support.google.com/websearch/answer/2466433

## One-click query generator

When the user wants click-to-search, give a working standard URL with URL-encoded terms and visible exact query; avoid unverifiable hand-built result links. Local optional script: `../../scripts/build_research_links.py` makes four links from a topic/goal. GitHub's `search` UI may require sign-in for code search. If direct search URL cannot be checked, present it as a *search query link*, not a verified result. Provide plain text query as fallback. The bundled generator runs with Python stdlib when local execution is available; otherwise generate the equivalent URLs directly.

## Output dossier schema

```yaml
profile_goal: 'independent real-time visual workflow'
profile_status: PROVISIONAL
subject_terms:
  - term: 'image processing'
    definition_source: 'pending field documentation'
    acceptance: CANDIDATE
resources:
  - title: ''
    author: ''
    url: ''
    role: OBJECT
    genre: SYLLABUS
    status: DISCOVERY_LEAD
    evidence_anchor: ''
    learner_level: ''
    license: UNKNOWN
    use: 'specific learning outcome'
    potential_rival: ''
rejected_or_contested_terms: []
open_debts: []
next_action: 'verify original syllabus'
```

## Consortium-compatible independent slices

When stakes and volume warrant, assign bounded roles: (A) outcome/profile verifier; (B) canonical terminology and primary sources; (C) professor/practitioner and critical alternatives; (D) provenance/licensing adversarial check. Keep worker packets independent; compare closures by source anchors before merging. Do not claim actual remote workers or tabs ran unless executed and witnessed. RMC's conditional gates govern decisions inside a slice, not a worker per reasoning stage. For ordinary small requests a single source scout is sufficient.
