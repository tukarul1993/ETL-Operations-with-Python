import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# create an Excel writer using xlsxwriter engine
writer = pd.ExcelWriter('D:\Python\ETL\Files\output.xlsx', engine='xlsxwriter')

# convert the dataframe to an xlsxwriter workbook object
df.to_excel(writer, sheet_name='Sheet1', index=False)

# get the xlsxwriter workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# add number formatting to the Salary column
format = workbook.add_format({'num_format': '$#,##0'})
worksheet.set_column('C:C', None, format)

# save the workbook and close the writer
writer.save()