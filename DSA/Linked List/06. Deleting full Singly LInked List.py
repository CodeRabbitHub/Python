class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert in Linked List

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse Singly Linked List

    def traverseList(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node in Singly Linked List

    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The node does not exist in this SLL"

    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    node = node.next
                    if node.next == self.tail:
                        node.next = None
                        self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(3, 0)
singlyLinkedList.insertSLL(4, -1)
singlyLinkedList.insertSLL(5, -1)
singlyLinkedList.insertSLL(7, 2)

print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()

print([node.value for node in singlyLinkedList])
