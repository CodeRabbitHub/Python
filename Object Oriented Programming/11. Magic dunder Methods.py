# Python - Object Oriented Programming
# In here we will use special methods, also called as Magic methods.
# Double underscore is called as dunder. We have seen dunder __init__ fuction
# we will see __repr__ and __str__ in here.
# we can also have custom dunder that we can create for performing certain
# tasks as functions.


class Employee:

    raise_amt = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"

    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #  __repr__ is a special method used to represent a class's objects as a string

    def __repr__(self):
        return f"Employee('{self.firstName}', '{self.lastName}', {self.pay})"

    # The __str__ method should be defined in a way that is easy to read
    # and outputs all the members of the class.

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # we can control the result of a sum of two objects by modifying or defying
    # the __add__ method. Takes first object as Self and second as other.

    def __add__(self, other):
        return self.pay + other.pay

    # __len__ as a method you can customize for any object

    def __len__(self):
        return len(self.fullname())


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Ricky", "Martin", 60000)

# Now when we print an object we  get a string output
print(employee_1)
print(str(employee_1))

# The output is string representation of object.
print(repr(employee_1))

print(employee_1.__repr__())
print(employee_1.__str__())

# Returns combined pay of employee_1 and employee_2
print(employee_1 + employee_2)

# Returns length of full name
print(len(employee_1))
