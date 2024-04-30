import unittest
from src.flower_selling_company import read_csv_to_graph, dfs

class PriorityQueueTest(unittest.TestCase):

    def test_no_file(self):
        with self.assertRaises(FileNotFoundError):
            read_csv_to_graph(None)
