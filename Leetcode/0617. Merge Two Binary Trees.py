class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        root = TreeNode(val1 + val2)

        root.left = self.mergeTrees(
            root1.left if root1 else 0, root2.left if root2 else 0
        )
        root.right = self.mergeTrees(
            root1.right if root1 else 0, root2.right if root2 else 0
        )
