point = {"x": 1, "y": 2}
# Keys should be immutable type
# values can be of any type
point = dict(x=1, y=2)

print(point["x"])
point["z"] = 3
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a", 0))  # if we dont have key "a" return 0

del point["x"]
print(point)

for key, val in point.items():
    print(key, val)
