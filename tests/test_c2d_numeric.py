import unittest
from sandboxlib.c2d_numeric import clamp_nonnegative


class NumericTests(unittest.TestCase):
    def test_clamp_nonnegative(self):
        self.assertEqual(clamp_nonnegative(-4, 8), 0)
        self.assertEqual(clamp_nonnegative(9, 6), 6)
        self.assertRaises(TypeError, clamp_nonnegative, True, 8)
