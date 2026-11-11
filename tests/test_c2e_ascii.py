import unittest
from sandboxlib.c2e_ascii import ascii_compact

class AsciiCompactTests(unittest.TestCase):
    def test_ascii_compact(self):
        self.assertEqual(ascii_compact(" Hi \tThere "), "hi-there")
        self.assertEqual(ascii_compact("A\r\nB\vC\fD"), "a-b-c-d")
        self.assertEqual(ascii_compact(" X  Y "), "x-y")
        self.assertEqual(ascii_compact("A\x1cB"), "a\x1cb")
        self.assertEqual(ascii_compact(" X "), "x")
        self.assertRaises(TypeError, ascii_compact, 1)
        self.assertRaises(TypeError, ascii_compact, None)
        self.assertRaises(ValueError, ascii_compact, "caf\u00e9")
        self.assertRaises(ValueError, ascii_compact, "\u00a0")
        self.assertRaises(ValueError, ascii_compact, " \t\r\n\v\f ")
