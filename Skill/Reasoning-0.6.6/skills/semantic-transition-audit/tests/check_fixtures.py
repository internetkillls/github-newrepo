#!/usr/bin/env python3
"""Structural check of semantic-transition fixtures and documentation.

Not a test of GPT-6 behavior, meaning correctness, evidence quality or model responses.
"""
import json
import pathlib
import sys
from collections import Counter, defaultdict

BASE = pathlib.Path(__file__).resolve().parent
SKILL = BASE.parent / 'SKILL.md'
RULES = BASE.parent / 'references' / 'rule-contract.md'
EVIDENCE = BASE.parent / 'references' / 'evidence-matrix.md'


def run():
    fixtures = [json.loads(x) for x in (BASE / 'paired-cases.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
    errors = []
    by_family = defaultdict(dict)
    ids = set()
    allowed = {'positive','negative','adversarial','transfer'}
    for case in fixtures:
        for key in ['id','family','rule_id','kind','stimulus','expected_behavior','provenance','behavior_status']:
            if not case.get(key): errors.append(f"{case.get('id','?')}: missing {key}")
        if case['kind'] not in allowed: errors.append('bad kind: '+case['id'])
        if case['id'] in ids: errors.append('duplicate: '+case['id'])
        ids.add(case['id'])
        if case['kind'] in ('positive','negative'):
            if case['kind'] in by_family[case['family']]: errors.append('duplicate paired kind: '+case['family'])
            by_family[case['family']][case['kind']] = case
        if case.get('actual_model_response') is None and case.get('behavior_status')!='UNVERIFIED':
            errors.append('fabricated model pass: '+case['id'])
    required={f'T{i:02d}' for i in range(1,13)}
    if set(by_family)!=required: errors.append('incorrect T01-T12 families')
    for family,pair in by_family.items():
        if set(pair)!={'positive','negative'}:
            errors.append('incomplete family: '+family)
            continue
        if pair['positive']['stimulus']==pair['negative']['stimulus']:errors.append('identical pair: '+family)
        if pair['positive']['expected_behavior']==pair['negative']['expected_behavior']:errors.append('nondiscriminating pair: '+family)
    rules = RULES.read_text(encoding='utf-8')
    evidence=EVIDENCE.read_text(encoding='utf-8')
    skill=SKILL.read_text(encoding='utf-8')
    for i in range(1,8):
        if f'ST-{i:02d}' not in rules: errors.append(f'rule missing ST-{i:02d}')
    for req in ['RULE_ID','TRIGGER_CONDITION','ADMISSIBILITY_GATE','OBSERVABLE_EXIT_TEST','COUNTEREXAMPLE','SOURCE_PROVENANCE','REGRESSION_TEST_ID']:
        if req not in rules: errors.append('typed rule field missing: '+req)
    for ref in ['Degen','Chalmers','Gaver','Meta4XNLI','ROBIN']:
        if ref.lower() not in evidence.lower(): errors.append('reference crosswalk missing: '+ref)
    for control in ['verbatim','forward pass','reverse pass','NO_MATERIAL_ISSUE','EXACT_INFERENTIAL_DEFECT','MATERIAL_UNRESOLVED']:
        if control.lower() not in skill.lower(): errors.append('entry/exit missing: '+control)
    if len([x for x in fixtures if x['kind']=='adversarial'])<2: errors.append('adversarial coverage too small')
    if len([x for x in fixtures if x['kind']=='transfer'])<2: errors.append('transfer coverage too small')
    result={'structural_status':'PASS' if not errors else 'FAIL','case_count':len(fixtures),'paired_families':len(by_family),'kinds':dict(Counter(x['kind'] for x in fixtures)),'behavioral_model_test':'NOT_RUN','errors':errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=='__main__': sys.exit(run())
