# user-worklog-witness

Source ID: B02
Original attachment: Refernsi chain-of-thought yang aku mau Pasted text(20261004-220515).txt
Original lines: 701–800
Classification: historical-conversation. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

701:       "repair_plan",
702:       "probe",
703:       "repair",
704:       "verification",
705:       "handoff"
706:     ],
707:     "gates": {
708:       "probe": "Repair probe/reproduction must be approved before broad repair when scope is costly or invasive."
709:     },
710:     "initial_phase": "repo_evidence"
711:   },
712:   "refactor": {
713:     "label": "Existing repo refactor",
714:     "phases": [
715:       "repo_evidence",
716:       "invariants",
717:       "planning",
718:       "probe",
719:       "implementation",
720:       "verification",
721:       "handoff"
722:     ],
723:     "gates": {
724:       "planning": "Refactor plan must be explicitly approved.",
725:       "probe": "Behavior-preserving probe must pass and be approved before broad refactor."
726:     },
727:     "initial_phase": "repo_evidence"
728:   },
729:   "migration": {
730:     "label": "Migration",
731:     "phases": [
732:       "repo_evidence",
733:       "target_evidence",
734:       "planning",
735:       "contract",
736:       "probe",
737:       "implementation",
738:       "verification",
739:       "handoff"
740:     ],
741:     "gates": {
742:       "planning": "Migration route must be explicitly approved.",
743:       "probe": "Migration witness must be approved before broad migration."
744:     },
745:     "initial_phase": "repo_evidence"
746:   },
747:   "integration": {
748:     "label": "Integration",
749:     "phases": [
750:       "discovery",
751:       "boundary_evidence",
752:       "planning",
753:       "contract",
754:       "probe",
755:       "implementation",
756:       "verification",
757:       "handoff"
758:     ],
759:     "gates": {
760:       "planning": "Integration plan must be explicitly approved.",
761:       "probe": "Cross-boundary probe must be approved before full implementation."
762:     },
763:     "initial_phase": "discovery"
764:   }
765: }
766: 
767: END_FILE id=F0012
768: ====================================================================================================
769: BEGIN_FILE id=F0013 path=ownership-model.md kind=note lang=markdown lines=13 sha256=ca13cd067af0f3ee621b16de440b7f4fe2d04073b2b2dc8f43b76e911c65fde8
770: ----------------------------------------------------------------------------------------------------
771: # File ownership model
772: 
773: PPC separates:
774: 
775: - **authority** — source of truth for a fact;
776: - **maintainer** — who/what may change it;
777: - **generation** — authored/generated/mirrored/external;
778: - **AI transportability** — whether it may appear in a feeder.
779: 
780: The strongest boundary is `.ppc/private/**`: it exists only so local tooling can resolve real repository locations and other operational details. It is CLI-owned, ignored by project Git, protected from AI ingest, and excluded from prompt compilation.
781: 
782: Scanner-owned host provenance is similarly protected from AI mutation. AI may challenge the interpretation of scanner evidence through decisions/execution strategy, but may not rewrite the observed snapshot.
783: 
784: END_FILE id=F0013
785: ====================================================================================================
786: BEGIN_FILE id=F0014 path=privacy-boundary.md kind=note lang=markdown lines=12 sha256=1442b79853d70e39e05c2325c3dfebd5fc121961df61bbef5eacb01101ae693d
787: ----------------------------------------------------------------------------------------------------
788: # Scanner privacy boundary
789: 
790: AI-facing scanner output is sanitized by construction. PPC does not intentionally collect environment-variable values, credentials, tokens, SSH keys, hostname, username, IP/MAC addresses, or cloud account/tenant/subscription identifiers. Raw local repository paths are stored only in `.ppc/private/repos.runtime.json`, which is excluded from AI feeders and project Git.
791: 
792: Scan depth:
793: 
794: - `capability` (default): recognized compilers, interpreters, package managers, shells, IDE/CLIs, container and cloud CLIs; versions only.
795: - `targeted`: capability scan + repository dependency declarations + only tools/packages requested in `.ppc/toolchain-request.json`.
796: - `full`: opt-in installed-package inventory for supported managers. Use only when the diagnostic value exceeds fingerprinting/noise cost.
797: 
798: Cloud account queries are not performed by the core scanner. Presence/version of a CLI is evidence of a capability, not evidence of authentication or permissions.
799: 
800: END_FILE id=F0014
