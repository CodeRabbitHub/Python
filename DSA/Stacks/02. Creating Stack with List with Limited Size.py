class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    #  Is Empty
    def isEmpty(self):
        if self.list == []:
            return True
        return False

    #  is Full
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False

    #  Push
    def push(self, value):
        if self.isFull():
            return "The stack is Full"
        self.list.append(value)
        return "The element has been succesfully inserted"

    #  Pop
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        return self.list.pop()

    #  Peek
    def peek(self):
        if self.isEmpty():
            return "There is no elemnet in the stack"
        return self.list[-1]

    #  Delete entire list
    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(customStack.push(5))
print("\n")
customStack.pop()
print(customStack)
print("\n")
print(customStack.peek())
customStack.delete()
