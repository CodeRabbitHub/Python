class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        headNode = ListNode()
        pointer = headNode
        carry, suM = 0, 0

        while l1 or l2:
            suM = carry
            if l1:
                suM += l1.val
                l1 = l1.next
            if l2:
                suM += l2.val
                l2 = l2.next

            carry = suM // 10
            s = suM % 10
            pointer.next = ListNode(s)
            pointer = pointer.next

        if carry > 0:
            pointer.next = ListNode(carry)

        return headNode.next
