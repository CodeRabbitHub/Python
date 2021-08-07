# A counter is a sub-class of the dictionary. It is used to keep
# the count of the elements in an iterable in the form of an unordered
# dictionary where the key represents the element in the iterable and
# value represents the count of that element in the iterable.


from collections import Counter

# with a list of items
print(Counter(["B", "B", "A", "B", "C", "A", "B", "B", "A", "C"]))

# with a dictionary
print(Counter({"A": 3, "B": 5, "C": 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))
