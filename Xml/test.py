import xml.etree.ElementTree as ET
import pandas as pd

# specify the file path of the XML file
xml_file  = 'D:\Python\ETL Operations with Python\Files\XML files\Metrics.xml'

# parse the XML file using ElementTree
tree = ET.parse(xml_file)
root = tree.getroot()

# create an empty Pandas dataframe with the required columns

df = pd.DataFrame(
    columns=['id', 'type', 'unit', 'count', 'sum', 'average', 'minValue', 'maxValue', 'standardDeviation'])

# iterate over the Metrics element to extract the data
rows = []
for metric in root.findall('.//Metrics/Metric'):
    print("1")
    # extract the attributes and text for each Metric element
    id = metric.get('id')
    type = metric.get('type')
    unit = metric.get('unit')
    count = metric.get('count')
    sum = metric.get('sum')
    average = metric.get('average')
    minValue = metric.get('minValue')
    maxValue = metric.get('maxValue')
    standardDeviation = metric.get('standardDeviation')
    text = metric.text

    # add a new row to the dataframe with the extracted data
    rows.append(
        {'id': id, 'type': type, 'unit': unit, 'count': count, 'sum': sum, 'average': average, 'minValue': minValue,
         'maxValue': maxValue, 'standardDeviation': standardDeviation, 'text': text})
    print(rows)
# concatenate the rows into a dataframe
df = pd.concat([df, pd.DataFrame(rows)])

# reset the index of the dataframe
df.reset_index(drop=True, inplace=True)

# print the resulting dataframe
print(df)
