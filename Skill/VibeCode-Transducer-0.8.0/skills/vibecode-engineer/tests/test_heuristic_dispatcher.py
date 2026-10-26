import unittest,sys,copy,json,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
from heuristic_dispatcher import dispatch,DispatchInputError
ROOT=Path(__file__).resolve().parents[1]

def ex(name):return json.loads((ROOT/'examples'/name).read_text())
def base(name='multimodel_discrete_continuum.json'):
    return {'allow_writes':False,'multimodel_problem':ex(name),'max_refinements':0}

class TestDispatcher(unittest.TestCase):
    def test_normal_conditional(self):
        r=dispatch(base());self.assertTrue(r['pipeline_executed_in_python']);self.assertEqual(r['decision_gate'],'CONDITIONAL_NUMERICAL_WITNESS')
        self.assertFalse(r['code_mutated'])
    def test_inverse_counterexample(self):
        r=dispatch(base('multimodel_hidden_state.json'))
        self.assertEqual(r['decision_gate'],'MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE')
        self.assertEqual(r['findings'][0]['initial_outcome'],'REFUTED_BY_WITNESS')
        self.assertFalse(r['findings'][0]['refinement'])
    def test_refinement_from_fail(self):
        d=base();d['multimodel_problem']['probes'][0]['parameters']['step']=.5
        d['multimodel_problem']['decision']['error_tolerance']=.02
        d['max_refinements']=6
        r=dispatch(d)
        self.assertEqual(r['findings'][0]['initial_outcome'],'REFUTED_BY_WITNESS')
        self.assertEqual(r['findings'][0]['refinement_status'],'REFINEMENT_MEETS_DECLARED_TOLERANCE')
        self.assertEqual(r['decision_gate'],'ORIGINAL_CLAIM_REFUTED_REFINED_VARIANT_PASSES')
        self.assertNotEqual(r['findings'][0]['refinement'][0]['parameters']['step'], .5)
    def test_refinement_budget(self):
        d=base();d['multimodel_problem']['probes'][0]['parameters']['step']=.5;d['multimodel_problem']['decision']['error_tolerance']=.000001
        d['max_refinements']=1
        r=dispatch(d);self.assertEqual(r['decision_gate'],'MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE')
        self.assertEqual(r['findings'][0]['refinement_status'],'BUDGET_EXHAUSTED_OR_LIMITED')
    def test_refinement_no_original_mutation(self):
        d=base();d['multimodel_problem']['probes'][0]['parameters']['step']=.5;d['max_refinements']=3
        before=copy.deepcopy(d);dispatch(d);self.assertEqual(d,before)
    def test_unknown_fields_rejected(self):
        d=base();d['shell']='rm -rf /';self.assertRaises(DispatchInputError,dispatch,d)
    def test_false_allow_writes_required(self):
        d=base();d.pop('allow_writes');self.assertRaises(DispatchInputError,dispatch,d)
    def test_int_budget_not_boolean(self):
        d=base();d['max_refinements']=True;self.assertRaises(DispatchInputError,dispatch,d)
    def test_finite_pass_not_proof(self):
        r=dispatch(base());self.assertIn('not',r['claim_ceiling'].lower());self.assertEqual(r['findings'][0]['initial_proof_status'],'UNPROVED_GENERAL_CLAIM')
    def test_arex_optional_not_applicable(self):
        self.assertEqual(dispatch(base())['arex_discovery']['status'],'NOT_APPLICABLE')
    def test_arex_missing_without_plugin_not_success(self):
        d=base();d['arex_query']='optimization solver'
        from unittest.mock import patch
        with patch('heuristic_dispatcher.Path.is_file',return_value=False):
            self.assertEqual(dispatch(d)['arex_discovery']['status'],'DONOR_METADATA_UNAVAILABLE')
    def test_feedback_not_prereq_cycle(self):
        r=dispatch(base('multimodel_hidden_state.json'));g=r['task_graph']
        self.assertIn('D04',g['prerequisite_order']);self.assertEqual(g['conditional_feedback'][0]['edge_type'],'REPAIR_NOT_PREREQUISITE')
    def test_method_not_proof(self):
        r=dispatch(base());self.assertTrue(all(x['status']=='METHOD_SELECTED_NOT_PROOF' for x in r['heuristics']))
    def test_frustum_revision(self):
        d=base();d['mahajan_case']='frustum_model_revision';r=dispatch(d)['mahajan_case_execution']
        self.assertEqual(r['coefficients_exact']['beta'],'1/3')
        self.assertTrue(all(x['new_matches_integral'] for x in r['witnesses']))
        self.assertNotEqual(r['witnesses'][0]['old'],r['witnesses'][0]['integrated_exact'])
    def test_lumping_error(self):
        d=base();d['mahajan_case']='gaussian_lumping';r=dispatch(d)['mahajan_case_execution']
        self.assertGreater(r['approximations'][0]['relative_error'],r['approximations'][1]['relative_error'])
    def test_bad_mahajan_case(self):
        d=base();d['mahajan_case']='magical';self.assertRaises(DispatchInputError,dispatch,d)
    def test_real_end_to_end_receipt_hash(self):
        d=base();r=dispatch(d);self.assertEqual(len(r['input_sha256']),64);self.assertGreater(len(r['task_graph']['tasks']),8)
    def test_dependency_no_cycles(self):
        g=dispatch(base())['task_graph'];order=g['prerequisite_order'];pos={x:i for i,x in enumerate(order)}
        for t in g['tasks']:
            for p in t['prerequisites']:self.assertLess(pos[p],pos[t['id']])

if __name__=='__main__':unittest.main()

class MoreDecisionTests(unittest.TestCase):
    def test_n3_region_observations_cannot_select_model(self):
        d=base(); d['multimodel_problem']['probes']=[{'id':'regions','type':'region_candidates','model_ids':['disc'],
            'parameters':{'observations':{'0':1,'1':2,'2':4,'3':8},'next_n':4}}]
        r=dispatch(d)
        self.assertEqual(r['decision_gate'],'NEEDS_DISCRIMINATING_OBSERVATION')
        self.assertFalse(r['findings'][0]['refinement'])
        self.assertIn('D05',r['task_graph']['prerequisite_order'])
    def test_graph_degree_non_identification(self):
        d=base();d['multimodel_problem']['probes']=[{'id':'same-degrees','type':'graph_degrees','parameters':{}}]
        r=dispatch(d)
        self.assertEqual(r['decision_gate'],'MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE')
    def test_dimension_incompatibility(self):
        d=base();d['multimodel_problem']['probes']=[{'id':'dims','type':'dimension_check','parameters':{'lhs':[1,0,0],'rhs':[1,0,-1]}}]
        r=dispatch(d);self.assertEqual(r['findings'][0]['initial_outcome'],'REFUTED_BY_WITNESS')
    def test_synthetic_input_is_not_empirical_proof(self):
        r=dispatch(base()); self.assertIn('synthetic/declared',r['claim_ceiling'])
    def test_auto_arex_does_not_run_without_query(self):
        d=base();d['multimodel_problem']['probes']=[{'id':'sym','type':'graph_degrees','parameters':{}}]
        self.assertEqual(dispatch(d)['arex_discovery']['status'],'NOT_APPLICABLE')
