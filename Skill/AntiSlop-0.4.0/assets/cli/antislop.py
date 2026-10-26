#!/usr/bin/env python3
"""AntiSlop 0.3: offline transcript index and typed evidence-ledger validator.

Does not read chats, query models, validate truth, execute arbitrary user code,
verify external citations, or classify author identity. Python 3.10+ stdlib.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

KINDS = {"question", "claim", "proposal", "decision", "adoption", "correction", "constraint", "term-sense", "test", "evidence", "debt", "retraction"}
ACTORS = {"user", "assistant", "tool", "source", "unknown"}
ORIGINS = {"user-authored", "user-quoted", "third-party", "prior-assistant", "generated-paste", "source-extract", "unknown"}
STATES = {"stated", "proposed", "accepted", "rejected", "superseded", "unresolved"}
FINDING_STATES = {"CONFIRMED", "SUPPORTED-RISK", "STYLE-SIGNAL", "UNVERIFIED", "NOT-APPLICABLE"}
CLASSES = set("QWLSINCAM")
WITNESSES = {"observed_runtime", "formal_check", "source_witness", "conversation_anchor", "structured_argument"}


def load_jsonl(path: Path):
    entries, issues = [], []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as exc:
            issues.append(f"line {lineno}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(record, dict):
            issues.append(f"line {lineno}: expected a JSON object")
            continue
        record = dict(record)
        record["__line"] = lineno
        entries.append(record)
    return entries, issues


def anchored(event):
    anchors = event.get("evidence_refs")
    return bool(isinstance(anchors, list) and anchors and all(
        isinstance(a, dict) and str(a.get("source_id", "")).strip() and str(a.get("locator", "")).strip()
        for a in anchors))


def validate_ledger(rows):
    errors, warnings, ids = [], [], {}
    required = ("event_id", "turn_id", "actor", "origin", "kind", "status", "text", "evidence_refs")
    for e in rows:
        line = e["__line"]
        missing = [k for k in required if k not in e]
        if missing:
            errors.append(f"line {line}: missing: {', '.join(missing)}")
            continue
        eid = e["event_id"]
        if not isinstance(eid, str) or not eid.strip():
            errors.append(f"line {line}: nonempty event_id required")
        elif eid in ids:
            errors.append(f"line {line}: duplicate event_id {eid}")
        else:
            ids[eid] = e
        if not isinstance(e["turn_id"], str) or not e["turn_id"].strip():
            errors.append(f"line {line}: turn_id must be a nonempty string")
        if any(not isinstance(e[k], str) for k in ("actor", "origin", "kind", "status")) or e["actor"] not in ACTORS or e["origin"] not in ORIGINS or e["kind"] not in KINDS or e["status"] not in STATES:
            errors.append(f"line {line}: unknown actor, origin, kind or status")
        if not isinstance(e["text"], str) or not e["text"].strip():
            errors.append(f"line {line}: nonempty text required")
        if not anchored(e):
            errors.append(f"line {line}: material events require source_id + locator evidence anchor")
        if e["kind"] == "adoption" and (e["actor"] != "user" or e["origin"] != "user-authored"):
            errors.append(f"line {line}: only an explicit user event can attest user adoption")
        if e["status"] == "superseded" and not e.get("superseded_by"):
            errors.append(f"line {line}: supersession needs an explicit replacement link")
        if e["status"] == "accepted" and e["actor"] == "assistant" and e["kind"] in {"proposal", "decision", "constraint"} and not e.get("adopted_by"):
            errors.append(f"line {line}: assistant-origin plan marked accepted without user-adoption link")
    if not rows:
        errors.append("ledger contains no records; cannot claim conversation coverage")
    # Explicit edge relations may be incomplete in a partial ledger. Do not infer intent.
    predecessors = {}
    for e in rows:
        if e.get("kind") != "question" or not isinstance(e.get("replaces"), str) or not e.get("replaces"):
            continue
        old = e["replaces"]
        if old in predecessors and predecessors[old] != e.get("event_id"):
            warnings.append(f"line {e['__line']}: question {old} has competing replacements; reconcile branch")
        predecessors[old] = e.get("event_id")
    for e in rows:
        line = e["__line"]
        target = e.get("superseded_by")
        if target and not isinstance(target, str):
            errors.append(f"line {line}: superseded_by must be an event-id string")
            target = None
        if target and target not in ids:
            errors.append(f"line {line}: superseded_by points to unknown event {target}")
        adopter = e.get("adopted_by")
        if adopter:
            if not isinstance(adopter, str):
                errors.append(f"line {line}: adopted_by must be an event-id string")
                continue
            ev = ids.get(adopter)
            if not ev or ev.get("actor") != "user" or ev.get("origin") != "user-authored" or ev.get("kind") != "adoption" or not anchored(ev):
                errors.append(f"line {line}: adopted_by must reference source-anchored user adoption")
            else:
                target_ids = ev.get("target_event_ids", [])
                if not isinstance(target_ids, list) or any(not isinstance(t, str) for t in target_ids):
                    errors.append(f"line {line}: target_event_ids must be a list of event ids")
                elif ev.get("target_event_id") != e.get("event_id") and e.get("event_id") not in target_ids:
                    errors.append(f"line {line}: user adoption does not identify this exact proposal/question")
                if ev in rows and e in rows and rows.index(ev) <= rows.index(e):
                    errors.append(f"line {line}: adoption must follow the proposal in supplied transcript order")
        replaces = e.get("replaces")
        if replaces and not isinstance(replaces, str):
            errors.append(f"line {line}: replaces must be an event-id string")
            replaces = None
        if replaces:
            old = ids.get(replaces)
            if e.get("kind") != "question" or not old or old.get("kind") != "question":
                errors.append(f"line {line}: replaces must connect two known questions")
            elif e.get("actor") != "user" and not e.get("adopted_by"):
                errors.append(f"line {line}: assistant question cannot replace user question without adoption")
        corrected = e.get("corrects")
        if corrected and not isinstance(corrected, str):
            errors.append(f"line {line}: corrects must be an event-id string")
            corrected = None
        if corrected:
            if e.get("kind") not in {"correction", "retraction"}:
                errors.append(f"line {line}: corrects only valid on correction/retraction")
            elif corrected not in ids:
                warnings.append(f"line {line}: correction target not in partial ledger: {corrected}")
        elif e.get("kind") in {"correction", "retraction"}:
            warnings.append(f"line {line}: correction has no explicit target; application unresolved")
        if e.get("kind") == "adoption":
            targets = ([e["target_event_id"]] if isinstance(e.get("target_event_id"), str) and e.get("target_event_id") else []) + (e.get("target_event_ids") if isinstance(e.get("target_event_ids"),list) else [])
            if not targets:
                warnings.append(f"line {line}: adoption is not linked to an exact proposal; do not infer blanket acceptance")
            for target_id in targets:
                if not isinstance(target_id, str):
                    errors.append(f"line {line}: adoption targets must be event-id strings")
                elif target_id not in ids:
                    warnings.append(f"line {line}: adoption target not in partial ledger: {target_id}")
        deps = e.get("depends_on", [])
        if not isinstance(deps, list):
            errors.append(f"line {line}: depends_on must be a list")
        else:
            for dep in deps:
                if not isinstance(dep, str):
                    errors.append(f"line {line}: depends_on entries must be event-id strings")
                elif dep not in ids:
                    warnings.append(f"line {line}: dependency {dep} is not in this (possibly partial) ledger")
    # Reject explicit question-replacement cycles, including multi-hop cycles.
    for first in predecessors:
        visited = set()
        q = first
        while q in predecessors:
            if q in visited:
                errors.append(f"question replacement cycle includes {q}")
                break
            visited.add(q)
            q = predecessors[q]
    return list(dict.fromkeys(errors)), list(dict.fromkeys(warnings))


def validate_findings(rows):
    errors = []
    for e in rows:
        line = e["__line"]
        if e.get("class") not in CLASSES:
            errors.append(f"line {line}: unknown class (must be Q/W/L/S/I/N/C/A/M)")
        if e.get("status") not in FINDING_STATES:
            errors.append(f"line {line}: unknown finding status")
        if not e.get("finding_id"):
            errors.append(f"line {line}: finding_id required")
        if e.get("status") == "CONFIRMED":
            if e.get("proof_type") not in WITNESSES:
                errors.append(f"line {line}: CONFIRMED needs a named witness type")
            if not (isinstance(e.get("artifact_anchor"), dict) and e["artifact_anchor"].get("locator")):
                errors.append(f"line {line}: CONFIRMED needs artifact locator")
            if not (isinstance(e.get("proof_anchor"), dict) and e["proof_anchor"].get("locator")):
                errors.append(f"line {line}: CONFIRMED needs proof locator")
            for k in ("expectation", "actual", "root_dependency", "repair", "retest"):
                if not isinstance(e.get(k), str) or not e[k].strip():
                    errors.append(f"line {line}: CONFIRMED needs {k}")
            # Structural validation alone NEVER verifies the claimed proof.
    return errors

# Deliberately tiny, high-precision leads. No correctness or AI-authorship verdict.
STYLE_PATTERNS = [
    ("ID_generic_opener", re.compile(r"\b(?:di era digital (?:saat ini|ini)|pernahkah anda bertanya.tanya)\b", re.I)),
    ("ID_contrast_formula", re.compile(r"\bbukan\b[^.!?\n]{1,100}\b(?:tapi|melainkan|tetapi)\b", re.I)),
    ("EN_contrast_formula", re.compile(r"\bnot\b[^.!?\n]{1,100}\bbut\b", re.I)),
    ("EN_cliche", re.compile(r"\b(?:delve into|ever.evolving landscape|in today's fast.paced world)\b", re.I)),
]


def scan_text(contents):
    findings = []
    for lineno, line in enumerate(contents.splitlines(), 1):
        for name, pattern in STYLE_PATTERNS:
            for match in pattern.finditer(line):
                findings.append({"line": lineno, "class": "I" if name.startswith("ID") else "W", "rule": name,
                                 "excerpt": match.group(0)[:160], "status": "STYLE-SIGNAL", "required_action": "review-in-context"})
    return findings


def recap(rows, coverage=None):
    """Return current evidence-supported state, not every historical mention."""
    errors, warnings = validate_ledger(rows)
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}
    ids = {e["event_id"]: e for e in rows}
    replaced = {e["replaces"] for e in rows if e.get("kind") == "question" and e.get("replaces") and e.get("status") in {"stated", "accepted"} and
                ((e.get("actor") == "user" and e.get("origin") == "user-authored") or e.get("adopted_by"))}
    def user_authorized(e):
        return (e.get("actor") == "user" and e.get("origin") == "user-authored") or bool(e.get("adopted_by"))
    questions = [e for e in rows if e.get("kind") == "question" and e.get("status") in {"stated", "accepted"}
                 and user_authorized(e) and e["event_id"] not in replaced]
    corrected = {e.get("corrects") for e in rows if e.get("kind") in {"correction", "retraction"} and
                 e.get("actor") == "user" and e.get("origin") == "user-authored" and e.get("corrects")}
    accepted = [e for e in rows if e.get("status") == "accepted" and user_authorized(e) and
                e.get("kind") not in {"adoption", "question"} and e["event_id"] not in corrected]
    proposals = [e for e in rows if e.get("kind") == "proposal" and e.get("status") in {"proposed", "unresolved"}]
    debts = [e for e in rows if e.get("kind") == "debt" and e.get("status") in {"stated", "proposed", "unresolved"}]
    corrections = [e for e in rows if e.get("kind") in {"correction", "retraction"} and e.get("actor") == "user" and e.get("origin") == "user-authored"]
    scopes = Counter((e.get("thread_id") or "default", e.get("scope") or "default") for e in questions)
    for (thread, scope), count in scopes.items():
        if count > 1:
            warnings.append(f"multiple unresolved active questions for thread={thread}, scope={scope}; no implicit replacement")
    if coverage is None:
        actual_coverage = {"status": "unknown", "basis": "no independently supplied coverage manifest"}
    elif isinstance(coverage, dict) and coverage.get("coverage") in {"partial", "unknown", "complete_for_requested_range"} and coverage.get("accessible"):
        actual_coverage = coverage
    else:
        return {"valid": False, "errors": ["coverage manifest missing accessible sources or legal coverage state"], "warnings": warnings}
    def light(e):
        return {"event_id": e["event_id"], "text": e["text"], "source_anchors": e.get("evidence_refs", [])}
    return {"valid": True, "coverage": actual_coverage,
            "counts": dict(Counter(e.get("kind") for e in rows)),
            "active_questions": [light(e) for e in questions],
            "accepted_events": [light(e) for e in accepted],
            "corrected_prior_events": [light(ids[i]) for i in corrected if i in ids],
            "unadopted_proposals": [light(e) for e in proposals],
            "corrections": [light(e) for e in corrections],
            "open_debts": [light(e) for e in debts],
            "warnings": warnings}


def index_transcript(path):
    """Validate and index only supplied simple JSONL transcripts: no semantic extraction."""
    entries, problems = load_jsonl(path)
    known, roles, index = set(), Counter(), []
    for e in entries:
        line = e["__line"]
        mid = e.get("message_id")
        role = e.get("role")
        content = e.get("content")
        if not isinstance(mid, str) or not mid.strip() or mid in known:
            problems.append(f"line {line}: missing or duplicate message_id")
        else:
            known.add(mid)
        if not isinstance(role, str) or role not in {"user", "assistant", "tool", "system", "developer"}:
            problems.append(f"line {line}: role must be one of user/assistant/tool/system/developer")
        if not isinstance(content, str):
            problems.append(f"line {line}: content must be a string; multipart exports require explicit preprocessing")
            continue
        roles[role] += 1
        index.append({"message_id": mid, "role": role, "source_id": path.name,
                      "locator": f"line:{line}", "preview": content[:140],
                      "timestamp": e.get("timestamp"), "thread_id": e.get("thread_id")})
    if not entries and not problems:
        problems.append("empty transcript; no accessible messages")
    return {"valid": not problems, "source_type": "user_supplied_transcript_only",
            "coverage": "unknown_account_coverage", "message_count": len(index),
            "roles": dict(roles), "message_index": index, "errors": problems,
            "note": "An index is not a semantic ledger, a claim of account-wide access, or proof of user assent."}


def verify_anchors(rows, transcript_path):
    """Verify transcript-source locators, roles, and optional literal quotes.

    This verifies attribution syntax and source presence, not stance or meaning.
    """
    transcript, errors = load_jsonl(transcript_path)
    warnings = []
    source_by_line = {f"line:{m['__line']}": m for m in transcript}
    checked = 0
    for e in rows:
        if not isinstance(e.get('evidence_refs'), list):
            errors.append(f"line {e.get('__line')}: missing evidence_refs list")
            continue
        for a in e['evidence_refs']:
            if not isinstance(a, dict):
                errors.append(f"line {e.get('__line')}: malformed evidence anchor")
                continue
            if a.get('source_id') != transcript_path.name:
                warnings.append(f"line {e.get('__line')}: source {a.get('source_id')} not in this supplied transcript; unchecked")
                continue
            m = source_by_line.get(a.get('locator'))
            if m is None:
                errors.append(f"line {e.get('__line')}: transcript locator {a.get('locator')} not found")
                continue
            if e.get('turn_id') != m.get('message_id'):
                errors.append(f"line {e.get('__line')}: event turn_id does not match referenced message_id")
            if e.get('actor') in {'user','assistant','tool'} and e.get('actor') != m.get('role'):
                errors.append(f"line {e.get('__line')}: event actor conflicts with transcript role")
            quote = a.get('quote')
            if isinstance(quote, str) and quote.strip():
                content = m.get('content')
                if not isinstance(content, str) or ' '.join(quote.split()) not in ' '.join(content.split()):
                    errors.append(f"line {e.get('__line')}: quoted evidence not present in referenced message")
            else:
                warnings.append(f"line {e.get('__line')}: anchor resolves but quote is absent; literal content not checked")
            checked += 1
    return {'valid':not errors,'checked_anchors':checked,'errors':errors,'warnings':warnings,
            'claim':'Only transcript identity, source presence, actor role and literal quote verified; no semantic verdict'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate-ledger", "recap", "audit-text", "validate-findings", "index-transcript", "verify-anchors"])
    parser.add_argument("path", type=Path)
    parser.add_argument("--coverage", type=Path, help="Optional explicit coverage manifest JSON for recap")
    parser.add_argument("--transcript", type=Path, help="Required supplied normalized JSONL transcript for verify-anchors")
    args = parser.parse_args(argv)
    if not args.path.is_file():
        parser.error(f"file not found: {args.path}")
    if args.command == "verify-anchors":
        if args.transcript is None or not args.transcript.is_file():
            parser.error("verify-anchors requires --transcript pointing to existing normalized JSONL file")
        rows, parser_errors = load_jsonl(args.path)
        result = verify_anchors(rows, args.transcript)
        result['errors'] = parser_errors + result['errors']
        result['valid'] = not result['errors']
        exit_code = 0 if result['valid'] else 1
    elif args.command == "index-transcript":
        result = index_transcript(args.path)
        exit_code = 0 if result["valid"] else 1
    elif args.command == "audit-text":
        result = {"status": "STYLE-SIGNALS-ONLY", "findings": scan_text(args.path.read_text(encoding="utf-8-sig"))}
        exit_code = 0
    else:
        rows, parser_errors = load_jsonl(args.path)
        if args.command == "validate-ledger":
            errors, warnings = validate_ledger(rows)
            errors = parser_errors + errors
            result = {"valid": not errors, "record_count": len(rows), "errors": errors, "warnings": warnings}
        elif args.command == "validate-findings":
            errors = parser_errors + validate_findings(rows)
            result = {"valid": not errors, "record_count": len(rows), "errors": errors, "warning": "Structural validation cannot authenticate evidence"}
        else:
            coverage = None
            if args.coverage:
                try:
                    coverage = json.loads(args.coverage.read_text(encoding="utf-8-sig"))
                except (OSError, ValueError) as exc:
                    parser.error(f"invalid coverage manifest: {exc}")
            result = recap(rows, coverage)
            if parser_errors:
                result["valid"] = False
                result.setdefault("errors", []).extend(parser_errors)
        exit_code = 0 if result.get("valid", False) else 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
