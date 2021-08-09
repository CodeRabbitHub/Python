# Python - Object Oriented Programming
# Class attributes are variables that are shared among all instances
# in the class. Instance variables can be unique for each instances
# line name, email and pay.


class Employee:

    # Creating a class attribute
    raise_amt = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"

    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    # A method where we will raise the pay.
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # we can use Employee.raise_amt as well as self.raise_amt
    # but not raise_amt.


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Test", "User", 60000)

print(f"Employee_1 salary {employee_1.pay}")
employee_1.apply_raise()
print(f"Employee_1 salary after raise {employee_1.pay}")
print("\n")

# We can access the raise amount class variable by calling
print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

# We noticed that we can access the class variable from both the
# class and the instance. As we try to acess an attribute on an
# instance, it first's checks whether the instance has that attribute
# or not, then it will see the class or any class that inherits from
# contains that attribute.
print(employee_1.__dict__)
print(Employee.__dict__)
print("\n")

# Here we can see that the instance does not contain attribute raise_amt
# where as the class contains it.

# Increasing the raise amount of emp_1 from instance and using
# self.raise_amt in the method.

employee_1.raise_amt = 1.05

print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

# Here we can see if we use self.raise_amt we can individually raise the
# amount of each employee by using that instance and raise_amt.
# Also using self here will allow any subclass to overwrite the constant
# if they wanted to.  Lets see another example where we don't want to
# use self in the next section.

Employee.raise_amt = 1.06

print(Employee.raise_amt)
print(employee_1.raise_amt)
print(employee_2.raise_amt)
print("\n")

# When we changed raise amount using class we see that the employee_1
# raise amount is stil 1.05 instead of 1.06
