x = (1,)
y = ()
z = 1, 2, 3

print(type(x))
print(type(y))
print(type(z))

point = (1, 2) * 3
print(point)

point = tuple([1, 2, 3])  # function takes iterable
print(point)
chars = tuple("hello")  # string is iterable
print(chars[0:2])

x, y, z = point  # unpacking
print(x, y, z)

for i in chars:  # iterating
    print(i)

# Tuples are  immutable. i.e we can't add or remove
