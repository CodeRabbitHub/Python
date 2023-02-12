class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.data)
            curr = curr.next
        print(curr.data)

    def add_after_node(self, key, data):
        curr = self.head
        while curr.next != self.head:
            if curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = curr
                return
            curr = curr.next
        if curr.data == key:
            self.append(data)

    def add_before_node(self, key, data):
        curr = self.head
        while curr.next != self.head:
            if curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                new_node.prev = prev
                return
            curr = curr.next
        if curr.data == key:
            self.prepend(data)

    def remove(self, key):
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            self.head.prev = curr
        else:
            curr = self.head
            while curr.next != self.head:
                if curr.data == key:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    return
                curr = curr.next
            if curr.data == key:
                prev = curr.prev
                prev.next = self.head
                self.head.prev = prev
                curr.next = None
                curr.prev = None


# Create an instance of the CircularDoublyLinkedList class
cdll = CircularDoublyLinkedList()

# Append elements to the list
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)

# Print the list
print("Print the list after appending elements:")
cdll.print_list()

# Prepend an element to the list
cdll.prepend(0)

# Print the list after prepending an element
print("\nPrint the list after prepending an element:")
cdll.print_list()

# Add an element after a given node
cdll.add_after_node(2, 5)

# Print the list after adding an element after a node
print("\nPrint the list after adding an element after a node:")
cdll.print_list()

# Add an element before a given node
cdll.add_before_node(4, 6)

# Print the list after adding an element before a node
print("\nPrint the list after adding an element before a node:")
cdll.print_list()

# Remove an element from the list
cdll.remove(0)

# Print the list after removing an element
print("\nPrint the list after removing an element:")
cdll.print_list()
