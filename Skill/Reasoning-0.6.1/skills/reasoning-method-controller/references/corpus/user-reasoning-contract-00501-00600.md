# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 501–600
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

501: ```text
502: candidate generation
503: → hard constraint check
504: → eliminate impossible candidates
505: → compare surviving candidates
506: ```
507: 
508: Hard constraints may include:
509: 
510: ```text
511: platform compatibility
512: license
513: privacy
514: budget
515: latency
516: hardware
517: source fidelity
518: required determinism
519: API availability
520: commercial-use requirements
521: academic corpus restrictions
522: ```
523: 
524: This avoids spending reasoning effort optimizing an impossible design.
525: 
526: ---
527: 
528: # XI. Stage 9 — Comparative Inference
529: 
530: For surviving alternatives, compare using explicit dimensions.
531: 
532: Example:
533: 
534: ```text
535:                 A       B       C
536: Accuracy        +       ++      +
537: Cost            ++      -       +
538: Portability     +       ++      -
539: Reproducible    ++      +       +
540: Risk            low     med     high
541: ```
542: 
543: The objective is not numerical pseudo-precision.
544: 
545: The objective is to make the **selection warrant** visible.
546: 
547: A recommendation should follow the form:
548: 
549: ```text
550: Given constraints C1–C4,
551: and evidence E1–E6,
552: candidate B dominates A on X and C on Y,
553: while its main residual risk is Z.
554: 
555: Therefore B is the current preferred route.
556: ```
557: 
558: ---
559: 
560: # XII. Stage 10 — Detect Design-Changing Findings
561: 
562: Not every discovered fact deserves equal attention.
563: 
564: A finding is especially important when:
565: 
566: ```text
567: without it → Decision A
568: with it    → Decision B
569: ```
570: 
571: These should be explicitly surfaced as:
572: 
573: ```text
574: DESIGN-CHANGING FINDING
575: ```
576: 
577: Examples:
578: 
579: ```text
580: The library cannot read the target file format.
581: 
582: The model's license excludes commercial use.
583: 
584: The target DAW exposes no required API.
585: 
586: The dataset domain does not match the intended instrument.
587: 
588: The claimed normalization destroys an invariant.
589: ```
590: 
591: This makes progress intelligible.
592: 
593: ---
594: 
595: # XIII. Stage 11 — Use Probes Before Expensive Commitment
596: 
597: When uncertainty is high and implementation cost is large:
598: 
599: ```text
600: do not build the architecture
