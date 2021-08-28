class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next:
            return head

        last, curr = None, head
        num_nodes = 0
        while curr:
            last = curr
            curr = curr.next
            num_nodes += 1

        k = k % num_nodes
        if k == 0:
            return head
        else:
            last.next = head
            temp = head
            for _ in range(num_nodes - k - 1):
                temp = temp.next
            tail = temp
            head = temp.next
            tail.next = None
        return head

    # Works but bad implementation
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next:
            return head

        def rotate(head):
            prev, curr = None, head
            while curr and curr.next:
                prev = curr
                curr = curr.next
            curr.next = head
            prev.next = None
            return curr

        curr = head
        for k in range(k):
            curr = rotate(curr)

        return curr
