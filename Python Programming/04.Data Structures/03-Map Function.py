items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

prices = []

for item in items:
    prices.append(item[1])

print(prices)

prices = map(lambda x: x[1], items)
print(prices)

for price in prices:
    print(price)

# map function takes a function and iterable
# returns an iterable object

lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, lst)))
