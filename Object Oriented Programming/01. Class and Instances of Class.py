"""
Python - Object oriented programming.
Description: We will be learning about Class,
Instances and Instance Attributes 

"""
# Lets start by creating an Employee class.
# Classes cannot be empty so lets add a pass
# statement to our class.


class Employee:
    pass


# Now lets create different instances of our class
# say employee_1 and employee_2. We can also refer
# them as object of Class Employee.

employee_1 = Employee()
employee_2 = Employee()

print(employee_1)
print(employee_2)
print("\n")

# Printing object class shows which class the
# object belongs to and it Memory Location. Lets
# say, now we want to add some attributes to
# our Employee objects say name, pay and email.
# We can do in the following manner.

employee_1.firstName = "Tom"
employee_1.lastName = "Hanks"
employee_1.pay = 50000
employee_1.email = "Tom.Hanks@Company.com"

employee_2.firstName = "Ricky"
employee_2.lastName = "Martin"
employee_2.pay = 60000
employee_2.email = "Ricky.Martin@Company.com"

print(employee_1.email)
print(employee_2.email)
print("\n")

# We see that all employees have the same or common
# attributes for each class objects. defining it
# every time is tedious. Lets look at a better
# method wherein we intialize the class with these
# attributes and variables.
class Employee:
    #  Initialize or (Constructor)
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"


# "__init__" is a reseved method in python classes.
# It is known as a constructor in object oriented concepts.
# This method is called when an object is created from the
# class and it allow the class to initialize the attributes
# of a class. "self" represents the instance of the class


employee_3 = Employee("Robie", "Wills", 55000)
employee_4 = Employee("Michael", "Jordan", 65000)

print(employee_3.email)
print(employee_4.email)
print("\n")

print(f"{employee_3.firstName} {employee_3.lastName}")
print(f"{employee_4.firstName} {employee_4.lastName}")

# Now we have how to create a class and different class
# objects and initalize the class with class attributes.
