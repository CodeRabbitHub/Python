class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        return f"Point({self.x},{self.y})"


point = Point.zero()
print(point.draw())
