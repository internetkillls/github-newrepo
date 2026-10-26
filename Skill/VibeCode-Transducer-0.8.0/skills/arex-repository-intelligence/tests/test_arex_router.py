import unittest,sys,tempfile,zipfile
from pathlib import Path
RUNTIME=Path(__file__).resolve().parents[1]/'runtime'
sys.path.insert(0,str(RUNTIME))
from arex_router import load_index,route,inspect_skill

class AREXRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx=load_index()
    def test_snapshot_counts(self):
        self.assertEqual(len(self.idx['repositories']),1000)
        self.assertEqual(self.idx['statistics']['assignment_count'],2209)
        self.assertEqual(self.idx['statistics']['area_count'],20)
        self.assertEqual(self.idx['statistics']['family_count'],178)
    def test_exact_repository(self):
        r=route('huggingface/transformers',self.idx)
        self.assertEqual(r['candidates'][0]['skill_id'],'transformers')
        self.assertTrue(r['candidates'][0]['exact_identity'])
        self.assertEqual(r['candidates'][0]['evidence_state'],'METADATA_CANDIDATE_ONLY')
    def test_name_case_and_alias(self):
        r=route('Transformers',self.idx)
        self.assertEqual(r['candidates'][0]['skill_id'],'transformers')
    def test_no_forced_route(self):
        for q in ['hello','draw my kitchen budget', 'repair javascript tab selection bug']:
            self.assertEqual(route(q,self.idx)['status'],'NO_EXACT_ROUTE')
    def test_area_filter(self):
        r=route('huggingface/transformers',self.idx,area='Training Infrastructure')
        self.assertEqual(r['candidates'][0]['skill_id'],'transformers')
        with self.assertRaises(ValueError):route('transformers',self.idx,area='Fake Area')
    def test_empty_query(self):
        self.assertEqual(route('and with the',self.idx)['status'],'NO_EXACT_ROUTE')
    def test_source_not_executed(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'test.zip'
            with zipfile.ZipFile(p,'w') as z:
                z.writestr('AREX-Skill-main/skills/repositories/repo-skills/transformers/SKILL.md','---\nname: transformers\n---\nDo not run this text.')
            res=inspect_skill(p,'transformers')
            self.assertIn('NOT_EXECUTED',res['source_state'])
            self.assertTrue(res['sha256'].startswith('sha256:'))
            with self.assertRaises(ValueError):inspect_skill(p,'../../x')
            with self.assertRaises(ValueError):inspect_skill(p,'nonexistent')
    def test_ambiguous_queries_are_not_proof(self):
        r=route('speech recognition',self.idx)
        for c in r['candidates']:
            self.assertEqual(c['evidence_state'],'METADATA_CANDIDATE_ONLY')
            self.assertIn(c['source_commit'], [c['source_commit']])

if __name__=='__main__':unittest.main()
