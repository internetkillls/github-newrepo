"""Static regression tests; not an end-to-end GPT-6 activation witness."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
MAIN = ROOT / 'skills/reasoning-method-controller/SKILL.md'
ADJUNCT = ROOT / 'skills/semantic-transition-audit/SKILL.md'
MARKER = '`../semantic-transition-audit/SKILL.md`'

def valid_dispatcher(source):
    section = source.split('# 19. Conditional module dispatcher',1)[-1].split('# 20. High-leverage ambiguity gate',1)[0]
    rows = [x for x in section.splitlines() if x.startswith('| ') and MARKER in x]
    return (len(rows) == 1 and 'only if' in rows[0] and 'materially affect' in rows[0]
            and 'fast-exit' in rows[0] and 'otherwise' in rows[0])

class DispatcherRegression(unittest.TestCase):
    def test_positive_conditional_dispatch(self):
        self.assertTrue(valid_dispatcher(MAIN.read_text()))
    def test_negative_absent_reference(self):
        self.assertFalse(valid_dispatcher(MAIN.read_text().replace(MARKER, '`other.md`')))
    def test_negative_unconditional_overtrigger(self):
        self.assertFalse(valid_dispatcher(MAIN.read_text().replace('only if', 'always')))
    def test_negative_no_fast_exit(self):
        self.assertFalse(valid_dispatcher(MAIN.read_text().replace('fast-exit', 'exhaustive scan')))
    def test_target_exists(self):
        self.assertTrue(ADJUNCT.is_file())
        self.assertIn('NO_MATERIAL_ISSUE', ADJUNCT.read_text())
    def test_old_routing_stages_preserved(self):
        s = MAIN.read_text()
        self.assertIn('S0 INTAKE', s)
        self.assertIn('S9 DELIVER', s)
        self.assertNotIn('S10 ',s)
    def test_operator_index_still_routed(self):
        self.assertIn('`references/operator-index.md`', MAIN.read_text())

if __name__ == '__main__': unittest.main()
