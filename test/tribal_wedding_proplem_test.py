import unittest

from src.tribal_wedding_proplem import count_pairs, read_input


class TribalWeddingTest(unittest.TestCase):

    def test_work_and_input(self):
        file = "../test/source/input.txt"
        n, pairs = read_input(file)
        self.assertEqual(count_pairs(n, pairs), 4)

    def test_zero(self):
        input1 = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(count_pairs(3, input1), 0)

    def test_empty(self):
        input1 = []
        self.assertEqual(count_pairs(0, input1), 0)


if __name__ == "__main__":
    unittest.main()
