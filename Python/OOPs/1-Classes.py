# Class: blueprint for creating new objects
# Object: instances of a class

# Class: Human
# Objects: John, Mary, Jack


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
