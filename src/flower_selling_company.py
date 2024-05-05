import csv
from typing import Tuple, List, Dict


def read_csv_to_graph(filename):

    """
    function that reads csv file
    from given location
    and returns graph as dictionary
    Args:
        filename:

    Returns:
    graph dict
    """

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

    """
    dfs function that receives
    Args:
        graph: dict
        start: str
        destination: str
    has visited - set
    and stack that contains:
    current elements(vortexes) - name, weight of edge to this element(vortex) , and path to this element
    Returns:
    path(as list) to destination and max flow to destination vortex from this path
    """

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


def decrease_weight_on_path(graph: Dict[str, Dict[str, int]], path: List[Tuple[str, str]], found_flow: int):
    """
    decreases weight of edges after 1 full run of dfs
    and if weight of edge = 0 deleting this edge
    Args:
        graph: dict
        path: list[tuple]
        found_flow: int

    Returns:
    graph(dict) that contains edges
    after run of this function returns
    this dict with decreased weight of edges
    or/and deleted ones
    """
    for edge in path:
        graph[edge[0]][edge[1]] -= found_flow
        if graph[edge[0]][edge[1]] == 0:
            del graph[edge[0]][edge[1]]


def max_flow(graph: Dict[str, Dict[str, int]], start: str, destination: str):

    """
    main function that runs dfs
    and decrease_weight func
    Args:
        graph:dict
        start:str
        destination:str

    Returns:
    max flow after calculation as int

    """
    total_flow = 0
    while True:
        path, found_flow = dfs(graph, start, destination)

        if found_flow == 0:
            break

        total_flow += found_flow
        decrease_weight_on_path(graph, path, found_flow)

    return total_flow
