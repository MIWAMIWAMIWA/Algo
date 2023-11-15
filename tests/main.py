from src.beer_problem import set_cover_beer
import filecmp
import unittest


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        set_cover_beer("input_file_1.txt", "output_file_1.txt")
        self.assertTrue(filecmp.cmp("output_file_1.txt","result_file_1.txt"))

    def test_upgraded_default_case(self):
        set_cover_beer("input_file_3.txt", "output_file_3.txt")
        self.assertTrue(filecmp.cmp("output_file_3.txt", "result_file_3.txt"))

    def test_complex_case(self):
        set_cover_beer("input_file_2.txt", "output_file_2.txt")
        self.assertTrue(filecmp.cmp("output_file_2.txt", "result_file_2.txt"))

