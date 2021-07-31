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

    #  Insertion Method in Doubly Linked List
    def insertDLL(self, value, location):
        if self.head == None:
            print("The node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode + 1
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    #  Traversal Method in Doubly Linked List
    def traverseDLL(self):
        if self.head == None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    #  Reverse Traversal Method in Doubly Linked List
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search Method in Doubly Linked List
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"


doublyLL = DlinkedList()
doublyLL.createDLL(3)
doublyLL.insertDLL(0, 0)
doublyLL.insertDLL(1, -1)
doublyLL.insertDLL(2, 1)
doublyLL.insertDLL(3, -1)

print([node.value for node in doublyLL])
print(doublyLL.searchDLL(2))
print(doublyLL.searchDLL(20))
