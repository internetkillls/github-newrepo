#!/usr/bin/env python3
"""RMC v0.6.6 declared-input consistency gate. Read-only; no LLM semantic adjudication.

Its input describes CLAIMS about tests, not necessarily true facts. It must never
turn declarative 'observed' booleans into a claim of independent verification.
"""
from __future__ import annotations
import argparse
import json
from typing import Any

_ALLOWED_FINDINGS={'PASS','NOT_APPLICABLE','UNVERIFIED','CONTRADICTED','UNSUPPORTED','PROVISIONAL'}
_ALLOWED_DISPOSITIONS={'CONTINUE','SKIP_CHECK','NARROW_CLAIM','WITHHOLD_CLAIM','REVISE_PREMISE','CHANGE_METHOD'}
_MAX_CLAIMS=200
_MAX_EDGES=500

class ContractError(ValueError):
    pass


def _bounded_name(value: Any, where: str) -> str:
    if not isinstance(value,str) or not value.strip() or len(value)>160:
        raise ContractError(f'{where} requires a nonblank string <=160 characters')
    return value


def _boolean(spec:dict, field:str, default=None):
    value=spec.get(field,default)
    if not isinstance(value,bool):
        raise ContractError(f'{field} must be a boolean, not a string/null')
    return value


def judge(spec: dict) -> dict:
    """Classify declared obligation, never claim independent source verification."""
    if not isinstance(spec,dict):
        raise ContractError('obligation must be object')
    claim_id=_bounded_name(spec.get('claim_id'), 'claim_id')
    applicable=_boolean(spec,'applicable')
    decision_change=_boolean(spec,'decision_change_if_fail')
    contradicted=_boolean(spec,'contradicted',False)
    method_supported=_boolean(spec,'method_supported',True)
    witness_required=_boolean(spec,'witness_required',False)
    witness_observed=_boolean(spec,'witness_observed',False)
    noncritical_debt=_boolean(spec,'noncritical_debt',False)
    # The caller must specify the restriction target when holding or revising a claim.
    affected=spec.get('claim_affected',claim_id)
    _bounded_name(affected,'claim_affected')
    if not applicable or not decision_change:
        status,action='NOT_APPLICABLE','SKIP_CHECK'
    elif contradicted:
        status,action='CONTRADICTED','REVISE_PREMISE'
    elif not method_supported:
        status,action='UNSUPPORTED','CHANGE_METHOD'
    elif witness_required and not witness_observed:
        status,action='UNVERIFIED','WITHHOLD_CLAIM'
    elif noncritical_debt:
        status,action='PROVISIONAL','NARROW_CLAIM'
    else:
        status,action='PASS','CONTINUE'
    assert status in _ALLOWED_FINDINGS and action in _ALLOWED_DISPOSITIONS
    return {'claim_id':claim_id,'finding':status,'disposition':action,
            'claim_affected':affected,'declared_input_only':True,
            'global_work_blocked':False,
            'claim_ceiling':'SCOPED_DECLARED_CHECK_ONLY',
            'repair_target':spec.get('repair_target') if status=='CONTRADICTED' else None}


def sort_prerequisites(edges: list) -> dict:
    """Kahn's algorithm for PREREQUISITE edges only; feedback edges excluded."""
    nodes={x for pair in edges for x in pair}
    indeg={n:0 for n in nodes}
    adj={n:set() for n in nodes}
    for a,b in edges:
        if b not in adj[a]:
            adj[a].add(b)
            indeg[b]+=1
    ready=sorted(n for n in nodes if indeg[n]==0)
    order=[]
    while ready:
        n=ready.pop(0)
        order.append(n)
        for m in sorted(adj[n]):
            indeg[m]-=1
            if indeg[m]==0:
                ready.append(m)
                ready.sort()
    blocked=sorted(n for n in nodes if indeg[n]>0)
    return {'status':'CIRCULAR_PREREQUISITE' if blocked else 'ORDERED',
            'ordering':None if blocked else order,
            'cyclic_or_blocked_nodes':blocked,
            'claim_ceiling':'DECLARED_PREREQUISITE_GRAPH_ONLY'}


def evaluate(payload: dict) -> dict:
    if not isinstance(payload,dict):
        raise ContractError('input must be JSON object')
    obligations=payload.get('obligations',[])
    edges=payload.get('edges',[])
    if not isinstance(obligations,list) or len(obligations)>_MAX_CLAIMS:
        raise ContractError('obligations must be bounded list')
    if not isinstance(edges,list) or len(edges)>_MAX_EDGES:
        raise ContractError('edges must be bounded list')
    findings=[judge(x) for x in obligations]
    lists={'PREREQUISITE':[], 'TRANSITION':[], 'REPAIR':[]}
    for e in edges:
        if not isinstance(e,dict) or set(e)!={'kind','source','target'}:
            raise ContractError('each edge must have exactly kind/source/target')
        kind=e['kind']
        if kind not in lists:
            raise ContractError('unrecognized edge kind')
        source=_bounded_name(e['source'],'edge source')
        target=_bounded_name(e['target'],'edge target')
        lists[kind].append((source,target))
    g=sort_prerequisites(lists['PREREQUISITE'])
    g.update({'excluded_transition_count':len(lists['TRANSITION']),
              'excluded_repair_count':len(lists['REPAIR']),
              'cycles_in_feedback_edges_not_tested_as_prerequisites':True})
    return {'kernel':'RMC-adaptive-gate','kernel_version':'0.6.6',
            'input_warrant':'CALLER_DECLARATIONS_UNVERIFIED',
            'findings':findings,'dependency_graph':g,
            'behavioral_compliance_verified':False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--spec',required=True,help='local JSON path, no writes/network')
    args=p.parse_args()
    with open(args.spec,encoding='utf-8') as f:
        payload=json.load(f)
    print(json.dumps(evaluate(payload),indent=2,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':
    main()
