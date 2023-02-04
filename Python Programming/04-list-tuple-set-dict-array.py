# Lists
# Lists are mutable, ordered collections of items
# Defining a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing elements in a list
print(fruits[0])  # Output: 'apple'

# Modifying elements in a list
fruits[0] = "orange"
print(fruits)  # Output: ['orange', 'banana', 'cherry']

# Adding elements to a list
fruits.append("grapes")
print(fruits)  # Output: ['orange', 'banana', 'cherry', 'grapes']

# Removing elements from a list
fruits.remove("banana")
print(fruits)  # Output: ['orange', 'cherry', 'grapes']

# Finding the length of a list
print(len(fruits))  # Output: 3

# Sorting a list
fruits.sort()
print(fruits)  # Output: ['cherry', 'grapes', 'orange']

# Reversing a list
fruits.reverse()
print(fruits)  # Output: ['orange', 'grapes', 'cherry']

# Using sorted method to sort the list
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['cherry', 'grapes', 'orange']

# Inserting an element at a specific index
fruits.insert(1, "mango")
print(fruits)  # Output: ['orange', 'mango', 'grapes', 'cherry']

# Extending a list with another list
fruits_2 = ["peach", "plum"]
fruits.extend(fruits_2)
print(fruits)  # Output: ['orange', 'mango', 'grapes', 'cherry', 'peach', 'plum']

# Removing the last element from a list
fruits.pop()
print(fruits)  # Output: ['orange', 'mango', 'grapes', 'cherry', 'peach']

# Removing an element at a specific index
fruits.pop(1)
print(fruits)  # Output: ['orange', 'grapes', 'cherry', 'peach']

# Checking if an element is in a list
print("cherry" in fruits)  # Output: True
print("kiwi" in fruits)  # Output: False

# Counting the number of occurrences of an element in a list
print(fruits.count("cherry"))  # Output: 1

# Index of an element in a list
print(fruits.index("cherry"))  # Output: 2

# List Operations

# Concatenation
fruits1 = ["kiwi", "pear"]
fruits2 = fruits + fruits1
print(fruits2)  # Output: ['mango', 'grapes', 'cherry', 'orange', 'kiwi', 'pear']

# Repetition
fruits3 = fruits * 3
print(
    fruits3
)  # Output: ['mango', 'grapes', 'cherry', 'orange', 'mango', 'grapes', 'cherry', 'orange', 'mango', 'grapes', 'cherry', 'orange']

# Looping
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# date
# elderberry

for i, fruit in enumerate(fruits):
    print(i, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
# 3 date
# 4 elderberry

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# Output:
# 0 apple
# 1 banana
# 2 cherry
# 3 date
# 4 elderberry

# List Comprehensions are a concise way of creating lists
squared = [x**2 for x in range(10)]
print(squared)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tuples

# Tuples are immutable, ordered collections of items
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry')

# Accessing Tuple Elements
print(fruits_tuple[0])  # Output: apple
# Accessing elements from the end
print(fruits_tuple[-1])  # Output: cherry
# Accessing a range of elements
print(fruits_tuple[0:2])  # Output: apple, banana

# Tuple Methods
# Tuples do not support item assignment
# but they have some useful methods like count and index
print(fruits_tuple.count("apple"))  # Output: 1
print(fruits_tuple.index("banana"))  # Output: 1

# Swapping two variables
a, b = 5, 10

# Using a temporary variable
temp = a
a = b
b = temp
print(a, b)  # 10 5

# Using tuple for unpacking
a, b = b, a
print(a, b)  # 5 10

# Sets

# Sets are a collection of unique elements. Sets are unordered,
# meaning that the items have no index and do not come in any particular order

# Definition
fruits_set = {"apple", "banana", "cherry"}
fruits_set2 = set(["banana", "cherry", "dragonfruit"])

# Union
fruits_set_union = fruits_set.union(fruits_set2)
print(fruits_set_union)  # Output: {'apple', 'banana', 'cherry', 'dragonfruit'}

# Intersection
fruits_set_intersection = fruits_set.intersection(fruits_set2)
print(fruits_set_intersection)  # Output: {'apple', 'banana', 'cherry'}

# Difference
fruits_set_difference = fruits_set.difference(fruits_set2)
print(fruits_set_difference)  # Output: {'apple'}

# Symmetric Difference
fruits_set_symmetric_difference = fruits_set.symmetric_difference(fruits_set2)
print(fruits_set_symmetric_difference)  # Output: {'apple', 'dragonfruit'}

# Subset
print(fruits_set.issubset(fruits_set_union))  # Output: True

# Superset
print(fruits_set_union.issuperset(fruits_set))  # Output: True

# Frozen Set
frozen_fruits_set = frozenset(fruits_set)
print(frozen_fruits_set)  # Output: frozenset({'banana', 'cherry', 'apple'})


# Dictionaries
# Dictionaries are unordered collections of key-value pairs
# Dictionary of Fruits
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Clear Method
print(
    "Before clear:", fruits_dict
)  # Before clear: {'apple': 1, 'banana': 2, 'cherry': 3}
fruits_dict.clear()
print("After clear:", fruits_dict)  # After clear: {}

# Copy Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
fruits_dict_copy = fruits_dict.copy()
print(
    "Copy of fruits_dict:", fruits_dict_copy
)  # Copy of fruits_dict: {'apple': 1, 'banana': 2, 'cherry': 3}

# Get Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print("Value of 'apple':", fruits_dict.get("apple"))  # Value of 'apple': 1
print(
    "Value of 'peach':", fruits_dict.get("peach", "not found")
)  # Value of 'peach': not found

# Items Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(
    "Items in fruits_dict:", fruits_dict.items()
)  # Items in fruits_dict: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])

# Keys Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(
    "Keys in fruits_dict:", fruits_dict.keys()
)  # Keys in fruits_dict: dict_keys(['apple', 'banana', 'cherry'])

# Pop Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print("Value of 'apple':", fruits_dict.pop("apple"))  # Value of 'apple': 1
print(
    "fruits_dict after pop:", fruits_dict
)  # fruits_dict after pop: {'banana': 2, 'cherry': 3}

# Update Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
new_fruits = {"peach": 4, "orange": 5}
fruits_dict.update(new_fruits)
print(
    "fruits_dict after update:", fruits_dict
)  # fruits_dict after update: {'apple': 1, 'banana': 2, 'cherry': 3, 'peach': 4, 'orange': 5}

# Values Method
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(
    "Values in fruits_dict:", fruits_dict.values()
)  # Values in fruits_dict: dict_values([1, 2, 3])

# Length
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(
    "Number of items in fruits_dict:", len(fruits_dict)
)  # Number of items in fruits_dict: 3

# Dictionary of Fruits
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}

# String Representation
print(
    "String representation of fruits_dict:", str(fruits_dict)
)  # String representation of fruits_dict: {'apple': 1, 'banana': 2, 'cherry': 3}

# Dictionary of Fruits
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Loop through dictionary using keys
print("Loop through dictionary using keys:")
for fruit in fruits_dict.keys():
    print(fruit)
# Output:
# Loop through dictionary using keys:
# apple
# banana
# cherry

# Loop through dictionary using items
print("Loop through dictionary using items:")
for fruit, value in fruits_dict.items():
    print(fruit, value)
# Output:
# Loop through dictionary using items:
# apple 1
# banana 2
# cherry 3

# Dictionary Comprehension
fruits_dict_squared = {fruit: value**2 for fruit, value in fruits_dict.items()}
print(
    "Fruits dictionary squared:", fruits_dict_squared
)  # Fruits dictionary squared: {'apple': 1, 'banana': 4, 'cherry': 9}


# Import the array module
from array import array

# Creating an array
numbers = array("i", [1, 2, 3, 4, 5])
print("Numbers Array:", numbers)  # Numbers Array: array('i', [1, 2, 3, 4, 5])

# Creating a list
numbers_list = [1, 2, 3, 4, 5]
print("Numbers List:", numbers_list)  # Numbers List: [1, 2, 3, 4, 5]

# The main difference between arrays and lists is that arrays are more memory-efficient, as they store elements of the same type.
# Lists, on the other hand, are more flexible as they can store elements of different types.

# Arrays are used when memory efficiency is important, for example when working with large data sets or when processing large amounts of numerical data.
# Lists are used when the elements are of different data types and when there is a need for more flexibility, such as when working with smaller data sets
# or when storing a mix of numerical and non-numerical data.

# Another difference is that arrays have a more limited set of operations compared to lists, but they are faster for mathematical operations.
# Lists, on the other hand, have a wider set of operations, but are slower for mathematical operations.

# To summarize, the choice between arrays and lists depends on the specific use case and the requirements for memory efficiency, flexibility, and processing speed.


# Import the array module
from array import array

# Creating an array
numbers = array("i", [1, 2, 3, 4, 5])
print("Numbers Array:", numbers)  # Numbers Array: array('i', [1, 2, 3, 4, 5])

# Accessing elements
print("First element of numbers:", numbers[0])  # First element of numbers: 1

# Modifying elements
numbers[0] = 10
print(
    "Numbers Array after modification:", numbers
)  # Numbers Array after modification: array('i', [10, 2, 3, 4, 5])

# Slicing an array
print("Sliced Array:", numbers[1:3])  # Sliced Array: array('i', [2, 3])

# Adding elements to an array
numbers.append(6)
print(
    "Numbers Array after adding elements:", numbers
)  # Numbers Array after adding elements: array('i', [10, 2, 3, 4, 5, 6])

# Removing elements from an array
numbers.pop(3)
print(
    "Numbers Array after removing elements:", numbers
)  # Numbers Array after removing elements: array('i', [10, 2, 3, 5, 6])

# Finding the length of an array
print("Length of numbers Array:", len(numbers))  # Length of numbers Array: 5

# Converting an array to a list
numbers_list = numbers.tolist()
print(
    "Numbers Array converted to list:", numbers_list
)  # Numbers Array converted to list: [10, 2, 3, 5, 6]
