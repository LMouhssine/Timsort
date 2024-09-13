import unittest
import random
from timsort import timsort

class TestTimsort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(timsort([]), [])

    def test_sorted_list(self):
        arr = list(range(100))
        self.assertEqual(timsort(arr), arr)

    def test_reverse_sorted_list(self):
        arr = list(range(100, 0, -1))
        self.assertEqual(timsort(arr), sorted(arr))

    def test_random_list(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(timsort(arr), sorted(arr))

    def test_list_with_duplicates(self):
        arr = [1, 5, 2, 8, 2, 1, 5, 9, 3, 5, 2]
        self.assertEqual(timsort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()