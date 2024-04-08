import sys
import unittest
from src.kth_largest_elem import KIsGreaterThenSizeOfArr, find_k_or_error

sys.path.append("E:\\projects\\algo_labs")


class TestKthLargestElement(unittest.TestCase):
    def test_find_kth_largest(self):
        self.assertEqual(find_k_or_error([3, 2, 1, 5, 6, 4], 1), 6)
        self.assertEqual(find_k_or_error([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_k_or_error([3, 2, 1, 5, 6, 4], 3), 4)

    def test_k_out_of_bounds(self):
        with self.assertRaises(KIsGreaterThenSizeOfArr):
            find_k_or_error([3, 2, 1, 5, 6, 4], 0)
        with self.assertRaises(KIsGreaterThenSizeOfArr):
            find_k_or_error([3, 2, 1, 5, 6, 4], 7)


if __name__ == "__main__":
    unittest.main()
