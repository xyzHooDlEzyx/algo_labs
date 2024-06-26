def islands_count(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = list()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            x, y = queue.pop(0)
            dirs = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
                [1, 1],
                [-1, -1],
                [1, -1],
                [-1, 1],
            ]

            for dx, dy in dirs:
                r, c = x + dx, y + dy
                if (
                    r in range(rows)
                    and c in range(cols)
                    and grid[r][c] == "1"
                    and (r, c) not in visited
                ):
                    queue.append((r, c))
                    visited.add((r, c))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                bfs(row, col)
                islands += 1
    return islands
