class Employee:
    def greet(self):
        print("Employee Greet")


class Manager:
    def greet(self):
        print("Manager Greet")


class Person(Employee, Manager):
    pass


p = Person()
p.greet()

# Changing order in inheritance changes the greet
# Multiple inheritance is good when the two classes
# have  no methods in common.
