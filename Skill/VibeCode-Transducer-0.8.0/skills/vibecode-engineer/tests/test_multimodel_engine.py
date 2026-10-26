import copy
import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from multimodel_engine import execute, MultiModelInputError


def spec(probes=None,bridges=None,decision=None):
    return {'goal':'Test cross-model evidence without claiming ontological identity',
            'target_claim':'Bounded relation between discrete and continuous representations',
            'source_id':'synthetic-fixture-v0.6',
            'representation':{'entity':'survival fraction','unit':'proportion',
               'measurement_scale':'ratio','observation_map':'aligned times and fractions','dimensionless':True},
            'models':[{'id':'DISC','domain':'discrete','operator':'Euler survival step','assumptions':['constant rate']},
                      {'id':'CONT','domain':'continuous','operator':'dx/dt=-r*x','assumptions':['constant rate']}],
            'bridges':bridges if bridges is not None else [{'from':'DISC','to':'CONT','kind':'sample-and-euler-discretize',
                       'preserved':'aligned-time fraction','lost_or_unverified':'finite-step approximation and empirical validity'}],
            'probes':probes if probes is not None else [{'id':'p0','type':'euler_decay',
                       'parameters':{'rate':0.7,'step':0.125,'duration':1},'model_ids':['DISC','CONT']}],
            'decision':decision if decision is not None else {'error_tolerance':0.02}}

class TestCrossModelEngine(unittest.TestCase):
    def test_euler_pass_tolerance(self):
        x=execute(spec());self.assertEqual(x['probe_receipts'][0]['state'],'EXECUTED');self.assertEqual(x['probe_receipts'][0]['outcome'],'CONDITIONAL_PASS')
    def test_euler_fails_tight_tolerance(self):
        x=execute(spec(decision={'error_tolerance':1e-6}));self.assertEqual(x['decision_gate'],'REVISE_CLAIM_OR_MODEL')
    def test_refinement_task(self):
        self.assertIn('M08',[i['id'] for i in execute(spec())['engineering_tasks']])
    def test_invalid_probability_not_assumed(self):
        x=execute(spec(probes=[{'id':'p','type':'euler_decay','parameters':{'rate':3,'step':1,'duration':1}}]));self.assertEqual(x['probe_receipts'][0]['state'],'INVALID_PROBE')
    def test_periodic_graph(self):
        x=execute(spec(probes=[{'id':'graph','type':'periodic_graph','parameters':{'nodes':64,'harmonic':1}}],decision={'error_tolerance':0.001}));self.assertEqual(x['probe_receipts'][0]['outcome'],'CONDITIONAL_PASS')
    def test_spectral_countercase(self):
        x=execute(spec(probes=[{'id':'graph','type':'periodic_graph','parameters':{'nodes':8,'harmonic':1}}],decision={'error_tolerance':0.001}));self.assertEqual(x['decision_gate'],'REVISE_CLAIM_OR_MODEL')
    def test_nonidentifiable_parameter(self):
        x=execute(spec(probes=[{'id':'inverse','type':'inverse_ambiguity','parameters':{'rate':0.7,'gain':3,'initial':2,'scale':2,'times':[0,1,2]}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'REFUTED_BY_WITNESS');self.assertIn('M07',[i['id'] for i in x['engineering_tasks']])
    def test_positive_inverse_control(self):
        x=execute(spec(probes=[{'id':'inverse','type':'inverse_ambiguity','parameters':{'rate':0.7,'gain':3,'initial':2,'scale':1,'times':[0,1,2]}}]));self.assertNotEqual(x['probe_receipts'][0]['outcome'],'REFUTED_BY_WITNESS')
    def test_graph_same_degrees_no_unique_graph(self):
        x=execute(spec(probes=[{'id':'degrees','type':'graph_degrees','parameters':{}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'REFUTED_BY_WITNESS')
    def test_unobservable_lti(self):
        x=execute(spec(probes=[{'id':'state','type':'observability_linear','parameters':{'A':[[-1,0],[0,-2]],'C':[1,0]}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'REFUTED_BY_WITNESS')
    def test_observable_lti_control(self):
        x=execute(spec(probes=[{'id':'state','type':'observability_linear','parameters':{'A':[[0,1],[-2,-3]],'C':[1,0]}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'EXECUTED')
    def test_regions_ambiguous(self):
        x=execute(spec(probes=[{'id':'regions','type':'region_candidates','parameters':{'observations':{'0':1,'1':2,'2':4,'3':8},'next_n':4}}]));self.assertEqual(x['decision_gate'],'DISCRIMINATING_EVIDENCE_REQUIRED');self.assertIn('M09',[t['id'] for t in x['engineering_tasks']])
    def test_regions_counterexample(self):
        x=execute(spec(probes=[{'id':'regions','type':'region_candidates','parameters':{'observations':{'0':1,'1':2,'2':4,'3':8,'4':15},'next_n':5}}]));self.assertFalse(x['probe_receipts'][0]['result']['fit_on_observed']['pow2']);self.assertEqual(x['probe_receipts'][0]['proof_status'],'UNPROVED_GENERAL_CLAIM')
    def test_regions_neither(self):
        x=execute(spec(probes=[{'id':'regions','type':'region_candidates','parameters':{'observations':{'0':1,'1':3},'next_n':3}}]));self.assertIn('M10',[t['id'] for t in x['engineering_tasks']])
    def test_dimension_mismatch(self):
        x=execute(spec(probes=[{'id':'dimension','type':'dimension_check','parameters':{'lhs':[1,0],'rhs':[1,-1]}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'REFUTED_BY_WITNESS')
    def test_dimension_match_not_proof(self):
        x=execute(spec(probes=[{'id':'dimension','type':'dimension_check','parameters':{'lhs':[1,0],'rhs':[1,0]}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'EXECUTED');self.assertEqual(x['probe_receipts'][0]['proof_status'],'UNPROVED_GENERAL_CLAIM')
    def test_interval_uncertain(self):
        x=execute(spec(probes=[{'id':'bounds','type':'interval_decision','parameters':{'lower':5,'upper':9,'threshold':7}}]));self.assertEqual(x['probe_receipts'][0]['outcome'],'UNDETERMINED')
    def test_interval_yes(self):
        x=execute(spec(probes=[{'id':'bounds','type':'interval_decision','parameters':{'lower':8,'upper':9,'threshold':7}}]));self.assertEqual(x['probe_receipts'][0]['result']['decision'],'ROBUST_YES')
    def test_datalog_no_base(self):
        x=execute(spec(probes=[{'id':'datalog','type':'datalog_reachability','parameters':{'edges':[['a','b'],['b','c']],'base_rule':False}}]));self.assertEqual(x['probe_receipts'][0]['result']['least_fixed_point'],[])
    def test_datalog_with_base(self):
        x=execute(spec(probes=[{'id':'datalog','type':'datalog_reachability','parameters':{'edges':[['a','b'],['b','c']],'base_rule':True}}]));self.assertIn(['a','c'],x['probe_receipts'][0]['result']['least_fixed_point'])
    def test_lens_getput_putget(self):
        x=execute(spec(probes=[{'id':'lens','type':'lens_laws','parameters':{'source':{'name':'a','hidden':9},'updated_view':{'name':'b'}}}]));self.assertTrue(x['probe_receipts'][0]['result']['GetPut']);self.assertTrue(x['probe_receipts'][0]['result']['PutGet'])
    def test_noise_no_is_iid(self):
        x=execute(spec(probes=[{'id':'noise','type':'noisy_derivative','parameters':{'step':.0001,'noise_bound':.001}}]));self.assertTrue(x['probe_receipts'][0]['result']['adversarial_noise_not_random'])
    def test_source_digest_stable(self):self.assertEqual(execute(spec())['source_sha256'],execute(spec())['source_sha256'])
    def test_no_code_mutation(self):self.assertFalse(execute(spec())['code_mutated'])
    def test_bridge_unknown(self):
        t=spec();t['bridges'][0]['kind']='is-exact-inverse'
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_bridge_missing_model(self):
        t=spec();t['bridges'][0]['to']='missing'
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_untyped_scale(self):
        t=spec();t['representation']['measurement_scale']='meaning'
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_missing_assumptions(self):
        t=spec();del t['models'][0]['assumptions']
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_empty_probes(self):
        t=spec();t['probes']=[]
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_probes_bounded(self):
        t=spec();t['probes']=t['probes']*51
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_unsupported_probe_type(self):
        t=spec();t['probes'][0]['type']='exec_python'
        with self.assertRaises(MultiModelInputError):execute(t)
    def test_no_universal_proof(self):
        x=execute(spec());self.assertTrue(any('proof' in p.lower() for p in x['proof_obligations']))
    def test_task_prerequisite_dag(self):
        ts=execute(spec())['engineering_tasks'];ids={t['id'] for t in ts};order={t['id']:i for i,t in enumerate(ts)}
        self.assertTrue(all(d in ids and order[d]<order[t['id']] for t in ts for d in t['prerequisites']))
    def test_duplicate_model_ids(self):
        t=spec();t['models'][1]['id']='DISC'
        with self.assertRaises(MultiModelInputError):execute(t)

if __name__=='__main__':unittest.main()
