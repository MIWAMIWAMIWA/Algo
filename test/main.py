import unittest
from src.KMP import kmp_search


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        self.assertEqual(kmp_search("a", "aaaa"), [0, 1, 2, 3])

    def test_more_complicated_case(self):
        self.assertEqual(kmp_search("ABABAB", "ABCABABABCABABABABCABAB"), [3, 10, 12])

    def test_more_complicated2_case(self):
        self.assertEqual(kmp_search("AA", "AAAACAAA"), [0, 1, 2, 5, 6])


