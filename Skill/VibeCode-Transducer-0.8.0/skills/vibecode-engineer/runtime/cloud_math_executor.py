#!/usr/bin/env python3
"""VCT 0.3 Python-first evidence kernel for bounded, typed mathematical data.

Runs ACTUAL stdlib calculations, not mathematical proofs or a hosted background
service. All inputs are explicit JSON; no eval, network, subprocess, code writes.
Every decision includes execution state, source digest, claim ceiling and tasks.
"""
from __future__ import annotations
import hashlib
import json
import math
import re
import statistics
import sys
import unicodedata
from collections import deque
from fractions import Fraction
from typing import Any

from math_model_router import ModelContractError, route

VERSION = 'vct-python-evidence/0.3.0'
MAX_PARAGRAPHS = 400
MAX_TOKENS = 16000
MAX_POINTS = 2000
MAX_NODES = 1000
MAX_MATRIX = 12
MAX_NUMERIC = 5000
TOKEN = re.compile(r"[^\W_]+(?:['’-][^\W_]+)*", re.UNICODE)
SENTENCE = re.compile(r'[^.!?\n]+(?:[.!?]+|$)', re.UNICODE)

def canonical_digest(obj:Any)->str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode('utf-8')).hexdigest()

def _num(v:Any)->float:
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
        raise ModelContractError('numeric observation requires finite numbers')
    return float(v)

def _tokens(x:str)->list[str]:
    return [unicodedata.normalize('NFC',m.group(0)).casefold() for m in TOKEN.finditer(x)]

def _sentences(paragraph:str)->list[list[str]]:
    return [t for chunk in SENTENCE.findall(paragraph) if (t:=_tokens(chunk))]

def _starts(tokens:list[str], phrase:list[str])->list[int]:
    n=len(phrase)
    return [i for i in range(len(tokens)-n+1) if tokens[i:i+n]==phrase] if n else []

def _phrase_matches(sents:list[list[str]],phrase:list[str],base:int=0)->list[int]:
    offsets=[];pos=base
    for sent in sents:
        offsets.extend(pos+i for i in _starts(sent,phrase));pos+=len(sent)
    return offsets

def lexical(p:dict)->dict:
    paragraphs=p.get('paragraphs')
    if not isinstance(paragraphs,list) or not paragraphs or len(paragraphs)>MAX_PARAGRAPHS or any(not isinstance(v,str) or len(v)>8000 for v in paragraphs):
        raise ModelContractError('lexical paragraphs must be 1..400 bounded strings')
    anchor=p.get('anchor'); boundary=p.get('boundary'); tracked=p.get('tracked',[])
    if not isinstance(anchor,str) or not _tokens(anchor):raise ModelContractError('nonempty anchor phrase required')
    if boundary is not None and (not isinstance(boundary,str) or not _tokens(boundary)):raise ModelContractError('boundary must be nonempty phrase')
    if not isinstance(tracked,list) or len(tracked)>20 or any(not isinstance(v,str) or not _tokens(v) for v in tracked):raise ModelContractError('tracked must be <=20 phrases')
    parsed=[_sentences(x) for x in paragraphs]
    flat=[sum(x,[]) for x in parsed]
    total=sum(map(len,flat))
    if total>MAX_TOKENS:raise ModelContractError('corpus too large (tokens)')
    bases=[];offset=0
    for words in flat:bases.append(offset);offset+=len(words)
    av=_tokens(anchor); bv=_tokens(boundary) if boundary else []
    matches=[]
    for j,sents in enumerate(parsed):
        for pos in _phrase_matches(sents,av,bases[j]):matches.append((j,pos))
    results=[]
    for pidx,start in matches[:80]:
        windows={}
        for k in (3,5):
            included=parsed[max(0,pidx-k+1):pidx+1]
            ws=[s for par in included for s in par]
            windows[f'W{k}']={}
            for word in tracked:
                tokens=_tokens(word); n=len(tokens)
                count=sum(len(_starts(s,tokens)) for s in ws)
                denom=sum(max(0,len(s)-n+1) for s in ws)
                windows[f'W{k}'][word]={'count':count,'eligible_positions':denom,'rate':count/denom if denom else None}
        lag=None
        if bv:
            last=start+len(av)-1
            endpoints=[]
            for j in range(pidx,min(len(parsed),pidx+4)):
                endpoints.extend(pos for pos in _phrase_matches(parsed[j],bv,bases[j]) if pos>last)
            if endpoints:lag=min(endpoints)-last-1
        results.append({'paragraph_id':pidx,'anchor_token_offset':start,'windows':windows,
                        'boundary_lag_tokens':lag,'boundary_censored':bool(bv) and lag is None})
    beta={}
    for word in tracked:
        token=_tokens(word); occ=[]
        for j, sents in enumerate(parsed):occ.extend(_phrase_matches(sents,token,bases[j]))
        gaps=[occ[i+1]-(occ[i]+len(token)) for i in range(len(occ)-1)]
        beta[word]={'occurrences':len(occ),'observed_gaps_tokens':gaps,'repeated_gap_established':len(gaps)>0}
    n_complete=sum(x['boundary_lag_tokens'] is not None for x in results)
    lags=[x['boundary_lag_tokens'] for x in results if x['boundary_lag_tokens'] is not None]
    return {'kind':'lexical_spans','anchor_count':len(matches),'events_evaluated':len(results),
            'events_truncated':max(0,len(matches)-len(results)),'events':results,'beta':beta,
            'complete_endpoints':n_complete,'censored_endpoints':sum(x['boundary_censored'] for x in results),
            'mean_complete_lag':statistics.mean(lags) if lags else None,
            'observational_constraints':['W3/W5 overlap; rates are descriptive, not independent tests',
                                         'Unseen boundary = censored, never lag zero',
                                         'Lexical absence does not establish semantic absence',
                                         'Single supplied document; no cross-document claim']}

def numeric(p:dict)->dict:
    values=p.get('values')
    if not isinstance(values,list) or not 1<=len(values)<=MAX_NUMERIC:raise ModelContractError('values must have 1..5000 numbers')
    nums=list(map(_num,values));m=statistics.median(nums)
    mad=statistics.median(abs(v-m) for v in nums)
    return {'kind':'numeric_samples','n':len(nums),'mean':statistics.fmean(nums),'median':m,
            'raw_mad':mad,'sample_stddev':statistics.stdev(nums) if len(nums)>1 else None,
            'observation_only':True,
            'claims_not_licensed':['independence','causality','generalization to population','p-value']}

def graph(p:dict)->dict:
    nodes=p.get('nodes');edges=p.get('edges');directed=p.get('directed',False)
    if not isinstance(nodes,list) or not isinstance(edges,list) or not isinstance(directed,bool):raise ModelContractError('nodes/edges arrays and boolean directed required')
    if len(nodes)>MAX_NODES or len(edges)>10000 or any(not isinstance(n,str) or not n for n in nodes) or len(set(nodes))!=len(nodes):raise ModelContractError('invalid graph nodes')
    index=set(nodes);adj={n:set() for n in nodes};dagadj={n:set() for n in nodes}; indeg={n:0 for n in nodes}
    for e in edges:
        if not isinstance(e,list) or len(e)!=2 or any(not isinstance(x,str) or x not in index for x in e):raise ModelContractError('graph edges must reference declared nodes')
        a,b=e;adj[a].add(b);adj[b].add(a)
        if b not in dagadj[a]:dagadj[a].add(b);indeg[b]+=1
    seen=set();components=[]
    for v in sorted(nodes):
        if v in seen:continue
        q=[v]; seen.add(v);comp=[]
        while q:
            curr=q.pop();comp.append(curr)
            for nei in sorted(adj[curr]):
                if nei not in seen:seen.add(nei);q.append(nei)
        components.append(sorted(comp))
    order=[]
    if directed:
        ready=deque(sorted(n for n in nodes if indeg[n]==0))
        while ready:
            v=ready.popleft();order.append(v)
            for nbr in sorted(dagadj[v]):
                indeg[nbr]-=1
                if indeg[nbr]==0:ready.append(nbr)
            ready=deque(sorted(ready))
    return {'kind':'graph_edges','node_count':len(nodes),'weak_component_count':len(components),
            'weak_components':components,'directed':directed,
            'topological_order':order if directed and len(order)==len(nodes) else None,
            'cycle_detected':bool(directed and len(order)!=len(nodes)),
            'graph_isomorphism_not_proven':True}

def matrix(p:dict)->dict:
    rows=p.get('rows');target=p.get('target')
    if not isinstance(rows,list) or not rows or len(rows)>MAX_MATRIX or not isinstance(rows[0],list) or not 1<=len(rows[0])<=MAX_MATRIX:
        raise ModelContractError('matrix rows must be rectangular <=12x12')
    ncol=len(rows[0])
    if any(not isinstance(r,list) or len(r)!=ncol for r in rows):raise ModelContractError('nonrectangular matrix')
    def rational(v):
        x=_num(v)
        if abs(x)>1e9:raise ModelContractError('matrix value too large for exact rational analysis')
        return Fraction(str(v))
    A=[[rational(v) for v in r] for r in rows]
    if target is not None:
        if not isinstance(target,list) or len(target)!=len(A):raise ModelContractError('target length mismatch')
        aug=[row+[rational(y)] for row,y in zip(A,target)]
    else:aug=[row[:] for row in A]
    def rref(mat):
        m=[r[:] for r in mat];piv=[];r=0
        for j in range(len(m[0])):
            pivot=next((k for k in range(r,len(m)) if m[k][j]),None)
            if pivot is None:continue
            m[r],m[pivot]=m[pivot],m[r];scale=m[r][j];m[r]=[v/scale for v in m[r]]
            for k in range(len(m)):
                if k!=r:
                    scale=m[k][j];m[k]=[a-scale*b for a,b in zip(m[k],m[r])]
            piv.append(j);r+=1
            if r==len(m):break
        return m,piv
    a_reduced,a_piv=rref(A); rank=len(a_piv);nullity=ncol-rank
    res={'kind':'matrix','shape':[len(A),ncol],'rank':rank,'nullity':nullity,'exact_fraction_arithmetic':True}
    if target is not None:
        reduced,piv=rref(aug);rank_aug=len(piv);unique=rank==rank_aug==ncol
        consistent=rank==rank_aug
        res.update({'rank_augmented':rank_aug,'consistent':consistent,'unique_solution':unique,
                    'solution_class':'NONE' if not consistent else 'UNIQUE' if unique else 'AFFINE_FAMILY',
                    'one_solution':[{ 'numerator':str(reduced[a_piv.index(j)][-1].numerator),
                                      'denominator':str(reduced[a_piv.index(j)][-1].denominator)} for j in range(ncol)] if unique else None})
    res['numerical_stability_not_established']=True
    return res

def geometry(p:dict)->dict:
    polygon=p.get('polygon');point=p.get('point')
    if not isinstance(polygon,list) or not 3<=len(polygon)<=MAX_POINTS or not isinstance(point,list) or len(point)!=2:raise ModelContractError('geometry requires polygon and point')
    def pair(x):
        if not isinstance(x,list) or len(x)!=2:raise ModelContractError('coordinates must be pairs')
        return _num(x[0]),_num(x[1])
    pts=list(map(pair,polygon));px,py=pair(point)
    inside=False; boundary=False
    for i,(ax,ay) in enumerate(pts):
        bx,by=pts[(i+1)%len(pts)]
        cross=(px-ax)*(by-ay)-(py-ay)*(bx-ax)
        if abs(cross)<=1e-12 and min(ax,bx)<=px<=max(ax,bx) and min(ay,by)<=py<=max(ay,by):boundary=True
        if ((ay>py)!=(by>py)) and px<(bx-ax)*(py-ay)/(by-ay)+ax:inside=not inside
    return {'kind':'geometry','point_location':'BOUNDARY' if boundary else 'INSIDE' if inside else 'OUTSIDE',
            'algorithm':'ray_crossing_bounded_float','self_intersection_not_checked':True}

FUNCTIONS={'lexical_spans':lexical,'numeric_samples':numeric,'graph_edges':graph,'matrix':matrix,'geometry':geometry}


def execute(spec:dict)->dict:
    """Run a concrete Python operation and bind decision support to its result.

    Caller MUST actually invoke this function in a Python runtime; emitting a
    plan or loading a file is not a receipt. No payload means NOT EXECUTED.
    """
    if not isinstance(spec,dict) or not isinstance(spec.get('math_problem'),dict):raise ModelContractError('math_problem object required')
    plan=route(spec['math_problem'])
    p=spec.get('observation_payload')
    result=None
    if p is None:state='NO_OBSERVATION_PAYLOAD'
    else:
        if not isinstance(p,dict):raise ModelContractError('observation_payload must be object')
        kind=plan['observation_kind']
        if p.get('kind')!=kind:raise ModelContractError('observation_payload.kind must match observation_kind')
        if kind not in FUNCTIONS:state='UNSUPPORTED_COMPUTATION'
        else:
            result=FUNCTIONS[kind](p)
            state='EXECUTED'
    claim=plan['claim_type']
    if state!='EXECUTED':decision='EVIDENCE_NOT_COMPUTED'
    elif claim in {'semantic','argument','causal','deductive','inverse'}:decision='OBSERVATION_ONLY_HIGHER_CLAIM_UNVERIFIED'
    elif claim=='statistical':decision='DESCRIPTIVE_RESULT_INFERENCE_UNVERIFIED'
    else:decision='COMPUTED_OBSERVATION_REVIEW_REQUIRED'
    findings=[]
    next_tasks=[]
    if state!='EXECUTED':
        next_tasks.append('Provide a bounded typed observation_payload; do not finalize mathematical decision')
    elif plan['observation_kind']=='lexical_spans':
        findings.append(f"Observed {result['anchor_count']} anchor(s); evaluated {result['events_evaluated']}")
        if result['censored_endpoints']:
            next_tasks.append('Preserve censored endpoints as null; estimate lag only on complete endpoints')
        if result['events_truncated']:
            next_tasks.append('Validate truncated sampling: bounded 80-event evidence is not a population minimum')
        if claim in {'semantic','argument'}:
            next_tasks.append('Obtain proposition-level annotations and independent interpretation validation')
    elif plan['observation_kind']=='matrix':
        findings.append('Rank/nullity computed exactly for the supplied rational matrix')
        if result.get('solution_class')=='AFFINE_FAMILY':
            next_tasks.append('Acquire additional independent constraints; inverse is nonunique')
        if result.get('solution_class')=='NONE':
            next_tasks.append('Investigate inconsistent equations or incompatible observations')
        if result.get('solution_class')=='UNIQUE':
            next_tasks.append('Validate model assumptions and numerical stability independently')
    elif plan['observation_kind']=='graph_edges':
        findings.append(f"Computed {result['weak_component_count']} weakly connected component(s)")
        if result['cycle_detected']:
            next_tasks.append('Reject topological order for cyclic graph; resolve dependency cycle if these are task edges')
    elif plan['observation_kind']=='numeric_samples':
        findings.append(f"Computed descriptive statistics on {result['n']} supplied values")
        next_tasks.append('Require sampling design, dependence model and uncertainty method before generalization')
    elif plan['observation_kind']=='geometry':
        findings.append('Point location computed with bounded float ray-crossing test')
        next_tasks.append('Validate polygon simplicity and coordinate robustness before critical engineering use')
    digest=canonical_digest(p) if p is not None else None
    return {'schema':VERSION,'python_execution':{'state':state,'python_version':sys.version.split()[0],
            'operation':plan['observation_kind'] if state=='EXECUTED' else None,
            'input_sha256':digest,'result_sha256':canonical_digest(result) if result is not None else None,
            'result':result,'execution_is_not_semantic_proof':True},
            'decision_support':{'state':decision,'operator_selection_state':plan['epistemic_status'],
                 'computed_evidence_available':state=='EXECUTED','claim_type':claim,
                 'forbidden_promotions':plan['forbidden_promotions'],
                 'computed_findings':findings, 'next_tasks':next_tasks,
                 'reopen_on':['counterexample','new measurement','invalid type/assumption','failed test']},
            'task_graph':plan['tasks'],'unresolved_features':plan['unresolved_features'],
            'operator_candidates':plan['operator_candidates'],
            'actual_execution_scope':list(FUNCTIONS),
            'limitations':['This receipt is valid only when generated by an actual Python tool invocation.',
                           'Unsupported registry operators are not executed or proved.',
                           'Runtime output cannot by itself verify target software behavior.']}
