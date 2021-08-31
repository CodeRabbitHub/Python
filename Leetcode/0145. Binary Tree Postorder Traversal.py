class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive approach
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: list[int]):
        if not root:
            return
        self.dfs(root.left, result)
        self.dfs(root.right, result)
        result.append(root.val)


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result


# Iterative approach
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]
