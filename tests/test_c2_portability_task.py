import unittest

from sandboxlib.c2_portability_task import normalize_tag


class NormalizeTagTests(unittest.TestCase):
    def test_normalize_tag(self):
        self.assertEqual(normalize_tag(" Hello  WORLD "), "hello-world")
        self.assertRaises(TypeError, normalize_tag, 12)
        self.assertRaises(ValueError, normalize_tag, " ")
