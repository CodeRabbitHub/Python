# Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyNode = ListNode()
        dummyNode.next = head
        prevNode, currNode = dummyNode, dummyNode.next

        while currNode:
            if currNode.val == val:
                prevNode.next = currNode.next
            else:
                prevNode = currNode
            currNode = currNode.next
        return dummyNode.next
