# An OrderedDict is also a sub-class of dictionary but unlike
# dictionary, it remembers the order in which the keys were inserted
# While deleting and re-inserting the same key will push the
# key to the last to maintain the order of insertion of the key

from collections import OrderedDict

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4

for key, value in od.items():
    print(key, value)

print("Before Deleting")
for key, value in od.items():
    print(key, value)

# deleting element
od.pop("a")

# Re-inserting the same
od["a"] = 1

print("\nAfter re-inserting")
for key, value in od.items():
    print(key, value)
