import xml.etree.ElementTree as ET

def process_element(element):
    # process the current element
    print(element.tag, element.text)

    # process each nested child element recursively
    for child in element:
        process_element(child)

# specify the path of the XML file
xml_file = 'D:\Python\ETL Operations with Python\Files\XML files\PurchaseOrder_1Row.xml'

# parse the XML file using ElementTree
tree = ET.parse(xml_file)

# get the root element of the XML file
root = tree.getroot()

# process each child element of the root element
for child in root:
    process_element(child)
