# Python - Object Oriented Programming
# Raise can be different for different employees or instances.
# But total number of employees will not be different for any instance.
# so lets create a class variable names num_of employees.
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


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Ricky", "Martin", 60000)

print(Employee.num_of_emps)
