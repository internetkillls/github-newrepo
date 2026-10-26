import csv,pathlib,unittest

REF=pathlib.Path(__file__).resolve().parents[1]/'references'

class RegistryProvenanceTests(unittest.TestCase):
    def test_99_unique_namespace_ids(self):
        with (REF/'registry_99_multimodel_audit.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),99)
        self.assertEqual({r['id'] for r in rows},{f'MATH-{i:03d}' for i in range(1,100)})
    def test_inherited_oa_sources_count_and_namespace(self):
        with (REF/'oa_multimodel_source_ledger.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),22)
        self.assertEqual({r['id'] for r in rows},{f'OA{i:02d}' for i in range(1,23)})
    def test_not_all_theorems_are_claimed_verified(self):
        with (REF/'registry_99_multimodel_audit.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        self.assertTrue(any('NOT_THEOREM_VERIFIED' in r['oa_linkage_status'] for r in rows))
        self.assertTrue(all(r['runtime_verification']!='VERIFIED_ALL_THEOREMS' for r in rows))
    def test_unresolved_original_reference_ids_not_certified(self):
        with (REF/'registry_99_multimodel_audit.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        self.assertTrue(any('UNRESOLVED' in r['source_Sxx_status'] for r in rows))
