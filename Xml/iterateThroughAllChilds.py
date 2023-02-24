import xml.etree.ElementTree as ET

# specify the path of the XML file
xml_file = 'D:\Python\ETL Operations with Python\Files\XML files\PurchaseOrder.xml'
xml_file = 'D:\Python\ETL Operations with Python\Files\XML files\PurchaseOrder_1Row.xml'

# parse the XML file using ElementTree
tree = ET.parse(xml_file)

# get the root element of the XML file
root = tree.getroot()

rows = []

# iterate over all child elements of the root element
for child in root:
    # print the tag name and text content of the child element
    print(child.tag, child.text)


    # iterate over all nested child elements of the child element
    for nested_child in child:

        # print the tag name and text content of the nested child element
        #print(nested_child.tag, nested_child.text)

        for ns_chld1 in nested_child:
            # print the tag name and text content of the nested child element
            #print(ns_chld1.tag, ns_chld1.text)

            for ns_chld2 in ns_chld1:
                pass
                # print the tag name and text content of the nested child element
                #print(ns_chld2.tag, ns_chld2.text)