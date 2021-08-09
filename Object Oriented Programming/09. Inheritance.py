# Python - Object Oriented Programming
# Inheritance allows us to inherit attributes and methods from a parent class
# This is useful because we can create subclasses and get all of the
# functionality of parent class and then we can add or overwrite completely new
# functionality without effecting the parent class.


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


# Creating a new subclass from Employee Class
class Developer(Employee):
    raise_amt = 1.10


developer_1 = Developer("Tom", "Hanks", 50000)
developer_2 = Developer("Ricky", "martin", 60000)

# print(help(Developer))

print(developer_1.email)
print(developer_2.email)

print(developer_1.pay)
developer_1.apply_raise()
print(developer_1.pay)
