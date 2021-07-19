print(type(5))
print(type(range(5)))


# All list, dictionaries and tuples are iterables

for i in (1, 2, 3, 4):
    print(i)

dict = {"a": 1, "b": 2, "c": 3}

for i, j in dict.items():
    print(i, j)

for i in [1, 2, 3, 4]:
    print(i)
