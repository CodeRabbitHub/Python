# Python - Object Oriented Programming
# In Python, functions are first class objects that means
# that functions in Python can be used or passed as arguments

# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists,..

# 1. Functions as objects


def capitalize(text):
    return text.upper()


print(capitalize("hello"))

bold = capitalize

print(bold("hello"))

# 2. Functions can be passes as arguments to other functions.


def capitalize(text):
    return text.upper()


def miniscule(text):
    return text.lower()


def fontStyle(func):
    style = func("Hi.! This is a test text")
    print(style)


fontStyle(capitalize)
fontStyle(miniscule)

# 3. Functions can return another functions


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
print(add_15(5))
