# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote the
# index of the node that tail's next pointer is connected to. Note that pos is not passed as
# a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Hash set  based solution
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        currNode = head
        while currNode:
            if currNode in s:
                return True
            else:
                s.add(currNode)
            currNode = currNode.next
        return False

    # slow-fast pointer based solution
    def hasCycle2(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
