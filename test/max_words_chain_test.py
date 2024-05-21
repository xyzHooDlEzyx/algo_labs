import unittest

from src.max_words_chain import read_input, write_output, max_chain_length


class MaxWordChainTest(unittest.TestCase):
    def setUp(self):
        self.input_file = "../test/source/wchain.in"
        self.output_file = "../test/source/wchain.out"

    def test_max_chain_length(self):
        words = read_input(self.input_file)

        expected_result = 6

        result = max_chain_length(words)

        self.assertEqual(result, expected_result)

    def test_read_input(self):
        expected_words = [
            "crates",
            "car",
            "cat",
            "cats",
            "crate",
            "rate",
            "at",
            "ate",
            "tea",
            "rat",
            "a",
        ]

        words = read_input(self.input_file)

        self.assertEqual(words, expected_words)

    def test_write_output(self):
        result = 6

        write_output(result, self.output_file)

        with open(self.output_file, "r", encoding="utf-8") as file:
            output = int(file.read().strip())

        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()
