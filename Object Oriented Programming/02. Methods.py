# Python - Object Oriented Programming
# In the previous section we have created a class
# and initialized it with some  instance attributes.
# We also created some class objects. Now lets look
# on to creating Class Methods.


class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"

    # Here we are creating a `method` named fullName on our class
    # which returns full name of the employee.
    def fullName(self):
        return f"{self.firstName} {self.lastName}"


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Ricky", "Martin", 60000)
employee_3 = Employee("Robie", "Wills", 55000)
employee_4 = Employee("Michael", "Jordan", 65000)

# Printing Employee full name. Notice the '()' in the end. This
# is because we are calling a method not an attribute.
# Without parenthesis it will return the method not the values.
print(employee_1.fullName())
print(employee_2.fullName())

# We can also run these methods using class name itself
print(Employee.fullName(employee_3))
print(Employee.fullName(employee_4))
