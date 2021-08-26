class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        right = left = dummy
        for _ in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
