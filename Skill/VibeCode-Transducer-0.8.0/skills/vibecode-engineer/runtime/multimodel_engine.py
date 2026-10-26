#!/usr/bin/env python3
"""VCT cross-representation mathematical execution, v0.6.

Bounded, typed, deterministic synthetic/declared-data probes. A report is neither
an empirical discovery nor a proof of an unrestricted theorem or code fix.
Requires no third-party packages and never evaluates caller-supplied Python.
"""
from __future__ import annotations
import hashlib
import json
import math
from typing import Any
import multimodel_kernel as K

VERSION = 'vct-multimodel/0.6.0'
PROBES = {'euler_decay','periodic_graph','inverse_ambiguity','graph_degrees',
          'observability_linear','noisy_derivative','region_candidates',
          'dimension_check','interval_decision','datalog_reachability','lens_laws'}
BRIDGES = {'sample-and-euler-discretize','graph-laplacian-continuum',
           'observation-map','coarse-grain','bidirectional-view','analogy',
           'algebraic-constraint'}
OUTCOME = {'EXECUTED','REFUTED_BY_WITNESS','UNDETERMINED','CONDITIONAL_PASS','UNSUPPORTED'}
MAX_PROBES = 50
MAX_BYTES = 180000

class MultiModelInputError(ValueError):
    pass

def _obj(v: Any, name: str) -> dict:
    if not isinstance(v,dict): raise MultiModelInputError(f'{name} must be object')
    return v

def _bounded_text(v: Any, name: str, maximum: int = 700) -> str:
    if not isinstance(v,str) or not 0 < len(v.strip()) <= maximum:
        raise MultiModelInputError(f'{name} must be nonempty string <= {maximum}')
    return v.strip()

def _num(v: Any, label: str) -> float:
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
        raise MultiModelInputError(f'{label} must be finite number')
    return float(v)

def _validate_input(data: dict) -> dict:
    if not isinstance(data,dict): raise MultiModelInputError('multimodel input must be object')
    try: size=len(json.dumps(data,ensure_ascii=False,allow_nan=False).encode('utf8'))
    except (TypeError,ValueError,OverflowError) as exc: raise MultiModelInputError('not valid finite JSON') from exc
    if size>MAX_BYTES: raise MultiModelInputError('input exceeds 180KB')
    goal=_bounded_text(data.get('goal'),'goal')
    claim=_bounded_text(data.get('target_claim'),'target_claim')
    provenance=_bounded_text(data.get('source_id'),'source_id')
    rep=_obj(data.get('representation'),'representation')
    for key in ('entity','unit','measurement_scale','observation_map'):
        _bounded_text(rep.get(key),f'representation.{key}')
    if rep['measurement_scale'] not in {'nominal','ordinal','interval','ratio','count','formal'}:
        raise MultiModelInputError('unrecognized measurement_scale')
    if not isinstance(rep.get('dimensionless'),bool):raise MultiModelInputError('explicit dimensionless boolean required')
    models=data.get('models')
    if not isinstance(models,list) or not 1<=len(models)<=12:raise MultiModelInputError('models length must be 1..12')
    ids=set()
    for idx,m in enumerate(models):
        m=_obj(m,'models entry');id_=_bounded_text(m.get('id'),'model.id',40)
        if id_ in ids:raise MultiModelInputError('duplicate model id')
        ids.add(id_)
        _bounded_text(m.get('domain'),'model.domain')
        _bounded_text(m.get('operator'),'model.operator')
        if not isinstance(m.get('assumptions'),list) or not all(isinstance(a,str) and a.strip() for a in m['assumptions']):
            raise MultiModelInputError('model.assumptions must be string list')
    bridges=data.get('bridges',[])
    if not isinstance(bridges,list) or len(bridges)>24:raise MultiModelInputError('0..24 bridges required')
    for b in bridges:
        b=_obj(b,'bridge')
        if b.get('from') not in ids or b.get('to') not in ids:raise MultiModelInputError('bridge must refer to existing models')
        if b.get('kind') not in BRIDGES:raise MultiModelInputError('unknown bridge kind')
        _bounded_text(b.get('preserved'),'bridge.preserved')
        _bounded_text(b.get('lost_or_unverified'),'bridge.lost_or_unverified')
    probes=data.get('probes')
    if not isinstance(probes,list) or not 1<=len(probes)<=MAX_PROBES:raise MultiModelInputError('probes length must be 1..50')
    keys=set()
    for p in probes:
        p=_obj(p,'probe');pid=_bounded_text(p.get('id'),'probe.id',64)
        if pid in keys:raise MultiModelInputError('duplicate probe id')
        keys.add(pid)
        _bounded_text(p.get('type'),'probe.type')
        if p['type'] not in PROBES:raise MultiModelInputError('unsupported probe type: '+p['type'])
        _obj(p.get('parameters'),'probe.parameters')
        if p.get('model_ids') is not None:
            if not isinstance(p['model_ids'],list) or not set(p['model_ids'])<=ids:raise MultiModelInputError('probe model_ids mismatch')
    decision=data.get('decision',{})
    _obj(decision,'decision')
    if 'error_tolerance' in decision and (_num(decision['error_tolerance'],'error_tolerance')<0):
        raise MultiModelInputError('error_tolerance must >= 0')
    return data

def _lens(p):
    src=_obj(p.get('source'),'lens.source')
    if 'name' not in src:raise MultiModelInputError('lens source requires name')
    view=_obj(p.get('updated_view'),'lens.updated_view')
    getput=K.lens_put(src,K.lens_get(src))==src
    putget=K.lens_get(K.lens_put(src,view))==view
    return {'GetPut':getput,'PutGet':putget,'hidden_state_retained_on_put':all(K.lens_put(src,view).get(k)==v for k,v in src.items() if k!='name'),
            'scope':'one name field projection; not universal bidirectional consistency proof'}

def _probe(t,p):
    if t=='euler_decay':
        step=_num(p.get('step'),'step');duration=_num(p.get('duration',1),'duration')
        if step<=0 or duration<0 or duration/step>1e7:raise MultiModelInputError('bounded Euler steps <= 10 million required')
        return K.euler_decay(_num(p.get('rate'),'rate'),step,duration)
    if t=='periodic_graph':return K.periodic_graph_eigenvalue(p.get('nodes'),p.get('harmonic',1))
    if t=='inverse_ambiguity':return K.inverse_ambiguity(_num(p.get('rate'),'rate'),_num(p.get('gain'),'gain'),_num(p.get('initial'),'initial'),_num(p.get('scale'),'scale'),p.get('times',[]))
    if t=='graph_degrees':return K.degrees_underdetermine_connectivity()
    if t=='observability_linear':return K.observability_linear(p.get('A'),p.get('C'))
    if t=='noisy_derivative':return K.noisy_central_derivative(_num(p.get('step'),'step'),_num(p.get('noise_bound',0.001),'noise_bound'))
    if t=='region_candidates':
        raw=p.get('observations');
        if not isinstance(raw,dict):raise MultiModelInputError('observations map required')
        try: obs={int(k):v for k,v in raw.items()}
        except (ValueError,TypeError) as exc: raise MultiModelInputError('integer observation keys required') from exc
        if len(obs)!=len(raw):raise MultiModelInputError('duplicate converted observations')
        next_n=p.get('next_n')
        if any(n<0 or n>1000 for n in obs) or (next_n is not None and (isinstance(next_n,bool) or not isinstance(next_n,int) or next_n>1000)):
            raise MultiModelInputError('region n must be integer 0..1000')
        return K.discriminate_regions(obs,next_n)
    if t=='dimension_check':return {'compatible':K.dimension_compatible(p.get('lhs'),p.get('rhs')),
                                     'scope':'dimension compatibility necessary, not sufficient for valid comparison'}
    if t=='interval_decision':return {'decision':K.robust_decision(_num(p.get('lower'),'lower'),_num(p.get('upper'),'upper'),_num(p.get('threshold'),'threshold'))}
    if t=='datalog_reachability':
        edges=p.get('edges')
        if not isinstance(edges,list) or len(edges)>150 or any(not isinstance(e,list) or len(e)!=2 or any(not isinstance(v,str) or not v for v in e) for e in edges):
            raise MultiModelInputError('edges require 0..150 pairs of strings')
        base=p.get('base_rule')
        if not isinstance(base,bool):raise MultiModelInputError('explicit base_rule bool required')
        paths=K.datalog_paths([tuple(e) for e in edges],base)
        return {'least_fixed_point':sorted([list(x) for x in paths]),'base_rule':base,'scope':'finite declared edge relation'}
    if t=='lens_laws':return _lens(p)
    raise MultiModelInputError('unsupported probe')

def _evaluate(t,result,decision):
    tol=decision.get('error_tolerance')
    if t=='dimension_check' and not result['compatible']:
        return 'REFUTED_BY_WITNESS','dimension mismatch for the declared comparison'
    if t=='inverse_ambiguity' and result['indistinguishable_outputs'] and result['different_parameters']:
        return 'REFUTED_BY_WITNESS','unique parameter reconstruction refuted in the specified forward model'
    if t=='graph_degrees' and result['same_degree_sequence'] and result['cycle_components']!=result['triangles_components']:
        return 'REFUTED_BY_WITNESS','degree sequence insufficient to reconstruct connectivity'
    if t=='observability_linear' and not result['observable']:
        return 'REFUTED_BY_WITNESS','declared 2D LTI state pair is not observable by rank diagnostic'
    if t=='region_candidates' and sum(result['fit_on_observed'].values())>1:
        return 'UNDETERMINED','multiple named families agree on supplied observations'
    if t=='region_candidates' and sum(result['fit_on_observed'].values())==0:
        return 'REFUTED_BY_WITNESS','all named candidate model families contradicted; revise model class'
    if t=='interval_decision' and result['decision']=='UNDETERMINED':
        return 'UNDETERMINED','decision boundary is crossed by the declared interval'
    if t=='lens_laws' and not (result['GetPut'] and result['PutGet']):
        return 'REFUTED_BY_WITNESS','lens law fails for supplied instance'
    if t=='euler_decay' and tol is not None:
        if result['absolute_bridge_error'] <= tol:return 'CONDITIONAL_PASS','observed step meets user-declared error tolerance at this time only'
        return 'REFUTED_BY_WITNESS','declared error tolerance exceeded at this time'
    if t=='periodic_graph' and tol is not None:
        if result['relative_error'] <= tol:return 'CONDITIONAL_PASS','specific periodic graph meets numeric tolerance at tested n only'
        return 'REFUTED_BY_WITNESS','specific periodic graph exceeds declared tolerance'
    return 'EXECUTED','bounded result computed; no general theorem or empirical interpretation follows'

def _tasks(data, probes):
    nodes=[('M00','Scope claim, source fingerprint and representation',[]),
           ('M01','Audit unit type, dimension, measurement and observables',['M00']),
           ('M02','Name rival models and lost structure',['M01']),
           ('M03','Check bridge preconditions and operator admissibility',['M02']),
           ('M04','Execute Python probes with typed inputs',['M03']),
           ('M05','Compare cross-representation results and uncertainty',['M04']),
           ('M06','Separate finite tests, formal proof obligations and empirical validation',['M05'])]
    dynamic=[]
    if any(p['type'] in ('inverse_ambiguity','observability_linear','graph_degrees') for p in probes):
        dynamic.append(('M07','Obtain independent observations or quotient by observational equivalence',['M05']))
    if any(p['type'] in ('euler_decay','periodic_graph','noisy_derivative') for p in probes):
        dynamic.append(('M08','Refinement study, sensitivity and approximation error budget',['M05']))
    if any(p['outcome']=='UNDETERMINED' for p in probes):
        dynamic.append(('M09','Design discriminating experiment; retain rival models',['M05']))
    if any(p['outcome']=='REFUTED_BY_WITNESS' for p in probes):
        dynamic.append(('M10','Revise earliest failed model assumption/representation and invalidate dependent claims',['M05']))
    nodes.extend(dynamic)
    nodes.append(('M11','Prepare conditional engineering acceptance criteria',['M06']+[n[0] for n in dynamic]))
    return [{'id':i,'action':name,'prerequisites':dep,'status':'PLANNED_NOT_EXECUTED'} for i,name,dep in nodes]

def execute(data:dict)->dict:
    data=_validate_input(data)
    digest=hashlib.sha256(json.dumps(data,sort_keys=True,allow_nan=False,ensure_ascii=False,separators=(',',':')).encode('utf8')).hexdigest()
    statuses=[]
    for p in data['probes']:
        try:
            raw=_probe(p['type'],p['parameters'])
            if not isinstance(raw,dict):raise MultiModelInputError('probe returned non-object')
            outcome,meaning=_evaluate(p['type'],raw,data.get('decision',{}))
            statuses.append({'id':p['id'],'type':p['type'],'state':'EXECUTED','outcome':outcome,'finding':meaning,
                             'result':raw,'evidence_scope':'PYTHON_COMPUTATION_SYNTHETIC_OR_DECLARED_INPUT_ONLY',
                             'proof_status':'UNPROVED_GENERAL_CLAIM','model_ids':p.get('model_ids',[])})
        except (ValueError,TypeError,OverflowError,KeyError,ZeroDivisionError) as exc:
            statuses.append({'id':p['id'],'type':p['type'],'state':'INVALID_PROBE','outcome':'UNSUPPORTED',
                             'finding':str(exc)[:300], 'result':None,'proof_status':'NOT_EVALUATED'})
    tasks=_tasks(data,statuses)
    any_invalid=any(r['state']=='INVALID_PROBE' for r in statuses)
    any_refuted=any(r['outcome']=='REFUTED_BY_WITNESS' for r in statuses)
    unresolved=any(r['outcome']=='UNDETERMINED' for r in statuses)
    decision='INVALID_PROBES_PRESENT' if any_invalid else 'REVISE_CLAIM_OR_MODEL' if any_refuted else 'DISCRIMINATING_EVIDENCE_REQUIRED' if unresolved else 'CONDITIONAL_NUMERIC_EVIDENCE'
    return {'schema':VERSION,'goal':data['goal'],'target_claim':data['target_claim'],
            'source_id':data['source_id'],'source_sha256':digest,
            'representation':data['representation'],'models':data['models'],'bridges':data.get('bridges',[]),
            'python_execution':'EXECUTED' if len(statuses)>0 and not any_invalid else 'PARTIAL_OR_INVALID',
            'decision_gate':decision,'probe_receipts':statuses,'engineering_tasks':tasks,
            'proof_obligations':['Theorem proof needs assumptions and a proof witness; finite numeric checks are not a universal proof',
              'Empirical construct validity and causal inference require independently sourced data/design',
              'Bridge convergence requires its topology, refinement regime, stability and error assumptions',
              'Reconstruction claims require identification and observability witnesses, or explicit equivalence classes'],
            'not_executed':['complete 99-entry theorem proving','empirical runtime/software validation','persistent cloud hosting'],
            'code_mutated':False}
