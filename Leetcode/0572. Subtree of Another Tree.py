# Given the roots of two binary trees root and subRoot, return true if there is a
# subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of
# this node's descendants. The tree tree could also be considered as a subtree of itself.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None:
            return False
        elif self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )

    def isSame(self, x, y):
        if not x and not y:
            return True
        elif not x or not y:
            return False
        return (
            x.val == y.val
            and self.isSame(x.left, y.left)
            and self.isSame(x.right, y.right)
        )
