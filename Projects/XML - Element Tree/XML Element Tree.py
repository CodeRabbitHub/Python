import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET module
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)

print("\n")

# Display functions in ET module
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)
