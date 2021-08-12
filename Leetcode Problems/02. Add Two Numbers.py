# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.


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


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()

result = s.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next
