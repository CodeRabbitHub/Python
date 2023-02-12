class CircularQueue:
    class EmptyQueueException(Exception):
        pass

    class FullQueueException(Exception):
        pass

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, value):
        if (self.tail + 1) % self.size == self.head:
            raise CircularQueue.FullQueueException("Queue is full")
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        if self.head == -1:
            self.head = 0

    def dequeue(self):
        if self.head == -1:
            raise CircularQueue.EmptyQueueException("Queue is empty")
        value = self.queue[self.head]
        self.queue[self.head] = None
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return value

    def peek(self):
        if self.head == -1:
            raise CircularQueue.EmptyQueueException("Queue is empty")
        return self.queue[self.head]

    def is_empty(self):
        return self.head == -1


queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Peek:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Peek:", queue.peek())
