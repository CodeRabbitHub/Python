from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# BFS - Iteration
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        hashmap = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        while queue:
            currNode = queue.popleft()
            for neighbour in currNode.neighbors:
                if neighbour not in hashmap:
                    queue.append(neighbour)
                    hashmap[neighbour] = Node(neighbour.val)
                hashmap[currNode].neighbors.append(hashmap[neighbour])
        return hashmap[node]


# DFS - Iteration
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        hashmap = {node: Node(node.val)}
        stack = [node]
        while stack:
            currNode = stack.pop()
            for neighbour in currNode.neighbors:
                if neighbour not in hashmap:
                    stack.append(neighbour)
                    hashmap[neighbour] = Node(neighbour.val)
                hashmap[currNode].neighbors.append(hashmap[neighbour])
        return hashmap[node]


# DFS - Recursion
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        hashmap = {node: Node(node.val)}

        def dfs(node, hashmap):
            for neighbour in node.neighbors:
                if neighbour not in hashmap:
                    hashmap[neighbour] = Node(neighbour.val)
                    dfs(neighbour, hashmap)
                hashmap[node].neighbors.append(hashmap[neighbour])

        dfs(node, hashmap)
        return hashmap[node]
