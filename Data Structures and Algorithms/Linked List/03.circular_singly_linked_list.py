class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr.data == key:
                    prev.next = curr.next
                    curr = curr.next

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count


# creating a circular linked list
cll = CircularSinglyLinkedList()

# appending elements to the list
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

# printing the list
print("Circular Linked List:")
cll.print_list()

# prepending an element to the list
cll.prepend(0)

# printing the list
print("Circular Linked List after prepending 0:")
cll.print_list()

# removing an element from the list
cll.remove(2)

# printing the list
print("Circular Linked List after removing 2:")
cll.print_list()

# checking the length of the list
print("Length of the Circular Linked List:", len(cll))
