import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from heuristic_inference import execute, HeuristicContractError
from vct_math_cli import combine


def base(claim='lexical',unit='event',scale='count',dim='dimensionless'):
    return {'goal':'Model a bounded phenomenon','claim_type':claim,
        'representation':{'unit':{'name':'phrase occurrence','kind':unit,
            'measurement_scale':scale,'dimension_kind':dim,
            'identity_rule':'same exact token span under pinned tokenizer',
            'boundary_rule':'within one sentence',
            'source_ref':'doc#sha256:known'},
            'required_relations':['token_order'],
            'preserved_relations':['token_order'],
            'operations':['frequency']}}

class HeuristicInferenceTests(unittest.TestCase):
    def test_valid_dimensionless_unit_is_only_declared_warrant(self):
        d=execute(base())
        self.assertEqual(d['representational_admissibility']['representational_warrant'],'DECLARED_WARRANT_NOT_INDEPENDENTLY_VERIFIED')
        self.assertEqual(d['decision_gate'],'REPRESENTATION_AUDIT_ONLY')
        self.assertTrue(d['representational_admissibility']['non_dimensional_does_not_mean_unidimensional'])
    def test_missing_source_and_identity_blocks_adequacy(self):
        p=base();p['representation']['unit']['identity_rule']='';p['representation']['unit']['source_ref']=''
        d=execute(p)
        self.assertEqual(d['decision_gate'],'NEEDS_REPRESENTATION_EVIDENCE')
        self.assertIn('UNIT_IDENTITY_RULE',d['representational_admissibility']['missing'])
        self.assertIn('OBSERVATION_PROVENANCE',d['representational_admissibility']['missing'])
    def test_nominal_mean_is_not_licensed(self):
        p=base(scale='nominal');p['representation']['operations']=['mean']
        d=execute(p)
        self.assertEqual(d['decision_gate'],'REPRESENTATION_CONTRADICTION')
    def test_ordinal_ratio_is_not_licensed(self):
        p=base(scale='ordinal');p['representation']['operations']=['ratio']
        self.assertEqual(execute(p)['decision_gate'],'REPRESENTATION_CONTRADICTION')
    def test_interval_ratio_is_not_licensed(self):
        p=base(scale='interval');p['representation']['operations']=['ratio']
        self.assertEqual(execute(p)['decision_gate'],'REPRESENTATION_CONTRADICTION')
    def test_dimensional_mismatch_blocks(self):
        p=base(dim='formal_assigned');p['representation']['dimension_checks']=[{'left':[1,0],'right':[1,-1]}]
        self.assertEqual(execute(p)['decision_gate'],'REPRESENTATION_CONTRADICTION')
    def test_consistent_formal_dimensions_are_not_reality_certificate(self):
        p=base(dim='formal_assigned');p['representation']['dimension_checks']=[{'left':[1,0],'right':[1,0]}]
        d=execute(p)
        self.assertEqual(d['decision_gate'],'REPRESENTATION_AUDIT_ONLY')
        self.assertIn('Formal dimension vectors',d['representational_admissibility']['warnings'][0])
    def test_latent_construct_requires_independent_validation(self):
        p=base(unit='latent_construct',dim='latent_construct',claim='semantic')
        self.assertIn('LATENT_CONSTRUCT_VALIDITY_EVIDENCE',execute(p)['representational_admissibility']['missing'])
    def test_lexical_unit_insufficient_for_semantic_claim(self):
        p=base(claim='semantic')
        d=execute(p)
        self.assertEqual(d['representational_admissibility']['task_relative_adequacy'],'TARGET_WARRANT_MISSING')
    def test_missing_relation_requires_warrant(self):
        p=base();p['representation']['required_relations'].append('argument_role')
        self.assertIn('UNPRESERVED_REQUIRED_RELATIONS',execute(p)['representational_admissibility']['missing'])
    def test_equal_exposure_rates_not_equal_semantics(self):
        p=base();p['normalization']={'method':'exposure_rate','observations':[{'count':2,'exposure':10},{'count':4,'exposure':20}]}
        d=execute(p)
        self.assertTrue(d['normalization']['equal_rates_do_not_identify_equal_semantics'])
        self.assertEqual(d['normalization']['rows'][0]['rate'],.2)
        self.assertIn('TEST_SEMANTIC_NONIDENTIFIABILITY',[q['action'] for q in d['engineering_tasks']])
    def test_zero_exposure_is_undefined_not_zero_rate(self):
        p=base();p['normalization']={'method':'exposure_rate','observations':[{'count':0,'exposure':0}]}
        d=execute(p)
        self.assertIsNone(d['normalization']['rows'][0]['rate'])
    def test_positive_count_on_zero_exposure_rejected(self):
        p=base();p['normalization']={'method':'exposure_rate','observations':[{'count':1,'exposure':0}]}
        with self.assertRaises(HeuristicContractError):execute(p)
    def test_missing_model_identifiability_with_1_2_4_8(self):
        p=base(claim='inductive');p['approximation']={'method':'candidate_discrimination',
            'candidates':['pow2','regions3'],'observations':[{'x':i,'y':2**i} for i in range(4)]}
        d=execute(p);a=d['heuristic_inference']
        self.assertEqual(a['state'],'UNDERDETERMINED')
        self.assertEqual(a['recommended_discriminating_x'],4)
        self.assertEqual({m['deductive_model_consequence_at_next_x'] for m in a['models']},{15,16})
        self.assertTrue(all(x['hypothesis_status']=='CANDIDATE_NOT_PROVEN' for x in a['models']))
    def test_fourth_plane_heldout_discriminates_only_finite_candidates(self):
        p=base(claim='abductive');p['approximation']={'method':'candidate_discrimination',
            'candidates':['pow2','regions3'],'observations':[{'x':i,'y':2**i} for i in range(4)],
            'holdout':[{'x':4,'y':15}]}
        a=execute(p)['heuristic_inference']
        self.assertEqual(a['state'],'DISCRIMINATED_ON_HELDOUT_ONLY')
        self.assertTrue(a['outside_candidate_set_unidentifiable'])
        self.assertTrue(next(x for x in a['models'] if x['id']=='regions3')['heldout_compatible'])
    def test_new_data_can_force_model_class_revision(self):
        p=base(claim='abductive');p['approximation']={'method':'candidate_discrimination',
            'candidates':['pow2','regions3'],'observations':[{'x':4,'y':17}]}
        self.assertEqual(execute(p)['heuristic_inference']['state'],'REVISE_MODEL_CLASS')
    def test_overlap_holdout_rejected(self):
        p=base();p['approximation']={'method':'candidate_discrimination','candidates':['pow2','regions3'],
            'observations':[{'x':3,'y':8}],'holdout':[{'x':3,'y':8}]}
        with self.assertRaises(HeuristicContractError):execute(p)
    def test_bounded_approximation_underdetermined_at_threshold(self):
        p=base();p['approximation']={'method':'bounded_decision','lower':0.15,'upper':0.25,'threshold':.2}
        self.assertEqual(execute(p)['heuristic_inference']['state'],'UNDETERMINED')
    def test_bounded_approximation_robust_answer(self):
        p=base();p['approximation']={'method':'bounded_decision','lower':0.31,'upper':0.35,'threshold':.2}
        self.assertEqual(execute(p)['heuristic_inference']['state'],'ROBUST_YES')
    def test_gaussian_lumping_reference_not_general_certificate(self):
        p=base();p['approximation']={'method':'gaussian_lumping'}
        d=execute(p)['heuristic_inference']
        self.assertAlmostEqual(d['relative_error_fwhm'],-0.0605,places=3)
        self.assertTrue(d['not_a_general_error_certificate'])
    def test_noninjectivity_counterexample_conditional(self):
        p=base(claim='semantic');p['deduction']={'rule':'noninjective_label_counterexample',
            'observations':[{'feature':.2,'label':'quotation'},{'feature':.2,'label':'assertion'}]}
        d=execute(p)
        self.assertEqual(d['deductive_check']['state'],'CONDITIONAL_COUNTEREXAMPLE_ESTABLISHED')
        self.assertIn('INVALIDATE_SUFFICIENT_FEATURE_CLAIM',[q['action'] for q in d['engineering_tasks']])
    def test_non_counterexample_not_proof(self):
        p=base();p['deduction']={'rule':'noninjective_label_counterexample',
            'observations':[{'feature':.2,'label':'quotation'},{'feature':.3,'label':'assertion'}]}
        self.assertEqual(execute(p)['deductive_check']['state'],'NO_DISCRIMINATING_COUNTEREXAMPLE')
    def test_combined_cli_receives_heuristic_gate_without_math_payload(self):
        p=base();p['approximation']={'method':'candidate_discrimination',
            'candidates':['pow2','regions3'],'observations':[{'x':i,'y':2**i} for i in range(4)]}
        d=combine({'math_problem':{'goal':'Consider sequence','claim_type':'lexical','observation_kind':'unknown'},
                   'heuristic_problem':p})
        self.assertEqual(d['decision_gate'],'MODEL_DISCRIMINATION_REQUIRED')
        self.assertEqual(d['math_python_execution']['python_execution']['state'],'NO_OBSERVATION_PAYLOAD')
        self.assertEqual(d['heuristic_reasoning_execution']['heuristic_inference']['state'],'UNDERDETERMINED')
    def test_task_dependencies_are_satisfied_and_planned(self):
        p=base(claim='semantic');p['deduction']={'rule':'noninjective_label_counterexample',
            'observations':[{'feature':.2,'label':'a'},{'feature':.2,'label':'b'}]}
        ts=execute(p)['engineering_tasks'];ids=set()
        for t in ts:
            self.assertTrue(set(t['depends_on'])<=ids)
            self.assertEqual(t['status'],'PLANNED_NOT_EXECUTED')
            ids.add(t['id'])
if __name__=='__main__':unittest.main()
