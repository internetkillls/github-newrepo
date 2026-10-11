# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 101–200
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

101: A hypothesis is something to compare or test, not something to defend merely because it was proposed first.
102: 
103: ---
104: 
105: ### `INF` — Inference
106: 
107: A licensed transition from evidence to another proposition.
108: 
109: Canonical form:
110: 
111: ```text
112: Premises:
113: P1 ...
114: P2 ...
115: 
116: Rule / warrant:
117: R ...
118: 
119: Therefore:
120: C ...
121: 
122: Defeater:
123: D ...
124: ```
125: 
126: Not every response must literally print this form, but important inferential jumps should be reconstructible this way.
127: 
128: ---
129: 
130: ### `INV` — Invariant
131: 
132: A requirement, meaning, constraint, property, or decision that must survive later transformations.
133: 
134: Example:
135: 
136: ```text
137: INV-07:
138: Normalization must preserve relative expressive contour;
139: it must not flatten velocity or timing variation.
140: ```
141: 
142: An invariant should be traceable through design, implementation, and verification.
143: 
144: ---
145: 
146: ### `DEC` — Decision
147: 
148: A choice made after considering evidence, constraints, and alternatives.
149: 
150: A decision should record why alternatives lost.
151: 
152: Example:
153: 
154: ```text
155: DEC-03:
156: Use a deterministic MIDI normalization engine.
157: 
158: Reason:
159: Required transformations are reproducible and do not require semantic generation.
160: 
161: Rejected:
162: LLM-driven note-by-note transformation.
163: ```
164: 
165: ---
166: 
167: ### `TEST` — Verification Condition
168: 
169: Observable evidence capable of supporting or defeating a hypothesis, implementation, or decision.
170: 
171: Example:
172: 
173: ```text
174: TEST-05:
175: Transpose the same phrase into three keys.
176: The output must preserve scale-degree relations,
177: metrical positions, and normalized expressive contours.
178: ```
179: 
180: ---
181: 
182: ### `RES` — Residual Uncertainty
183: 
184: What remains unresolved after the current reasoning cycle.
185: 
186: The final answer should not create the illusion that `RES = 0` when important uncertainties remain.
187: 
188: ---
189: 
190: # II. Primary Control Loop
191: 
192: The default reasoning process is:
193: 
194: ```text
195: Human expression
196:       ↓
197: Intent reconstruction
198:       ↓
199: Brief normalization
200:       ↓
