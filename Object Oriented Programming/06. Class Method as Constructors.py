# Python - Object Oriented Programming
# In here we will set a @classmethod 'from_string'
# as a constructor.


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str.split("-")
        return cls(firstName, lastName, pay)


employee_1 = Employee("Tom", "Hanks", 50000)
employee_2 = Employee("Ricky", "Martin", 60000)

# Class methods as alternative constructors

employee_str_3 = "John-Woo-70000"
employee_str_4 = "steve-Jobs-80000"
employee_str_5 = "Mary-Jane-30000"

newEmployee_3 = Employee.from_string(employee_str_3)

print(newEmployee_3.email)
print(newEmployee_3.pay)
