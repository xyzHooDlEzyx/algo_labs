count = 0
visited = set()
graph = {}


def read_input(file_name):
    with open(file_name, "r") as file:
        edges_count = int(file.readline().strip())
        edges_strings = list()
        for _ in range(edges_count):
            line = file.readline().strip()
            group1, group2 = map(int, line.split())
            edges_strings.append((group1, group2))
    # print(z, inp)
    return edges_count, edges_strings


def write_output(file_name, possible_prs):
    with open(file_name, "w") as file:
        file.write(str(possible_prs))


def dfs(node, is_male):
    global count
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            if is_male and neighbour % 2 == 0:
                count += 1
                # print(count)
            elif not is_male and neighbour % 2 != 0:
                count += 1
            dfs(neighbour, not is_male)


def count_pairs(tribes, couples):
    global graph
    graph = {}
    for i in range(1, tribes * 2 + 1):
        graph[i] = []

    for pair in couples:

        x, y = pair
        if x == 0 and y == 0:
            return 0
        else:
            graph[x].append(y)
            graph[y].append(x)

    global visited

    global count

    for i in range(1, tribes * 2 + 1):
        if i not in visited:
            dfs(i, i % 2 != 0)
    return count * 2
