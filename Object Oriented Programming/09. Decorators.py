# Python - Object Oriented Programming
# Decorators are very powerful and useful tool in Python
# since it allows programmers to modify the behavior of
# function or class. Decorators allow us to wrap another
# function in order to extend the behavior of the wrapped
# function, without permanently modifying it.


def divide(x, y):
    return x / y


print(divide(4, 2))
print(divide(2, 4))
print("\n")

# We notice we have different answers. What if we want to
# write a program that divides larger number with smaller
# number irrespective or position in which it is passed.

# Function Decorators
class smartMath:
    def smart(func):
        def check_func(x, y):
            if x < y:
                x, y = y, x
            return func(x, y)

        return check_func

    @smart
    def divide(x, y):
        return x / y


print(smartMath.divide(2, 4))


# Class Decorators
class smartMath:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, y):
        if x < y:
            x, y = y, x
        return self.func(x, y)


@smartMath
def subtract(x, y):
    return x / y


print(subtract(2, 4))
