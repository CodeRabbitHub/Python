# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(cur):
            if not cur:
                return None
            if cur == p or cur == q:
                return cur
            left = dfs(cur.left)
            right = dfs(cur.right)
            if left and right:
                return cur
            return left if left else right

        return dfs(root)
