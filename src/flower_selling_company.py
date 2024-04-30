import csv
from typing import Tuple, List, Dict


def read_csv_to_graph(filename):
    graph_dict = {}
    with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        farms = next(reader)[0].split(",")
        stores = next(reader)[0].split(",")

        all_nodes = set(farms + stores)
        for row in reader:
            source, destination, capacity = row
            all_nodes.add(source)
            all_nodes.add(destination)

        for node in all_nodes:
            graph_dict[node] = {}

        csvfile.seek(0)
        next(reader)
        next(reader)

        for row in reader:
            if row:
                source, destination, capacity = row
                capacity = (
                    float("inf") if capacity.strip().lower() == "inf" else int(capacity)
                )
                graph_dict[source][destination] = capacity

    return graph_dict


def dfs(graph: Dict[str, Dict[str, int]], start: str, destination: str):

    stack = [(start, float("inf"), [])]
    visited = set()

    while stack:
        current_element, current_weight, path = stack.pop()

        if current_element == destination:
            return path, current_weight

        visited.add(current_element)

        for next_element, weight in graph[current_element].items():
            if next_element not in visited and weight > 0:
                new_flow = min(current_weight, weight)
                stack.append(
                    (next_element, new_flow, path + [(current_element, next_element)])
                )

    return [], 0


def decrease_weight_on_path(graph2, path: List[Tuple[str, str]], found_flow: int):
    """_summary_

    Args:
        graph2 (_type_): _description_
        path (_type_): [(A, B), (B, C), (C, L)]
        found_flow (_type_): _description_
    """
    for edge in path:
        graph2[edge[0]][edge[1]] -= found_flow
        if graph2[edge[0]][edge[1]] == 0:
            del graph2[edge[0]][edge[1]]


def max_flow(graph3, start, destination):
    total_flow = 0
    while True:
        path, found_flow = dfs(graph3, start, destination)

        if found_flow == 0:
            break

        total_flow += found_flow
        decrease_weight_on_path(graph3, path, found_flow)

    return total_flow


if __name__ == "__main__":

    file = "source/roads.csv"
    graph_dictionary = read_csv_to_graph(file)
    print(graph_dictionary)
    print(max_flow(graph_dictionary, "VS", "VD"))
