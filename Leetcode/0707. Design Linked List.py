class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        # index steps needed
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # index is greater than size of the list
        # then it will not be inserted
        if index > self.size:
            return

        # if index is less than zero it'll be inserted
        # at the head of the list

        if index < 0:
            index = 0

        # finding the predecessor of the node where
        # the node has to be added
        pred = self.head

        # returns'(i-1)'th as predecessor if we are adding
        # 'i'th node
        for _ in range(index):
            pred = pred.next

        # linking chains for addition
        newNode = ListNode(val)
        newNode.next = pred.next
        pred.next = newNode

        # incrementing the size after addition
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        # finding predecessor of the node to be deleted
        pred = self.head

        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next

        # decresing the size after removing
        self.size -= 1
