# Import the collections module
import collections

# Counter
# The Counter class takes an iterable object as input and returns a dictionary-like object with the elements of the iterable
# as keys and their count as the corresponding values.

# Example usage
# Count the occurrences of elements in a list
counter = collections.Counter([1, 2, 3, 1, 2, 1, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7])
print("Counter result:", counter)

# OrderedDict
# An OrderedDict is a subclass of the built-in dict class that maintains the order of elements in the dictionary. The elements
# in an OrderedDict are stored in the order in which they were added.

# Example usage
# Create an ordered dictionary with key-value pairs
ordered_dict = collections.OrderedDict(
    [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
)
print("OrderedDict:", ordered_dict)

# DefaultDict
# A DefaultDict is a subclass of the built-in dict class that provides a default value for any non-existent key. The default value
# is specified when the DefaultDict is created.

# Example usage
# Create a default dictionary with a default value of 0 for non-existent keys
default_dict = collections.defaultdict(int)
default_dict["key1"] = "value1"
default_dict["key2"] = "value2"
print("DefaultDict:", default_dict)
print("Value for non-existent key:", default_dict["key3"])

# ChainMap
# A ChainMap is a class that provides a way to link multiple dictionaries together into one mapping. The dictionaries are linked
# in the order in which they are passed to the ChainMap.

# Example usage
# Create a chain map with multiple dictionaries
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = {"key3": "value3", "key4": "value4"}
chain_map = collections.ChainMap(dict1, dict2)
print("ChainMap:", chain_map)

# NamedTuple
# A NamedTuple is a subclass of the built-in tuple class that has named fields instead of just indices. NamedTuples are similar to
# tuples, but they have named fields that can be accessed using dot notation.

# Example usage
# Create a named tuple with named fields
Person = collections.namedtuple("Person", ["name", "age"])
person = Person("John Doe", 30)
print("NamedTuple:", person)
print("Name:", person.name)
print("Age:", person.age)


# Deque
# A Deque (double-ended queue) is a class that provides a way to insert and remove elements from both the ends of the queue. Deques
# have a similar interface to lists, but they are optimized for inserting and removing elements from both the ends of the queue.

# Example usage
# Create a deque and perform various operations
deque = collections.deque([1, 2, 3, 4])

##Add elements to the left side of the deque using appendleft()
deque.appendleft(0)
print("Deque after adding elements to the left side:", deque)

# Add elements to the right side of the deque using append()
deque.append(5)
print("Deque after adding elements to the right side:", deque)

# Remove elements from the left side of the deque using popleft()
left_element = deque.popleft()
print("Left element:", left_element)
print("Deque after removing elements from the left side:", deque)

# Remove elements from the right side of the deque using pop()
right_element = deque.pop()
print("Right element:", right_element)
print("Deque after removing elements from the right side:", deque)

# Rotate the deque using rotate()
deque.rotate(-1)
print("Deque after rotating it by -1:", deque)

# Check if an element is present in the deque using count()
print("The number of occurrences of 3 in the deque:", deque.count(3))

# Extend the deque using extend()
deque.extend([3, 4, 5])
print("Deque after extending it with [3, 4, 5]:", deque)

# Limit the size of the deque using maxlen parameter
deque = collections.deque([1, 2, 3, 4], maxlen=2)
print("Deque after limiting the size to 2:", deque)
