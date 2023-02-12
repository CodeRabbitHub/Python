class MultiStack:
    class FullStackException(Exception):
        pass

    def __init__(self, stack_count, default_size):
        self.stack_count = stack_count
        self.default_size = default_size
        self.array = [None] * (stack_count * default_size)
        self.sizes = [0] * stack_count

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise MultiStack.FullStackException("Stack is full")

        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise MultiStack.FullStackException("Stack is full")

        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise MultiStack.FullStackException("Stack is full")

        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.default_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.default_size
        return offset + self.sizes[stack_num] - 1


stack = MultiStack(3, 2)
stack.push(0, 1)
stack.push(0, 2)
stack.push(1, 3)
stack.push(1, 4)
stack.push(2, 5)
stack.push(2, 6)

print("Top element of stack 0:", stack.peek(0))
print("Top element of stack 1:", stack.peek(1))
print("Top element of stack 2:", stack.peek(2))

print("Popped element from stack 0:", stack.pop(0))
print("Popped element from stack 1:", stack.pop(1))
print("Popped element from stack 2:", stack.pop(2))

print("After popping from stack 0:", stack.peek(0))
print("After popping from stack 1:", stack.peek(1))
print("After popping from stack 2:", stack.peek(2))
