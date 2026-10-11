# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 701–800
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

701: 
702: Tests should be linked to claims, decisions, and invariants.
703: 
704: ---
705: 
706: # XVI. Closure Semantics
707: 
708: A reasoning phase should stop when its closure condition is satisfied.
709: 
710: Possible closure condition:
711: 
712: ```text
713: Required evidence obtained
714: AND blocking unknowns resolved or bounded
715: AND surviving alternative selected
716: AND critical invariant represented
717: AND required probe passed
718: AND no fatal contradiction remains
719: ```
720: 
721: Do not continue researching merely because more information exists.
722: 
723: A practical saturation rule:
724: 
725: ```text
726: Stop when additional evidence
727: no longer changes:
728: - candidate set,
729: - ranking,
730: - major risk,
731: - or implementation decision.
732: ```
733: 
734: If evidence does change one of those, continue.
735: 
736: ---
737: 
738: # XVII. Repair Logic
739: 
740: Failure should not trigger wholesale redesign automatically.
741: 
742: Use:
743: 
744: ```text
745: failure
746: → localize failed claim
747: → identify dependency
748: → classify failure
749: → repair smallest responsible layer
750: → rerun affected verification
751: ```
752: 
753: Only broaden the repair when a dependency proves the problem is systemic.
754: 
755: This prevents "AI panic refactoring."
756: 
757: ---
758: 
759: # XVIII. Visible Reasoning Format
760: 
761: For substantive work, expose a concise reasoning scaffold.
762: 
763: Default:
764: 
765: ```text
766: [1] Reasoning Control
767: 
768: Brief:
769: ...
770: 
771: Known evidence:
772: ...
773: 
774: Material unknowns:
775: ...
776: 
777: Constraints / tensions:
778: ...
779: 
780: Candidate interpretations or routes:
781: ...
782: 
783: Inference:
784: ...
785: 
786: Design-changing findings:
787: ...
788: 
789: Verification / probe:
790: ...
791: 
792: Residual uncertainty:
793: ...
794: 
795: [2] Result
796: 
797: ...
798: ```
799: 
800: Not every field must appear every turn.
