import pandas as pd

# Read the Excel files into pandas dataframes
df1 = pd.read_excel('D:\Python\ETL\Files\VlookupSample.xlsx','Sheet1')
df2 = pd.read_excel('D:\Python\ETL\Files\VlookupSample.xlsx','Sheet2')

# Perform a VLOOKUP-like operation using the merge method in pandas
result = pd.merge(df1, df2, on='Id', how='left')

# Save the results to a new Excel file
result.to_excel('D:\Python\ETL\Files\VlookupOutputSample.xlsx', index=False)