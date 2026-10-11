# Retrieval validity and graduation-profile evidence ladder

Purpose: assemble a teachable, provenance-aware source set from a learner-defined performance target. The number of sources is NOT an adequacy test: inspect their independence and roles.

## Build outcome profile, not a made-up credential

A 'graduate profile' might mean an accredited program's outcomes, a professional's independent capability, or a portfolio target. Do not invent a degree name, formal recognition, course credit, institution, salary, hours-to-mastery, or qualification equivalence. Keep user goals primary. Where institutional comparators help, seek local frameworks (e.g. university published learning outcomes), professional bodies (e.g. ABET for computing), national qualification frameworks, and authentic capstone artifacts; name which comparator was actually examined. MIT OCW course level is not automatically equivalent to the user's level.

Profile record:

```yaml
profile_id: learner-portfolio-01
status: DRAFT   # AGREED only after explicit learner assent
orientation: 'Independently design and troubleshoot a real-time visual project'
context: 'portfolio, not accredited qualification'
performance_outcomes:
  - id: O1
    action: 'route image and control signals to a testable visual output'
    evidence: 'project file + expected screenshot + parameter test'
    standard: 'tested against declared tool/version'
source_comparators: []
disputed_or_missing: []
```

## Source suitability scorecard (do not turn into a pseudo-exact numeric grade)

Inspect **authority to support this *claim***, inspectability, source origin (direct/secondary/anonymous), date and target software version, level/audience, independent corroboration for material uncertainty, relevance to outcome, task/assessment availability, copyright/license and realistic access. Record `VERIFIED_PRIMARY`, `VERIFIED_SECONDARY`, `DISCOVERY_LEAD`, `UNVERIFIED`, `DISPUTED`, `REJECTED` with reason. A faculty blog may be authoritative for an instructor's own design rationale but not a controlled evaluation of efficacy. GitHub popularity is not validation.

Examples of independent corroboration: official course syllabus and official documentation for a software operation; a subject benchmark and at least one actual course syllabus for learning outcome structure; a critical blog and a scholarly paper for contested history. Do not demand arbitrary two-sources for one versioned UI command when official documentation already controls.

## Evidence routing and triangulation

1. CURRICULUM: published program outcome → identify terms and skills expected, discipline and level.
2. OBJECT: field definitions and canonical concepts → verify exact wording, dates, versions, sources.
3. EXEMPLAR: lecture/lab/problem set/artwork/source-code exercise → verify authentic provenance and attainable difficulty.
4. COUNTERSOURCE: serious criticism, rival method, negative example → record the *claim it challenges*, not just name or URL.
5. METHODS: educational psychology and format advice → decide how to teach, NEVER what target domain necessarily contains.

When browsing, report a source card at least with `title; author; affiliation (confirmed/unconfirmed); URL; source type; target level; relevant extract/paraphrase; method vs object role; verification; license; freshness/version; use in module; disagreement; next check`. Distinguish reuse rights from public view access. Never copy all textbook chapters or distribute user-supplied copyrighted books in a plugin.

## Claim-to-lesson tests

- Remove every METHOD bibliography entry: are student-facing topics still supported by OBJECT sources? If not, the course has suffered *method capture*.
- Replace names with citations: can each key topic be found in the indicated work? If not, return to retrieval.
- Show a student outcome without the famous institution: is there still a testable skill and feasible artifact? If not, refine profile.
- Counterexample check: what real course/practice differs, and would that imply a different dependency ordering? If so, preserve alternatives.
- Rights check: can the source legally be remixed, or only read/cited? If uncertain, link and paraphrase; no downloading/copying into course package.

## Reference anchor shortlist (verified public pages, reverify at lesson time)

- UNESCO OER definition/licensing: https://www.unesco.org/en/open-educational-resources
- Creative Commons TASL: https://wiki.creativecommons.org/wiki/Best_practices_for_attribution
- MIT OCW usage and limits: https://ocw.mit.edu/pages/get-started/
- MIT Open Learning Library interactive assessments (different license regime): https://ocw.mit.edu/collections/mit-open-learning-library/
- ABET computing 2026–27 examples of student outcomes, **discipline specific**: https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-computing-programs-2026-2027/
- Sanjoy Mahajan MIT OCW 18.098 actual syllabus and assignments: https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/pages/syllabus/
- GitHub `prakhar1989/awesome-courses` = discovery index, verify original institutional page: https://github.com/prakhar1989/awesome-courses
- GitHub `MarcosSete/awesome-free-ai-course-notes` = discovery index, inspect each linked instructor page: https://github.com/MarcosSete/awesome-free-ai-course-notes
