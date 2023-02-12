class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element is:", stack.peek())
print("Popped element is: ", stack.pop())
print("Stack elements:")
temp = stack.head
while temp is not None:
    print(temp.data)
    temp = temp.next
