import pathlib,sys,tempfile,time,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from autopatcher_control import ControlPlane,gateway_sign,capability_report
from autopatcher_core import JobStore,GateError,digest
KEY=b'test-only-hmac-gateway-authorization-secret-material-32'
class Tests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup)
  self.store=JobStore(pathlib.Path(self.t.name)/'jobs.db');self.addCleanup(self.store.close)
  self.registry={'fixture/repo':{'root':'not-accessed-in-control-plane'}}
  self.service=ControlPlane(self.store,self.registry,KEY)
  self.spec={'repo_id':'fixture/repo','base_sha':'0'*40,
             'patch':{'path':'config.json','old':'one','new':'two','expected_sha256':'a'*64},
             'test':{'kind':'json_value','id':'toy.value','path':'config.json','pointer':'/value','expected':2}}
 def auth(self,action,body_hash,repo_id='fixture/repo',**extra):
  f={'audience':'vct-autopatcher-control-v1','subject':'dev-operator','repo_id':repo_id,
     'action':action,'body_hash':body_hash,'expires_at':time.time()+60};f.update(extra)
  return gateway_sign(f,KEY)
 def submit(self):
  key='operation-123'
  auth=self.auth('submit',digest({'spec':self.spec,'idempotency_key':key}))
  return self.service.submit_patch_job(self.spec,key,auth)['job_id']
 def test_signed_submit_pending_only(self):
  jid=self.submit();self.assertEqual(self.store.status(jid)['state'],'REQUESTED')
 def test_unsigned_rejected(self):
  with self.assertRaisesRegex(GateError,'UNAUTHENTICATED'):
   self.service.submit_patch_job(self.spec,'operation-123',{})
 def test_payload_tamper_rejected(self):
  a=self.auth('submit',digest({'spec':self.spec,'idempotency_key':'operation-123'}))
  self.spec['test']['expected']=3
  with self.assertRaisesRegex(GateError,'UNAUTHORIZED'):
   self.service.submit_patch_job(self.spec,'operation-123',a)
 def test_wrong_repo_rejected(self):
  with self.assertRaisesRegex(GateError,'UNAUTHORIZED'):
   self.service.submit_patch_job(self.spec,'operation-123',self.auth('submit',digest({'spec':self.spec,'idempotency_key':'operation-123'}),repo_id='other/repo'))
 def test_expired_assertion_rejected(self):
  with self.assertRaisesRegex(GateError,'UNAUTHENTICATED'):
   self.service.submit_patch_job(self.spec,'operation-123',self.auth('submit',digest({'spec':self.spec,'idempotency_key':'operation-123'}),expires_at=time.time()-1))
 def test_status_rejects_read_without_grant(self):
  jid=self.submit()
  with self.assertRaisesRegex(GateError,'UNAUTHENTICATED'):self.service.get_job_status(jid,{})
 def test_status_with_scoped_grant(self):
  jid=self.submit();a=self.auth('status',digest({'job_id':jid}))
  self.assertEqual(self.service.get_job_status(jid,a)['state'],'REQUESTED')
 def test_cross_action_is_rejected(self):
  jid=self.submit();a=self.auth('status',digest({'job_id':jid}))
  with self.assertRaisesRegex(GateError,'UNAUTHORIZED'):self.service.get_job_receipt(jid,a)
 def test_cancel_only_queued(self):
  jid=self.submit();a=self.auth('cancel',digest({'job_id':jid}))
  self.assertEqual(self.service.cancel_queued_job(jid,a)['state'],'CANCELLED')
  with self.assertRaisesRegex(GateError,'CANNOT_CANCEL_RUNNING_JOB'):
   self.service.cancel_queued_job(jid,a)
 def test_receipt_not_fabricated(self):
  jid=self.submit();a=self.auth('receipt',digest({'job_id':jid}))
  self.assertIsNone(self.service.get_job_receipt(jid,a)['receipt'])
 def test_no_hosting_claim(self):
  self.assertFalse(capability_report()['mcp_sdk_connected'])
if __name__=='__main__':unittest.main()
