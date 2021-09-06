from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        # number of rows and columns in rooms
        ROWS, COLS = len(rooms), len(rooms[0])

        # queue for BFS
        queue = deque()

        # set for storing the coordinates of the room that has been visited
        visited = set()

        # traversing through rooms to find all the gates
        for x in range(ROWS):
            for y in range(COLS):
                if rooms[x][y] == 0:
                    # adding coordinates of the gate to the queue
                    queue.append((x, y))
                    # adding coordinates of the gate to visited
                    visited.add((x, y))

        # marking gates at level 0
        level = 0

        # directions in which adjacent rooms are present
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # LevelOrderTraversal to adjacent rooms using BFS
        while queue:

            # updating level (i.e. distance from gate)
            level += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()

                # visiting all the adjacent rooms
                for dx, dy in directions:
                    x_new, y_new = x + dx, y + dy

                    # ignore rooms if they are out boundary
                    if x_new < 0 or y_new < 0 or x_new == ROWS or y_new == COLS:
                        continue

                    # ignore room if it has been already visited
                    elif (x_new, y_new) in visited:
                        continue

                    # ignore if wall is present
                    elif rooms[x_new][y_new] == -1:
                        continue

                    # mark the room and add it to visited and append it to queue
                    else:
                        rooms[x_new][y_new] = level
                        visited.add((x_new, y_new))
                        queue.append((x_new, y_new))

        # unvisited rooms are by default marked as INF so
        # leave it as it is and return rooms
        return rooms
