#!/usr/bin/env python3
"""Operator-local VCT v0.8 patch-canary CLI; no grant minting or deployment."""
import argparse
import json
import os
from pathlib import Path
from autopatcher_core import JobStore,GateError,run_canary_job,capability_report
from autopatcher_control import ControlPlane


def load_json(path):return json.loads(Path(path).read_text(encoding='utf-8'))

def secret(name):
    val=os.environ.get(name,'')
    try:data=bytes.fromhex(val)
    except ValueError:raise GateError('MISSING_OPERATOR_SECRET',name)
    if len(data)<32:raise GateError('MISSING_OPERATOR_SECRET',name)
    return data


def main():
    p=argparse.ArgumentParser(description='VCT operator-only canary orchestrator; no arbitrary test execution')
    p.add_argument('action',choices=['capabilities','submit','status','receipt','cancel','run-canary'])
    p.add_argument('--db',help='persistent SQLite path')
    p.add_argument('--registry',help='operator-owned repo allowlist JSON')
    p.add_argument('--spec',help='typed canary spec JSON')
    p.add_argument('--assertion',help='signed gateway assertion JSON')
    p.add_argument('--grant',help='signed per-job patch grant JSON')
    p.add_argument('--idempotency',help='stable request id')
    p.add_argument('--job',help='job ID')
    a=p.parse_args()
    if a.action=='capabilities':print(json.dumps(capability_report(),indent=2));return 0
    if not a.db or not a.registry:raise GateError('MISSING_ARG','db and operator registry are required')
    reg=load_json(a.registry)
    store=JobStore(Path(a.db))
    try:
        if a.action=='run-canary':
            if not a.job or not a.grant:raise GateError('MISSING_ARG','job and grant required')
            result=run_canary_job(store,a.job,reg,load_json(a.grant),secret('VCT_PATCH_GRANT_HMAC_HEX'))
        else:
            svc=ControlPlane(store,reg,secret('VCT_GATEWAY_HMAC_HEX'))
            if not a.assertion:raise GateError('MISSING_ARG','signed gateway assertion required')
            assertion=load_json(a.assertion)
            if a.action=='submit':
                if not a.spec or not a.idempotency:raise GateError('MISSING_ARG','spec and idempotency required')
                result=svc.submit_patch_job(load_json(a.spec),a.idempotency,assertion)
            else:
                if not a.job:raise GateError('MISSING_ARG','job required')
                result={'status':svc.get_job_status,'receipt':svc.get_job_receipt,'cancel':svc.cancel_queued_job}[a.action](a.job,assertion)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    finally:store.close()

if __name__=='__main__':
    try:raise SystemExit(main())
    except (GateError,ValueError,KeyError,OSError) as error:
        print(json.dumps({'error':getattr(error,'code','INVALID_INPUT'),'detail':str(error)}));raise SystemExit(2)
