# Python - Object Oriented Programming
# A class method is a method which is bound to the class and not
# the object of the class. They have the access to the state of
# the class as it takes a class parameter that points to the class
# and not the object instance. It can modify a class state that
# would apply across all the instances of the class.

# `Decorators` are very powerful and useful tool in Python since it
# allows programmers to modify the behavior of  function or class.
# Decorators allow us to wrap another function in order to extend the
# behavior of the wrapped function, without permanently modifying it.


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # @classmethod decorator

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Ricky", "Martin", 60000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

employee_1.set_raise_amt(1.06)
print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

Employee.raise_amt = 1.01
print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

employee_1.raise_amt = 1.02
print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")
