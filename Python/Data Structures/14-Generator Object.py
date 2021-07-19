values = [x * 2 for x in range(10)]
print(values)

for x in values:
    print(x)

# insted of 10 we have a billion,
# we dont want to store all that into memory.

values = (x * 2 for x in range(10))
print(values)

for x in values:
    print(x)

from sys import getsizeof

values = (x * 2 for x in range(1000000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(values))

# genrator objects don't store all of values in memory
# so we cant get length
