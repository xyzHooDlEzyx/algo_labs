import unittest
from src.flower_selling_company import read_csv_to_graph, dfs, max_flow


class FordFulkersonTest(unittest.TestCase):

    def setUp(self):
        file = "../test/source/roads.csv"
        self.graph_dictionary = read_csv_to_graph(file)

    def test_input_and_max_flow(self):
        self.assertEqual(max_flow(self.graph_dictionary, "VS", "VD"), 29)

    def test_read_csv_to_graph(self):
        csv_content = ["A,B,C\n", "D,E,F\n", "A,D,10\n", "B,E,5\n", "C,F,8\n"]
        with open("../test/source/test.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            csvfile.writelines(csv_content)

        graph_dict = read_csv_to_graph("../test/source/test.csv")

        self.assertEqual(len(graph_dict), 6)
        self.assertIn("A", graph_dict)
        self.assertIn("B", graph_dict)
        self.assertIn("C", graph_dict)
        self.assertIn("D", graph_dict)
        self.assertIn("E", graph_dict)
        self.assertIn("F", graph_dict)

    def test_dfs(self):
        graph_dict = {"A": {"B": 5, "C": 3}, "B": {"D": 2}, "C": {"D": 1}, "D": {}}

        path, flow = dfs(graph_dict, "A", "D")

        self.assertEqual(path, [("A", "C"), ("C", "D")])
        self.assertEqual(flow, 1)

    def test_max_flow(self):
        graph_dict = {"A": {"B": 3, "C": 5}, "B": {"D": 2}, "C": {"D": 2}}

        max_flow_value = max_flow(graph_dict, "A", "D")

        self.assertEqual(max_flow_value, 4)


if __name__ == "__main__":
    unittest.main()
