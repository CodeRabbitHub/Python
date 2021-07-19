# In python list can have any data types

lst = ["a", "b", 1, [0, 1], (2.3), {"p": 77, "q": 90}, True, False]
print(lst)

zeros = [0] * 5
print(zeros)

matrix = [[0, 1], [2, 3]]
print(matrix)

a = [1, 2]
b = [3, 4]
c = a + b
print(c)

numbers = list(range(20))
print(numbers)

chars = list("Hello")
print(chars)
print(len(chars))

# Accesing Items in List

letters = ["a", "b", "c", "d"]
print(letters)
print(letters[0])

letters[0] = "A"  # Modifying Values
print(letters)

print(letters[0:2])  # slicing

numbers = list(range(20))
print(numbers[::2])

# List unpacking

numbers = [1, 2, 3]
first, second, third = numbers
# the numbers on both side should be equal
print(first)

first, *other = numbers  # packing others in another list
print(other)

first, *other, last = numbers
print(first, last)
print(*other)

# Looping over a list

x = list(range(20, 30, 2))
print(x)

for idx, items in enumerate(x):
    print(idx, items)

# Adding or removing items in list

x.append(44)
print(x)
x.append([1, 2, 3])
print(x)
x = list(range(20, 30, 2))
x.extend([1, 2, 3])  # extends the list
print(x)

x.insert(0, "a")
print(x)
x.pop(0)
print(x)

x.remove(3)  # removes first occurence of 3
print(x)

del x[0:3]
print(x)

x.clear()
print(x)

# Finding items in list

letters = ["a", "b", "c"]

if "d" in letters:
    print(letters.index("d"))

print(letters.count("d"))

# Sorting lists

numbers = [3, 51, 2, 8, 4]
numbers.sort(reverse=True)
print(numbers)  # it has modified the list

print(sorted(numbers))  # new sorted list doesnt modify
print(numbers)

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
