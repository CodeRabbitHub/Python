def floyd_warshall(graph):
    n = len(graph)
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] is not None:
                distances[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )

    return distances


graph = [
    [0, 3, 8, float("inf"), -4],
    [float("inf"), 0, float("inf"), 1, 7],
    [float("inf"), 4, 0, float("inf"), float("inf")],
    [2, float("inf"), -5, 0, float("inf")],
    [float("inf"), float("inf"), float("inf"), 6, 0],
]

distances = floyd_warshall(graph)

for row in distances:
    print(row)
