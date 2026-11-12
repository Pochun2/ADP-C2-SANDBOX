import unittest
from sandboxlib.cost_report import cost_estimate_line
class CostReportCases(unittest.TestCase):
    def test_estimate_labeling(self):
        self.assertEqual(cost_estimate_line(5, 24, 17), 'tokens=5;credit_eq_micro=24;api_usd_eq_micro=17;billing=ESTIMATE_NOT_ACTUAL')
        self.assertEqual(cost_estimate_line(0, 0, 0), 'tokens=0;credit_eq_micro=0;api_usd_eq_micro=0;billing=ESTIMATE_NOT_ACTUAL')
        self.assertRaises(TypeError, cost_estimate_line, True, 0, 0)
        self.assertRaises(TypeError, cost_estimate_line, 0, False, 0)
        self.assertRaises(TypeError, cost_estimate_line, 0, 0, 1.0)
        self.assertRaises(ValueError, cost_estimate_line, -1, 0, 0)
        self.assertRaises(ValueError, cost_estimate_line, 0, -1, 0)
        self.assertRaises(ValueError, cost_estimate_line, 0, 0, -1)
