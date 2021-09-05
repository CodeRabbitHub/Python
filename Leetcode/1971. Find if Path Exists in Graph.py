from collections import defaultdict, deque


# BFS - Iteration
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            currNode = queue.popleft()
            if currNode == end:
                return True
            visited.add(currNode)
            for neighbour in adjList[currNode]:
                if neighbour not in visited:
                    queue.append(neighbour)
        return False


# DFS - Recursion
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set()

        def dfs(currNode):
            if currNode == end:
                return True
            visited.add(currNode)
            for neighbour in adjList[currNode]:
                if neighbour not in visited and dfs(neighbour):
                    return True
            return False

        return dfs(start)


# DFS - Iteration
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = [0] * n
        stack = [start]

        while stack:
            currNode = stack.pop()
            if currNode == end:
                return True
            if visited[currNode] == 1:
                continue
            visited[currNode] = 1
            for neighbour in adjList[currNode]:
                if visited[neighbour] == 1:
                    continue
                stack.append(neighbour)

        return False
