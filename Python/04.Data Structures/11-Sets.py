numbers = [1, 1, 4, 4, 5, 2, 6, 7, 2]
uniques = set(numbers)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(uniques)

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # subtraction
print(a ^ b)  # not in both

# sets are not ordered so we cannot access with index
