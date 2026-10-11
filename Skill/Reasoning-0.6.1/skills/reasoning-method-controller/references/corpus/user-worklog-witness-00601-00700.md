# user-worklog-witness

Source ID: B02
Original attachment: Refernsi chain-of-thought yang aku mau Pasted text(20261004-220515).txt
Original lines: 601–700
Classification: historical-conversation. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

601: The chain need not be fully formal, but every critical invariant should point to its origin and verification evidence.
602: 
603: ## Closure semantics
604: 
605: A phase may advance only when its required outputs exist, blocking gates are approved, and structural verification does not report a fatal error. This gives AI work a termination condition rather than an open-ended impulse to keep restructuring.
606: 
607: END_FILE id=F0010
608: ====================================================================================================
609: BEGIN_FILE id=F0011 path=generated-project-layout.md kind=note lang=markdown lines=62 sha256=70713a535bf1785d6dd25be2d84a7577e85756ad09f981b3b68d8aa6c23660f6
610: ----------------------------------------------------------------------------------------------------
611: # Generated project layout
612: 
613: ```text
614: Project/
615: ├─ AGENTS.md
616: ├─ system-build-webses.md
617: ├─ PROJECT.local.code-workspace       # local-only operational workspace
618: ├─ .ppc/
619: │  ├─ project.json
620: │  ├─ intake.json                     # sanitized intake
621: │  ├─ constitution.json
622: │  ├─ topology.json
623: │  ├─ targets.json
624: │  ├─ providers.json
625: │  ├─ integrations.json
626: │  ├─ repos.json                      # public alias map; no raw paths
627: │  ├─ execution-strategy.json
628: │  ├─ scan-policy.json
629: │  ├─ privacy.json
630: │  ├─ toolchain-request.json
631: │  ├─ script-plan.json
632: │  ├─ environment/
633: │  │  └─ host.snapshot.json           # sanitized provenance/capabilities
634: │  ├─ private/                        # NEVER feed to AI / never commit
635: │  │  ├─ intake.runtime.json
636: │  │  └─ repos.runtime.json           # raw local paths required by PPC
637: │  ├─ state.json
638: │  ├─ approvals.json
639: │  ├─ evidence.json
640: │  ├─ requirements.json
641: │  ├─ tensions.json
642: │  ├─ invariants.json
643: │  ├─ plans.json
644: │  ├─ decisions.json
645: │  ├─ trace.json
646: │  ├─ ownership.json
647: │  ├─ logs/
648: │  └─ reports/
649: ├─ docs/
650: │  ├─ requirements/
651: │  ├─ spec/
652: │  ├─ interfaces/
653: │  ├─ decisions/
654: │  └─ handoff/
655: ├─ prompts/
656: │  ├─ INITIAL-FEED.md
657: │  └─ generated/
658: ├─ skills/
659: ├─ scripts/
660: │  ├─ ppc.py
661: │  └─ generated/
662: │     ├─ doctor.py
663: │     ├─ run-task.py
664: │     └─ <task>.ps1 / <task>.sh
665: └─ repos/
666:    └─ <generated repos only>
667: ```
668: 
669: Existing repositories may remain anywhere on the local machine. PPC stores their operational paths only in `.ppc/private/repos.runtime.json`; every AI-facing artifact uses `@repo/<alias>`.
670: 
671: The generated filesystem is a control-plane ontology. It does not imply that the product itself is local, monorepo, Windows-specific, Docker-specific, or VS Code-specific.
672: 
673: END_FILE id=F0011
674: ====================================================================================================
675: BEGIN_FILE id=F0012 path=modes.json kind=config lang=json lines=90 sha256=57e7817551ae90007d83b965be4bc98592c869781251589440d131a123924988
676: ----------------------------------------------------------------------------------------------------
677: {
678:   "greenfield": {
679:     "label": "Greenfield build",
680:     "phases": [
681:       "discovery",
682:       "planning",
683:       "contract",
684:       "probe",
685:       "topology",
686:       "implementation",
687:       "verification",
688:       "handoff"
689:     ],
690:     "gates": {
691:       "planning": "Plan selection must be explicitly approved before contract commitment.",
692:       "probe": "Probe must be explicitly approved before full implementation."
693:     },
694:     "initial_phase": "discovery"
695:   },
696:   "bugfix": {
697:     "label": "Existing repo bug fix",
698:     "phases": [
699:       "repo_evidence",
700:       "reproduction",
