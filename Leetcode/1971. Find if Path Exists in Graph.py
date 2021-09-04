from collections import defaultdict, deque

# BFS - Solution
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        queue = deque()
        queue.append(start)
        visited = set()

        while queue:
            currNode = queue.popleft()
            if currNode == end:
                return True
            visited.add(currNode)
            for neighbour in graph[currNode]:
                if neighbour not in visited:
                    queue.append(neighbour)
        return False


# DFS - Solution
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        def dfs(currNode):
            if currNode == end:
                return True
            visited.add(currNode)
            for neighbour in graph[currNode]:
                if neighbour not in visited and dfs(neighbour):
                    return True
            return False

        return dfs(start)
