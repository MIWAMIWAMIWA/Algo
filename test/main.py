import unittest
from src.calculate_rope import calculate_rope


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        self.assertEqual(2738.18, calculate_rope(4, [56, 18, 17, 94, 23, 7, 21, 94, 29, 54,
                                                     44, 26, 86, 79, 4, 15, 5, 91, 25, 17,
                                                     88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
                                                     75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35,
                                                     52, 3, 93, 34, 57, 51, 11, 39, 72]))

    def test_communism(self):
        self.assertEqual(300, calculate_rope(100, [1, 1, 1, 1]))

    def test_communism_2(self):
        self.assertEqual(5.66, calculate_rope(2, [3, 3, 3]))

