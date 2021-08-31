class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive approach
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: list[int]):
        if not root:
            return
        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result


# Iterative approach
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result
