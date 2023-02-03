class BankAccount:
    # class variable to keep track of the interest rate
    interest_rate = 0.05

    # magic method to define how the object will be represented as a string
    def __repr__(self):
        return f"BankAccount({self.owner}, {self.balance})"

    # magic method to define how two objects should be compared
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    # a class method to change the interest rate for all instances of the class
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    # the constructor
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # a method to calculate and add interest to the balance
    def add_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

    # a getter method to access the balance
    @property
    def balance(self):
        return self._balance

    # a setter method to set the balance
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")

    # a deleter method to delete the balance
    @balance.deleter
    def balance(self):
        del self._balance


# a subclass that adds a new method to the parent class
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        # calling the constructor of the parent class
        super().__init__(owner, balance)
        self.fee = fee

    # a method that subtracts the fee from the balance
    def subtract_fee(self):
        self.balance -= self.fee


# creating an instance of the subclass
c = CheckingAccount("Jane Doe", 1000, 10)

# using the methods and properties of the parent class
print(c.balance)  # 1000
c.balance = 2000
print(c.balance)  # 2000
c.add_interest()
print(c.balance)  # 2100

# using the new method of the subclass
c.subtract_fee()
print(c.balance)  # 2090

# using the class method of the parent class
BankAccount.set_interest_rate(0.10)
c.add_interest()
print(c.balance)  # 2399

# using the magic methods of the parent class
c2 = CheckingAccount("Jane Doe", 1000, 10)
print(c == c2)  # False
print(c)  # BankAccount(Jane Doe, 2399)

# a decorator function that adds a prefix to the method name
def prefix_decorator(func):
    def wrapper(*args, **kwargs):
        return f"Prefix: {func(*args, **kwargs)}"

    return wrapper


# applying the decorator to a method
@prefix_decorator
def test_method(text):
    return text


# using the decorated method
print(test_method("Hello World"))  # Prefix: Hello World
