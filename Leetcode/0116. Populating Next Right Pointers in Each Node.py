from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Recursive
class Solution:
    def connect(self, root: Node) -> Node:
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root


# BFS - Iteration
class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


# BFS - Iteration (using previously connected next values)
class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            currNode = queue.popleft()
            if currNode.left and currNode.right:
                currNode.left.next = currNode.right
                if currNode.next:
                    currNode.right.next = currNode.next.left
                queue.append(currNode.left)
                queue.append(currNode.right)

        return root


# DFS - Iteration
class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
