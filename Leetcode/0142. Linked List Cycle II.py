class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return None

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                seeker = head
                while seeker != slow:
                    slow = slow.next
                    seeker = seeker.next
                return slow
