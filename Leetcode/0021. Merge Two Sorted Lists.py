# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        currNode = head

        while l1 and l2:
            if l1.val < l2.val:
                currNode.next = l1
                l1 = l1.next
            else:
                currNode.next = l2
                l2 = l2.next
            currNode = currNode.next

        currNode.next = l1 or l2
        return head.next


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))


s = Solution()

result = s.mergeTwoLists(l1, l2)

while result:
    print(result.val)
    result = result.next
