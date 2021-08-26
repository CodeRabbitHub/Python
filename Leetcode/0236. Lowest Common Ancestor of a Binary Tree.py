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
