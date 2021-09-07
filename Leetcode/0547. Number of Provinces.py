class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        # Find the number of vertices
        N = len(isConnected)

        # create space for storing root and rank
        root = [i for i in range(N)]
        rank = [1] * N

        # Path Compression Optimization for find function.
        # After finding the root node, we can update the parent node
        # of all traversed elements to their root node.

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        # union by rank, we choose the root node of the vertex with a larger `rank`
        # We will merge the shorter tree under the taller tree and assign the root
        # node of the taller tree as the root node for both vertices.

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1

        # Joining the vertices
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    x = find(i)
                    y = find(j)
                    if x != y:
                        union(x, y)

        # Finding the roots
        for i in range(N):
            find(i)

        # Number of roots present
        return len(set(root))
