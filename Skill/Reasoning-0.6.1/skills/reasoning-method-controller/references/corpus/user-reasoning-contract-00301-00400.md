# user-reasoning-contract

Source ID: B01
Original attachment: Pasted text(20261004-222006)(1).txt
Original lines: 301–400
Classification: user-contract. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

301: What is not yet determined?
302: ```
303: 
304: Do not design before the brief is sufficiently stable.
305: 
306: ---
307: 
308: # V. Stage 3 — Build a Dependency Graph
309: 
310: Determine which conclusions depend on which unresolved premises.
311: 
312: Example:
313: 
314: ```text
315: Choose annotation architecture
316:         │
317:         ├── depends on → annotation ontology
318:         ├── depends on → corpus scale
319:         ├── depends on → licensing constraints
320:         ├── depends on → local hardware
321:         └── depends on → accuracy requirement
322: ```
323: 
324: Then investigate high-centrality unknowns first.
325: 
326: The priority of an unknown should roughly follow:
327: 
328: ```text
329: Priority(UNK)
330: ≈ probability it changes the decision
331: × magnitude of the consequence
332: × cost of discovering it later
333: ```
334: 
335: This prevents spending time researching details that cannot affect the architecture.
336: 
337: ---
338: 
339: # VI. Stage 4 — Evidence Before Synthesis
340: 
341: Do not jump directly:
342: 
343: ```text
344: request → architecture
345: ```
346: 
347: Prefer:
348: 
349: ```text
350: request
351: → evidence
352: → constraints
353: → alternatives
354: → architecture
355: ```
356: 
357: For existing code or repositories, local evidence normally has priority:
358: 
359: ```text
360: repository structure
361: → manifests
362: → actual implementation
363: → tests
364: → logs
365: → issues/history
366: → external references only for remaining unknowns
367: ```
368: 
369: For greenfield work:
370: 
371: ```text
372: problem
373: → use cases
374: → constraints
375: → comparable systems
376: → reusable patterns
377: → candidate architecture
378: ```
379: 
380: For academic work:
381: 
382: ```text
383: primary text
384: → textual claim
385: → argumentative role
386: → interpretation
387: → criticism
388: → extension
389: ```
390: 
391: Never silently replace source reasoning with general background knowledge.
392: 
393: ---
394: 
395: # VII. Stage 5 — Separate Evidence from Interpretation
396: 
397: The AI should preserve this direction:
398: 
399: ```text
400: evidence
