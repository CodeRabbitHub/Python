class Circle:
    pi = 3.14

    @staticmethod
    def calc_area(radius):
        return Circle.pi * radius**2

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.calc_area(self.radius)


def shape_area(shape, radius):
    return shape.calc_area(radius)


circle = Circle(5)
print(f"Circle area using instance method: {circle.area()}")

# Use calc_area as a static method
print(f"Circle area using static method: {Circle.calc_area(5)}")

# Use shape_area as a first-class function
print(f"Circle area using first-class function: {shape_area(Circle, 5)}")

"""
Static methods in object-oriented programming (OOP) are methods that belong to a class, rather than to an instance of a class. 
They are defined using the @staticmethod decorator in Python, and they do not receive any arguments that refer to the instance or the class.
Static methods are often used to define utility functions that perform some specific task and do not depend on the state of the instances or the class itself.

In this example:

+ pi is a class variable that holds the value of Pi.
+ @staticmethod decorator is used to define a static method calc_area, which calculates the area of a circle given its radius.
+ __init__ method is a constructor that sets the radius attribute of the instance.
+ area method is an instance method that uses the calc_area static method to calculate the area of the circle.
+ shape_area is a first-class function that takes two arguments: shape and radius. It returns the result of calling shape.calc_area(radius).
+ circle is an instance of the Circle class with a radius of 5.
+ print(f"Circle area using instance method: {circle.area()}") prints the area of the circle calculated using the instance method.
+ print(f"Circle area using static method: {Circle.calc_area(5)}") prints the area of the circle calculated using the static method.
+ print(f"Circle area using first-class function: {shape_area(Circle, 5)}") prints the area of the circle calculated using the first-class function shape_area.
+ This example demonstrates how static methods and first-class functions can be used to encapsulate logic and reuse it in multiple places.

"""
