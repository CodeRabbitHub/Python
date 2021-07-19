items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# lambda parameters:expression

items.sort(key=lambda item: item[1])
print(items)

x = ["lion", "tiger", "fox", "elephant"]
x.sort(key=len)
print(x)

# key takes and function and
# passes each element in the list

x = lambda a, b: a * b
print(x(5, 6))
