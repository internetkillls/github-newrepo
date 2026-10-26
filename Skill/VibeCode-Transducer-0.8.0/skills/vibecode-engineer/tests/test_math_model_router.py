import importlib.util
import json
import pathlib
import subprocess
import sys
import unittest

BASE=pathlib.Path(__file__).resolve().parents[1]
RUNTIME=BASE/'runtime'
sys.path.insert(0,str(RUNTIME))
from math_model_router import route, load_registry, ModelContractError, topo
from vct_math_cli import combine

def problem(claim='lexical',obs='lexical_spans',**features):
    return {'goal':'Analyze a bounded corpus feature without claiming rhetoric','claim_type':claim,
            'observation_kind':obs,'features':features}

class MathModelRouterTests(unittest.TestCase):
    def test_full_100_registry_and_proposed100(self):
        rows=load_registry()
        self.assertEqual(len(rows),100)
        self.assertTrue(rows['MATH-100']['current_case_status'].startswith('PROPOSED'))
    def test_namespace_matches(self):
        result=route(problem())
        self.assertTrue(all(x['math_id'].startswith('MATH-') for x in result['operator_candidates']))
        self.assertNotIn('ATLAS-034',[x['math_id'] for x in result['operator_candidates']])
    def test_lexical_with_declared_evidence(self):
        r=route(problem(sentence_bounded_tokens=True,traceable_offsets=True,defined_denominator=True))
        finite=next(x for x in r['operator_candidates'] if x['math_id']=='MATH-043')
        self.assertEqual(finite['eligibility'],'ELIGIBLE_AS_METHOD')
        self.assertEqual(r['epistemic_status'],'METHODS_PROVISIONALLY_ELIGIBLE')
        self.assertIn('T06',r['dependency_order'])
        self.assertNotIn('T10',r['dependency_order'])
    def test_censoring_cannot_promote_to_semantic(self):
        r=route(problem('semantic',censored_endpoints=True,overlapping_windows=True,
                        sentence_bounded_tokens=True,traceable_offsets=True,defined_denominator=True))
        self.assertEqual(r['epistemic_status'],'SEMANTIC_CLAIM_NOT_ESTABLISHED')
        self.assertIn('T10',r['dependency_order'])
        self.assertIn('word_count_implies_semantic_absence',r['forbidden_promotions'])
    def test_annotated_semantics_still_not_proven(self):
        f={'annotated_propositions':True,'annotation_validation':True,'theorem_assumptions':True,
           'sentence_bounded_tokens':True,'traceable_offsets':True,'defined_denominator':True}
        r=route(problem('argument',**f))
        self.assertIn('T11',r['dependency_order'])
        self.assertNotEqual(r['epistemic_status'],'PROVED')
        self.assertTrue(all(x['not_a_proof'] for x in r['operator_candidates']))
    def test_statistical_no_naive_iid_without_design(self):
        r=route(problem('statistical','numeric_samples',overlapping_windows=True))
        self.assertIn('sampling_design',r['unresolved_features'])
        self.assertIn('T09',r['dependency_order'])
    def test_causal_guard_not_prediction(self):
        r=route(problem('causal','numeric_samples',sampling_design=True))
        self.assertEqual(r['epistemic_status'],'CAUSAL_CLAIM_NOT_ESTABLISHED')
        self.assertIn('T12',r['dependency_order'])
    def test_inverse_uniqueness_stability(self):
        r=route(problem('inverse','matrix',forward_model=True,inverse_domain=True))
        self.assertEqual(r['epistemic_status'],'INVERSE_UNIQUENESS_OR_STABILITY_UNVERIFIED')
        self.assertIn('uniqueness_witness',r['unresolved_features'])
    def test_dimensional_group_requires_matrix(self):
        r=route(problem('engineering','symbolic',physical_quantities=True))
        o=next(x for x in r['operator_candidates'] if x['math_id']=='MATH-100')
        self.assertEqual(o['eligibility'],'NEEDS_EVIDENCE')
        self.assertIn('dimension_matrix',o['missing_preconditions'])
    def test_no_physical_quantities_no_pi_suggestion(self):
        r=route(problem('lexical'))
        self.assertNotIn('MATH-100',[x['math_id'] for x in r['operator_candidates']])
    def test_owner_handoff_requires_both_approval_and_checkout(self):
        a=route(problem('engineering','code_state',owner_approval=True))
        b=route(problem('engineering','code_state',owner_approval=True,runtime_checkout=True))
        self.assertNotIn('T16',a['dependency_order'])
        self.assertIn('T16',b['dependency_order'])
        self.assertTrue(all(x['status']=='PLANNED_NOT_EXECUTED' for x in b['tasks']))
    def test_cycles_and_missing_dependencies_rejected(self):
        with self.assertRaises(ModelContractError):topo([{'id':'x','depends_on':['y']}])
        with self.assertRaises(ModelContractError):topo([{'id':'x','depends_on':['y']},{'id':'y','depends_on':['x']}])
    def test_flags_must_be_boolean_and_known(self):
        for flags in ({'annotated_propositions':'true'}, {'magic_feature':True}):
            with self.subTest(flags=flags),self.assertRaises(ModelContractError):route({'goal':'x','claim_type':'semantic','observation_kind':'lexical_spans','features':flags})
    def test_combined_cli_no_engineering_spec_does_not_fake_analysis(self):
        d=combine({'math_problem':problem()})
        self.assertNotIn('engineering_static_analysis',d)
        self.assertEqual(d['execution_claim'],'READ_ONLY_SELECTION_NOT_PROOF_NOT_PATCH')
    def test_revision_is_not_auto_executed(self):
        d=route(problem())
        self.assertNotIn('T17',d['dependency_order'])
        self.assertEqual(d['revision_on_falsifier']['task'],'T17')

if __name__=='__main__':unittest.main()
