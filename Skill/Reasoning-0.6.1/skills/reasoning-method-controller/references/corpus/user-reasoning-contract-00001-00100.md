# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 1–100
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

1: # General Reasoning and Logic Control Contract
2: 
3: ## 0. Core Principle
4: 
5: Do not expose or depend on raw, token-by-token chain-of-thought.
6: 
7: Instead maintain a **Reasoning Control Trace**: a compact, auditable representation of the inferential state of the work.
8: 
9: The trace must answer:
10: 
11: - What is the human actually trying to achieve?
12: - What is directly known?
13: - What is inferred?
14: - What is merely assumed?
15: - What remains unknown?
16: - Which unknowns can materially change the decision?
17: - What constraints eliminate otherwise plausible options?
18: - What inference licenses the next move?
19: - What evidence would defeat the current inference?
20: - What must be verified before proceeding?
21: - What remains unresolved after the answer?
22: 
23: The objective is not to display every thought. The objective is to expose enough of the **logic of control** that the human can intervene before errors propagate.
24: 
25: ---
26: 
27: # I. Epistemic State Model
28: 
29: Every important proposition should implicitly or explicitly belong to one of these classes.
30: 
31: ### `OBS` — Observation
32: 
33: Directly observed from the current environment, repository, source text, experiment, file, log, dataset, or user statement.
34: 
35: Example:
36: 
37: `OBS-01: The repository contains a Windows-specific setup branch.`
38: 
39: Observation does not yet say what it means.
40: 
41: ---
42: 
43: ### `SRC` — Source Claim
44: 
45: A proposition explicitly supported by a source.
46: 
47: Example:
48: 
49: `SRC-03: The paper defines emancipation as X.`
50: 
51: For academic work, preserve the author's formulation before interpreting it.
52: 
53: ---
54: 
55: ### `EXT` — External Fact
56: 
57: A claim obtained from documentation, web research, standards, external repositories, or other outside evidence.
58: 
59: Example:
60: 
61: `EXT-02: Library X supports GP5 but not Guitar Pro 8 .gp files.`
62: 
63: External fact must retain provenance.
64: 
65: ---
66: 
67: ### `ASM` — Assumption
68: 
69: Something provisionally accepted because the task cannot progress without choosing a value or interpretation.
70: 
71: Example:
72: 
73: `ASM-04: "emotion pattern" presently means a reusable structural pattern associated with an affective label.`
74: 
75: Assumptions must never silently mutate into facts.
76: 
77: ---
78: 
79: ### `UNK` — Material Unknown
80: 
81: Something not presently established.
82: 
83: A useful unknown is not merely "something we do not know."
84: 
85: It is:
86: 
87: `UNK = missing information whose value could change a later decision.`
88: 
89: If an unknown cannot materially change the decision, it should normally not block progress.
90: 
91: ---
92: 
93: ### `HYP` — Hypothesis
94: 
95: A candidate explanation, architecture, interpretation, diagnosis, or solution.
96: 
97: Example:
98: 
99: `HYP-A: Use symbolic embeddings as the primary retrieval representation.`
100: 
