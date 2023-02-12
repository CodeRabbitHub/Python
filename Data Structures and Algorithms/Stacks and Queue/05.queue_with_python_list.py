class Queue:
    class EmptyQueueException(Exception):
        pass

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise Queue.EmptyQueueException("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Queue.EmptyQueueException("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Peek:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Peek:", queue.peek())
