class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CSLinkedList:
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

    #  Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"


circularSLL = CSLinkedList()
circularSLL.createCSLL(1)
print(circularSLL.createCSLL(1))
print([node.value for node in circularSLL])
