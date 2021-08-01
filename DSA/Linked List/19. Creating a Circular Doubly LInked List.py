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

    #  Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                self.head.prev = newNode
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = self.head
                self.head = newNode
            if location == -1:
                self.head.prev = newNode
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"

    #  Traversal of Circular Doubly Linked List
    def traverseCDLL(self):
        if self.head is None:
            return "There is no node to traverse"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    #  Reverse traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
        if self.head is None:
            return "There is no node to traverse"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    #  Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in CDLL to search"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next

    #  Delete a node from Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

    #  Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")


circularDLL = CDLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])
