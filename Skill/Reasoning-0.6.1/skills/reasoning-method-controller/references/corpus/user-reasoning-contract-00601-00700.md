# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 601–700
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

601: to discover whether its premise works.
602: ```
603: 
604: Instead construct the smallest witness capable of testing the critical assumption.
605: 
606: Examples:
607: 
608: ```text
609: one MIDI file
610: one DAW operation
611: one database record
612: one embedding query
613: one parsing path
614: one transformation invariant
615: one paragraph reconstruction
616: ```
617: 
618: A probe must answer a specific uncertainty.
619: 
620: Bad probe:
621: 
622: ```text
623: "Let's build an MVP."
624: ```
625: 
626: Good probe:
627: 
628: ```text
629: "Can the Studio Pro bridge read notes,
630: modify one note,
631: and verify the changed value through readback?"
632: ```
633: 
634: ---
635: 
636: # XIV. Stage 12 — Propagate Invariants
637: 
638: Critical intent must survive transformations.
639: 
640: Example:
641: 
642: ```text
643: User statement
644:     ↓
645: REQ-04
646:     ↓
647: INV-02
648:     ↓
649: Architecture decision
650:     ↓
651: API contract
652:     ↓
653: Implementation
654:     ↓
655: TEST-09
656: ```
657: 
658: If an important requirement disappears between stages, that is an error even when the code works.
659: 
660: Use the question:
661: 
662: ```text
663: Where is this requirement represented now?
664: ```
665: 
666: at every major transformation.
667: 
668: ---
669: 
670: # XV. Stage 13 — Verification Must Target Claims
671: 
672: Verification should not merely ask:
673: 
674: ```text
675: "Does it run?"
676: ```
677: 
678: It should ask:
679: 
680: ```text
681: Which claim are we attempting to establish?
682: ```
683: 
684: Examples:
685: 
686: ```text
687: CLAIM:
688: Normalization preserves expressive contour.
689: 
690: TEST:
691: Measure rank/correlation of relative velocity contour before and after transformation.
692: ```
693: 
694: ```text
695: CLAIM:
696: The interpretation follows Bhaskar's argument.
697: 
698: TEST:
699: Identify textual premises and verify that the reconstructed inference does not require a premise absent from the text.
700: ```
