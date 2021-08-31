class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive approach
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: list[int]):
        if not root:
            return
        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result


# Iterative approach
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
