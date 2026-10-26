"""Bounded regression seeded by user-provided VCT transducer transcription fixture.
Not a conversational behavior test, not a measured false-positive rate.
Run: python -m unittest discover -s skills/reasoning-method-controller/tests -p 'test_*.py' -v
"""
import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
import adaptive_gate as gate

class GateTests(unittest.TestCase):
    def c(self,name,**overrides):
        s={'claim_id':name,'applicable':True,'decision_change_if_fail':True,
           'contradicted':False,'method_supported':True,
           'witness_required':False,'witness_observed':False,'noncritical_debt':False}
        s.update(overrides)
        return gate.judge(s)

    def test_original_probes_classification(self):
        # 7 hand-labelled synthetic cases preserved from uploaded original.
        cases=[
            ('simple_logic_no_external_research',{'applicable':False},'NOT_APPLICABLE','SKIP_CHECK'),
            ('runtime_completion_without_receipt',{'witness_required':True},'UNVERIFIED','WITHHOLD_CLAIM'),
            ('external_source_essential_but_missing',{'witness_required':True},'UNVERIFIED','WITHHOLD_CLAIM'),
            ('directly_contradicted_operator_premise',{'contradicted':True},'CONTRADICTED','REVISE_PREMISE'),
            ('known_safe_scoped_computation',{'witness_required':True,'witness_observed':True},'PASS','CONTINUE'),
            ('conceptual_theory_without_numeric_measurement',{'applicable':False},'NOT_APPLICABLE','SKIP_CHECK'),
            ('no_proof_required_for_conjecture',{'applicable':False},'NOT_APPLICABLE','SKIP_CHECK'),
        ]
        for name,kwargs,status,action in cases:
            with self.subTest(name=name):
                r=self.c(name,**kwargs)
                self.assertEqual((r['finding'],r['disposition']),(status,action))
                self.assertFalse(r['global_work_blocked'])

    def test_missing_noncritical_evidence_is_provisional(self):
        r=self.c('interpretive_debt',noncritical_debt=True)
        self.assertEqual((r['finding'],r['disposition']),('PROVISIONAL','NARROW_CLAIM'))

    def test_nonmaterial_check_skipped_before_absence(self):
        r=self.c('no_statistical_test_needed',decision_change_if_fail=False,
                 witness_required=True,contradicted=True,method_supported=False)
        self.assertEqual(r['finding'],'NOT_APPLICABLE')

    def test_contradiction_takes_precedence_over_missing_witness(self):
        r=self.c('failed_premise',contradicted=True,witness_required=True)
        self.assertEqual(r['finding'],'CONTRADICTED')

    def test_unsupported_is_not_falsification(self):
        r=self.c('semantic_claim_to_math',method_supported=False)
        self.assertEqual((r['finding'],r['disposition']),('UNSUPPORTED','CHANGE_METHOD'))

    def test_boolean_string_rejected(self):
        with self.assertRaises(gate.ContractError):
            self.c('bad_bool',witness_required='false')

    def test_prerequisite_vs_feedback(self):
        base=[{'kind':'PREREQUISITE','source':'S0','target':'S1'},
              {'kind':'PREREQUISITE','source':'S1','target':'S2'},
              {'kind':'TRANSITION','source':'S5','target':'S6'},
              {'kind':'REPAIR','source':'S6','target':'S5'}]
        g=gate.evaluate({'edges':base})['dependency_graph']
        self.assertEqual(g['status'],'ORDERED')
        self.assertEqual(g['excluded_repair_count'],1)
        self.assertEqual(g['excluded_transition_count'],1)

    def test_true_circular_prerequisite(self):
        g=gate.evaluate({'edges':[
            {'kind':'PREREQUISITE','source':'requires_operator','target':'requires_test'},
            {'kind':'PREREQUISITE','source':'requires_test','target':'requires_operator'}]})['dependency_graph']
        self.assertEqual(g['status'],'CIRCULAR_PREREQUISITE')
        self.assertIsNone(g['ordering'])

    def test_same_edges_wrongly_cast_as_prereqs_are_not_exonerated(self):
        g=gate.evaluate({'edges':[
            {'kind':'PREREQUISITE','source':'S5','target':'S6'},
            {'kind':'PREREQUISITE','source':'S6','target':'S5'}]})['dependency_graph']
        self.assertEqual(g['status'],'CIRCULAR_PREREQUISITE')

    def test_status_does_not_assert_earned_external_verification(self):
        out=gate.evaluate({'obligations':[{
            'claim_id':'user_declares_pass','applicable':True,
            'decision_change_if_fail':True,'witness_required':True,
            'witness_observed':True}]})
        self.assertTrue(out['findings'][0]['declared_input_only'])
        self.assertFalse(out['behavioral_compliance_verified'])

    def test_invalid_graph_type_rejected(self):
        with self.assertRaises(gate.ContractError):
            gate.evaluate({'edges':[{'kind':'RANDOM','source':'A','target':'B'}]})

if __name__=='__main__':unittest.main()
