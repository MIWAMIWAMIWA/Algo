import math
import unittest


def MinimalSqaure(n, w, h):
    if n < 0 or n > 1012 or w < 0 or w > 109 or h < 0 or h > 109:
        return -1

    min = math.floor(math.sqrt(n * w * h))

    max = w * h * n

    while (min < max):

        mid= (max+min) // 2

        if (mid // w) * (mid // h) >= n:
            max = mid

        else:
            min = mid + 1

    return max


class SortedTest(unittest.TestCase):

    def test_original_values(self):
        size = MinimalSqaure(10, 2, 3)
        self.assertEqual(size, 9)

    def test_bigger_weapons(self):
        size = MinimalSqaure(2, 100, 99)
        self.assertEqual(size, 198)

    def test_square_values(self):
        size = MinimalSqaure(4, 1, 1)
        self.assertEqual(size, 2)

    def test_wrong_values(self):
        size = MinimalSqaure(0, 19999999, 199999996)
        self.assertEqual(size, -1)


if __name__ == '__main__':
    unittest.main()
