import unittest


def find_not_sorted(arr):
    n = len(arr)
    max_index = -1
    min_index = -1
    min_element = None
    max_element = 0
    if n != 1 or n != 0:
        for current in range(n - 1):
            if arr[current] > max_element:
                max_element = arr[current]
            else:
                max_index = current
            if arr[current] > arr[current + 1]:
                if min_element is None or min_element > arr[current + 1]:
                    min_element = arr[current + 1]
                    max_index = current + 1
            if max_element > arr[n - 1]:
                max_index = n - 1
        if min_element is not None:
            if min_element < arr[0]:
                min_index = 0
            else:
                for current in range(n - 1):
                    if arr[current] <= min_element < arr[current + 1]:
                        min_index = current + 1
                        break
    return min_index, max_index




class SortedTest(unittest.TestCase):

    def test_original_values(self):
        first, last = find_not_sorted([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
        self.assertEqual(first, 3)
        self.assertEqual(last, 9)

    def test_sorted_values(self):
        first, last = find_not_sorted([1, 2, 4, 7, 10, 11])
        self.assertEqual(first, -1)
        self.assertEqual(last, -1)

    def test_solo_values(self):
        first, last = find_not_sorted([1])
        self.assertEqual(first, -1)
        self.assertEqual(last, -1)

    def test_zero_values(self):
        first, last = find_not_sorted([])
        self.assertEqual(first, -1)
        self.assertEqual(last, -1)

    def test_complicated_values(self):
        first, last = find_not_sorted([1, 2, 3, 13, 9, 12, 15, 16, 20, 17, 19, 25, 26])
        self.assertEqual(first, 3)
        self.assertEqual(last, 10)

    def test_nosorted_values(self):
        first, last = find_not_sorted([5, 4, 3, 2, 1])
        self.assertEqual(first, 0)
        self.assertEqual(last, 4)

    def test_complicated_values2(self):
        first, last = find_not_sorted([1, 2, 4, 3, 8, 7])
        self.assertEqual(first, 2)
        self.assertEqual(last, 5)

    def test_bigger_values(self):
        first, last = find_not_sorted([13456, 54356, 23456, 37585, 87385, 75854])
        self.assertEqual(first, 1)
        self.assertEqual(last, 5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
