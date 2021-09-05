from collections import defaultdict, deque

# BFS - Iteration
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        queue = deque()
        queue.append([(0, [0])])  # appending node and path
        target = len(graph) - 1

        while queue:
            currNode, route = queue.popleft()
            if currNode == target:
                result.append(route)
            else:
                for neighbour in graph[currNode]:
                    queue.append((neighbour, route + [neighbour]))
        return result


# DFS - Iteration
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        stack = [(0, [0])]  # appending node and path
        target = len(graph) - 1
        while stack:
            currNode, route = stack.pop()
            if currNode == target:
                result.append(route)
            else:
                for neighbour in graph[currNode]:
                    stack.append((neighbour, route + [neighbour]))
        return result


# DFS - Recursion
class Solution(object):
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        target = len(graph) - 1

        def get_paths(currNode, route=[]):
            if currNode == target:
                result.append(route + [currNode])
            else:
                route = route + [currNode]
                for neighbour in graph[currNode]:
                    get_paths(neighbour, route)

        get_paths(0, route=[])
        return result
