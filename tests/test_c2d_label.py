import unittest
from sandboxlib.c2d_label import label_key


class LabelTests(unittest.TestCase):
    def test_label_key(self):
        self.assertEqual(label_key(" Hi  A "), "hi_a")
        self.assertRaises(TypeError, label_key, 10)
        self.assertRaises(ValueError, label_key, "  ")
