"""
XML Element

Below is a sample xml file content for understanding

<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="children">
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
<bookstore>

<title>, <author>, <year>, and <price> have text content because they contain text (like 29.99).
<bookstore> and <book> have element contents, because they contain elements.
<book> has an attribute (category="children").
First line is called XML Prolog.
<bookstore> is the root of the tree.
"""

import xml.etree.ElementTree as ET

# Loading an xml tree
tree = ET.parse("sample.xml")

# Finding the root of the tree
root = tree.getroot()
print(root.tag)
print("****")

# Selecting a child of root
print(root[0].tag)
print(root[0].attrib)
print("****")

# Looking for all child nodes
for x in root:
    print(x.tag, x.text)
print("****")

# Finding bounding box coordinates
for x in root.findall("object"):
    for y in x.find("bndbox"):
        print(y.tag, y.text)
