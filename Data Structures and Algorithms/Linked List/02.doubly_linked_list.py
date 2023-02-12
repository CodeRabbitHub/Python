class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def add_after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = curr
                return
            curr = curr.next

    def add_before_node(self, key, data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                new_node.prev = prev
                return
            curr = curr.next

    def remove(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                if not curr.next:
                    curr = None
                    self.head = None
                    return
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif curr.data == key:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    return
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    return
            curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            curr.prev = nxt
            prev = curr
            curr = nxt
        self.head = prev


# Creating a linked list
dl_list = DoublyLinkedList()
dl_list.append(1)
dl_list.append(2)
dl_list.append(3)
dl_list.append(4)

# Printing the linked list
print("Original list:")
dl_list.print_list()

# Adding a node after a key
dl_list.add_after_node(2, 5)
print("List after adding 5 after key 2:")
dl_list.print_list()

# Adding a node before a key
dl_list.add_before_node(3, 6)
print("List after adding 6 before key 3:")
dl_list.print_list()

# Removing a node
dl_list.remove(4)
print("List after removing node with key 4:")
dl_list.print_list()

# Reversing the linked list
dl_list.reverse()
print("Reversed list:")
dl_list.print_list()
