import unittest
from sandboxlib.c2e_range import cap_in_range
class RangeCases(unittest.TestCase):
    def test_range_complete(self):
        self.assertEqual(cap_in_range(3, 1, 5), 3)
        self.assertEqual(cap_in_range(-5, -1, 5), -1)
        self.assertEqual(cap_in_range(6, -1, 5), 5)
        self.assertEqual(cap_in_range(5, 5, 5), 5)
        self.assertEqual(cap_in_range(10**100, 0, 10), 10)
        self.assertEqual(cap_in_range(-(10**100), -10, 10), -10)
        self.assertRaises(TypeError, cap_in_range, True, 0, 2)
        self.assertRaises(TypeError, cap_in_range, 1, False, 2)
        self.assertRaises(TypeError, cap_in_range, 1, 0, True)
        self.assertRaises(TypeError, cap_in_range, 1.2, 0, 2)
        self.assertRaises(TypeError, cap_in_range, 1, "0", 2)
        self.assertRaises(TypeError, cap_in_range, 1, 0, None)
        self.assertRaises(ValueError, cap_in_range, 1, 3, 2)
