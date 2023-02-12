class FixedSizeStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.size

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Stack is full, can't push more elements")

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


stack = FixedSizeStack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Top element is:", stack.peek())
print("Stack elements after push:", stack.stack)
print("Popped element is: ", stack.pop())
print("Stack elements after pop:", stack.stack)
