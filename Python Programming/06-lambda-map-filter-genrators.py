# Lambda Functions

# Lambda functions, also known as anonymous functions, are small, one-line functions that are defined without a name.
# They are used when you need to pass a function as an argument to another function or return a function as a result.

# Syntax for defining a lambda function
# lambda arguments: expression

# Defining a lambda function to find the square of a number
square = lambda x: x**2
print(square(5))  # 25


# Map Function

# The `map()` function takes a function and an iterable as arguments, and returns a new iterable that is the result of
# applying the function to each element of the original iterable.

# Syntax for map function
# map(function, iterable)

# Example: Using the map function to find the square of a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]


# Filter Function

# The `filter()` function takes a function and an iterable as arguments and returns a new iterable that contains only
# the elements for which the function returns `True`.

# Syntax for filter function
# filter(function, iterable)

# Example: Using the filter function to find even numbers in a list
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Generator Objects

# A generator is an iterable created using a function with a `yield` statement instead of a `return` statement.
# When the function is called, it returns a generator object, which can be iterated over using a for loop.
# Each time the for loop iterates, the generator function runs until it encounters the next `yield` statement.

# Example: Using a generator to generate the squares of numbers
def square_generator(numbers):
    for number in numbers:
        yield number**2


squared_numbers = square_generator([1, 2, 3, 4, 5])
for number in squared_numbers:
    print(number)
# Output:
# 1
# 4
# 9
# 16
# 25
