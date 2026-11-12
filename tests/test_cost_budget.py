import unittest
from sandboxlib.cost_budget import budget_tokens_remaining
class CostBudgetCases(unittest.TestCase):
    def test_budget_reservation(self):
        self.assertEqual(budget_tokens_remaining(100, 20, 30), 50)
        self.assertEqual(budget_tokens_remaining(0, 0, 0), 0)
        self.assertEqual(budget_tokens_remaining(10, 10, 0), 0)
        self.assertRaises(ValueError, budget_tokens_remaining, 5, 4, 2)
        self.assertRaises(ValueError, budget_tokens_remaining, -1, 0, 0)
        self.assertRaises(ValueError, budget_tokens_remaining, 5, -1, 0)
        self.assertRaises(TypeError, budget_tokens_remaining, True, 0, 0)
        self.assertRaises(TypeError, budget_tokens_remaining, 5, False, 0)
        self.assertRaises(TypeError, budget_tokens_remaining, 5, 2, 0.0)
