# Python - Object Oriented Programming
# In here we will set attributes first and last name as private
# We can set an attribute private by using single underscore (__)
# That means we cannot modify those attributes from outside the class
# Note: There is nothing really private in python that we cannot access
# We can access all methods and attributes and modify them even though
# are private

# - single underscore: protected (can be accessed and modified)
# - double underscore: private (can be accessed and modified)


class Employee:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    # getter method
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    @property
    def email(self):
        return f"{self.__firstName}.{self.__lastName}@email.com"

    @property
    def fullName(self):
        return f"{self.__firstName} {self.__lastName}"

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(" ")
        self.__firstName = firstName
        self.__lastName = lastName

    @fullName.deleter
    def fullName(self):
        print("Deleted Name!")
        self.__firstName = None
        self.__lastName = None


employee_1 = Employee("John", "Woo")
print(employee_1.fullName)
print(employee_1.email)

# We can access the employee private attributes and modify them
print(employee_1.__dict__)
employee_1._Employee__firstName = "Tom"
print(employee_1._Employee__firstName)
print(employee_1.fullName)

# We can get first name by calling getter method
print(employee_1.getFirstName())

# Modifying employee name by using property setter method
# We can access property methods as attributes without calling
# as functions.
employee_1.fullName = "Steve Jobs"
print(employee_1.fullName)
print(employee_1.email)

# Deleting attributes with property deleter
del employee_1.fullName
print(employee_1.fullName)
