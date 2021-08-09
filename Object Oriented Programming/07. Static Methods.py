# Python - Object Oriented Programming
# We have seen that Regular method automatically pass the instance as arguments
# self, Class method automatically pass the class as aurgument cls, Static
# method dont pass anything automatically. so they behave like regular function
# except we include them in class because they have seme logical connection
# with the class.
import datetime


class Employee:

    num_of_empls = 0
    raise_amt = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@Company.com"

        Employee.num_of_empls += 1

    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Constructor
    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str.split("-")
        return cls(firstName, lastName, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Test", "User", 60000)

# checking a day is working day or not
my_date = datetime.date(2019, 11, 2)

print(Employee.is_workday(my_date))
