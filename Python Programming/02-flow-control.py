# Comparing Operators
a = 10
b = 20

# Equality (==)
print("a == b: ", a == b)  # Output: False

# Not Equal (!=)
print("a != b: ", a != b)  # Output: True

# Greater Than (>)
print("a > b: ", a > b)  # Output: False

# Greater Than or Equal (>=)
print("a >= b: ", a >= b)  # Output: False

# Less Than (<)
print("a < b: ", a < b)  # Output: True

# Less Than or Equal (<=)
print("a <= b: ", a <= b)  # Output: True

# Conditional Statements
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")

# Ternary Operator
print("a is less than b" if a < b else "a is not less than b")

# Logical Operators
c = False
d = True

# AND (c and d)
print("c and d: ", c and d)  # Output: False

# OR (c or d)
print("c or d: ", c or d)  # Output: True

# NOT (not c)
print("not c: ", not c)  # Output: True

# Short Circuit Evaluation
print("c or d is True: ", c or d is True)  # Output: True

# Chaining Comparison Operators
e = 50
print(10 < e < 60)  # Output: True

# For Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For-Else Loops
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
        break
else:
    print("No even number found")


# Nested Loops
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    for j in numbers:
        print(i, j)

# Iterables
numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)
print(next(numbers_iter))
print(next(numbers_iter))

# While Loops
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Infinite Loops
# while True:
#     print("Infinite Loop")
