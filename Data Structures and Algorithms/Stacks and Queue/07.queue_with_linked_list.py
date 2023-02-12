class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    class EmptyQueueException(Exception):
        pass

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def dequeue(self):
        if not self.head:
            raise Queue.EmptyQueueException("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return not self.head

    def peek(self):
        if not self.head:
            raise Queue.EmptyQueueException("Queue is empty")
        return self.head.value


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.peek())  # 3
queue.enqueue(4)
print(queue.is_empty())  # False
print(queue.dequeue())  # 3
print(queue.dequeue())  # 4
print(queue.is_empty())  # True
