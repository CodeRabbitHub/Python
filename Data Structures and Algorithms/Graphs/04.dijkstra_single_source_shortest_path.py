import heapq
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        min_heap = [(0, src)]
        heapq.heapify(min_heap)

        while min_heap:
            u_dist, u = heapq.heappop(min_heap)
            if u_dist > dist[u]:
                continue

            for v, weight in self.graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return dist


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)
s = 0

print("Following are the distances from the vertex", s)
dist = g.dijkstra(s)
for i in range(9):
    print("Vertex", i, "is at distance", dist[i], "from the source vertex", s)
