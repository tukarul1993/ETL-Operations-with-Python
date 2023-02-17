import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# export dataframe to excel
df.to_excel('D:\Python\ETL\Files\ExportDataOutput.xlsx', index=False)
