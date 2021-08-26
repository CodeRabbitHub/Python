class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyNode = ListNode()
        dummyNode.next = head
        prevNode, currNode = dummyNode, dummyNode.next

        while currNode:
            if currNode.val == prevNode.val:
                prevNode.next = currNode.next
            else:
                prevNode = currNode
            currNode = currNode.next

        return dummyNode.next
