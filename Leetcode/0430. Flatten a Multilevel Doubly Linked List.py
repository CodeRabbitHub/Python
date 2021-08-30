from collections import deque


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# DFS - Iteration
class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return None
        pseudoHead = Node(None, None, head, None)
        stack = deque()
        stack.append(head)
        prev = pseudoHead
        while stack:
            curr = stack.pop()
            curr.prev = prev
            prev.next = curr
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        pseudoHead.next.prev = None
        return pseudoHead.next


# DFS - Recursive
class Solution:
    def flatten(self, head):
        if not head:
            return head

        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        pseudoHead.next.prev = None
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)
