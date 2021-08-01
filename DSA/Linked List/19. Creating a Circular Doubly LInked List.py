class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    #  Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        return "The CDLL is created Succesfully"


circularDLL = CDLinkedList()
circularDLL.createCDLL(5)
