# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 401–500
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

401:    ↓
402: interpretation
403:    ↓
404: evaluation
405:    ↓
406: recommendation
407: ```
408: 
409: Never reverse it:
410: 
411: ```text
412: desired recommendation
413:    ↓
414: select convenient evidence
415: ```
416: 
417: When the distinction matters, phrase findings as:
418: 
419: ```text
420: Source establishes:
421: ...
422: 
423: I infer:
424: ...
425: 
426: This inference assumes:
427: ...
428: 
429: An alternative reading is:
430: ...
431: 
432: The decision changes if:
433: ...
434: ```
435: 
436: ---
437: 
438: # VIII. Stage 6 — Identify Tensions, Not Merely Requirements
439: 
440: Many design problems are structured by competing goods.
441: 
442: Examples:
443: 
444: ```text
445: accuracy ↔ compute cost
446: 
447: generalization ↔ domain specialization
448: 
449: automation ↔ inspectability
450: 
451: flexibility ↔ reproducibility
452: 
453: local inference ↔ model quality
454: 
455: semantic richness ↔ annotation cost
456: 
457: fast implementation ↔ architectural durability
458: ```
459: 
460: Do not prematurely "solve" a tension.
461: 
462: First identify whether it is:
463: 
464: ```text
465: a genuine trade-off
466: a false dichotomy
467: a sequencing problem
468: an abstraction problem
469: an optimization problem
470: or an unresolved empirical question
471: ```
472: 
473: Often the correct solution changes once the kind of tension is identified.
474: 
475: ---
476: 
477: # IX. Stage 7 — Generate Constrained Alternatives
478: 
479: Do not immediately elaborate the first plausible solution.
480: 
481: Produce a bounded candidate set:
482: 
483: ```text
484: HYP-A
485: HYP-B
486: HYP-C
487: ```
488: 
489: Candidates should be meaningfully different, not cosmetic variants.
490: 
491: Then compare them under common criteria.
492: 
493: ---
494: 
495: # X. Stage 8 — Eliminate by Hard Constraints First
496: 
497: Before ranking candidates by elegance, remove those that violate hard constraints.
498: 
499: Canonical sequence:
500: 
