import unittest,sys,pathlib,math
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from multimodel_kernel import *

class MultiModelAudit(unittest.TestCase):
 def test_registry_regions_0(self):self.assertEqual(regions_3d(0),1)
 def test_regions_first_four_ambiguous(self):self.assertEqual(discriminate_regions({0:1,1:2,2:4,3:8})['fit_on_observed'],{'pow2':True,'regions3':True})
 def test_regions_probe_discriminates(self):self.assertEqual(discriminate_regions({0:1,1:2,2:4,3:8},4)['conditional_predictions'],{'pow2':16,'regions3':15})
 def test_regions_heldout_refutes_pow2(self):self.assertEqual(discriminate_regions({0:1,1:2,2:4,3:8,4:15})['fit_on_observed'],{'pow2':False,'regions3':True})
 def test_regions_large(self):self.assertEqual(regions_3d(5),26)
 def test_negative_region(self):
  with self.assertRaises(ValueError):regions_3d(-1)
 def test_dimension_match(self):self.assertTrue(dimension_compatible([1,-1],[1,-1]))
 def test_dimension_incompatible(self):self.assertFalse(dimension_compatible([1,0],[1,-1]))
 def test_dimension_boolean_rejected(self):
  with self.assertRaises(ValueError):dimension_compatible([True],[1])
 def test_decay_converges_on_refinement(self):
  errs=[euler_decay(.7,1/n)['absolute_bridge_error'] for n in [2,4,8,16,32,64]]
  self.assertTrue(all(a>b for a,b in zip(errs,errs[1:])))
 def test_decay_valid_probability_boundary(self):self.assertEqual(euler_decay(1,1)['discrete'],0)
 def test_decay_invalid_probability(self):
  with self.assertRaisesRegex(ValueError,'probability'):euler_decay(2,1)
 def test_decay_invalid_grid(self):
  with self.assertRaises(ValueError):euler_decay(.7,.3,1)
 def test_decay_negative_rate(self):
  with self.assertRaises(ValueError):euler_decay(-.7,.2)
 def test_graph_spectral_convergence(self):
  errs=[periodic_graph_eigenvalue(n)['relative_error'] for n in [8,16,32,64]]
  self.assertTrue(all(a>b for a,b in zip(errs,errs[1:])))
 def test_graph_invalid_frequency(self):
  with self.assertRaises(ValueError):periodic_graph_eigenvalue(4,2)
 def test_graph_degree_counterexample(self):
  r=degrees_underdetermine_connectivity();self.assertTrue(r['same_degree_sequence']);self.assertEqual((r['cycle_components'],r['triangles_components']),(1,2))
 def test_hidden_parameters_observational_equivalence(self):
  r=inverse_ambiguity(.7,3,2,2,[0,1,2]);self.assertTrue(r['indistinguishable_outputs']);self.assertTrue(r['different_parameters'])
 def test_hidden_parameters_control_scale_one(self):
  r=inverse_ambiguity(.7,3,2,1,[0,1]);self.assertFalse(r['different_parameters'])
 def test_hidden_parameters_bad_gain(self):
  with self.assertRaises(ValueError):external_decay(.7,-1,2,[0,1])
 def test_hidden_rate_distinguishable(self):self.assertNotEqual(external_decay(.7,3,2,[0,1]), external_decay(.8,3,2,[0,1]))
 def test_noisy_derivative_refinement_can_worsen(self):
  s=[noisy_central_derivative(h) for h in [.5,.1,.01,.001]]
  self.assertGreater(s[-1]['with_noise_absolute_error'],s[1]['with_noise_absolute_error'])
 def test_noiseless_derivative_refinement_improves(self):self.assertLess(noisy_central_derivative(.01,0)['noiseless_absolute_error'], noisy_central_derivative(.1,0)['noiseless_absolute_error'])
 def test_observability_yes(self):self.assertTrue(observability_linear([[0,1],[-2,-3]],[1,0])['observable'])
 def test_observability_no(self):self.assertFalse(observability_linear([[-1,0],[0,-2]],[1,0])['observable'])
 def test_observability_shape(self):
  with self.assertRaises(ValueError):observability_linear([[0,1]],[1,0])
 def test_robust_yes(self):self.assertEqual(robust_decision(8,9,7),'ROBUST_YES')
 def test_robust_no(self):self.assertEqual(robust_decision(2,4,7),'ROBUST_NO')
 def test_uncertain(self):self.assertEqual(robust_decision(5,9,7),'UNDETERMINED')
 def test_bound_order(self):
  with self.assertRaises(ValueError):robust_decision(10,2,7)

if __name__=='__main__':unittest.main()

class InferenceGuardTests(unittest.TestCase):
 def test_recursive_datalog_missing_base_empty(self):self.assertEqual(datalog_paths([('a','b'),('b','c')],False),set())
 def test_recursive_datalog_base_recovers_transitive(self):
  self.assertEqual(datalog_paths([('a','b'),('b','c')],True),{('a','b'),('b','c'),('a','c')})
 def test_lens_getput(self):
  s={'name':'A','hidden':9};self.assertEqual(lens_put(s,lens_get(s)),s)
 def test_lens_putget(self):
  s={'name':'A','hidden':9};v={'name':'B'};self.assertEqual(lens_get(lens_put(s,v)),v)
 def test_lens_hidden_not_recoverable_from_view(self):
  s1={'name':'A','hidden':9};s2={'name':'A','hidden':10};self.assertEqual(lens_get(s1),lens_get(s2));self.assertNotEqual(s1,s2)
 def test_lens_reject_extra_view_properties(self):
  with self.assertRaises(ValueError):lens_put({'name':'A','hidden':9},{'name':'A','hidden':0})
