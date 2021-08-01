class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, value):
        self.items.append(value)
        print(f"The element {value} is inserted in the end of queue")
        return None

    def dequeue(self):
        if self.isEmpty():
            print("No elements to remove")
            return None
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            print("No elements to peek")
            return
        return self.items[0]

    def delete(self):
        self.items = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(2)
customQueue.enqueue(5)
customQueue.enqueue(9)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
