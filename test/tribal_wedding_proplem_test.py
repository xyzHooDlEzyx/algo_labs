import sys
import unittest

from src.tribal_wedding_proplem import count_pairs

sys.path.append("E:\\projects\\algo_labs")


class TribalWeddingTest(unittest.TestCase):

    def test_work(self):
        self.assertEqual(count_pairs(3, [(1, 2), (3, 4), (5, 6)]), 6)

    def test_zero(self):
        input1 = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(count_pairs(3, input1), 0)

    def test_empty(self):
        input1 = []
        self.assertEqual(count_pairs(0, input1), 0)


if __name__ == "__main__":
    unittest.main()
