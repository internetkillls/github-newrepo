#!/usr/bin/env python3
"""VCT mathematical mental-model router: a bounded, read-only derivation planner.

All inferences are about eligibility given USER DECLARATIONS, never proofs of
real-world semantics or successful code behavior. No eval, network, mutation or
untrusted code execution. stdlib only.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA = 'vct-math-model-router/0.2.0'
CLAIMS = {'lexical','semantic','argument','statistical','causal','inverse','deductive','engineering'}
OBSERVATIONS = {'lexical_spans','numeric_samples','graph_edges','matrix','geometry','symbolic','code_state','unknown'}
FEATURES = {
 'sentence_bounded_tokens','traceable_offsets','defined_denominator',
 'overlapping_windows','censored_endpoints','repeated_observations',
 'annotated_propositions','annotation_validation','sampling_design',
 'noise_model','causal_design','identification_assumptions',
 'forward_model','inverse_domain','uniqueness_witness','stability_witness',
 'declared_dependencies','runtime_checkout','owner_approval',
 'theorem_assumptions','proof_object','type_contract',
 'dimension_matrix','physical_quantities','real_behavior_observed'
}
MAX_LEN = 3000

class ModelContractError(ValueError): pass

def _str(v:Any, field:str)->str:
    if not isinstance(v,str) or not v.strip() or len(v)>MAX_LEN:
        raise ModelContractError(f'{field} must be a nonempty bounded string')
    return v.strip()

def validate(spec:dict)->dict:
    if not isinstance(spec,dict):raise ModelContractError('spec must be an object')
    goal=_str(spec.get('goal'),'goal')
    claim=_str(spec.get('claim_type'),'claim_type')
    obs=_str(spec.get('observation_kind'),'observation_kind')
    if claim not in CLAIMS:raise ModelContractError('unsupported claim_type')
    if obs not in OBSERVATIONS:raise ModelContractError('unsupported observation_kind')
    flags=spec.get('features',{})
    if not isinstance(flags,dict) or len(flags)>len(FEATURES):raise ModelContractError('features must be a bounded object')
    for name,value in flags.items():
        if name not in FEATURES or not isinstance(value,bool):raise ModelContractError('features must use known boolean flags: '+str(name))
    if 'claim' in spec:_str(spec['claim'],'claim')
    return {'goal':goal,'claim_type':claim,'observation_kind':obs,'features':flags,
            'claim':spec.get('claim',''),'source_id':spec.get('source_id') if isinstance(spec.get('source_id'),str) else None}

def _operator(registry:dict[str,dict],mid:str,role:str,needed:set[str],features:dict,admissible:bool=True)->dict:
    if mid not in registry:raise ModelContractError('missing registry entry '+mid)
    missing=sorted(n for n in needed if features.get(n) is not True)
    state='NOT_APPLICABLE' if not admissible else 'NEEDS_EVIDENCE' if missing else 'ELIGIBLE_AS_METHOD'
    return {'math_id':mid,'name':registry[mid]['concept'],'role':role,'eligibility':state,
            'missing_preconditions':missing,'evidence_ceiling':'METHOD_ELIGIBILITY_ONLY',
            'not_a_proof':True}

def load_registry(path:Path|None=None)->dict[str,dict]:
    path=path or Path(__file__).resolve().parents[1]/'references'/'math_001_100_crosswalk.csv'
    with path.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    found={x['math_id']:x for x in rows}
    if len(found)!=100 or any(f'MATH-{i:03}' not in found for i in range(1,101)):
        raise ModelContractError('math crosswalk must contain 100 unique MATH-001..MATH-100 records')
    if 'PROPOSED' not in found['MATH-100']['current_case_status']:
        raise ModelContractError('MATH-100 must remain identified as proposed')
    return found

def task_graph(claim:str,obs:str,features:dict)->list[dict]:
    # Declarative DAG. Branches are conditional; absent capability != proof of failure.
    rows=[('T00','scope_and_provenance',[]),('T01','problem_and_claim_typing',['T00']),
          ('T02','observation_relations_and_spans',['T01']),
          ('T03','measurement_invariance_and_loss',['T02']),
          ('T04','instance_signature_and_rival_models',['T03']),
          ('T05','operator_eligibility_and_selection',['T04'])]
    data_tasks=[]
    if obs=='lexical_spans':
        rows.append(('T06','alpha_beta_lexical_extraction',['T05']))
        data_tasks.append('T06')
        if claim in {'semantic','argument'}:
            rows.append(('T07','candidate_surface_marker_gates',['T05']))
            data_tasks.append('T07')
    else:
        rows.append(('T06','typed_observation_or_engineering_probe',['T05']))
        data_tasks.append('T06')
    rows.append(('T08','observational_contract_qa',data_tasks))
    active=['T08']
    if claim=='statistical':
        rows.append(('T09','statistical_uncertainty_branch',['T08']))
        active.append('T09')
    if claim in {'semantic','argument'}:
        rows.append(('T10','semantic_proposition_annotation',['T08']))
        active.append('T10')
    if claim=='argument':
        rows.append(('T11','toulmin_warrant_graph',['T10']))
        active.append('T11')
    if claim in {'causal','inverse'}:
        rows.append(('T12','inverse_and_causal_eligibility',['T04','T08']))
        active.append('T12')
    rows.extend([('T13','engineering_intermediate_representation',active),
                 ('T14','acceptance_and_negative_controls',['T13']),
                 ('T15','mde_krr_projection',['T14'])])
    if features.get('owner_approval') and features.get('runtime_checkout'):
        rows.append(('T16','guarded_vct_build_handoff',['T15']))
    # Revision is an EVENT-DRIVEN trigger, not a node in the initial acyclic plan.
    return [{'id':tid,'name':name,'depends_on':deps,'status':'PLANNED_NOT_EXECUTED'} for tid,name,deps in rows]

def topo(tasks:list[dict])->list[str]:
    ids={t['id'] for t in tasks}
    deps={t['id']:set(t['depends_on']) for t in tasks}
    if any(not d<=ids for d in deps.values()):raise ModelContractError('dangling task dependency')
    order=[]
    while deps:
        ready=sorted(x for x,v in deps.items() if not v)
        if not ready:raise ModelContractError('task derivation contains cycle')
        for x in ready:
            order.append(x);deps.pop(x)
        for v in deps.values():v.difference_update(ready)
    return order

def route(spec:dict,registry_path:Path|None=None)->dict:
    s=validate(spec); reg=load_registry(registry_path)
    c=s['claim_type']; obs=s['observation_kind']; f=s['features']
    ops=[]
    def add(mid,role,needs=(),ok=True):ops.append(_operator(reg,mid,role,set(needs),f,ok))
    # Core cross-domain rules. No keyword-only promotion or automatic candidate scoring.
    add('MATH-007','universal-claim counterexample, bounded negative case')
    add('MATH-091','preserve abductive rivals, not proof')
    add('MATH-098','distinguish model, metamodel, implementation')
    if f.get('declared_dependencies'):
        add('MATH-061','task DAG order on declared user prerequisites',('declared_dependencies',))
    if obs=='lexical_spans':
        add('MATH-043','finite discrete offsets/gaps only',('sentence_bounded_tokens','traceable_offsets','defined_denominator'))
        if c in {'semantic','argument','inverse'}:
            add('MATH-088','do not infer semantics from noninjective lexical feature',('forward_model','inverse_domain'))
    if c in {'semantic','argument'}:
        add('MATH-001','modus ponens requires actual premises, not marker similarity',('annotated_propositions','theorem_assumptions'))
        add('MATH-008','test both directions of alleged semantic equivalence',('annotated_propositions','annotation_validation'))
    if c=='statistical':
        add('MATH-088','model-dependent estimation needs a well-posed interpretation',('sampling_design','noise_model'))
    if c=='inverse':add('MATH-088','existence uniqueness stability are separate',('forward_model','inverse_domain','uniqueness_witness','stability_witness'))
    if c=='causal':add('MATH-090','causal identification is separate from prediction',('causal_design','identification_assumptions'))
    if c=='deductive':add('MATH-001','premises to consequence under explicitly known assumptions',('theorem_assumptions','proof_object'))
    if f.get('physical_quantities'):
        add('MATH-100','Buckingham Pi is a PROPOSED registry addition, not automatically activated',('physical_quantities','dimension_matrix'))
    if obs=='graph_edges' or obs=='matrix':
        add('MATH-088','structural identifiability not implied by invariants',('forward_model','inverse_domain'))
    if c in {'argument','semantic'}:
        forbidden=['lexical_marker_implies_argument','word_count_implies_semantic_absence',
                   'surface_proxy_is_morphological_parser','phi_marker_is_formal_proof']
    elif c=='causal':forbidden=['correlation_proves_causation','prediction_proves_intervention_effect']
    elif c=='inverse':forbidden=['solver_returns_one_value_therefore_unique','regularization_recovers_ground_truth']
    else:forbidden=['operator_selected_means_target_behavior_verified']
    task_rows=task_graph(c,obs,f)
    missing=sorted({j for o in ops for j in o['missing_preconditions']})
    readiness='NEEDS_EVIDENCE' if missing else 'METHODS_PROVISIONALLY_ELIGIBLE'
    if c in {'semantic','argument'} and (not f.get('annotated_propositions') or not f.get('annotation_validation')):
        readiness='SEMANTIC_CLAIM_NOT_ESTABLISHED'
    if c=='causal' and (not f.get('causal_design') or not f.get('identification_assumptions')):
        readiness='CAUSAL_CLAIM_NOT_ESTABLISHED'
    if c=='inverse' and (not f.get('uniqueness_witness') or not f.get('stability_witness')):
        readiness='INVERSE_UNIQUENESS_OR_STABILITY_UNVERIFIED'
    return {'schema':SCHEMA,'task_goal':s['goal'],'claim_type':c,'observation_kind':obs,
            'source_id':s['source_id'],
            'epistemic_status':readiness,'operator_candidates':ops,
            'unresolved_features':missing,'forbidden_promotions':forbidden,
            'tasks':task_rows,'dependency_order':topo(task_rows),
            'revision_on_falsifier':{'task':'T17','trigger':['T08.failure','T14.failure'],
                                     'action':'revisit earliest failed representation/assumption; invalidate downstream receipts'},
            'notes':['The 100th math entry is PROPOSED, not pre-existing proof.',
                     'This is a specification-level mathematical strategy selector, not a proof engine.',
                     'Evidence flags are declarations; a real code/test witness must verify them.',
                     'Chosen operators are heuristic candidates, not installed numerical executors.',
                     'No source code was modified and no target behavior was tested.']}

def main()->int:
    p=argparse.ArgumentParser(description='VCT mathematical model selection / evidence gated task plan')
    p.add_argument('--spec',help='Read JSON spec from path; else stdin')
    p.add_argument('--output',help='Optional output file; not a repository patch')
    ns=p.parse_args()
    try:
        if ns.spec:
            with open(ns.spec,encoding='utf-8') as handle:spec=json.load(handle)
        else:spec=json.load(sys.stdin)
        result=route(spec)
        text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
        if ns.output:
            with open(ns.output,'w',encoding='utf-8') as out:out.write(text)
        else:sys.stdout.write(text)
        return 0
    except (ValueError,TypeError,OSError) as exc:
        print('INVALID_INPUT: '+str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
