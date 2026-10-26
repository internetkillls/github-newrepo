#!/usr/bin/env python3
"""AntiSlop engineering verification adjunct (stdlib, offline).

This verifies evidence structure, repository-bound artifacts, command receipt
provenance and state-transition invariants. It cannot prove semantic correctness.
External projects are *not vendored*; see references/engineering-upstreams.md.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path


def read_json(path):
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)


def inside_root(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        return None
    root = Path(root).resolve()
    candidate = (root / name).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate


def current_head(root):
    try:
        proc = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                              check=True, capture_output=True, text=True, timeout=4)
        return proc.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def check_evidence(root, evidence, head):
    reasons = []
    if not isinstance(evidence, dict):
        return ["Evidence must be an object"]
    ref = evidence.get("path")
    path = inside_root(root, ref)
    if path is None:
        return ["Missing or unsafe repo-relative evidence path"]
    if not path.is_file():
        return [f"Referenced artifact not found: {ref}"]
    kind = evidence.get("kind")
    if kind == "command_receipt":
        try:
            receipt = read_json(path)
        except (ValueError, OSError):
            return [f"Invalid command receipt JSON: {ref}"]
        if receipt.get("schema_version") != "anti-slop-command-receipt.v1":
            reasons.append("Unsupported command receipt schema")
        cmd = receipt.get("command")
        if not (isinstance(cmd, list) and cmd and all(isinstance(a, str) and a for a in cmd)):
            reasons.append("Receipt has no valid command argv")
        exitcode = receipt.get("exit_code")
        if isinstance(exitcode, bool) or not isinstance(exitcode, int):
            reasons.append("Receipt exit code missing/invalid")
        elif exitcode != evidence.get("expected_exit_code", 0):
            reasons.append("Command exit code does not match required outcome")
        if not isinstance(receipt.get("started_at"), str):
            reasons.append("Receipt timestamp missing")
        receipt_head = receipt.get("git_head")
        if head and receipt_head != head:
            reasons.append("Receipt git HEAD mismatches current checkout")
        if not head:
            reasons.append("Git HEAD unavailable: cannot verify receipt freshness")
    elif kind == "behavior":
        if evidence.get("observed") is not True:
            reasons.append("Behavior evidence lacks observed=true")
        if evidence.get("outcome") != "pass":
            reasons.append("Behavior evidence has not passed")
        if not all(isinstance(evidence.get(k), str) and evidence[k].strip()
                   for k in ("input", "expected", "actual")):
            reasons.append("Behavior evidence requires input, expected, actual")
        if evidence.get("execution_mode") in ("dry_run", "mock_only", "proposed", None):
            reasons.append("Behavior was not established in an identified real runtime")
    elif kind == "review":
        if evidence.get("observed") is not True or not evidence.get("reviewer"):
            reasons.append("Review needs observed=true and reviewer identifier")
    else:
        reasons.append("Unsupported evidence kind")
    return reasons


def verify_contract(root, doc):
    findings = []
    if not isinstance(doc, dict) or not isinstance(doc.get("task_id"), str) or not doc["task_id"]:
        return {"status":"INCOMPLETE", "findings":["Missing task_id"]}
    requirements = doc.get("requirements")
    evidence = doc.get("evidence")
    if not isinstance(requirements, list) or not requirements:
        return {"status":"INCOMPLETE", "findings":["No requirements"]}
    if not isinstance(evidence, list):
        return {"status":"INCOMPLETE", "findings":["Evidence must be a list"]}
    by_id = {}
    head = current_head(root)
    for row in evidence:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
            findings.append("Evidence record without ID")
            continue
        if row["id"] in by_id:
            findings.append("Duplicate evidence ID: " + row["id"])
        by_id[row["id"]] = row
    seen = set()
    for req in requirements:
        if not isinstance(req, dict) or not isinstance(req.get("id"), str) or not req["id"]:
            findings.append("Requirement without ID")
            continue
        rid = req["id"]
        if rid in seen:
            findings.append(f"{rid}: duplicate requirement ID")
        seen.add(rid)
        if not isinstance(req.get("description"), str) or not req["description"].strip():
            findings.append(f"{rid}: missing description")
        refs = req.get("verification")
        if not isinstance(refs, list) or not refs:
            findings.append(f"{rid}: no verification references")
            continue
        negatives = req.get("negative_controls", [])
        if not isinstance(negatives, list):
            findings.append(f"{rid}: negative_controls must be a list")
            negatives = []
        if req.get("risk") in ("stateful", "concurrent", "security") and not negatives:
            findings.append(f"{rid}: risk requires negative control")
        for evid in refs + negatives:
            if not isinstance(evid, str) or evid not in by_id:
                findings.append(f"{rid}: unresolved evidence reference {evid!r}")
                continue
            row = by_id[evid]
            if row.get("requirement_id") != rid:
                findings.append(f"{rid}: evidence {evid} belongs to another requirement")
            if evid in negatives and row.get("test_role") != "negative_control":
                findings.append(f"{rid}: {evid} not marked negative_control")
            for error in check_evidence(root, row, head):
                findings.append(f"{rid}/{evid}: {error}")
    return {"status": "INCOMPLETE" if findings else "EVIDENCE_PRESENT_REVIEW_REQUIRED",
            "task_id": doc["task_id"], "checked_requirements": len(requirements),
            "findings": findings,
            "limitation": "Structural receipts and declared observations are not proof of behavior correctness."}


def verify_trace(trace, policy):
    findings = []
    if not isinstance(trace, dict) or not isinstance(policy, dict):
        return {"status":"INCOMPLETE", "findings":["Trace and policy must be objects"]}
    calls = trace.get("tool_calls", [])
    events = trace.get("events", [])
    if not isinstance(calls, list) or not isinstance(events, list):
        return {"status":"INCOMPLETE", "findings":["Trace lists are invalid"]}
    denied = set(policy.get("denied_tools", []))
    allowed = policy.get("allowed_tools")
    for item in calls:
        if not isinstance(item, dict):
            findings.append("Malformed tool call")
            continue
        name = item.get("name") or item.get("tool") or item.get("tool_name")
        if name in denied or (allowed is not None and name not in allowed):
            findings.append(f"Disallowed tool call: {name}")
    goal = policy.get("expected_goal")
    if goal:
        actual = [e.get("id") for e in events if isinstance(e, dict) and e.get("type") == "goal"]
        if goal not in actual or any(x != goal for x in actual):
            findings.append("Goal integrity not demonstrated")
    return {"status":"FAIL" if findings else "PASS", "findings":findings,
            "limitation":"Trace assertions cover recorded events only, not uninstrumented actions."}


def verify_queue(trace):
    if not isinstance(trace, dict) or not isinstance(trace.get("items"), list):
        return {"status":"INCOMPLETE", "findings":["Expected items list"]}
    findings = []
    seen_ids = set()
    order = ["send_attempted", "send_acknowledged", "response_completed", "complete"]
    for item in trace["items"]:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
            findings.append("Queue entry has no ID")
            continue
        ident = item["id"]
        if ident in seen_ids:
            findings.append(f"{ident}: duplicate queue item ID")
        seen_ids.add(ident)
        events = item.get("events", [])
        if not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
            findings.append(f"{ident}: events must be objects in a list")
            continue
        types = [x.get("type") for x in events]
        if "complete" in types and ("send_acknowledged" not in types or "response_completed" not in types):
            findings.append(f"{ident}: false completion without acknowledged send and response completion")
        if types.count("send_acknowledged") > 1:
            findings.append(f"{ident}: multiple acknowledged sends; investigate duplicate submission")
        if "response_completed" in types and "send_acknowledged" not in types:
            findings.append(f"{ident}: response completion without send acknowledgment")
        if "complete" not in types:
            findings.append(f"{ident}: incomplete or uncertain completion")
        if all(k in types for k in order):
            indices = [types.index(k) for k in order]
            if indices != sorted(indices):
                findings.append(f"{ident}: out-of-order queue transition")
        if "complete" in types and types.index("complete") != len(types) - 1:
            findings.append(f"{ident}: events follow completion")
    if not trace["items"]:
        findings.append("Queue contains no items")
    return {"status":"FAIL" if findings else "PASS", "findings":findings,
            "limitation":"Recorded events and UI truth must be independently checked by the caller."}


def main(argv=None):
    parser = argparse.ArgumentParser(description="AntiSlop evidence and state-transition checker")
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("contract")
    a.add_argument("contract")
    a.add_argument("--root", default=".")
    b = sub.add_parser("agent-trace")
    b.add_argument("trace")
    b.add_argument("policy")
    c = sub.add_parser("queue-trace")
    c.add_argument("trace")
    args = parser.parse_args(argv)
    try:
        if args.command == "contract":
            result = verify_contract(Path(args.root), read_json(args.contract))
        elif args.command == "agent-trace":
            result = verify_trace(read_json(args.trace), read_json(args.policy))
        else:
            result = verify_queue(read_json(args.trace))
    except (OSError, ValueError) as exc:
        result = {"status": "INCOMPLETE", "findings": [f"Cannot parse input: {exc}"]}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] in ("PASS", "EVIDENCE_PRESENT_REVIEW_REQUIRED") else 1


if __name__ == "__main__":
    sys.exit(main())
