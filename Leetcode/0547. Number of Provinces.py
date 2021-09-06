class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        numNodes = len(isConnected)
        id = [i for i in range(numNodes)]

        def connected(p, q):
            return id[p] == id[q]

        def union(p, q):
            pid, qid = id[p], id[q]
            for i in range(n):
                if id[i] == qid:
                    id[i] = pid

        for x in range(n):
            for y in range(x + 1, n):
                if isConnected[x][y]:
                    union(x, y)

        return len(set(id))
