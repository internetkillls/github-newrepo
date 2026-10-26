import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from cloud_math_executor import execute
from math_model_router import ModelContractError
from vct_math_cli import combine

def task(kind='lexical_spans',claim='lexical',p=None):
    return {'math_problem':{'goal':'Decide using measured evidence','claim_type':claim,'observation_kind':kind,'features':{}},'observation_payload':p}

class ExecutedMathTests(unittest.TestCase):
    def test_no_observation_no_execution(self):
        r=execute(task(p=None))
        self.assertEqual(r['python_execution']['state'],'NO_OBSERVATION_PAYLOAD')
        self.assertEqual(r['decision_support']['state'],'EVIDENCE_NOT_COMPUTED')
    def test_lexical_alpha_and_beta_and_censoring(self):
        p={'kind':'lexical_spans','paragraphs':['A mentions z. z follows.','B appears. A with z.','There is no boundary.'], 'anchor':'A','boundary':'B','tracked':['z']}
        r=execute(task(p=p));o=r['python_execution']['result']
        self.assertEqual(o['anchor_count'],2)
        self.assertEqual(o['events_evaluated'],2)
        self.assertEqual(o['beta']['z']['occurrences'],3)
        self.assertEqual(o['censored_endpoints'],1)
        self.assertTrue(o['events'][0]['boundary_lag_tokens']>=0)
        self.assertNotEqual(o['events'][1]['boundary_lag_tokens'],0)
        self.assertEqual(r['decision_support']['state'],'COMPUTED_OBSERVATION_REVIEW_REQUIRED')
    def test_sentence_split_no_cross_phrase(self):
        p={'kind':'lexical_spans','paragraphs':['the alpha. beta appears','the alpha beta appears'], 'anchor':'alpha beta','tracked':[]}
        self.assertEqual(execute(task(p=p))['python_execution']['result']['anchor_count'],1)
    def test_censored_not_zero(self):
        p={'kind':'lexical_spans','paragraphs':['Alpha appears.','No endpoint'], 'anchor':'Alpha','boundary':'Omega'}
        o=execute(task(p=p))['python_execution']['result']
        self.assertIsNone(o['events'][0]['boundary_lag_tokens'])
        self.assertTrue(o['events'][0]['boundary_censored'])
    def test_overlap_not_independent_and_semantics_unverified(self):
        p={'kind':'lexical_spans','paragraphs':['X has z.','Y has z.','X has z.'], 'anchor':'X','tracked':['z']}
        r=execute(task(claim='semantic',p=p));o=r['python_execution']['result']
        self.assertIn('overlap',o['observational_constraints'][0])
        self.assertEqual(r['decision_support']['state'],'OBSERVATION_ONLY_HIGHER_CLAIM_UNVERIFIED')
    def test_numeric_mad_not_inference(self):
        p={'kind':'numeric_samples','values':[10,11,12,13,200]}
        r=execute(task('numeric_samples','statistical',p));self.assertEqual(r['python_execution']['result']['raw_mad'],1)
        self.assertEqual(r['decision_support']['state'],'DESCRIPTIVE_RESULT_INFERENCE_UNVERIFIED')
    def test_numeric_nan_rejected(self):
        with self.assertRaises(ModelContractError):execute(task('numeric_samples','statistical',{'kind':'numeric_samples','values':[float('nan')]}))
    def test_graph_dag_and_cycle(self):
        p={'kind':'graph_edges','nodes':['a','b','c'],'edges':[['a','b'],['b','c']],'directed':True}
        r=execute(task('graph_edges','engineering',p));self.assertEqual(r['python_execution']['result']['topological_order'],['a','b','c'])
        p['edges'].append(['c','a'])
        r2=execute(task('graph_edges','engineering',p));self.assertTrue(r2['python_execution']['result']['cycle_detected'])
        self.assertIsNone(r2['python_execution']['result']['topological_order'])
    def test_graph_degree_nonidentifiable(self):
        c6={'kind':'graph_edges','nodes':[str(x) for x in range(6)],'edges':[[str(i),str((i+1)%6)] for i in range(6)]}
        two_tri={'kind':'graph_edges','nodes':[str(x) for x in range(6)],'edges':[['0','1'],['1','2'],['2','0'],['3','4'],['4','5'],['5','3']]}
        r1=execute(task('graph_edges','inverse',c6))['python_execution']['result']
        r2=execute(task('graph_edges','inverse',two_tri))['python_execution']['result']
        self.assertNotEqual(r1['weak_component_count'],r2['weak_component_count'])
    def test_matrix_unique_vs_family_and_inconsistent(self):
        def run(rows,b):return execute(task('matrix','inverse',{'kind':'matrix','rows':rows,'target':b}))['python_execution']['result']
        self.assertEqual(run([[1,0],[0,1]],[4,3])['solution_class'],'UNIQUE')
        self.assertEqual(run([[1,1],[2,2]],[3,6])['solution_class'],'AFFINE_FAMILY')
        self.assertEqual(run([[1,1],[2,2]],[3,7])['solution_class'],'NONE')
    def test_polygon_boundary(self):
        p={'kind':'geometry','polygon':[[0,0],[2,0],[2,2],[0,2]],'point':[0,1]}
        self.assertEqual(execute(task('geometry','engineering',p))['python_execution']['result']['point_location'],'BOUNDARY')
    def test_unsupported_symbolic_computation_explicit(self):
        r=execute(task('symbolic','deductive',{'kind':'symbolic','expression':'x+1'}))
        self.assertEqual(r['python_execution']['state'],'UNSUPPORTED_COMPUTATION')
        self.assertFalse(r['decision_support']['computed_evidence_available'])
    def test_input_kind_mismatch_rejected(self):
        with self.assertRaises(ModelContractError):execute(task('matrix','inverse',{'kind':'lexical_spans','paragraphs':['a']}))
    def test_combined_cli_includes_execution(self):
        d=combine(task('numeric_samples','statistical',{'kind':'numeric_samples','values':[1,2,3]}))
        self.assertEqual(d['decision_gate'],'PYTHON_EVIDENCE_AVAILABLE')
        self.assertEqual(d['math_python_execution']['python_execution']['state'],'EXECUTED')
        self.assertIn('math_model_selection',d)
    def test_no_target_code_mutation(self):
        p={'kind':'numeric_samples','values':[3,1,2]}; before=list(p['values'])
        execute(task('numeric_samples','statistical',p));self.assertEqual(p['values'],before)
if __name__=='__main__': unittest.main()
