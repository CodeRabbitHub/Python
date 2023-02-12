class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next


llist = LinkedList()

# Append elements to the linked list
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

# Print the list
print("Linked List after appending elements:")
llist.print_list()

# Prepend an element to the start of the list
llist.prepend(0)

# Print the list
print("\nLinked List after prepending an element:")
llist.print_list()

# Insert an element after a specific node
llist.insert_after_node(llist.head.next, 5)

# Print the list
print("\nLinked List after inserting an element:")
llist.print_list()

# Delete an element with a specific key
llist.delete_node(5)

# Print the list
print("\nLinked List after deleting an element:")
llist.print_list()

# Delete an element at a specific position
llist.delete_node_at_pos(2)

# Print the list
print("\nLinked List after deleting an element at position:")
llist.print_list()

# Find the length of the list iteratively
print("\nLength of the linked list (iteratively):", llist.len_iterative())

# Find the length of the list recursively
print("Length of the linked list (recursively):", llist.len_recursive(llist.head))
