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

    # Insertion Method in Circular Doubly Linked List
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
            if location  == -1:
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
                tempNode.next= newNode
            return "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    def traverseCDLL(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail.next:
                    break
                tempNode = tempNode.next

        def searchCDLL(self, value):
            if self.head is None:

                    
            




