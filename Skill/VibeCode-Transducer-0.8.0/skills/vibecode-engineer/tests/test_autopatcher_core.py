import hashlib, importlib, json, pathlib, subprocess, sys, tempfile, time, unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from autopatcher_core import (JobStore,GateError,repo_preflight,verified_snapshot,digest,canonical,
    sign_grant,verify_grant,run_canary_job,inspect_fixture,apply_exact,validate_spec,capability_report)

SIGNING_KEY=b'unit-test-only-development-operator-key-material-32-bytes'

def git(root,*args):
    p=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,check=True)
    return p.stdout.strip()

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=pathlib.Path(self.tmp.name)
        self.repo=self.root/'source';self.repo.mkdir()
        git(self.repo,'init','-q')
        (self.repo/'config.json').write_text('{"result": 1}\n')
        git(self.repo,'add','config.json')
        git(self.repo,'-c','user.name=Test','-c','user.email=test@example.test','commit','-qm','init')
        self.commit=git(self.repo,'rev-parse','HEAD')
        self.registry={'fixture/repo':{'root':str(self.repo),'permitted_paths':['config.json'],'trusted_for_canary':True}}
        self.dbpath=self.root/'jobs.sqlite'
        self.store=JobStore(self.dbpath)
        self.addCleanup(self.store.close)
        self.patch={'path':'config.json','old':'"result": 1','new':'"result": 2',
                    'expected_sha256':digest((self.repo/'config.json').read_bytes())}
        self.test={'kind':'json_value','id':'regression.correct_result', 'path':'config.json','pointer':'/result','expected':2}
        self.spec={'repo_id':'fixture/repo','base_sha':self.commit,'patch':self.patch,'test':self.test}

    def submit(self,key='canary-run-123'):
        return self.store.submit(self.spec,key)['job_id']
    def grant(self,jid,**overrides):
        fields={'job_id':jid,'repo_id':self.spec['repo_id'],'base_sha':self.commit,
                'patch_hash':digest(self.spec['patch']),'permitted_paths':['config.json'],
                'operation':'apply_isolated','expires_at':time.time()+1000,
                'nonce':'nonce-'+jid+'-fixed','policy_version':'vct-autopatch-policy-1'}
        fields.update(overrides)
        return sign_grant(fields,SIGNING_KEY)

    def test_red_before_green_after_without_source_mutation(self):
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['state'],'CANARY_RED_GREEN')
        self.assertEqual(r['receipt']['before']['status'],'FAIL')
        self.assertEqual(r['receipt']['after']['status'],'PASS')
        self.assertFalse(r['permission_to_push']);self.assertFalse(r['patch_persisted_in_source'])
        self.assertEqual((self.repo/'config.json').read_text(),'{"result": 1}\n')
        self.assertEqual(git(self.repo,'rev-parse','HEAD'),self.commit)
        self.assertTrue(self.store.verify_chain(jid))

    def test_baseline_green_does_not_prove_bug_fix(self):
        self.test['expected']=1
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['state'],'BASELINE_NOT_REPRODUCED')
        self.assertEqual(r['claim'],'BUG_FIXED_WITHHELD')

    def test_after_failure_is_not_patch_success(self):
        self.test['expected']=3
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['state'],'AFTER_TEST_FAILED')

    def test_unsigned_grant_denied(self):
        jid=self.submit();g=self.grant(jid);g['mac']='0'*64
        self.assertEqual(run_canary_job(self.store,jid,self.registry,g,SIGNING_KEY)['reason'],'GRANT_INVALID')
    def test_expired_grant_denied(self):
        jid=self.submit();g=self.grant(jid,expires_at=time.time()-1)
        self.assertEqual(run_canary_job(self.store,jid,self.registry,g,SIGNING_KEY)['reason'],'GRANT_EXPIRED')
    def test_wrong_repo_bound_grant_denied(self):
        jid=self.submit();g=self.grant(jid,repo_id='fixture/other')
        self.assertEqual(run_canary_job(self.store,jid,self.registry,g,SIGNING_KEY)['reason'],'GRANT_SCOPE_MISMATCH')
    def test_wrong_diff_bound_grant_denied(self):
        jid=self.submit();g=self.grant(jid,patch_hash='0'*64)
        self.assertEqual(run_canary_job(self.store,jid,self.registry,g,SIGNING_KEY)['reason'],'GRANT_SCOPE_MISMATCH')
    def test_wrong_operation_grant_denied(self):
        jid=self.submit();g=self.grant(jid,operation='deploy_production')
        self.assertEqual(run_canary_job(self.store,jid,self.registry,g,SIGNING_KEY)['reason'],'GRANT_SCOPE_MISMATCH')
    def test_missing_allowlist_repo_denied(self):
        jid=self.submit();r=run_canary_job(self.store,jid,{},self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['reason'],'REPO_NOT_ALLOWLISTED')
    def test_path_outside_operator_registry_denied(self):
        self.registry['fixture/repo']['permitted_paths']=[]
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['reason'],'REPO_POLICY_DENIED')
    def test_dirty_git_preflight_denied(self):
        (self.repo/'untracked.txt').write_text('dirty')
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['reason'],'DIRTY_REPOSITORY')
    def test_stale_git_preflight_denied(self):
        (self.repo/'config.json').write_text('{"result": 99}\n')
        git(self.repo,'add','config.json')
        git(self.repo,'-c','user.name=Test','-c','user.email=test@example.test','commit','-qm','modified')
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertEqual(r['reason'],'STALE_COMMIT')
    def test_non_git_source_denied(self):
        p=self.root/'not-repo';p.mkdir()
        with self.assertRaises(GateError):repo_preflight(p,self.commit)
    def test_symlink_in_source_denied(self):
        (self.repo/'link.json').symlink_to('config.json')
        git(self.repo,'add','link.json')
        git(self.repo,'-c','user.name=Test','-c','user.email=test@example.test','commit','-qm','symlink')
        with self.assertRaisesRegex(GateError,'UNSAFE_GIT_ENTRY'):
            repo_preflight(self.repo,git(self.repo,'rev-parse','HEAD'))
    def test_test_edit_forbidden(self):
        self.patch['path']='tests/test_config.py';self.test['path']='tests/test_config.py'
        with self.assertRaisesRegex(GateError,'PROTECTED_PATH'):validate_spec(self.spec)
    def test_command_injection_not_interpreted(self):
        self.spec['test']['command']='curl https://untrusted.invalid'
        # Reject unknown text rather than retaining it in a job ledger.
        with self.assertRaisesRegex(GateError,'INVALID_JOB'):self.submit()
        self.assertEqual(capability_report()['user_project_tests'],'NOT_EXECUTED_SANDBOX_REQUIRED')
    def test_idempotent_submit(self):
        a=self.store.submit(self.spec,'same-job-123');b=self.store.submit(self.spec,'same-job-123')
        self.assertEqual(a['job_id'],b['job_id']);self.assertTrue(b['replayed'])
    def test_idempotency_conflict(self):
        self.store.submit(self.spec,'same-job-123')
        self.spec['test']['expected']=7
        with self.assertRaisesRegex(GateError,'IDEMPOTENCY_CONFLICT'):
            self.store.submit(self.spec,'same-job-123')
    def test_job_survives_store_reopen(self):
        jid=self.submit();self.store.close();self.store=JobStore(self.dbpath)
        self.assertEqual(self.store.status(jid)['state'],'REQUESTED')
    def test_event_tampering_detected(self):
        jid=self.submit();self.store.db.execute('UPDATE events SET payload=? WHERE job_id=?',('{"wrong":1}',jid))
        self.assertFalse(self.store.verify_chain(jid))
    def test_fresh_grant_single_use(self):
        jid=self.submit();g=self.grant(jid)
        self.store.consume_grant(g['fields']['nonce'],jid)
        with self.assertRaisesRegex(GateError,'GRANT_REPLAY'):
            self.store.consume_grant(g['fields']['nonce'],jid)
    def test_claim_does_not_overpromote_on_positive(self):
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.assertIn('NOT_TARGET_SUITE',r['receipt']['proof_ceiling'])
        self.assertNotEqual(r['state'],'DEPLOYED')
    def test_reject_invalid_test_claim(self):
        self.test['kind']='shell'
        with self.assertRaisesRegex(GateError,'UNSUPPORTED_TEST'):validate_spec(self.spec)
    def test_reject_other_fixture_path(self):
        self.test['path']='else.json'
        with self.assertRaisesRegex(GateError,'TEST_SCOPE_MISMATCH'):validate_spec(self.spec)
    def test_reject_stale_file_hash(self):
        self.patch['expected_sha256']='a'*64
        jid=self.submit()
        with self.assertRaisesRegex(GateError,'STALE_FILE_HASH'):
            run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
    def test_snapshot_is_ephemeral(self):
        with verified_snapshot(self.repo,self.commit) as (snap,pre):
            self.assertEqual((snap/'config.json').read_text(),'{"result": 1}\n')
            location=snap
        self.assertFalse(location.exists())
    def test_receipt_survives_restart_and_matches_hash(self):
        jid=self.submit();r=run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.store.close();self.store=JobStore(self.dbpath)
        self.assertEqual(digest(self.store.receipt(jid)),r['receipt_sha256'])
        self.assertTrue(self.store.verify_chain(jid))

    def test_cancel_queued_and_refuse_execution(self):
        jid=self.submit();self.store.cancel(jid)
        self.assertEqual(self.store.status(jid)['state'],'CANCELLED')
        with self.assertRaisesRegex(GateError,'INVALID_TRANSITION'):
            run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)

    def test_receipt_tampering_detected(self):
        jid=self.submit();run_canary_job(self.store,jid,self.registry,self.grant(jid),SIGNING_KEY)
        self.store.db.execute('UPDATE receipts SET body=? WHERE job_id=?',('{"modified":true}',jid))
        self.assertEqual(self.store.receipt(jid),{'integrity_error':'RECEIPT_TAMPERED'})

    def test_unrecognized_spec_fields_rejected(self):
        self.spec['token']='SHOULD_NOT_BE_STORED'
        with self.assertRaisesRegex(GateError,'INVALID_JOB'):self.submit()

    def test_target_suite_or_production_never_exposed(self):
        info=capability_report()
        self.assertIs(info['deploy'],False)
        self.assertIs(info['git_push'],False)
        self.assertIs(info['mcp_cloud_connected'],False)

if __name__=='__main__':unittest.main()
