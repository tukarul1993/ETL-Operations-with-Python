import xml.etree.ElementTree as ET
import pandas as pd

# specify the file path of the XML file
xml_file  = 'D:\Python\ETL Operations with Python\Files\XML files\PurchaseOrder.xml'

# parse the XML file using ElementTree
tree = ET.parse(xml_file)
root = tree.getroot()
#print(tree)
print(root)     #PurchaseOrders

df = pd.DataFrame(
    columns=['PurchaseOrderNumber'])

rows = []

for metric in root.findall('PurchaseOrder'):
    print("PurchaseOrder")
    PurchaseOrderNumber = metric.get('PurchaseOrderNumber')
    OrderDate = metric.get('OrderDate')
    for address in root.findall('PurchaseOrder/Address'):
        print("Address")
        for Name in root.findall('PurchaseOrder/Address/Name'):
            Name=Name.text
            print("Name",Name)
