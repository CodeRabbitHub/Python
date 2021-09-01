class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root, root)

    def isMirror(self, t1: TreeNode, t2: TreeNode):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return (
            t1.val == t2.val
            and self.isMirror(t1.right, t2.left)
            and self.isMirror(t1.left, t2.right)
        )


# Iteration
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            curr = stack.pop()
            left, right = curr[0], curr[1]
            if not left and not right:
                continue
            if not left and right or not right and left or left.val != right.val:
                return False
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        return True
