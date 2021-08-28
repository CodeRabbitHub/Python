class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = evenHead = head.next

        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            even = even.next
            odd = odd.next

        odd.next = evenHead
        return head
