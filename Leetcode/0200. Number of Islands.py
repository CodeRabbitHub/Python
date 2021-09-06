from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        # If grid is empty
        if not grid:
            return 0

        # no. of rows and columns in grid
        ROWS, COLS = len(grid), len(grid[0])

        visit = set(0)

        # counting number of islands
        islands = 0

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROWS)
                        and c in range(COLS)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        queue.append((r, c))
                        visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
