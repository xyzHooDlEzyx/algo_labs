import unittest
from lab1_var3 import kIsGreaterThenSizeOfArr, find_k_max

class TestKMax(unittest.TestCase):
    def test_k_is_less_then_size(self):
        arr = [-1, 22, 40, -2222, 1111, -2, 3, 1000]
        max_element, position = find_k_max(3, arr)
        self.assertEqual(max_element, 40)
        self.assertEqual(position, 2)
    def test_k_is_greater_then_size(self):
        arr = [-1, 22, 40, -2222, 1111, -2, 3, 1000]
        with self.assertRaises(kIsGreaterThenSizeOfArr):
            find_k_max(10, arr)

if __name__ == '__main__':
    unittest.main()
