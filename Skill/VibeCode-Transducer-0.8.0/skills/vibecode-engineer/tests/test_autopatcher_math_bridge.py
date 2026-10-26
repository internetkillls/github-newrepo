import json,pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
from autopatcher_math_bridge import evaluate_model_before_patch
class TestBridge(unittest.TestCase):
 def load(self,file):return json.loads((ROOT/'examples'/file).read_text())
 def test_euler_refinement_keeps_original_refutation(self):
  data=self.load('dispatcher_euler_refinement.json')
  r=evaluate_model_before_patch(data)
  self.assertTrue(r['calculation_executed']);self.assertEqual(r['finding'],'CONTRADICTED')
  self.assertFalse(r['can_issue_write_authorization'])
 def test_inverse_cannot_claim_unique_recovery(self):
  data=self.load('dispatcher_inverse_blocked.json')
  r=evaluate_model_before_patch(data)
  self.assertEqual(r['finding'],'CONTRADICTED');self.assertFalse(r['can_issue_write_authorization'])
 def test_invalid_probe_no_auto_write(self):
  self.assertEqual(evaluate_model_before_patch({'allow_writes':True})['disposition'],'CHANGE_METHOD')
if __name__=='__main__':unittest.main()
