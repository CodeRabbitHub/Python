# Introduction to Exception Handling in Python

# Exceptions are errors that occur during the execution of a program. They can be handled to prevent the program from crashing and allow it
# to continue running even if an error occurs.

# Handling Exceptions

# The most basic way to handle exceptions in Python is using a try-except block.

# Example: Handling a Divide by Zero Exception
try:
    # Division operation that might raise an exception
    result = 5 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")

# Multiple Exceptions
# You can handle multiple exceptions in the same try-except block by specifying multiple exception types in the except clause.

try:
    # Division operation that might raise an exception
    result = 5 / 0
except (ZeroDivisionError, TypeError):
    # Code to handle the exception
    print("You can't divide by zero or perform division with non-numeric types!")

# Cleaning Up After an Exception
# You can use the finally clause to specify code that must be executed no matter what, even if an exception occurs.
# This is useful for cleaning up resources such as files or sockets.

try:
    # Division operation that might raise an exception
    result = 5 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")
finally:
    # Clean up code
    print("Cleaning up...")

# Raising Exceptions
# You can raise an exception in your code using the raise statement.
# This allows you to signal that an error has occurred and force the program to stop executing.

# Example: Raising a ValueError Exception
def divide(a, b):
    if b == 0:
        raise ValueError("You can't divide by zero!")
    return a / b


try:
    result = divide(5, 0)
except ValueError as e:
    print(e)

# Conclusion
# Exception handling is an essential part of writing robust and maintainable code.
# It allows you to handle errors in a graceful manner and continue executing your program even if an error occurs.
# With the try-except, finally, with, and raise statements, you can handle exceptions, clean up resources, and raise your own exceptions.
