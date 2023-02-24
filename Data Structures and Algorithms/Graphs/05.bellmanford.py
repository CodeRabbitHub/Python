def bellman_ford(graph, source):
    distances = [float("inf")] * len(graph)
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for u, v, w in graph:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in graph:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            return None

    return distances


graph = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3),
]

distances = bellman_ford(graph, 0)

if distances is not None:
    print("Shortest distances from source vertex 0:", distances)
else:
    print("The graph contains a negative weight cycle.")
