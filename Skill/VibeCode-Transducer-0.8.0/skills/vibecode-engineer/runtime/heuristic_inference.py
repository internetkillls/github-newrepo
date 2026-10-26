#!/usr/bin/env python3
"""VCT v0.4: bounded representation, heuristic approximation and inference evidence.

No arbitrary expression evaluation, network, writes, probabilistic confidence invention,
or claim that declared relations are empirically verified. Candidate families are
explicit and finite. This is a computational *decision aid*, not an epistemic oracle.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, isfinite, log, pi, sqrt
from statistics import fmean
from typing import Any
import hashlib
import json
import sys

SCHEMA='vct-heuristic-inference/0.4.0'
CLAIMS={'lexical','semantic','argument','statistical','causal','inverse','deductive','engineering','abductive','inductive'}
SCALES={'nominal','ordinal','interval','ratio','count','none'}
KINDS={'physical','dimensionless','formal_assigned','latent_construct','unspecified'}
OPS={'count','order','sum','mean','ratio','frequency','classification'}
METHODS={'none','exposure_rate','candidate_discrimination','bounded_decision','gaussian_lumping'}
MODELS={'pow2','regions3'}
MAX_TEXT=1000
class HeuristicContractError(ValueError):pass

def _text(v:Any,field:str,required:bool=True)->str:
    if v is None and not required:return ''
    if not isinstance(v,str) or (required and not v.strip()) or len(v)>MAX_TEXT:
        raise HeuristicContractError(field+' must be a bounded string')
    return v.strip()

def _number(x:Any,field:str)->float:
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or abs(x)>1e12:
        raise HeuristicContractError(field+' must be a finite bounded number')
    return float(x)

def _digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,allow_nan=False,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()

def _representation(r:dict,claim:str)->dict:
    if not isinstance(r,dict):raise HeuristicContractError('representation object required')
    unit=r.get('unit')
    if not isinstance(unit,dict):raise HeuristicContractError('representation.unit object required')
    kind=_text(unit.get('kind'),'unit.kind')
    if kind not in {'event','entity','relation','property','latent_construct'}:raise HeuristicContractError('invalid unit.kind')
    scale=_text(unit.get('measurement_scale'),'unit.measurement_scale')
    if scale not in SCALES:raise HeuristicContractError('invalid measurement scale')
    dim=_text(unit.get('dimension_kind'),'unit.dimension_kind')
    if dim not in KINDS:raise HeuristicContractError('invalid dimension kind')
    for key in ['name','identity_rule','boundary_rule','source_ref']:
        _text(unit.get(key),f'unit.{key}',required=False)
    operations=r.get('operations',[])
    if not isinstance(operations,list) or len(operations)>8 or any(o not in OPS for o in operations):
        raise HeuristicContractError('operations must be subset of known primitives')
    if len(set(operations))!=len(operations):raise HeuristicContractError('duplicate operation')
    preserved=r.get('preserved_relations',[])
    required=r.get('required_relations',[])
    if (not isinstance(preserved,list) or not isinstance(required,list) or
        len(preserved)>12 or len(required)>12 or
        any(not isinstance(v,str) or not v or len(v)>70 for v in preserved+required)):
        raise HeuristicContractError('relation names must be bounded text')
    blocked=[]; missing=[];warnings=[]
    if not unit.get('name'):missing.append('UNIT_NAME')
    if not unit.get('identity_rule'):missing.append('UNIT_IDENTITY_RULE')
    if not unit.get('boundary_rule'):missing.append('UNIT_BOUNDARY_RULE')
    if not unit.get('source_ref'):missing.append('OBSERVATION_PROVENANCE')
    if not set(required)<=set(preserved):missing.append('UNPRESERVED_REQUIRED_RELATIONS')
    if scale in {'nominal','none'} and any(o in operations for o in ('mean','ratio','sum','order')):
        blocked.append('OPERATIONS_NOT_LICENSED_BY_MEASUREMENT_SCALE')
    if scale=='ordinal' and any(o in operations for o in ('mean','ratio','sum')):
        blocked.append('ARITHMETIC_NOT_LICENSED_BY_ORDINAL_SCALE')
    if scale=='interval' and 'ratio' in operations:
        blocked.append('RATIO_NOT_LICENSED_BY_INTERVAL_SCALE')
    if dim=='latent_construct':missing.append('LATENT_CONSTRUCT_VALIDITY_EVIDENCE')
    if dim=='formal_assigned':missing.append('FORMAL_DIMENSION_CONSISTENCY_TEST')
    dimension_equalities=[]
    checks=r.get('dimension_checks',[])
    if not isinstance(checks,list) or len(checks)>12:raise HeuristicContractError('dimension_checks must be bounded list')
    for entry in checks:
        if not isinstance(entry,dict) or not all(k in entry for k in ('left','right')):raise HeuristicContractError('dimension check requires left/right vectors')
        l=entry['left'];rr=entry['right']
        if not isinstance(l,list) or not isinstance(rr,list) or len(l)!=len(rr) or not 1<=len(l)<=8:
            raise HeuristicContractError('dimension vectors must be equal length <=8')
        a=[_number(x,'dimension exponent') for x in l];b=[_number(x,'dimension exponent') for x in rr]
        eq=a==b
        dimension_equalities.append({'equal':eq,'left':a,'right':b})
        if not eq:blocked.append('DIMENSIONALLY_INCONSISTENT_RELATION')
    if dim=='formal_assigned' and dimension_equalities and all(x['equal'] for x in dimension_equalities):
        missing.remove('FORMAL_DIMENSION_CONSISTENCY_TEST')
        warnings.append('Formal dimension vectors satisfy declared constraints only; assignment is not empirically identified')
    if claim in {'semantic','argument','causal'} and kind in {'event','property'}:
        missing.append('HIGHER_ORDER_CLAIM_REQUIRES_SEPARATE_WARRANT')
    if claim in {'semantic','argument'} and 'frequency' in operations:
        warnings.append('Counted lexical events do not entail proposition identity or rhetorical role')
    state='REJECTED' if blocked else 'SPECIFICATION_INCOMPLETE' if missing else 'DECLARED_WARRANT_NOT_INDEPENDENTLY_VERIFIED'
    adequacy='INCOMPATIBLE_FOR_TARGET_CLAIM' if blocked else 'TARGET_WARRANT_MISSING' if ('HIGHER_ORDER_CLAIM_REQUIRES_SEPARATE_WARRANT' in missing or 'LATENT_CONSTRUCT_VALIDITY_EVIDENCE' in missing) else 'CONDITIONALLY_ADEQUATE_FOR_DECLARED_TASK'
    return {'representational_warrant':state,'task_relative_adequacy':adequacy,
            'missing':sorted(set(missing)),'contradictions':sorted(set(blocked)),
            'preserved_relations_are_user_declarations':True,
            'dimension_checks':dimension_equalities,'warnings':warnings,
            'non_dimensional_does_not_mean_unidimensional':True}

def _normalize(n:dict)->dict:
    if not isinstance(n,dict):raise HeuristicContractError('normalization must be object')
    kind=_text(n.get('method','none'),'normalization.method')
    if kind not in {'none','exposure_rate'}:raise HeuristicContractError('unsupported normalization')
    if kind=='none':return {'method':'none','state':'NO_NORMALIZATION_REQUESTED','observational_only':True}
    pairs=n.get('observations')
    if not isinstance(pairs,list) or not 1<=len(pairs)<=200:raise HeuristicContractError('exposure_rate needs 1..200 observations')
    rows=[]
    for q in pairs:
        if not isinstance(q,dict):raise HeuristicContractError('observations must be objects')
        numerator=q.get('count');denom=q.get('exposure')
        if not isinstance(numerator,int) or isinstance(numerator,bool) or numerator<0 or not isinstance(denom,int) or isinstance(denom,bool) or denom<0:
            raise HeuristicContractError('count and exposure must be nonnegative integers')
        if denom==0 and numerator>0:
            raise HeuristicContractError('positive hits with zero eligible positions violate the counting contract')
        if denom==0:
            rows.append({'count':numerator,'exposure':denom,'rate':None,'state':'UNDEFINED_ZERO_EXPOSURE'});continue
        if numerator>denom:
            raise HeuristicContractError('count cannot exceed eligible binary positions; change count contract if multiple hits per position')
        rows.append({'count':numerator,'exposure':denom,'rate':numerator/denom,'state':'COMPUTED'})
    complete=[q['rate'] for q in rows if q['rate'] is not None]
    same=(len(complete)>1 and len(set(complete))==1)
    return {'method':kind,'state':'COMPUTED_DESCRIPTIVE_RATES','rows':rows,
            'equal_rates_do_not_identify_equal_semantics':same,
            'sampling_independence_not_inferred':True}

def _model(mid:str,x:int)->int:
    if mid=='pow2':return 2**x
    if mid=='regions3':return sum(comb(x,k) for k in range(min(x,3)+1))
    raise HeuristicContractError('unsupported model')

def _case(c:dict)->tuple[int,float]:
    if not isinstance(c,dict):raise HeuristicContractError('cases must be objects')
    x=c.get('x');y=c.get('y')
    if isinstance(x,bool) or not isinstance(x,int) or x<0 or x>30:
        raise HeuristicContractError('x must be integer between 0 and 30')
    return x,_number(y,'observed y')

def _discriminate(p:dict)->dict:
    ids=p.get('candidates',[]);cases=p.get('observations',[]);held=p.get('holdout',[])
    if not isinstance(ids,list) or len(ids)<2 or len(ids)>len(MODELS) or len(set(ids))!=len(ids) or any(x not in MODELS for x in ids):
        raise HeuristicContractError('need two distinct supported candidate models')
    if not isinstance(cases,list) or not 1<=len(cases)<=32 or not isinstance(held,list) or len(held)>16:
        raise HeuristicContractError('bounded observations and holdout required')
    fit=[_case(c) for c in cases];test=[_case(c) for c in held]
    if len({x for x,y in fit})!=len(fit):raise HeuristicContractError('duplicate observation x: specify measurement reconciliation')
    if set(x for x,y in fit)&set(x for x,y in test):raise HeuristicContractError('holdout must not overlap training x')
    tol=_number(p.get('tolerance',0),'tolerance')
    if tol<0:raise HeuristicContractError('tolerance must not be negative')
    models=[]
    for mid in ids:
        err=[abs(_model(mid,x)-y) for x,y in fit]
        h_err=[abs(_model(mid,x)-y) for x,y in test]
        models.append({'id':mid,'training_max_abs_error':max(err),'training_compatible':all(e<=tol for e in err),
                       'heldout_max_abs_error':max(h_err) if h_err else None,
                       'heldout_compatible':all(e<=tol for e in h_err) if h_err else None,
                       'deductive_model_consequence_at_next_x':_model(mid,max(x for x,y in fit)+1),
                       'hypothesis_status':'CANDIDATE_NOT_PROVEN'})
    train=[m for m in models if m['training_compatible']]
    survivors=[m for m in train if not test or m['heldout_compatible']]
    if not train:status='REVISE_MODEL_CLASS'
    elif len(survivors)>1:status='UNDERDETERMINED'
    elif len(survivors)==1 and test:status='DISCRIMINATED_ON_HELDOUT_ONLY'
    elif not survivors:status='REVISE_MODEL_CLASS'
    else:status='PROVISIONALLY_UNIQUE_IN_DECLARED_CANDIDATE_SET'
    nextx=next((n for n in range(max(x for x,y in fit)+1,31) if len({_model(mid,n) for mid in ids})>1),None)
    return {'method':'candidate_discrimination','state':status,'models':models,
            'abduction':'COMPATIBLE_EXPLANATIONS_ONLY','induction':'OBSERVED_INSTANCES_ONLY',
            'deduction':'MODEL_CONDITIONAL_PREDICTIONS_ONLY',
            'recommended_discriminating_x':nextx,'holdout_independent_by_contract_only':bool(test),
            'outside_candidate_set_unidentifiable':True,
            'next_tasks':['Test a predicted divergence using independently obtained evidence' if nextx is not None else 'Find new candidate families',
                          'Inspect structural assumptions; passing finitely many cases is not a proof']}

def _bounds(p:dict)->dict:
    a=_number(p.get('lower'),'lower');b=_number(p.get('upper'),'upper');th=_number(p.get('threshold'),'threshold')
    if a>b:raise HeuristicContractError('lower bound exceeds upper bound')
    direction=p.get('rule','greater_equal')
    if direction not in {'greater_equal','less_equal'}:raise HeuristicContractError('unsupported decision rule')
    if direction=='greater_equal':status='ROBUST_YES' if a>=th else 'ROBUST_NO' if b<th else 'UNDETERMINED'
    else:status='ROBUST_YES' if b<=th else 'ROBUST_NO' if a>th else 'UNDETERMINED'
    return {'method':'bounded_decision','state':status,'bounds':[a,b],'threshold':th,
            'rule':direction,'bounds_are_assumed_not_estimated':True,
            'next_tasks':['Collect tighter justified bounds before committing' if status=='UNDETERMINED' else 'Verify source and semantics of the asserted bounds']}

def _gaussian()->dict:
    exact=sqrt(pi);one_e=2.;fwhm=2*sqrt(log(2))
    return {'method':'gaussian_lumping','state':'REFERENCE_EXAMPLE_COMPUTED',
            'exact':exact,'one_over_e':one_e,'fwhm':fwhm,
            'relative_error_one_over_e':(one_e-exact)/exact,
            'relative_error_fwhm':(fwhm-exact)/exact,
            'not_a_general_error_certificate':True}

def _deduction(d:dict)->dict:
    if not isinstance(d,dict):raise HeuristicContractError('deduction object required')
    rule=d.get('rule','none')
    if rule=='none':return {'rule':'none','state':'NO_DEDUCTION_REQUESTED'}
    if rule!='noninjective_label_counterexample':raise HeuristicContractError('unsupported deductive rule')
    observations=d.get('observations')
    if not isinstance(observations,list) or len(observations)!=2 or any(not isinstance(q,dict) for q in observations):
        raise HeuristicContractError('two feature-label witnesses required')
    left,right=observations
    for q in (left,right):
        if 'feature' not in q or 'label' not in q:raise HeuristicContractError('witness needs feature and label')
        if not isinstance(q['label'],str) or not q['label']:raise HeuristicContractError('label must be nonempty string')
    match=(left['feature']==right['feature'])
    incompatible=left['label']!=right['label']
    return {'rule':rule,'state':'CONDITIONAL_COUNTEREXAMPLE_ESTABLISHED' if match and incompatible else 'NO_DISCRIMINATING_COUNTEREXAMPLE',
            'feature_equal':match,'label_different':incompatible,
            'conclusion':'No single-valued deterministic g(feature) recovers both labels if observations and labels are valid' if match and incompatible else 'Insufficient to refute deterministic feature-to-label mapping',
            'witness_truth_is_declared_not_independently_validated':True}

def execute(spec:dict)->dict:
    if not isinstance(spec,dict):raise HeuristicContractError('heuristic_problem must be object')
    claim=_text(spec.get('claim_type'),'claim_type')
    if claim not in CLAIMS:raise HeuristicContractError('unsupported claim type')
    _text(spec.get('goal'),'goal')
    rep=_representation(spec.get('representation'),claim)
    normalization=_normalize(spec.get('normalization',{'method':'none'}))
    a=spec.get('approximation',{'method':'none'})
    if not isinstance(a,dict):raise HeuristicContractError('approximation must be object')
    method=a.get('method','none')
    if method not in METHODS:raise HeuristicContractError('unsupported approximation method')
    if method=='candidate_discrimination':approx=_discriminate(a)
    elif method=='bounded_decision':approx=_bounds(a)
    elif method=='gaussian_lumping':approx=_gaussian()
    elif method=='exposure_rate':approx=_normalize({**a,'method':'exposure_rate'})
    else:approx={'method':'none','state':'NO_APPROXIMATION_REQUESTED'}
    deduction=_deduction(spec.get('deduction',{'rule':'none'}))
    tasks=[]
    if rep['contradictions']:
        tasks.append({'id':'H01','action':'REVISE_UNIT_OR_OPERATION','reason':rep['contradictions']})
    if rep['missing']:
        tasks.append({'id':'H02','action':'ESTABLISH_REPRESENTATION_WARRANT','reason':rep['missing']})
    if normalization.get('equal_rates_do_not_identify_equal_semantics'):
        tasks.append({'id':'H03','action':'TEST_SEMANTIC_NONIDENTIFIABILITY','reason':'equal rates can hide different discourse roles'})
    if approx['state'] in {'UNDERDETERMINED','REVISE_MODEL_CLASS','UNDETERMINED'}:
        tasks.append({'id':'H04','action':'DISCRIMINATE_RIVALS_OR_REVISE_MODEL_CLASS','reason':approx['state']})
    if approx['state']=='DISCRIMINATED_ON_HELDOUT_ONLY':
        tasks.append({'id':'H05','action':'VALIDATE_OUT_OF_SAMPLE_GENERALIZATION','reason':'a held-out case does not prove a law'})
    if deduction['state']=='CONDITIONAL_COUNTEREXAMPLE_ESTABLISHED':
        tasks.append({'id':'H06','action':'INVALIDATE_SUFFICIENT_FEATURE_CLAIM','reason':'noninjectivity conditional on labels'})
    for i,item in enumerate(tasks):
        item['depends_on']=[tasks[i-1]['id']] if i else []
        item['status']='PLANNED_NOT_EXECUTED'
    tasks.append({'id':'H07','action':'TRANSLATE_CONDITIONAL_RESULTS_TO_VCT_TASKS',
                  'reason':'evidence ceiling and tests must be carried into engineering',
                  'depends_on':[tasks[-1]['id']] if tasks else [],'status':'PLANNED_NOT_EXECUTED'})
    no_numeric=(method=='none' and normalization['method']=='none' and deduction['rule']=='none')
    state=('REPRESENTATION_CONTRADICTION' if rep['contradictions'] else
           'NEEDS_REPRESENTATION_EVIDENCE' if rep['missing'] else
           'REPRESENTATION_AUDIT_ONLY' if no_numeric else 'EVIDENCE_GATED_COMPUTATION_EXECUTED')
    return {'schema':SCHEMA,'runtime':{'engine':'bounded_python_stdlib','python_version':sys.version.split()[0],
                'input_sha256':_digest(spec)},
            'representational_admissibility':rep,'normalization':normalization,'heuristic_inference':approx,
            'deductive_check':deduction,'engineering_tasks':tasks,
            'decision_gate':state,
            'epistemic_ceiling':'CONDITIONAL_COMPUTATIONAL_EVIDENCE_ONLY',
            'limitations':['Declared unit identity and preserved relations are not empirically proved',
                           'Limited candidate grammar; does not autonomously invent arbitrary valid models',
                           'No inferential population statistics, causal effect, arbitrary theorem prover, or semantic annotation validator',
                           'No deployment or persistent cloud execution is provided by this source']}
