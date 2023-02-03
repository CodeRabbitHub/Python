class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle("Rectangle", 10, 20)
circ = Circle("Circle", 5)

print(f"{rect.name} has an area of {rect.area()}")
print(f"{circ.name} has an area of {circ.area()}")


"""
Subclassing is a key concept in object-oriented programming (OOP), and it refers to creating a new class based on an existing class, 
inheriting all its attributes and methods. In Python, you can use the super function to call the parent class's methods from the child class.

In this example:

Shape is a class that defines a name attribute and an area method that returns 0.
Rectangle is a subclass of Shape. It has its own implementation of the __init__ method that sets the name, width, and height attributes, 
and an implementation of the area method that calculates the area of the rectangle. The super().__init__(name) call is used to initialize 
the name attribute of the parent class.
Circle is a subclass of Shape. It has its own implementation of the __init__ method that sets the name and radius attributes, 
and an implementation of the area method that calculates the area of the circle. The super().__init__(name) call is used to initialize the 
name attribute of the parent class.
rect = Rectangle("Rectangle", 10, 20) creates an instance of the Rectangle class, with the name "Rectangle" and dimensions 10 x 20.
circ = Circle("Circle", 5) creates an instance of the Circle class, with the name "Circle" and radius 5.

The output of this code will be:

    Rectangle has an area of 200
    Circle has an area of 78.5

This example demonstrates the use of super to initialize the attributes of the parent class, and how subclasses can override methods to provide custom behavior. 
The use of inheritance and subclassing allows us to reuse code and build upon existing functionality to create more specialized classes.
"""
