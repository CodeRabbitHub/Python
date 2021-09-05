class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):

        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
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

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

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
