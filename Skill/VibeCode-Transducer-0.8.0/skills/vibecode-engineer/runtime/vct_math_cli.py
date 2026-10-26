#!/usr/bin/env python3
"""Optional combined read-only VCT output: model router + legacy static transducer.

No automatic server, no code mutation, no proof claims.
"""
from __future__ import annotations
import argparse
import json
import sys
from math_model_router import route, ModelContractError

def combine(spec:dict)->dict:
    if not isinstance(spec,dict) or not any(k in spec for k in ('math_problem','multimodel_problem','heuristic_dispatcher')):
        raise ModelContractError('expected math_problem, multimodel_problem, or heuristic_dispatcher object')
    report={}
    if 'math_problem' in spec:
        if not isinstance(spec['math_problem'],dict):raise ModelContractError('math_problem must be object')
        from cloud_math_executor import execute
        report['math_model_selection']=route(spec['math_problem'])
        report['math_python_execution']=execute(spec)
    if 'heuristic_dispatcher' in spec:
        from heuristic_dispatcher import dispatch
        report['heuristic_dispatch_execution']=dispatch(spec['heuristic_dispatcher'])
    if 'multimodel_problem' in spec:
        from multimodel_engine import execute as multi_execute
        report['cross_representation_execution']=multi_execute(spec['multimodel_problem'])
    report['mathematical_decision_requires_python']=True
    if 'heuristic_problem' in spec:
        from heuristic_inference import execute as heuristic_execute
        report['heuristic_reasoning_execution']=heuristic_execute(spec['heuristic_problem'])
        report['heuristic_reasoning_interaction']='Computed counterexamples/model constraints override plan-only router claims; consult claim-specific evidence ceiling.'
    if 'engineering_spec' in spec:
        if not isinstance(spec['engineering_spec'],dict):raise ModelContractError('engineering_spec must be object')
        from vibe_transducer import transduce  # existing plugin runtime; no copies or patching
        report['engineering_static_analysis']=transduce(spec['engineering_spec'])
    report['execution_claim']='READ_ONLY_SELECTION_NOT_PROOF_NOT_PATCH'
    has_math=report.get('math_python_execution',{}).get('python_execution',{}).get('state')=='EXECUTED'
    has_dispatch='heuristic_dispatch_execution' in report
    has_multimodel=report.get('cross_representation_execution',{}).get('python_execution')=='EXECUTED'
    has_heuristic='heuristic_reasoning_execution' in report
    report['decision_gate']='PYTHON_EVIDENCE_AVAILABLE' if has_math or has_heuristic or has_multimodel or has_dispatch else 'PYTHON_COMPUTATION_REQUIRED'
    if has_heuristic:
        gate=report['heuristic_reasoning_execution']['decision_gate']
        if gate in {'REPRESENTATION_CONTRADICTION','NEEDS_REPRESENTATION_EVIDENCE'}:
            report['decision_gate']=gate
        elif any(t['action']=='DISCRIMINATE_RIVALS_OR_REVISE_MODEL_CLASS' for t in report['heuristic_reasoning_execution']['engineering_tasks']):
            report['decision_gate']='MODEL_DISCRIMINATION_REQUIRED'
    if has_dispatch:
        report['decision_gate']='DISPATCH_'+report['heuristic_dispatch_execution']['decision_gate']
        report['proof_claim']='BOUNDED_COMPUTATION_AND_CONDITIONAL_TASKS_NOT_DEPLOYMENT'
    if 'cross_representation_execution' in report:
        mmgate=report['cross_representation_execution']['decision_gate']
        if mmgate!='CONDITIONAL_NUMERIC_EVIDENCE':
            report['decision_gate']='MULTIMODEL_'+mmgate
        report['proof_claim']='FINITE_COMPUTATION_NOT_GENERAL_PROOF'
    return report

def main()->int:
    ap=argparse.ArgumentParser(description='Combined VCT math and engineering analysis')
    ap.add_argument('--spec',required=True)
    ns=ap.parse_args()
    try:
        with open(ns.spec,encoding='utf-8') as f:spec=json.load(f)
        print(json.dumps(combine(spec),ensure_ascii=False,indent=2))
        return 0
    except (ValueError,TypeError,OSError) as e:
        print('INVALID_INPUT: '+str(e),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
