from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSum, levelNodes = 0, len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levelSum / levelNodes)
        return result
