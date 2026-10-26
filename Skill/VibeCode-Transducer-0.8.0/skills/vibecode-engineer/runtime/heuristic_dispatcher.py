#!/usr/bin/env python3
"""VCT/AREX bounded executable heuristic dispatcher 0.7.0.

Coordinates actual local Python multimodel probes, conditional Mahajan heuristics,
finite refinement, scoped falsification and optional metadata-only AREX discovery.
Read only: never executes donor code, edits repositories or launches test commands.
"""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from multimodel_engine import execute as execute_models, MultiModelInputError

VERSION = 'vct-heuristic-dispatcher/0.7.0'
_HEURISTICS = {
    'dimensions': 'Mahajan ch.1: require comparable quantities and declared units; valid dimensions not sufficient',
    'easy_cases': 'Mahajan ch.2: test boundaries and serious rivals; finite passes are not a proof',
    'lumping': 'Mahajan ch.3: coarse-grain only with target-relative error and lost information',
    'pictorial_proofs': 'Mahajan ch.4: diagram can disclose structural invariants, but source drawings are not formal proof receipts',
    'taking_out_big_part': 'Mahajan ch.5: prioritize dominant uncertainty and preserve remainder estimate',
    'analogy': 'Mahajan ch.6: use transfer with an explicit structural correspondence and defeater'
}

class DispatchInputError(ValueError):
    pass

def _text(s: Any, label: str, n: int = 2000) -> str:
    if not isinstance(s, str) or not s.strip() or len(s) > n:
        raise DispatchInputError(f'{label} must be nonempty string <= {n}')
    return s.strip()

def _sha(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(',', ':')).encode('utf-8')).hexdigest()

def _heuristics(spec: dict) -> list[dict]:
    types = {p['type'] for p in spec['probes']}
    h = ['dimensions', 'easy_cases', 'taking_out_big_part']
    if types & {'euler_decay','periodic_graph','noisy_derivative'}: h.append('lumping')
    if spec.get('bridges'): h.append('analogy')
    if types & {'graph_degrees','region_candidates','datalog_reachability','lens_laws'}: h.append('pictorial_proofs')
    return [{'name': k, 'warrant': _HEURISTICS[k], 'source': 'Mahajan 2010, Street-Fighting Mathematics', 'status': 'METHOD_SELECTED_NOT_PROOF'} for k in h]

def _refinement(probe: dict, max_rounds: int, tolerance: float | None) -> tuple[list[dict], str]:
    """Return a series of REAL rerun receipts, while preserving original failed witness.

    Only Euler steps and periodic cycles have a supported deterministic refinement law.
    Does not retrieve new observations or fit altered assumptions silently.
    """
    probe_type = probe['type']
    if probe_type not in {'euler_decay','periodic_graph'}:
        return [], 'NOT_APPLICABLE'
    if tolerance is None:
        return [], 'NO_DECLARED_TOLERANCE'
    reports = []
    params = copy.deepcopy(probe['parameters'])
    for j in range(1, max_rounds + 1):
        if probe_type == 'euler_decay':
            params['step'] = params['step'] / 2
            if params['step'] <= 0: break
        else:
            if isinstance(params.get('nodes'), bool) or not isinstance(params.get('nodes'), int): break
            params['nodes'] = params['nodes'] * 2
            if params['nodes'] > 4096: break
        # Re-enter the EXISTING typed v0.6 executor for the actual computation.
        current = {'goal': 'bounded refinement of ' + probe['id'],
                   'target_claim': 'finite-step bridge error within explicit tolerance',
                   'source_id': 'dispatcher-refinement:'+probe['id'],
                   'representation': {'entity':'original probe derived-state', 'unit':'original probe metric',
                     'measurement_scale':'ratio','dimensionless':True,'observation_map':'same underlying declared synthetic model'},
                   'models': [{'id':'candidate','domain':'declared','operator':probe_type,'assumptions':['original forward model unchanged']}],
                   'bridges': [],
                   'probes': [{'id': probe['id'], 'type': probe_type, 'parameters': copy.deepcopy(params), 'model_ids':['candidate']}],
                   'decision':{'error_tolerance':tolerance}}
        rr = execute_models(current)['probe_receipts'][0]
        reports.append({'iteration':j,'input_hash':_sha(current),'parameters':copy.deepcopy(params),
                       'outcome':rr['outcome'],'finding':rr['finding'],'result':rr['result']})
        if rr['outcome'] == 'CONDITIONAL_PASS':
            return reports, 'REFINEMENT_MEETS_DECLARED_TOLERANCE'
        if rr['state'] != 'EXECUTED':return reports, 'INVALID_REFINEMENT'
    return reports, 'BUDGET_EXHAUSTED_OR_LIMITED'

def _mahajan_case(case: str | None) -> dict | None:
    if case is None:return None
    if case == 'frustum_model_revision':
        # Mahajan 2010, ch.2 pp. 17-20: three constraints and missing ab term.
        alpha=Fraction(1,3);gamma=Fraction(1,3)
        beta=Fraction(1)-alpha-gamma
        def old(a,b,h):return h*(a*a+b*b)/2
        def revised(a,b,h):return h*(alpha*a*a+beta*a*b+gamma*b*b)
        witnesses=[]
        for a,b,h in [(0,2,1),(2,0,1),(2,2,1),(1,2,3),(0,0,1)]:
            a,b,h=Fraction(a),Fraction(b),Fraction(h)
            geometric_integral=h*(a*a+a*(b-a)+(b-a)**2/Fraction(3))
            witnesses.append({'a':str(a),'b':str(b),'h':str(h),
              'old':str(old(a,b,h)),'revised':str(revised(a,b,h)),
              'integrated_exact':str(geometric_integral),
              'new_matches_integral':revised(a,b,h)==geometric_integral})
        # Exact polynomial integration (with t in [0,1]):
        # int (a+(b-a)*t)^2 dt = a²+a(b-a)+(b-a)²/3
        # = (a²+ab+b²)/3, coefficient identity in Q[a,b].
        return {'case':case,'model_revision':'ADD_INTERACTION_TERM_ab',
          'old_model':'h*(a^2+b^2)/2', 'revised_model':'h*(a^2+a*b+b^2)/3',
          'coefficients_exact':{'alpha':str(alpha),'beta':str(beta),'gamma':str(gamma)},
          'symbolic_argument':'Integrate squared linear cross-section over normalized height t in [0,1]; expand polynomial exactly.',
          'witnesses':witnesses,'identity_level':'EXACT_POLYNOMIAL_IDENTITY_GIVEN_GEOMETRIC_CROSS_SECTION_ASSUMPTION',
          'source':'Mahajan (2010), ch.2, pp.17–20; geometry requires parallel similar square sections'}
    if case == 'gaussian_lumping':
        exact=math.sqrt(math.pi)
        candidates={'one_over_e':2.0,'FWHM':2.0*math.sqrt(math.log(2.0))}
        return {'case':case,'exact_sqrt_pi':exact,
          'approximations':[{'method':m,'value':v,'relative_error':abs(v-exact)/exact,
            'scope':'This Gaussian only, not universal error bound'} for m,v in candidates.items()],
          'source':'Mahajan (2010), ch.3, sec.3.2; approximation NOT mathematical proof'}
    raise DispatchInputError('unknown mahajan_case: '+str(case))

def _arex_route(query: str | None, *, injected_index: dict | None = None) -> dict:
    if query is None: return {'status':'NOT_APPLICABLE','reason':'No AREX question required; do not search by ritual','candidates':[]}
    _text(query, 'arex_query', 4000)
    # Load the existing sibling AREX adapter only; no network or untrusted code.
    path = Path(__file__).resolve().parents[2] / 'arex-repository-intelligence' / 'runtime' / 'arex_router.py'
    if not path.is_file():
        return {'status':'DONOR_METADATA_UNAVAILABLE','reason':'Packaged AREX router is absent from this test environment', 'candidates':[]}
    try:
        loader=importlib.util.spec_from_file_location('_vct_packaged_arex_router',path)
        module=importlib.util.module_from_spec(loader)
        loader.loader.exec_module(module)
        index = injected_index if injected_index is not None else module.load_index()
        result = module.route(query, index, top=5)
        return {'status':result['status'],'candidates':result['candidates'],
                'evidence_state':'METADATA_CANDIDATE_ONLY','source':'PACKAGED_AREX_OFFLINE_INDEX',
                'reason':result.get('reason',''),'code_executed_from_donors':False,'donor_installed':False}
    except (ValueError,TypeError,OSError,KeyError) as exc:
        return {'status':'AREX_ROUTE_UNVERIFIED','reason':str(exc)[:250],'candidates':[]}

def _task_graph(model_tasks: list[dict], findings: list[dict], arex: dict) -> dict:
    tasks=[{'id':t['id'],'action':t['action'],'prerequisites':t['prerequisites'],
            'state':'PLANNED','evidence':'NOT_EXECUTED'} for t in model_tasks]
    ids={x['id'] for x in tasks}
    additions=[('D00','Inspect input and hard constraints',[]),
               ('D01','Select only applicable Mahajan heuristic and falsifier',['D00']),
               ('D02','Execute model probes in Python',['D01']),
               ('D03','Separate conditional numerical witness from mathematical proof',['D02'])]
    if any(f['initial_outcome']=='REFUTED_BY_WITNESS' for f in findings):
        additions.append(('D04','Repair earliest contradicted assumption, retaining failure receipt',['D03']))
    if any(f['initial_outcome']=='UNDETERMINED' for f in findings):
        additions.append(('D05','Collect discriminating data; retain competing hypotheses',['D03']))
    if any(f['refinement'] for f in findings):
        additions.append(('D06','Review refinement stability and remaining error budget',['D03']))
    if arex['status'] not in {'NOT_APPLICABLE','DONOR_METADATA_UNAVAILABLE'}:
        additions.append(('D07','Inspect selected AREX source, license and prerequisites before donor tests',['D03']))
    additions.append(('D08','Review patch preview and request target-repository authorization',['D03']))
    for tid,action,pre in additions:
        if tid in ids:raise DispatchInputError('task ID collision')
        tasks.append({'id':tid,'action':action,'prerequisites':pre,'state':'PLANNED','evidence':'NOT_EXECUTED'})
    names={t['id'] for t in tasks}
    missing=[(t['id'],p) for t in tasks for p in t['prerequisites'] if p not in names]
    if missing:raise DispatchInputError(f'unknown task prerequisites: {missing}')
    # Required edges are acyclic; a repair edge is feedback, not a DAG prerequisite.
    indegree={t['id']:len(t['prerequisites']) for t in tasks}
    children={t['id']:[] for t in tasks}
    for t in tasks:
        for p in t['prerequisites']:children[p].append(t['id'])
    ready=sorted(i for i,degree in indegree.items() if degree==0)
    order=[]
    while ready:
        k=ready.pop(0);order.append(k)
        for c in children[k]:
            indegree[c]-=1
            if indegree[c]==0:ready.append(c);ready.sort()
    if len(order)!=len(tasks):raise DispatchInputError('invalid prerequisite DAG cycle')
    return {'tasks':tasks,'prerequisite_order':order,
            'conditional_feedback':[{'from':'D04','to':'D01','edge_type':'REPAIR_NOT_PREREQUISITE'}] if 'D04' in names else [],
            'tasks_executed':False}

def dispatch(spec: dict, *, _test_arex_index: dict | None = None) -> dict:
    if not isinstance(spec,dict):raise DispatchInputError('spec must be object')
    if spec.get('allow_writes') is not False:
        raise DispatchInputError('explicit allow_writes=false required; this dispatcher is read-only')
    if set(spec)-{'multimodel_problem','arex_query','max_refinements','allow_writes','engineering_spec','mahajan_case'}:
        raise DispatchInputError('unknown top-level fields; arbitrary commands and patches not supported')
    mm=spec.get('multimodel_problem')
    if not isinstance(mm,dict):raise DispatchInputError('multimodel_problem object required')
    refinements=spec.get('max_refinements',0)
    if isinstance(refinements,bool) or not isinstance(refinements,int) or not 0<=refinements<=6:
        raise DispatchInputError('max_refinements must be integer 0..6')
    base=execute_models(copy.deepcopy(mm))
    findings=[]
    by_id={p['id']:p for p in mm['probes']}
    tol=mm.get('decision',{}).get('error_tolerance')
    for receipt in base['probe_receipts']:
        original=by_id[receipt['id']]
        rounds=[];rstate='NOT_APPLICABLE'
        if receipt['outcome']=='REFUTED_BY_WITNESS' and receipt['type'] in {'euler_decay','periodic_graph'}:
            rounds,rstate=_refinement(original,refinements,tol)
        findings.append({'probe_id':receipt['id'],'type':receipt['type'],
            'initial_outcome':receipt['outcome'],'initial_witness':receipt['result'],
            'initial_finding':receipt['finding'],'initial_proof_status':receipt['proof_status'],
            'refinement':rounds,'refinement_status':rstate,
            'final_scope':'FINITE_SYNTHETIC_OR_DECLARED_TESTS_ONLY; REFINEMENT_IS_A_DIFFERENT_CONFIGURATION_NOT_RETROACTIVE_SUCCESS'})
    ar=_arex_route(spec.get('arex_query'),injected_index=_test_arex_index)
    mahajan=_mahajan_case(spec.get('mahajan_case'))
    tasks=_task_graph(base['engineering_tasks'],findings,ar)
    any_refuted=any(f['initial_outcome']=='REFUTED_BY_WITNESS' and f['refinement_status']!='REFINEMENT_MEETS_DECLARED_TOLERANCE' for f in findings)
    any_invalid=any(r['state']=='INVALID_PROBE' for r in base['probe_receipts'])
    unresolved=any(f['initial_outcome']=='UNDETERMINED' for f in findings)
    if any_invalid:gate='INVALID_OBSERVATION_OR_PROBE'
    elif any_refuted:gate='MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE'
    elif unresolved:gate='NEEDS_DISCRIMINATING_OBSERVATION'
    elif any(f['refinement_status']=='REFINEMENT_MEETS_DECLARED_TOLERANCE' for f in findings):gate='ORIGINAL_CLAIM_REFUTED_REFINED_VARIANT_PASSES'
    else:gate='CONDITIONAL_NUMERICAL_WITNESS'
    eng=None
    if 'engineering_spec' in spec:
        try:
            from vibe_transducer import transduce
            eng=transduce(spec['engineering_spec'])
        except ImportError:
            eng={'status':'ENGINEERING_RUNTIME_UNAVAILABLE','reason':'legacy transducer unavailable in this environment'}
    return {'schema':VERSION,'input_sha256':_sha(spec),'code_mutated':False,'pipeline_executed_in_python':True,
        'heuristics':_heuristics(mm), 'mahajan_case_execution':mahajan, 'initial_model_result':base,
        'findings':findings,'arex_discovery':ar,'engineering_analysis':eng,
        'task_graph':tasks,'decision_gate':gate,
        'claim_ceiling':'Bounded synthetic/declared-data numeric checks only; cannot certify general theorems, empirical observability of unmeasured reality, donor code, or target patch',
        'next_required_evidence':'Provide independent target-runtime test receipts and necessary observations before declaring validated engineering repair',
        'patch_state':'NO_TARGET_MUTATION_PREVIEW_OR_HUMAN_APPROVAL_REQUIRED'}
