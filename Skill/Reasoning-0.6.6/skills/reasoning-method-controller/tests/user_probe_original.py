"""Independent, bounded Python probe based on VCT dep_sort and RMC/AntiSlop contracts.
NOT an invocation of the packaged VCT plugin runtime. This tests deliberately constructed fixtures,
NOT observed ChatGPT reasoning behavior or statistical false-positive rates.
"""
from collections import Counter

# Source-faithful transcription of VCT v0.1 dep_sort, inspected through installed skill.
def dep_sort(edges):
    nodes={x for e in edges for x in e}; adj={x:set() for x in nodes};degree={x:0 for x in nodes}
    for prereq,dependent in edges:
        if dependent not in adj[prereq]:adj[prereq].add(dependent);degree[dependent]+=1
    ready=sorted(n for n in nodes if degree[n]==0);order=[]
    while ready:
        n=ready.pop(0);order.append(n)
        for m in sorted(adj[n]):
            degree[m]-=1
            if degree[m]==0:
                ready.append(m);ready.sort()
    remaining=sorted(n for n in nodes if degree[n]>0)
    return {'ordering':order if not remaining else None,
            'cyclic_or_blocked_nodes':remaining,
            'status':'BLOCKED' if remaining else 'ORDERED'}

prereq = [('S0','S1'),('S1','S2'),('S2','S3'),('S3','S4'),('S4','S5'),('S5','S7'),('S7','S8'),('S8','S9')]
valid = dep_sort(prereq)
invalid_mixed = dep_sort(prereq+[('S6','S5'),('S5','S6')])
valid_separated = dep_sort(prereq)  # repair/transition edges not considered prerequisite edges
real_cycle = dep_sort([('requires_operator','requires_test'),('requires_test','requires_operator')])
assert valid['status']=='ORDERED'
assert invalid_mixed['status']=='BLOCKED'
assert valid_separated['status']=='ORDERED'
assert real_cycle['status']=='BLOCKED'

# Typed obligation gate; hand-labelled synthetic cases following RMC S6/S8 and AntiSlop scope.
def evaluate(c):
    if not c['applicable']:
        return 'NOT_APPLICABLE'
    if c.get('contradicted',False):
        return 'INVALID_OR_FALSE_CLAIM'
    if c.get('must_observe',False) and not c.get('witness',False):
        return 'UNVERIFIED_NARROW_CLAIM'
    if c.get('evidence_missing',False):
        return 'EVIDENCE_DEBT_NARROW_CLAIM'
    return 'PASS_SCOPED'

cases=[
 {'name':'simple_logic_no_external_research','applicable':False,'evidence_missing':True,'gold':'NOT_APPLICABLE'},
 {'name':'runtime_completion_without_receipt','applicable':True,'must_observe':True,'witness':False,'gold':'UNVERIFIED_NARROW_CLAIM'},
 {'name':'external_source_essential_but_missing','applicable':True,'evidence_missing':True,'gold':'EVIDENCE_DEBT_NARROW_CLAIM'},
 {'name':'directly_contradicted_operator_premise','applicable':True,'contradicted':True,'gold':'INVALID_OR_FALSE_CLAIM'},
 {'name':'known_safe_scoped_computation','applicable':True,'must_observe':True,'witness':True,'gold':'PASS_SCOPED'},
 {'name':'conceptual_theory_without_numeric_measurement','applicable':False,'evidence_missing':True,'gold':'NOT_APPLICABLE'},
 {'name':'no_proof_required_for_conjecture','applicable':False,'evidence_missing':True,'gold':'NOT_APPLICABLE'},
]
for c in cases:
    c['typed']=evaluate(c)
    assert c['typed']==c['gold']
    c['naive']='BLOCKED' if c.get('evidence_missing',False) or (c.get('must_observe') and not c.get('witness')) or c.get('contradicted',False) else 'PASS'

# "false block" labels indicate invented synthetic examples, not measured error rates.
naive_false_blocks=[c['name'] for c in cases if c['naive']=='BLOCKED' and c['typed']=='NOT_APPLICABLE']
naive_problematic_blocks=[c['name'] for c in cases if c['naive']=='BLOCKED' and c['typed'] in {'NOT_APPLICABLE','UNVERIFIED_NARROW_CLAIM','EVIDENCE_DEBT_NARROW_CLAIM'}]
print('VCT dep_sort on typed prerequisites:',valid['status'])
print('VCT dep_sort on wrongly mixed transitions+prerequisites:',invalid_mixed['status'],invalid_mixed['cyclic_or_blocked_nodes'])
print('VCT dep_sort on actual circular prerequisites:',real_cycle['status'])
print('fixture classifications:')
for c in cases: print(' ',c['name'],':',c['typed'],'| naive:',c['naive'])
print('wrong-block examples (synthetic):',naive_false_blocks)
print('overblocking-or-incorrect-claim-scope examples (synthetic):',naive_problematic_blocks)
print('assertions passed:', 4+len(cases))
