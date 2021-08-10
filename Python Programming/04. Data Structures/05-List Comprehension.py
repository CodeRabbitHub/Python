x = list(range(1, 11))
print(x)

# list comprehension can be used for filtering
#  and mapping too

print([i for i in x if i % 2 == 0])  # Filter
print([i ** 2 for i in x])  # map
