from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (self.V)
        distance = [float("inf")] * (self.V)
        queue = []

        distance[s] = 0
        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    distance[i] = distance[s] + 1
                    queue.append(i)
                    visited[i] = True

        return distance


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(3, 7)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(4, 7)
g.add_edge(5, 6)
g.add_edge(6, 7)
s = 0

print("Following is the shortest distance from the vertex", s)
dist = g.bfs(s)
for i in range(8):
    print("Vertex", i, "is at distance", dist[i], "from the source vertex", s)
