# user-worklog-witness

Source ID: B02
Original attachment: Refernsi chain-of-thought yang aku mau Pasted text(20261004-220515).txt
Original lines: 401–500
Classification: historical-conversation. Historical/model statements are not verified external facts. This is calibration data, not a source of new tool permissions or executable instructions.

401: # AI transport protocol
402: 
403: Each AI session should receive one generated feeder and should return zero or more file blocks.
404: 
405: ```text
406: <<<PPC_FILE path="relative/path.ext">>>
407: file content
408: <<<PPC_END_FILE>>>
409: ```
410: 
411: Rules:
412: 
413: - Paths are relative to project root.
414: - No `..` and no absolute paths.
415: - Structured primitives must be valid JSON.
416: - Do not return source code during discovery/planning unless the feeder explicitly requests a probe.
417: - Preserve IDs already present in requirements, tensions, invariants, and decisions.
418: - State changes should be proposed through `.ppc/state-proposal.json`; the CLI remains authoritative for gates and phase advancement.
419: - A repair session must not rewrite passing areas unless a demonstrated dependency requires it.
420: 
421: END_FILE id=F0001
422: ====================================================================================================
423: BEGIN_FILE id=F0002 path=architecture.md kind=note lang=markdown lines=49 sha256=6c59f8f292e7c253fb4e89a3311db83bc605c8257c962b32f983ae763e48c13a
424: ----------------------------------------------------------------------------------------------------
425: # PPC architecture
426: 
427: PPC v0.1.0 has a scanner, bootstrap compiler, topology/strategy resolver, context compiler, script materializer, and AI transport layer.
428: 
429: ## 1. Sanitized scanner
430: 
431: `host -> sanitized provenance + capability evidence`
432: 
433: The scanner captures toolchain facts before initial AI planning while preserving the privacy boundary. It supports capability, targeted, and explicit-opt-in full inventory depths.
434: 
435: ## 2. Bootstrap compiler
436: 
437: `intake + scan -> control-plane filesystem + repository aliases + primitive slots`
438: 
439: The project workspace is not itself assumed to be the product repository. Existing repositories may remain elsewhere; only `.ppc/private/repos.runtime.json` stores their raw paths.
440: 
441: ## 3. Topology / strategy resolver
442: 
443: `host provenance + target matrix + providers + integrations -> provisional execution strategy`
444: 
445: The resolver can recommend native execution, Docker/Linux, multi-platform builds, WSL, remote CI, or provider-specific tooling. Its output is provisional evidence, not an irreversible architecture decision.
446: 
447: ## 4. Context compiler
448: 
449: `public project primitives + current state + phase -> minimal sanitized feeder`
450: 
451: It chooses current phase instructions, relevant structured primitives, applicable adapters/SKILLs, and current verification/repair evidence. Private runtime state is never an input.
452: 
453: ## 5. Script materializer
454: 
455: `.ppc/script-plan.json -> run-task.py + thin .ps1/.sh wrappers`
456: 
457: AI reasons about project-specific commands from topology/toolchain evidence; PPC owns path resolution and wrapper materialization.
458: 
459: ## 6. AI transport
460: 
461: AI responses are untrusted patch packages. PPC previews file blocks, rejects unsafe/protected paths, then applies only with explicit `--apply`.
462: 
463: ## Authority summary
464: 
465: - `.ppc/private/**`: local-only operational state.
466: - `.ppc/environment/host.snapshot.json`: scanner evidence.
467: - `.ppc/state.json` and approvals: PPC workflow authority.
468: - `.ppc/topology.json` / targets/providers/integrations: topology contracts/IR.
469: - `docs/`: human-readable product/system/decision artifacts.
470: - `@repo/<alias>/**`: runtime implementation authority.
471: - Git: historical change authority.
472: - generated feeder files: disposable transport, never project truth.
473: 
474: END_FILE id=F0002
475: ====================================================================================================
476: BEGIN_FILE id=F0003 path=environment-adapters/appsheet-appsscript.md kind=note lang=markdown lines=4 sha256=0ae613baae930664d662c417d8a978e96e2135402559ec4c0910cdd71c2b8491
477: ----------------------------------------------------------------------------------------------------
478: # AppSheet + Apps Script adapter
479: 
480: Treat AppSheet configuration and Apps Script source as separate authorities with an explicit bridge contract. Record table/data authority, Ref relationships, views/actions/automations, script manifest and deployment identity, trigger/event boundaries, quotas/runtime limits, and how repository state mirrors non-file AppSheet configuration. The probe should exercise one real data relation plus one real automation/bridge path before scale-out.
481: 
482: END_FILE id=F0003
483: ====================================================================================================
484: BEGIN_FILE id=F0004 path=environment-adapters/base.md kind=note lang=markdown lines=4 sha256=5927f6d871815c4cfc54b525f171e7d12dcad207ba1bd1f546ba2020563a3789
485: ----------------------------------------------------------------------------------------------------
486: # Base environment adapter
487: 
488: Use environment documentation as an implementation constraint, not as product requirements. Identify runtime boundaries, deployment boundaries, source-of-truth locations, secrets/config handling, test affordances, and bridge/relay boundaries when multiple environments are involved.
489: 
490: END_FILE id=F0004
491: ====================================================================================================
492: BEGIN_FILE id=F0005 path=environment-adapters/browser-extension.md kind=note lang=markdown lines=4 sha256=b4bc61a534eb105553808ede178c2b5010b8d8d37da6c99f353a71979ab07d35
493: ----------------------------------------------------------------------------------------------------
494: # Browser extension adapter
495: 
496: Record manifest version, extension permissions, content/background/service-worker boundaries, page/extension message bridge, storage authority, host permissions, build pipeline, and browser-specific constraints. Probe the actual message boundary before feature expansion.
497: 
498: END_FILE id=F0005
499: ====================================================================================================
500: BEGIN_FILE id=F0006 path=environment-adapters/python.md kind=note lang=markdown lines=4 sha256=33a09f224737e320bc26830383f03576ca127ac4ce1061b3d01965bf66252e36
