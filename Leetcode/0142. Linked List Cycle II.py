class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        currNode = head
        while currNode:
            if currNode in s:
                return currNode
            else:
                s.add(currNode)
                currNode = currNode.next
        return None
