from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = deque()
        depth = 1
        queue.append(root)
        while queue:
            for _ in len(queue):
                node = queue.popleft()
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
