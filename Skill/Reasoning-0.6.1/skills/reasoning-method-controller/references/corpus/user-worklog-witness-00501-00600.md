# user-worklog-witness

Source ID: B02
Original attachment: Refernsi chain-of-thought yang aku mau Pasted text(20261004-220515).txt
Original lines: 501–600
Classification: historical-conversation. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

501: ----------------------------------------------------------------------------------------------------
502: # Python project adapter
503: 
504: Record supported Python version, package/runtime boundary, dependency authority, entry points, configuration/secrets, persistence, test command, lint/type-check commands if used, and packaging/deployment expectations. Keep the bootstrapper itself standard-library-only unless the project contract says otherwise.
505: 
506: END_FILE id=F0006
507: ====================================================================================================
508: BEGIN_FILE id=F0007 path=environment-adapters/webapp.md kind=note lang=markdown lines=4 sha256=c60c12d6dd8a9e7965404011722454b35682f4898b6c0c08951ebffdfcc3bf2b
509: ----------------------------------------------------------------------------------------------------
510: # Web application adapter
511: 
512: For a general web app, identify frontend runtime, backend/runtime if any, data authority, auth boundary, deployment target, environment variables, persistence, observability, and one vertical walking-skeleton probe that crosses the real boundaries.
513: 
514: END_FILE id=F0007
515: ====================================================================================================
516: BEGIN_FILE id=F0008 path=environment-model.md kind=note lang=markdown lines=14 sha256=64b35cdeaa95dc9a08606a5b20a825be53ac556cfcdbc1609687fd835e7966cf
517: ----------------------------------------------------------------------------------------------------
518: # Environment model
519: 
520: PPC separates **provenance**, **target compatibility**, **execution substrate**, **provider/service**, and **integration/transport**.
521: 
522: `host.snapshot.json` answers: *where and with what capabilities is this project currently being worked on?*
523: 
524: `targets.json` answers: *where must the resulting artifact execute or remain compatible?*
525: 
526: `topology.json` answers: *what nodes and boundaries constitute the project?*
527: 
528: `execution-strategy.json` answers: *given provenance + targets + constraints, what is the least-friction build/execution strategy?*
529: 
530: A project created on Windows may intentionally target Linux; a Mac ARM host may build Linux AMD64 through Docker Buildx or remote CI. Creation provenance must never silently narrow product compatibility.
531: 
532: END_FILE id=F0008
533: ====================================================================================================
534: BEGIN_FILE id=F0009 path=evidence-policy.md kind=note lang=markdown lines=26 sha256=15a9e83353820a14dc223968fcdaeeab55a8100a9c5a342d6f0d44682112d19f
535: ----------------------------------------------------------------------------------------------------
536: # Evidence policy
537: 
538: Evidence source depends on project mode.
539: 
540: ## Greenfield
541: 
542: Start from problem/context/use cases. External open-source references may be used to find approaches and heuristics. Search budget is a saturation heuristic, not a sacred count: stop when additional sources add no materially new pattern; continue when the candidate architecture is still changing.
543: 
544: Classify references as:
545: 
546: - `stem`: a plausible architectural lineage for the project;
547: - `borrow`: a specific heuristic/module/pattern worth taking;
548: - `filter`: an approach explicitly rejected, with reason.
549: 
550: ## Existing repo / bugfix
551: 
552: Start from local evidence:
553: 
554: 1. repository structure and manifest files;
555: 2. reproduction/failure signal;
556: 3. tests, logs, issues, and recent diffs/history;
557: 4. relevant source path and dependency boundaries;
558: 5. external references only when local evidence leaves a material unknown.
559: 
560: This avoids doing greenfield research when the repository itself is the primary evidence source.
561: 
562: END_FILE id=F0009
563: ====================================================================================================
564: BEGIN_FILE id=F0010 path=formal-model.md kind=note lang=markdown lines=41 sha256=da1164b8c8325fb93b57213baad3c12c2320e8b8ccce7d68c20a62192b6d09d9
565: ----------------------------------------------------------------------------------------------------
566: # Formal model
567: 
568: PPC models project work as typed transformations rather than a pile of documents.
569: 
570: ```text
571: Source input
572:   -> Evidence
573:   -> Normalized primitives
574:   -> Candidate plans
575:   -> Hard-constraint elimination
576:   -> Comparative selection
577:   -> System contract
578:   -> Small probe / architecture witness
579:   -> Approval gate
580:   -> Full implementation
581:   -> Verification
582:   -> Repair or release/handoff
583: ```
584: 
585: ## Three normative levels
586: 
587: 1. **Global constitution**: reusable rules of the compiler/work method.
588: 2. **Project constitution**: constraints and bans specific to this project.
589: 3. **Task/phase instruction**: what the current AI/agent is asked to do.
590: 
591: These answer *where a rule gets authority*.
592: 
593: ## Invariant propagation
594: 
595: Invariant propagation answers a different question: does an important rule/decision remain represented through later transformations?
596: 
597: ```text
598: OBS-004 -> DEC-002 -> INV-003 -> SRS-007 -> TEST-005
599: ```
600: 
