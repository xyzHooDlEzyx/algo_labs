import unittest
from src.islands_counter import islands_count


class TestIslandsCount(unittest.TestCase):

    def test_islands_count_diagonal(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]

        result = islands_count(grid)
        self.assertEqual(result, 1)

    def test_no_land(self):
        grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        result = islands_count(grid)
        self.assertEqual(result, 0)

    def test_all_is_land(self):
        grid = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
        result = islands_count(grid)
        self.assertEqual(result, 1)

    def test_empty_grid(self):
        grid = []
        result = islands_count(grid)
        self.assertEqual(result, 0)

    def test_multiple_islands(self):
        grid = [
            ["1", "0", "1", "0", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "1", "0", "1", "0", "1", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "1", "0", "0", "0"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"],
            ["0", "1", "0", "1", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0"],
            ["0", "0", "0", "1", "0", "0", "1", "1", "1", "0"],
            ["1", "0", "1", "0", "1", "0", "0", "1", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"],
        ]
        result = islands_count(grid)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
