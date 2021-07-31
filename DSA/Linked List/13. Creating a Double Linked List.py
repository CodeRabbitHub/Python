class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #  Creating a Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created Succesfully"


doublyLL = DlinkedList()
print(doublyLL.createDLL(3))
