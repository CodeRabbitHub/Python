class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        if head is not None:
            self.flatten_rec(head)
        return head

    def flatten_rec(self, head):
        curr, tail = head, head
        while curr is not None:
            child = curr.child
            next = curr.next
            if child is not None:
                _tail = self.flatten_rec(child)
                _tail.next = next
                if next is not None:
                    next.prev = _tail
                curr.next = child
                child.prev = curr
                curr.child = None
                curr = tail
            else:
                curr = next
            if curr is not None:
                tail = curr
        return tail
