class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.count = 0
        self.maxSize = k
        self.start = -1
        self.end = -1

    def enQueue(self, value: int) -> bool:
        if self.count == self.maxSize:
            return False
        else:
            if self.end == -1:
                self.end = self.start = 0
            else:
                self.end = (self.end + 1) % self.maxSize
            self.queue[self.end] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.queue[self.start] = None
            if self.start == self.end:
                self.start = self.end = -1
            else:
                self.start = (self.start + 1) % self.maxSize
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxSize
