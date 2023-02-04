# Stacks
# A stack is a data structure that follows the Last In First Out (LIFO) principle.
# This means that the last item to be added to the stack will be the first one to be removed.

# Common methods of a stack:
# 1. push() - Adds an item to the top of the stack.
# 2. pop() - Removes the item from the top of the stack.
# 3. peek() - Returns the item at the top of the stack without removing it.
# 4. is_empty() - Returns True if the stack is empty, otherwise False.

# Use case:
# Imagine you are in a web browser and you navigate to different pages.
# The pages you navigate to are added to the stack, and when you hit the back button, the page at the top of the stack is removed.
# This is a classic example of how a stack is used in the real world.
# Implementing a Stack in Python using a List

# Define the Stack class
class Stack:

    # Initialize an empty stack
    def __init__(self):
        self.stack = []

    # Adds an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # Removes the item from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    # Returns the item at the top of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    # Returns True if the stack is empty, otherwise False
    def is_empty(self):
        return len(self.stack) == 0


# Example usage
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.peek())  # Output: 3
print(my_stack.pop())  # Output: 3
print(my_stack.pop())  # Output: 2
print(my_stack.pop())  # Output: 1
print(my_stack.pop())  # Output: None

# Queues
# A queue is a data structure that follows the First In First Out (FIFO) principle.
# This means that the first item to be added to the queue will be the first one to be removed.

# Common methods of a queue:
# 1. enqueue() - Adds an item to the end of the queue.
# 2. dequeue() - Removes the item from the front of the queue.
# 3. peek() - Returns the item at the front of the queue without removing it.
# 4. is_empty() - Returns True if the queue is empty, otherwise False.

# Use case:
# Imagine you are in a line at a grocery store.
# The people in front of you are added to the queue, and when a cashier becomes available, the person at the front of the queue is served.
# This is a classic example of how a queue is used in the real world.


class Queue:
    # Initialize the queue as an empty list
    def __init__(self):
        self.queue = []

    # Add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Remove the item from the front of the queue
    def dequeue(self):
        # Check if the queue is not empty before removing
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    # Return the item at the front of the queue without removing it
    def peek(self):
        # Check if the queue is not empty before returning the item
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0


# Example usage
queue = Queue()

# Add 3 people to the queue
queue.enqueue("person 1")
queue.enqueue("person 2")
queue.enqueue("person 3")

# Peek at the person at the front of the queue
print(queue.peek())  # Output: person 1

# Remove the person at the front of the queue
queue.dequeue()

# Peek at the person at the front of the queue again
print(queue.peek())  # Output: person 2
