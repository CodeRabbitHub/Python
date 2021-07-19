numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

values = list(range(5))
print(values)
values = [*range(5), *"Hello"]
print(values)


first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}  # unpacking
print(combined)

# if same keys are present the latest
#  key value pair will be used.
