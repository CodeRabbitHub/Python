from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # no of rows and columns in grid
        ROWS = len(grid)
        COLS = len(grid[0])

        # directions where adjacent cell can be found
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # if start or end is not open
        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] != 0:
            return -1

        # set up the BFS. add coordinates and distance to queue
        queue = deque([(0, 0, 1)])

        # store all the visited cells
        visited = set((0, 0))

        # Do the BFS.
        while queue:
            x, y, distance = queue.popleft()

            # if end is encountered
            if (x, y) == (ROWS - 1, COLS - 1):
                return distance

            # visiting all the adjacent cells
            for dx, dy in directions:
                x_new, y_new = x + dx, y + dy

                # ignore cell if out of boundary
                if x_new < 0 or y_new < 0 or x_new == ROWS or y_new == COLS:
                    continue

                # ignore cell if already visited
                if (x_new, y_new) in visited:
                    continue

                # add new cell to visited
                visited.add((x_new, y_new))

                # if cell is in path append it to queue
                if grid[x_new][y_new] == 0:
                    queue.append((x_new, y_new, distance + 1))

        # if we dont reach the end of the grid in clear path
        return -1
