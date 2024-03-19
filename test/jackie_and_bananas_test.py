import sys
import unittest
from src.jackie_and_bananas import min_eating_speed, JackieWillBeCaught
sys.path.append('E:\\projects\\algo_labs')


class TestMinEatingSpeed(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_h_is_less_then_piles(self):
        with self.assertRaises(JackieWillBeCaught):
            min_eating_speed([3, 2, 1, 5, 6, 4], 0)
        with self.assertRaises(JackieWillBeCaught):
            min_eating_speed([3, 2, 1, 5, 6, 4], 5)


if __name__ == "__main__":
    unittest.main()
