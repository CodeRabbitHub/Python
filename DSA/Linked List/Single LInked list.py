class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()

print(singlyLinkedList.head)
print(singlyLinkedList.tail)

node1 = Node(1)
node2 = Node(2)

print(node1)

singlyLinkedList.head = node1
singlyLinkedList.tail = node2
singlyLinkedList.head.next = node2

print(singlyLinkedList.head.next.value)
