import unittest
from sandboxlib.cost_usage import sum_settled_tokens
class CostUsageCases(unittest.TestCase):
    def test_settlement_accounting(self):
        self.assertEqual(sum_settled_tokens([]), 0)
        self.assertEqual(sum_settled_tokens([('A', 12), ('B', 0), ('C', 7)]), 19)
        self.assertRaises(ValueError, sum_settled_tokens, [('A', 1), ('A', 2)])
        self.assertRaises(ValueError, sum_settled_tokens, [('', 1)])
        self.assertRaises(ValueError, sum_settled_tokens, [('A', -1)])
        self.assertRaises(TypeError, sum_settled_tokens, [('A', True)])
        self.assertRaises(TypeError, sum_settled_tokens, [(3, 1)])
        self.assertRaises(TypeError, sum_settled_tokens, (('A', 1),))
        self.assertRaises(TypeError, sum_settled_tokens, [('A', 1, 2)])
