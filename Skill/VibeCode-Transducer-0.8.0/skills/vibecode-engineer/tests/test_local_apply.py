import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'runtime'))
from local_apply import apply_local,ApplyError,runner_receipt
from vibe_transducer import sha

class LocalPatchTests(unittest.TestCase):
    def test_flags_required(self):
        with tempfile.TemporaryDirectory() as p:
            f=pathlib.Path(p)/'module.py';f.write_text('x=1\n')
            with self.assertRaises(ApplyError):apply_local(p,[{'path':'module.py','old':'1','new':'2','sha256':sha('x=1\n')}],['python','-m','unittest'],approved=False,writes_enabled=True)
            self.assertEqual(f.read_text(),'x=1\n')
    def test_real_tests_receipt_applies(self):
        with tempfile.TemporaryDirectory() as p:
            root=pathlib.Path(p);root.joinpath('module.py').write_text('x=1\n');(root/'tests').mkdir()
            (root/'tests'/'test_module.py').write_text('import unittest\nfrom module import x\nclass X(unittest.TestCase):\n def test_val(self): self.assertEqual(x,2)\n')
            c=[{'path':'module.py','old':'x=1','new':'x=2','sha256':sha('x=1\n')}]
            r=apply_local(p,c,[sys.executable,'-m','unittest','discover','-s','tests','-v'],approved=True,writes_enabled=True)
            self.assertEqual(r['state'],'PATCH_APPLIED_TEST_RECEIPT',r)
            self.assertEqual(root.joinpath('module.py').read_text(),'x=2\n')
    def test_failed_tests_restore(self):
        with tempfile.TemporaryDirectory() as p:
            root=pathlib.Path(p);root.joinpath('module.py').write_text('x=1\n');(root/'tests').mkdir()
            (root/'tests'/'test_module.py').write_text('import unittest\nclass X(unittest.TestCase):\n def test_fail(self): self.assertTrue(False)\n')
            c=[{'path':'module.py','old':'x=1','new':'x=2','sha256':sha('x=1\n')}]
            r=apply_local(p,c,[sys.executable,'-m','unittest','discover','-s','tests','-v'],approved=True,writes_enabled=True)
            self.assertEqual(r['state'],'ROLLED_BACK',r)
            self.assertEqual(root.joinpath('module.py').read_text(),'x=1\n')
    def test_fake_echo_runner_denied(self):
        with tempfile.TemporaryDirectory() as p:
            root=pathlib.Path(p);root.joinpath('module.py').write_text('x=1\n')
            c=[{'path':'module.py','old':'x=1','new':'x=2','sha256':sha('x=1\n')}]
            with self.assertRaises(ApplyError):
                apply_local(p,c,['echo','4 passed'],approved=True,writes_enabled=True)
            self.assertEqual(root.joinpath('module.py').read_text(),'x=1\n')
    def test_zero_tests_not_receipt(self):
        self.assertFalse(runner_receipt(['python'], 'Ran 0 tests in 0.000s\n\nOK\n'))
    def test_hash_rejects_prewrite(self):
        with tempfile.TemporaryDirectory() as p:
            root=pathlib.Path(p);root.joinpath('module.py').write_text('x=99\n')
            with self.assertRaises(ApplyError):apply_local(p,[{'path':'module.py','old':'x=1','new':'x=2','sha256':sha('x=1\n')}],[sys.executable,'-m','unittest'],approved=True,writes_enabled=True)
    def test_test_file_protected(self):
        with tempfile.TemporaryDirectory() as p:
            root=pathlib.Path(p);root.joinpath('test_x.py').write_text('x=1\n')
            with self.assertRaises(ApplyError):apply_local(p,[{'path':'test_x.py','old':'1','new':'2','sha256':sha('x=1\n')}],[sys.executable],approved=True,writes_enabled=True)
if __name__=='__main__':unittest.main()
