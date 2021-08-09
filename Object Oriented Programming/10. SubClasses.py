# Python - Object Oriented Programming
# Sometimes we need to initiate our subclasses with more information than our
# parent class can handle. Lets say we want to pass on main programming lang
# as an attribute but currently our Employee Class accepts only 3 attributes
# namely first, last and pay


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


# Creating a developer class which has prog_language as
# attribute.
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# Creating a manager class which has employees attribute
# which is a list of employees he handles.
class Manger(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


developer_1 = Developer("Tom", "Hanks", 50000, "Python")
developer_2 = Developer("Ricky", "Martin", 60000, "Java")

manager_1 = Manger("Susan", "Smith", 90000, [developer_1])

print(developer_1.email)
print(developer_1.prog_lang)
print("\n")

print(manager_1.email)
print(manager_1.print_emps())
print("\n")

manager_1.add_emp(developer_2)
print(manager_1.print_emps())
print("\n")

manager_1.remove_emp(developer_1)
print(manager_1.print_emps())
print("\n")

# Is instance function

print(isinstance(manager_1, Manger))
print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))
print("\n")

# Is subclasses function

print(issubclass(Developer, Employee))
print(issubclass(Manger, Employee))
print(issubclass(Manger, Developer))
