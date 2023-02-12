import queue


class Queue:
    def __init__(self):
        self.queue = queue.Queue()

    def enqueue(self, value):
        self.queue.put(value)

    def dequeue(self):
        try:
            return self.queue.get(block=False)
        except queue.Empty:
            raise queue.Empty("Queue is empty")

    def is_empty(self):
        return self.queue.empty()

    def peek(self):
        if self.is_empty():
            raise queue.Empty("Queue is empty")
        return self.queue.queue[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.dequeue())  # Output: 3

try:
    q.dequeue()
except queue.Empty as e:
    print(e)  # Output: "Queue is empty"
