import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")
root = tree.getroot()

# We add height and width child to bounding box

for x in root.iter("object"):
    for y in x.iter("bndbox"):

        height = int(y.find("ymax").text) - int(y.find("ymin").text)
        width = int(y.find("xmax").text) - int(y.find("xmin").text)

        ht = ET.SubElement(y, "height")
        ht.text = str(height)

        wh = ET.SubElement(y, "width")
        wh.text = str(width)

        y.set("updated", "yes")

tree.write("newSample.xml")
