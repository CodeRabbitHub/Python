# Given the head of a singly linked list, return the middle node
# of the linked list. If there are two middle nodes, return the second
# middle node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        currNode = head
        count = 0
        while currNode:
            currNode = currNode.next
            count += 1
        middle = count // 2 + 1
        result = head
        for i in range(middle - 1):
            result = result.next
        return result

    # fast and slow pointer
    def middleNode1(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
