import pandas as pd
import mimetypes
import os
# Load the JSON data

folderPath='D:\Python\ETL Operations with Python\Files\jsonDataFile.json'

with open(folderPath, 'r') as file:
    data = file.read()

# Read the JSON data into a Pandas DataFrame
df = pd.read_json(data)

# Print the DataFrame
print(df)
print("###################################")
print(df.iloc[:, 0])
print("###################################")
print(df.iloc[0:3, 0:1])


file_path = os.path.join(folderPath)
file_type = mimetypes.guess_type(file_path)[0]
print(file_type)
##df.iloc[row_start:row_end , col_start:col_end]

ColNames=""
for name, dtype in df.dtypes.items():
    print("Name",name)
    ColNames = ColNames + name + ","
print("ColNames:",ColNames)