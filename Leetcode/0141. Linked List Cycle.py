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


class Solution:
    # slow-fast pointer based solution
    def hasCycle(self, head: ListNode) -> bool:
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
