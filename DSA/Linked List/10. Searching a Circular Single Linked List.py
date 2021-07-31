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

    #  Insertion of a node in circular singly linked list
    def insertCSLL(self, value, location):
        if self.head == None:
            return "The head refrence is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode + 1
                    index = +1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        return "The node has been succesfully inserted"

    #  Traversal of a node in circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    #  Searching for a node in circular singly linked list
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"


circularSLL = CSLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(2, -1)
circularSLL.insertCSLL(3, 0)
circularSLL.insertCSLL(7, 1)

circularSLL.searchCSLL(3)
