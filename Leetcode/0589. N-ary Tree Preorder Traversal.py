class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Iterative
class Solution:
    def preorder(self, root: Node) -> list[int]:
        if root is None:
            return []

        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output


# Recursive
class Solution(object):
    def preorder(self, root: Node) -> list[int]:
        output = []
        self.dfs(root, output)
        return output

    def dfs(self, root, output):
        if root is None:
            return
        output.append(root.val)
        for child in root.children:
            self.dfs(child, output)
