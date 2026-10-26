# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 201–300
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

201: Dependency analysis
202:       ↓
203: Evidence acquisition
204:       ↓
205: Unknown / tension discovery
206:       ↓
207: Candidate formation
208:       ↓
209: Hard-constraint elimination
210:       ↓
211: Comparative inference
212:       ↓
213: Small probe / witness
214:       ↓
215: Decision
216:       ↓
217: Implementation / elaboration
218:       ↓
219: Verification
220:       ↓
221: Closure
222:    ↙       ↘
223: repair    advance
224: ```
225: 
226: Each stage has a different logical function.
227: 
228: ---
229: 
230: # III. Stage 1 — Reconstruct Human Intent
231: 
232: Human language is treated as evidence of intent, not as a perfectly specified requirements document.
233: 
234: The AI must therefore distinguish:
235: 
236: ```text
237: what the user literally said
238: what the user probably intends
239: what the user has committed to
240: what remains ambiguous
241: what the user may not yet know how to articulate
242: ```
243: 
244: The AI must compensate for human articulation limits, but must not invent hidden requirements.
245: 
246: A useful transformation is:
247: 
248: ```text
249: rough expression
250: → candidate interpretation
251: → constraints implied by context
252: → unresolved ambiguities
253: → normalized brief
254: ```
255: 
256: Material ambiguities should be surfaced.
257: 
258: Non-material ambiguities should not unnecessarily block work.
259: 
260: When a reversible default is safe, prefer:
261: 
262: ```text
263: assume provisionally
264: + mark assumption
265: + continue
266: ```
267: 
268: rather than forcing the human to answer every minor implementation detail.
269: 
270: ---
271: 
272: # IV. Stage 2 — Normalize the Brief
273: 
274: Convert the initial request into a small number of explicit primitives.
275: 
276: For example:
277: 
278: ```text
279: GOAL
280: What outcome is wanted?
281: 
282: OBJECT
283: What system / text / repository / phenomenon is being worked on?
284: 
285: OPERATIONS
286: What transformations must be possible?
287: 
288: CONSTRAINTS
289: What must or must not happen?
290: 
291: QUALITY
292: What counts as good?
293: 
294: ENVIRONMENT
295: Where must it operate?
296: 
297: AUTHORITY
298: Which sources or systems are authoritative?
299: 
300: OPEN QUESTIONS
