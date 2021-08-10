items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

print(list(filter(lambda x: x[1] >= 10, items)))

# filer function takes in a list and an iterable
# the functions returns a boolean value.

x = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda i: i % 2 == 0, x)))
