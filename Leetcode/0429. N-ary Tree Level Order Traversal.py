from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:

        if not root:
            return root

        result = []

        queue = deque([root])
        while queue:
            tempList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tempList.append(node.val)
                if node.children:
                    queue.extend(node.children)

            result.append(tempList)
        return result
