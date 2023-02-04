import xml.etree.ElementTree as ET

# Let's start by parsing an XML string into an ElementTree object
xml_string = """
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
</data>
"""
root = ET.fromstring(xml_string)

# Once the ElementTree is created, you can access elements using the 'find' method
# The 'find' method returns the first matching element or 'None' if no match is found
# Let's find the first 'country' element:
first_country = root.find("country")

# To access the attributes of an element, use the 'attrib' property
print(first_country.attrib)  # Output: {'name': 'Liechtenstein'}

# To access the text of an element, use the 'text' property
print(first_country.find("rank").text)  # Output: '1'

# The 'findall' method returns a list of all matching elements
neighbors = first_country.findall("neighbor")

# You can iterate over the list of elements to access each one individually
for neighbor in neighbors:
    print(neighbor.attrib)

# Output:
# {'name': 'Austria', 'direction': 'E'}
# {'name': 'Switzerland', 'direction': 'W'}

# Another way to iterate over elements is to use the 'iter' method
for element in root.iter():
    print(element.tag, element.attrib)

# Output:
# data {}
# country {'name': 'Liechtenstein'}
# rank {}
# year {}
# gdppc {}
# neighbor {'name': 'Austria', 'direction': 'E'}
# neighbor {'name': 'Switzerland', 'direction': 'W'}
# country {'name': 'Singapore'}
# rank {}
# year {}
# gdppc {}
# neighbor {'name': 'Malaysia', 'direction': 'N'}

# You can use the 'find' method with an 'xpath' argument to search for elements using xpath expressions
# For example, to find all 'neighbor' elements:
neighbors = root.findall(".//neighbor")

for neighbor in neighbors:
    print(neighbor.attrib)

# Output:
# {'name': 'Austria', 'direction': 'E'}
# {'name': 'Switzerland', 'direction': 'W'}
# {'name': 'Malaysia', 'direction': 'N'}

# To search for elements with a specific attribute, use the '[@attribute="value"]' xpath expression
# For example, to find all 'country' elements with the 'name' attribute equal to 'Singapore':
singapore = root.find(".//country[@name='Singapore']")

print(singapore.attrib)  # Output: {'name': 'Singapore'}

# You can also modify the XML data in memory, and then write it back to a file or string
# For example, to add a new 'neighbor' element to the 'Singapore' country:
new_neighbor = ET.Element("neighbor", attrib={"name": "Indonesia", "direction": "S"})
singapore.append(new_neighbor)

# To write the modified XML data to a string, use the 'tostring' method
modified_xml_string = ET.tostring(root, encoding="unicode")
print(modified_xml_string)

# Output:
# <data>
#     <country name="Liechtenstein">
#         <rank>1</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor direction="E" name="Austria" />
#         <neighbor direction="W" name="Switzerland" />
#     </country>
#     <country name="Singapore">
#         <rank>4</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor direction="N" name="Malaysia" />
#         <neighbor direction="S" name="Indonesia" />
#     </country>
# </data>
