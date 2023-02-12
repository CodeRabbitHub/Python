from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        try:
            return self.queue.popleft()
        except IndexError:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())  # 1
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.dequeue())  # 3
print(queue.is_empty())  # True
