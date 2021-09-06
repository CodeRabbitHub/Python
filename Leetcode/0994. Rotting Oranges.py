from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        # no. of rows and cols in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # checking if grid is empty
        if ROWS == 0:
            return -1

        # queue for BFS
        queue = deque()

        # keeping count of fresh oranges
        fresh_oranges = 0

        # visiting each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    # adding all the rotten orange coordinates to queue
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    # updating count of fresh oranges
                    fresh_oranges += 1

        # all possible directions in which adjacent cell can be found
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # keeping track of the time
        minutes_elapsed = 0

        # If there are rotten oranges in the queue and there are still
        # fresh oranges in the grid keep looping
        while queue and fresh_oranges > 0:

            # updating the minutes elapsed
            minutes_elapsed += 1

            # process rotten oranges on the current level
            for _ in range(len(queue)):
                x, y = queue.popleft()

                # visiting all the adjacent cells
                for dx, dy in directions:
                    x_new, y_new = x + dx, y + dy
                    # ignore cells if they are out of grid boundary
                    if x_new < 0 or x_new == ROWS or y_new < 0 or y_new == COLS:
                        continue
                    # ignore cells if its empty or visited before
                    if grid[x_new][y_new] == 0 or grid[x_new][y_new] == 2:
                        continue
                    # mark the fresh orange as rotted
                    grid[x_new][y_new] = 2
                    # update the fresh orange count
                    fresh_oranges -= 1
                    # add the current rottten to queue

                    queue.append((x_new, y_new))
        # return the time taken for all the fresh orages to become rotten
        # if there are leftover fresh oranges (that means there were no adjacent
        # rotten oranges to make them rotten) return -1
        return minutes_elapsed if fresh_oranges == 0 else -1
