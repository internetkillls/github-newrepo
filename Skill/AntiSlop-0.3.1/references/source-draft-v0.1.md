**# Anti-Slop Spec v0.1**



Compiled 2026-10-09. Nine slop classes, one deterministic cascade, one repo compilation.



**## Posisi**



1\. Object. Slop here is output that is locally well-formed and globally uninformative or unwarranted. Each of the nine classes you named has one recurring failure shape, listed in Analysis A with its source thread.

2\. Method. A detector is an artifact that returns the same verdict on the same input. The LLM is confined to extraction into a fixed schema. Verdicts come from code, and from a formal checker wherever a formalism exists (AST, regex, CAS, Lean). Two reasons: LLM judges can be gamed, and Wikipedia's editors state that surface signs are symptoms of deeper defects, so repairing the signs alone hides the defect and makes detection harder.

3\. Sources. Your history supplies failure signatures. Public repositories supply lexicons and checkers. Where nothing public exists (Indonesian), the spec says so and gives a build path.

4\. Sequence. Analysis A recalls the corpus. Analysis B fixes the cascade. Analysis C gives per-class reasoning. Output gives the master table, the repo compilation, the corpus schema, and the assumptions.



**## Analysis**



**### A. Recalled corpus**



Scope: these rows are your critiques of GPT-side sessions and of drafts, as you stated them. Raw GPT transcripts were not in view, so no row is a measured output.



\| ID | Class | Failure signature | Source thread |

\|---|---|---|---|

\| Q-01 | query | Sound inference over wrongly indexed external knowledge: Chalmers and Quine read as research references where you use them as guardrails for discussion with you | Reasoning Method Controller, Session 1 |

\| Q-02 | query | Name-based search missed the substantive pages; thematic search plus parallel fetch found them | Learning and research strategy |

\| W-01 | writing | Summarizing closers | standing preference |

\| W-02 | writing | Contrastive "ini bukan A, tetapi B" used as a distinguishing move | standing preference |

\| W-03 | writing | Unsourced metaphor ("lantai"); a term reused in a second sense without a flag | standing preference |

\| W-04 | writing | Preamble and filler; one explanation repeated in the same phrasing when it failed to land | standing preference |

\| L-01 | interaction | Governing question re-posed five times; the fifth (transport to priority) drifted unmarked between turn 1 and turn 10 | distributor argument |

\| L-02 | interaction | Assistant proposals absorbed as commitments; kept apart as "proposed, not adopted" | distributor argument |

\| L-03 | interaction | GPT sketch and skill wrong despite the Claude chain-of-thought reference supplied | GPT reasoning contract |

\| S-01 | sense-making | Labels (transcendental, sui generis, epistentrum) placed at the hardest point of analysis, where an explanation was due | distributor argument |

\| S-02 | sense-making | "Too many seen, few understood": accumulation of information without understanding | distributor argument |

\| I-01 | Indonesian | Register drift away from the Suryajaya register; contrastive construction (W-02) | standing preference |

\| N-01 | naming | Vault convention is predicate-first directional bigrams (from/to) over ID strings; extension to code identifiers is untested | Obsidian redesign |

\| C-01 | coding | Four layered bugs, all structurally valid: hardcoded lyric strings, constant suffering vectors, deterministic pitch hashing, static imagery | diary-to-song system |

\| C-02 | coding | Kernel, backend and UI layers conflated | PromptForge |

\| C-03 | coding | Bash mount served stale OneDrive copies; Read is the authority | Josh Interface |

\| A-01 | argument | Drafts lack explicit concise argument distribution: "erotetic illusion without iuris premises" | distributor argument |

\| A-02 | argument | Epistemic-to-normative leaps left undefended | Learning and research strategy |

\| A-03 | argument | Equivocal coinage ("transcendental transport signifier"); "distorted" presupposes an undistorted original; "ameliorative" taken as the centre | distributor argument |

\| M-01 | mathematics | No incident recorded. Seeded by your requirements: deterministic output, 4 dp rounding, stated assumptions | standing preference |



**### B. Cascade**



\- L0, deterministic scan: lexicon, regex, AST, schema validation. Cheap, same verdict every run.

\- L1, extraction: the LLM converts text into typed records (queries, claims, identifiers, proof blocks) under a JSON schema at temperature 0, model version pinned. It never says pass or fail.

\- L2, predicates: code evaluates the records against the class gates in the master table. A failed gate triggers regeneration with the failing record quoted back.

\- L3, adversary, residual only: an LLM pass states the strongest opposing reading of what survived L2. Two independent passes (different prompts, ideally different models) must agree; disagreement goes to you.

\- L4, regression: every confirmed slop instance becomes a labeled row in the corpus (schema in Output). The cascade is re-run over the corpus whenever a prompt, model or threshold changes.



Why L1 is extraction only: the EQ-Bench Creative Writing autograder shows the failure of LLM-as-judge (Surge reports agreement with expert writers as low as 43% in some categories; Surge runs a competing leaderboard, so weigh it accordingly). DeepResearch Bench's RACE scoring does use a judge LLM, but against reference reports with adaptive criteria, which is closer to extraction against a fixed rubric.



**### C. Per-class reasoning**



**\*\*1 Browsing queries.\*\*** The recorded failure sits in indexing, with inference intact (Q-01), and thematic search outperformed name search (Q-02). Public work measures query quality thinly: the open-deep-research paper (arXiv 2508.10152) observes that earlier benchmarks do not test autonomous query generation, and Dr.Mi-Bench scores planning, retrieval and reasoning as separate modules, which is the decomposition needed here. A query becomes a record: object, discriminating predicate, source type, falsifier, role. Gates: at least one discriminating token absent from the user's prompt; lexical overlap with every earlier query below a threshold; a source-type tag from a closed list; a fixed share of adversarial queries (your X tag for counter-literature).



**\*\*2 Writing.\*\*** Lexical and structural tells are deterministic: word lists, em-dash counts, "it's not X, it's Y" patterns, over-represented trigrams. The Antislop paper defines overuse as the ratio ρ(p) = f_LLM(p) / f_human(p) and reports patterns above 1,000x. Your own constraints (W-01 to W-04) form a lexicon no public list has. The lexicon score is a flag. The pass condition is the removal test: the L1 extractor lists the claims each sentence carries, and any sentence with zero claims that is not on a connective whitelist is flagged. slopkit's author likewise holds that chasing detectors degrades prose.



**\*\*3 Linear monolith.\*\*** L-01 and L-02 are interaction-level slop: the governing question shifts without a mark, and the assistant's proposals harden into commitments. LongMemEval (500 questions) names five abilities a history store needs (extraction, multi-session reasoning, temporal reasoning, knowledge update, abstention) and reports a 30% accuracy drop for commercial assistants and long-context models over sustained interaction. Its better designs decompose sessions, expand keys with facts, and expand queries with time. Compressing to bare facts costs overall accuracy and helps multi-session reasoning, so the store keeps both. Replace the transcript with three tables in one markdown file: a Question register (governing question, marked by, consented y/n, supersedes), a Claim table (status in stated, accepted, offered-not-adopted, superseded; origin; date), a Sense register (term, sense id, originator, first use). Gates: a turn that changes the governing question appends a register row; any claim originating with the assistant is created as offered-not-adopted; one term with two sense ids in one document fails.



**\*\*4 Sense-making.\*\*** S-01 and S-02 share a shape: a word stands where a mechanism was due. Admission rule: a term enters a document with provenance (originator, source-language form), one sense, one worked case, one sibling or counter case. Substitution test: replace the term with its definition; if the sentence stops being truth-evaluable, the term was a label. Active Apprehension's open fork (does Stress-test re-contact the world, or check only the model's coherence?) applies directly: an LLM judging coherence performs a coherence check, so admission requires external contact, meaning a retrieved source or a case.



**\*\*5 Indonesian.\*\*** No curated Indonesian slop lexicon was found; awesome-slop covers Korean, Russian, Chinese, Vietnamese and Filipino. Tells reported in Indonesian press come from English-language sources (generic openers such as "Pernahkah Anda bertanya-tanya" and "Di era digital saat ini", uniform formal positivity, em-dash overuse); one copywriter post adds sentence-initial "tapi", four-clause paragraphs and emoji bullets. All of it is anecdotal. Measured resources exist for the baseline: IndoNLU supplies Indo4B (23 GB, about four billion words) and IndoBERT; a Telkom University study trains an IndoBERT classifier for human versus AI sentences (detection, no repair); IndoMMLU measures competence, not style. Build: run the Antislop pipeline in Indonesian. Human baseline: your own Indonesian writing plus an Indo4B sample. LLM sample: identical prompts across several models. Keep n-grams with ρ above a threshold and above a frequency floor. The sampler's README itself advises rolling your own list. Layer your preference rules (Suryajaya register, W-02, 200-word ceiling) on top as the rule pack.



**\*\*6 Naming.\*\*** arXiv 2506.12014 reports an LLM preference for longer, descriptive snake_case names and rising adoption of that style in GitHub repositories. Practitioner write-ups (weak sources) describe a swing between hyper-descriptive names and generic ones (temp, data, helper). Each name is locally plausible; the defect is inconsistency across files, one concept under several names. Detection research exists: a University of St. Gallen study built more than 6,000 annotations over 28 naming guidelines. Design: a glossary-first contract (concept, canonical identifier tokens, forbidden aliases), executable. Gates: banned generic tokens outside narrow scopes; alias collision; identifier tokens inside the glossary or the language and framework vocabulary; name-length z-score against the project baseline. The LLM proposes glossary entries from the spec and never judges a name.



**\*\*7 Coding.\*\*** Public detectors catch structure: stubs, phantom imports, disconnected pipelines, clone clusters, inflated docs (AI-SLOP-Detector); deferral, hedge and placeholder language via regex plus AST (antislop, distributed on crates.io and npm); comment slop with why-comments preserved (athola slop-detector); PR-level classification on public repos without blocking merges (CodeRabbit). None checks whether output varies with input. C-01 passes every structural check: the code runs, the types hold, the output is constant. The detector is metamorphic testing (T. Y. Chen et al., technical report, 1998): perturb an input along an axis the spec says matters and assert the output changes by a stated relation; perturb along an axis that must not matter and assert invariance. Add your standing rules as gates: no new layer until the layer below passes its tests (C-02); hard exit with install instructions in place of an API fallback; credentials from environment variables; verify file state with Read (C-03).



**\*\*8 Argument.\*\*** A-01 to A-03 ask for explicit distribution of the argument from its source, which is your own thesis about how an argument travels. Public fallacy work argues against free-form judging. Jin et al. (LOGIC, 2,449 samples over 13 types) found pretrained LLMs poor, with a structure-aware classifier ahead by 5.46 F1. SmartyPat-Bench (502 sentences) reports that longer reasoning chains hurt detection while structured reasoning helps categorization. So structure comes first. Each inference becomes a record: conclusion; premises, each with a source id; warrant (Toulmin, *\*The Uses of Argument\**, 1958); the question it answers; defeater. Gates: conclusion without premise ids; premise without source; an adjective predicated of an argument (valid, pivotal, ameliorative) without a question index; a normative conclusion whose premises include no normative source; one term with two sense ids. L3 states the strongest opposing view first and names a sibling case in the history of thought, which is your correction format.



**\*\*9 Mathematics.\*\*** Where a statement formalizes, Lean checks the proof deterministically. Brando Miranda argues (June 2026) that judging effort belongs on whether the formal statement is the right theorem, because a valid proof of a wrong statement is worse than no proof. For natural-language proofs, Pseudo-Formalization with Block Verification (Stanford, arXiv 2605.20531) rewrites a proof into blocks checked independently, and its ArxivMathGradingBench holds 35 papers with 40 known errors. A graduate-level Lean 4 benchmark (arXiv 2603.26996) rests on the same premise: natural-language solutions can hide subtle errors that human and LLM graders both miss. For your level: every number produced by code, rounded to 4 dp, inputs echoed; symbolic steps checked in a CAS (sympy, assuming Python is available); proofs cut into blocks that each carry their hypotheses; Lean where the statement formalizes. The LLM extracts blocks and translates statements. The verdict comes from sympy or Lean.



**## Output**



**### 1. Master table**



\| Class | L0 deterministic | L1 extracts | L2 gate (fail means regenerate) | Repair rule |

\|---|---|---|---|---|

\| Browsing queries | Token overlap against prior queries; closed source-type list | Query records: object, predicate, source type, falsifier, role | No new discriminating token; overlap above threshold; no adversarial share; missing source type | Rewrite with the missing field; add an adversarial query |

\| Writing | Lexicon, em-dash and trigram counts, contrast-pattern regex, your W-pack | Claims per sentence | Sentence with zero claims, not connective; W-pack hit | Delete the sentence or attach its claim; never swap synonyms |

\| Linear monolith | Schema validation of the three tables | Governing question per turn; claim origin; term senses | Question changed with no register row; assistant claim not born as offered-not-adopted; two senses for one term | Append the row; re-mark status |

\| Sense-making | Term register completeness | Terms, definitions, cases | Term without provenance, sense, worked case or sibling case; substitution test fails | Define or delete the term |

\| Indonesian | ρ-lexicon from your baseline; rule pack | Sentence-level register tag | Lexicon hit above threshold; W-02 pattern; length ceiling | Rewrite the sentence from its claim, not from the flagged phrase |

\| Naming | Generic-token list; glossary membership; alias table | Identifier to concept map | Banned token; alias collision; out-of-glossary token | Rename to the canonical form; extend the glossary by decision |

\| Coding | AST: stubs, phantom imports, clones; tests | Spec axes (matters / must not matter) | Metamorphic relation fails; layer rule broken | Fix the layer below first |

\| Argument | Argument-record schema validation | Conclusion, premises, source ids, warrant, question, defeater | Missing premise id or source; unindexed argument adjective; normative leap; two senses | Supply the premise or withdraw the conclusion |

\| Mathematics | sympy; Lean; rounding to 4 dp | Proof blocks with hypotheses; formal statement | Block fails check; statement unverified against intent; unechoed input | Repair the block; re-state the theorem before proving |



**### 2. Repository and paper compilation**



All entries were located through search listings, and awesome-slop was fetched in full. None was cloned or run. Star counts are as listed on the cited date.



\| Resource | Class | What it gives | Caveat |

\|---|---|---|---|

\| [hwajongpark/awesome-slop]\(https\://github.com/hwajongpark/awesome-slop) | writing, languages | Curated list by language: research, linters, classifiers, humanizers, word lists | 5 stars; the maintainer also maintains slop-gate and discloses it; no Indonesian |

\| [hwajongpark/slop-gate]\(https\://github.com/hwajongpark/slop-gate) | writing | Zero-dependency CLI; em-dash and about 40 English tells; JSON rule packs per language | Listed by awesome-slop; not fetched |

\| [sam-paech/antislop-sampler]\(https\://github.com/sam-paech/antislop-sampler) | writing | Backtracking sampler; thousands of phrases and regex patterns; ICLR 2026 | Needs control of decoding, so local models only (inference); backtracking slows throughput |

\| [sam-paech/auto-antislop]\(https\://github.com/sam-paech/auto-antislop) and [arXiv 2510.15061]\(https\://arxiv.org/abs/2510.15061) | writing, Indonesian | Pipeline to profile model-specific slop against a human baseline (the ρ method); FTPO fine-tuning | Default list is auto-generated and uncurated by the authors' own note |

\| [EQ-Bench Slop Score]\(https\://eqbench.com/slop-score.html); [lemon07r/SlopScoreTool]\(https\://github.com/lemon07r/SlopScoreTool) | writing | Slop words, contrast patterns, trigrams; the Go port weights 60/25/15 | Calibrated on essays and creative writing; technical text may under-report |

\| [Wikipedia: Signs of AI writing]\(https\://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing); [WikiProject AI Cleanup]\(https\://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) | writing, argument | Evidence-based field guide; descriptive, with the warning to fix the defect and not the sign | Wikipedia-specific; some punctuation and formatting signs may not transfer |

\| [hardikpandya/stop-slop]\(https\://github.com/hardikpandya/stop-slop) | writing | One SKILL.md plus reference files (phrases, structures); five-dimension rubric: directness, rhythm, trust, authenticity, density | About 15,200 stars on 5 Aug 2026 per Analytics Vidhya; popularity is not validity |

\| [ahmedak/defluff]\(https\://github.com/ahmedak/defluff) | writing | Deterministic prose linter with MCP server, weighted categories, user lexicon overlay | Lexicon-based; flags listed filler only |

\| [ehmo/slopkit]\(https\://github.com/ehmo/slopkit) | writing | Anti-slop writing skill with public benchmarks | Ranks tools on its own rubric (stop-slop 68, skill-deslop 72); author-run |

\| [blader/humanizer]\(https\://github.com/blader/humanizer); [stephenturner/skill-deslop]\(https\://github.com/stephenturner/skill-deslop); [apurvrdx1/tagore]\(https\://github.com/apurvrdx1/tagore) | writing | Further Claude skills; tagore lists a 29-pattern catalog and 8-dimension rubric | Seen in listings only |

\| [flamehaven01/AI-SLOP-Detector]\(https\://github.com/flamehaven01/AI-SLOP-Detector) (PyPI \`ai-slop-detector\`) | coding | AST analysis: stubs, phantom imports, disconnected pipelines, clones, inflated docs | Structural only; says nothing on input-output variation |

\| [skew202/antislop]\(https\://github.com/skew202/antislop) | coding | Linter for deferral, hedge and placeholder language; regex plus AST; crates.io and npm | Targets leftover phrases |

\| [athola/claude-night-market]\(https\://github.com/athola/claude-night-market) (slop-detector skill) | coding, writing | Density-based slop audit that preserves why-comments | Skill inside a larger bundle |

\| [CodeRabbit slop detection]\(https\://docs.coderabbit.ai/pr-reviews/slop-detection) | coding | PR-level slop classification | Public repos only; notes, does not block; tuning in progress per its docs |

\| [Shaib et al., Measuring AI "Slop" in Text, arXiv 2509.19163]\(https\://arxiv.org/abs/2509.19163) | writing | Slop taxonomy from expert interviews and span annotation | As described by awesome-slop |

\| [DeepResearch Bench, arXiv 2506.11763]\(https\://arxiv.org/abs/2506.11763); [FutureSearch Deep Research Bench, arXiv 2506.06287]\(https\://arxiv.org/abs/2506.06287); [BrowseComp-Plus, arXiv 2508.06600]\(https\://arxiv.org/abs/2508.06600); [ResearchRubrics, arXiv 2511.07685]\(https\://arxiv.org/abs/2511.07685); [Dr.Mi-Bench, arXiv 2512.00986]\(https\://arxiv.org/abs/2512.00986) | queries | Report-quality rubrics; frozen-web replay; fixed corpus with verified evidence; planning, retrieval and reasoning scored separately | None isolates query quality; Dr.Mi-Bench is closest |

\| [LongMemEval]\(https\://github.com/xiaowu0162/LongMemEval), [arXiv 2410.10813]\(https\://arxiv.org/abs/2410.10813) | linear monolith | Five memory abilities; session decomposition, fact-augmented keys, time-aware query expansion | Benchmarks assistants; supplies the test set for your ledger |

\| [causalNLP/logical-fallacy]\(https\://github.com/causalNLP/logical-fallacy) (Jin et al., EMNLP Findings 2022); [SmartyPat-Bench, arXiv 2504.12312]\(https\://arxiv.org/abs/2504.12312); [arXiv 2404.05213]\(https\://arxiv.org/abs/2404.05213) | argument | Fallacy datasets and LLM evaluations | Short, quiz-style sentences; shows what LLM labelling misses |

\| [IndoNLU]\(https\://github.com/indobenchmark/indonlu); [IndoMMLU]\(https\://github.com/fajri91/IndoMMLU) | Indonesian | Indo4B corpus and IndoBERT; competence benchmark | No slop lexicon in either |

\| [arXiv 2506.12014]\(https\://arxiv.org/abs/2506.12014) | naming | Measured LLM naming preferences in code | Description, no linter |

\| [Lean 4 graduate benchmark, arXiv 2603.26996]\(https\://arxiv.org/abs/2603.26996); [Pseudo-Formalization, arXiv 2605.20531]\(https\://arxiv.org/abs/2605.20531); [Miranda, Judge the Spec]\(https\://cs.stanford.edu/people/brando9/2026/06/18/judge-the-spec-not-the-proof.html) | mathematics | Formal checking; block verification; where judgment belongs | Research results; Miranda's piece is a position essay |



**### 3. Corpus row schema (JSONL)**



\`\`\`json

{"id":"C-01","class":"coding","signature":"output constant under input change","origin":"user-reported","thread":"diary-to-song","evidence":null,"detector":"metamorphic","repair":"fix lower layer first","status":"open"}

\`\`\`



\`origin\` takes \`user-reported\` or \`measured\`. \`evidence\` stays null until a raw transcript or output is attached.



**### 4. Assumptions and gaps**



\- Raw GPT transcripts and Notion pages were not swept. Paste or point me to them and the ρ computation turns rows into measured lexicons.

\- Thresholds (overlap τ, ρ cutoff, frequency floor, length z-score) are uncalibrated and must be set on your golden set.

\- Your vault naming convention (N-01) is assumed to extend to code identifiers; you have not stated that.

\- The Indonesian lexicon does not exist publicly. The build path above is the only route found.

\- No mathematics incident appears in the history. The class rests on your stated requirements and the external work.

\- Python with sympy is assumed available for L0 mathematics checks.

\- Hosted chat models do not expose decoding, so antislop-sampler applies to local models only; for hosted models the cascade regenerates after L2 (inference, not tested).
