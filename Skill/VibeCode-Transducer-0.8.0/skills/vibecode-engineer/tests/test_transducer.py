import hashlib
import json
import pathlib
import sys
import unittest

RUNTIME=pathlib.Path(__file__).resolve().parents[1]/'runtime'
sys.path.insert(0,str(RUNTIME))
from vibe_transducer import ContractError,sha,transduce

BASE={'task_kind':'debug','goal':'Fix selection','expected_behavior':'new copy selected','observed_behavior':'old selected'}

class TransducerTests(unittest.TestCase):
    def test_empty_request_is_incomplete(self):
        d=transduce(BASE)
        self.assertEqual(d['decision_gate'],'INCOMPLETE')
        self.assertEqual(d['epistemic_state'],'REQUEST_ONLY')
        self.assertTrue(any('source snapshot' in x for x in d['missing_verification']))
        self.assertEqual(d['operator_plan'][0]['execution_status'],'AVAILABLE_NOT_RUN')
    def test_parse_python_functions_and_lines(self):
        d=transduce({**BASE,'files':{'x.py':'def a():\n    return 1\n'}})
        self.assertEqual(d['source_structure'][0]['functions'][0]['name'],'a')
        self.assertEqual(d['source_structure'][0]['status'],'PYTHON_AST_PARSED')
    def test_parse_failure_not_code_execution(self):
        d=transduce({**BASE,'files':{'x.py':'def broken(\n'}})
        self.assertEqual(d['source_structure'][0]['status'],'PARSE_FAILED')
    def test_self_donor_excluded_and_zero_overlap_excluded(self):
        d=transduce({**BASE,'target_file':'a.py','files':{'a.py':'def selector():\n pass','b.py':'def marker():\n pass','c.py':'def selector():\n pass'}})
        self.assertEqual([x['path'] for x in d['donor_candidates']],['c.py'])
        self.assertTrue(d['donor_candidates'][0]['candidate_only'])
    def test_comments_are_not_donor_code(self):
        d=transduce({**BASE,'target_file':'a.py','files':{'a.py':'def foo():\n pass','b.py':'# foo\ndef bar():\n pass'}})
        self.assertFalse(d['donor_candidates'])
    def test_zero_dependency_cycle_blocks(self):
        d=transduce({**BASE,'task_kind':'refactor','dependencies':[['a','b'],['b','a']]})
        self.assertEqual(d['decision_gate'],'BLOCKED')
    def test_dependency_dag(self):
        d=transduce({**BASE,'task_kind':'refactor','dependencies':[['a','b'],['b','c']]})
        self.assertEqual(d['dependency_order']['ordering'],['a','b','c'])
        self.assertEqual(d['decision_gate'],'INCOMPLETE')
    def test_retry_isolation(self):
        es=[{'case_id':'q','attempt_id':'1','event':'ACK','timestamp':'2026-10-23T01:00:00Z'},
            {'case_id':'q','attempt_id':'2','event':'COMMIT','timestamp':'2026-10-23T01:00:00Z'},
            {'case_id':'q','attempt_id':'2','event':'ACK','timestamp':'2026-10-23T01:00:01Z'}]
        d=transduce({**BASE,'task_kind':'trace','events':es,'trace_complete':True})
        self.assertEqual([g['state'] for g in d['trace']['groups']],['BLOCKED','ORDER_OBSERVED'])
    def test_tz_aware_chronology(self):
        es=[{'case_id':'q','event':'ACK','timestamp':'2026-10-23T10:00:00+07:00'},
            {'case_id':'q','event':'COMMIT','timestamp':'2026-10-23T04:00:00+00:00'}]
        d=transduce({**BASE,'task_kind':'trace','events':es,'trace_complete':True})
        self.assertEqual(d['trace']['groups'][0]['state'],'BLOCKED')
    def test_ambiguous_time_is_not_pass(self):
        es=[{'case_id':'q','event':'ACK','timestamp':'2026-10-23T10:00:00Z'},
            {'case_id':'q','event':'COMMIT','timestamp':'2026-10-23T10:00:00+00:00'}]
        d=transduce({**BASE,'task_kind':'trace','events':es,'trace_complete':True})
        self.assertEqual(d['trace']['groups'][0]['state'],'OBSERVABILITY_GAP')
    def test_absent_commit_not_proven_if_incomplete(self):
        d=transduce({**BASE,'task_kind':'trace','events':[{'case_id':'q','event':'ACK','timestamp':'2026-10-23T10:00:00Z'}]})
        self.assertEqual(d['decision_gate'],'INCOMPLETE')
    def test_naive_timestamp_rejected(self):
        with self.assertRaises(ContractError):transduce({**BASE,'task_kind':'trace','events':[{'case_id':'q','event':'ACK','timestamp':'2026-10-23T10:00:00'}]})
    def test_mad(self):
        d=transduce({**BASE,'task_kind':'performance','measurements':[10,11,12,13,200]})
        self.assertEqual(d['numeric_summary']['mad'],1)
    def test_nan_rejected(self):
        with self.assertRaises(ContractError):transduce({**BASE,'measurements':[float('nan')]})
    def test_preview_exact_sha(self):
        text='def fun():\n return False\n'
        d=transduce({**BASE,'files':{'f.py':text},'edits':[{'path':'f.py','old':'False','new':'True','sha256':sha(text)}]})
        self.assertFalse(d['patch_previews'][0]['applied'])
        self.assertIn('+ return True',d['patch_previews'][0]['diff'])
    def test_stale_patch_rejected(self):
        with self.assertRaises(ContractError):transduce({**BASE,'files':{'f.py':'x'},'edits':[{'path':'f.py','old':'x','new':'y','sha256':'0'*64}]})
    def test_ambiguous_patch_rejected(self):
        with self.assertRaises(ContractError):transduce({**BASE,'files':{'f.py':'xx'},'edits':[{'path':'f.py','old':'x','new':'y','sha256':sha('xx')}]})
    def test_secret_and_traversal_rejected(self):
        for path in ('.env','../secret.py','a/../file.py','C:\\repo\\file.py','.git/config.py','folder/secret.py'):
            with self.subTest(path=path),self.assertRaises(ContractError):transduce({**BASE,'files':{path:'x'}})
    def test_limit(self):
        with self.assertRaises(ContractError):transduce({**BASE,'files':{'x.py':'a'*100001}})
    def test_missing_contract_issue_not_blocker(self):
        d=transduce({'task_kind':'design','goal':'Create a page'})
        self.assertEqual(len(d['issues']),2)
        self.assertEqual(d['decision_gate'],'INCOMPLETE')
        self.assertIn('[ISSUE:',d['prompt_preview'])
    def test_false_trace_completeness_rejected(self):
        with self.assertRaises(ContractError):transduce({**BASE,'trace_complete':'yes'})
    def test_task_invalid(self):
        with self.assertRaises(ContractError):transduce({**BASE,'task_kind':'magic-do-everything'})

if __name__=='__main__':unittest.main()
