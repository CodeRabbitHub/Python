class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element is:", stack.peek())
print("Stack elements after push:", stack.stack)
print("Popped element is: ", stack.pop())
print("Stack elements after pop:", stack.stack)
