class Solution:

    WHITE = 0
    GRAY = 1
    BLACK = 2

    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)

        return self.leadsToDest(graph, source, destination, [Solution.WHITE] * n)

    def leadsToDest(self, graph, node, dest, states):

        # If the state is GRAY, this is a backward edge and hence, it creates a Loop.
        if states[node] != Solution.WHITE:
            return states[node] == Solution.BLACK

        # If this is a leaf node, it should be equal to the destination.
        if len(graph[node]) == 0:
            return node == dest

        # Now, we are processing this node. So we mark it as GRAY.
        states[node] = Solution.GRAY

        for next_node in graph[node]:

            # If we get a `false` from any recursive call on the neighbors, we short circuit and return from there.
            if not self.leadsToDest(graph, next_node, dest, states):
                return False

        # Recursive processing done for the node. We mark it BLACK.
        states[node] = Solution.BLACK
        return True


from collections import defaultdict


class Solution:
    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:

        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)

        if len(graph[destination]) != 0:
            return False

        visited = set()

        def dfs(node, visited):
            if len(graph[node]) == 0:
                return node == destination
            for neighbor in graph[node]:
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                if not dfs(neighbor, visited):
                    return False
                visited.remove(neighbor)
            return True

        return dfs(source, visited)
