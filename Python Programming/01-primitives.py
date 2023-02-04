# Integer type
x = 10  # x is an integer type variable with a value of 10
print(type(x))  # Output: <class 'int'>

# Float type
y = 20.5  # y is a float type variable with a value of 20.5
print(type(y))  # Output: <class 'float'>

# String type
z = "Hello, World!"  # z is a string type variable with a value of "Hello, World!"
print(type(z))  # Output: <class 'str'>

# Boolean type
a = True  # a is a boolean type variable with a value of True
print(type(a))  # Output: <class 'bool'>

# Complex type
b = 3 + 4j  # b is a complex type variable with a value of 3 + 4j
print(type(b))  # Output: <class 'complex'>

# Variable Naming Conventions
# 1. Use snake_case for variable names
# 2. Start variable names with a lowercase letter
# 3. Avoid using Python keywords as variable names

# Creating Variables
first_name = "John"  # string type variable
last_name = "Doe"  # string type variable
age = 30  # integer type variable
height = 5.9  # float type variable
is_student = False  # boolean type variable

# String Escape Sequences
# \n: new line
# \t: tab
# \\: backslash

# String Formatting
# 1. Using f-strings (Python 3.6+)
full_name = f"{first_name} {last_name}"
print(f"My name is {full_name}")  # Output: My name is John Doe

# 2. Using .format() method
message = "My name is {} {}".format(first_name, last_name)
print(message)  # Output: My name is John Doe

# 3. Using % operator
message = "My name is %s %s" % (first_name, last_name)
print(message)  # Output: My name is John Doe

# String Methods
# 1. len()
print(
    "Length of string '{}': {}".format(full_name, len(full_name))
)  # Output: Length of string 'John Doe': 8

# 2. lower()
print(
    "Lowercase of string '{}': {}".format(full_name, full_name.lower())
)  # Output: Lowercase of string 'John Doe': john doe

# 3. upper()
print(
    "Uppercase of string '{}': {}".format(full_name, full_name.upper())
)  # Output: Uppercase of string 'John Doe': JOHN DOE

# 4. title()
print(
    "Titlecase of string '{}': {}".format(full_name, full_name.title())
)  # Output: Titlecase of string 'John Doe': John Doe

# 5. find()
sentence = "Hello, World!"
print("'l' found at index:", sentence.find("l"))  # Output: 'l' found at index: 2

# 6. replace()
print(
    "Replaced string '{}': {}".format(full_name, full_name.replace("John", "Jane"))
)  # Output: Replaced string 'John Doe': Jane Doe

# Working with Numbers
# 1. Arithmetic operations
sum = 2 + 3  # Output: sum = 5
difference = 5 - 2  # Output: difference = 3
product = 3 * 4  # Output: product = 12
quotient = 10 / 3  # Output: quotient = 3.333333
modulus = 10 % 3  # Output: modulus = 1

# 2. Comparison operations
is_greater = 5 > 2  # Output: is_greater = True
is_less = 5 < 2  # Output: is_less = False
is_equal = 5 == 2  # Output: is_equal = False
is_not_equal = 5 != 2  # Output: is_not_equal = True

# Number Methods from math module
import math

# 1. floor
print(
    "Floor value of {}: {}".format(3.14, math.floor(3.14))
)  # Output: Floor value of 3.14: 3


# 2. round
print(
    "Rounded value of {}: {}".format(3.14, round(3.14))
)  # Output: Rounded value of 3.14: 3

# 3. abs
print(
    "Absolute value of {}: {}".format(-10, abs(-10))
)  # Output: Absolute value of -10: 10

# 4. ceil
print(
    "Ceiling value of {}: {}".format(3.14, math.ceil(3.14))
)  # Output: Ceiling value of 3.14: 4

# 5. sqrt
print("Square root of {}: {}".format(9, math.sqrt(9)))  # Output: Square root of 9: 3.0
