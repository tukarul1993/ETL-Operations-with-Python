import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('D:\Python\ETL Operations with Python\Files\PythonExcelLookupExample.xlsx')

# Select the worksheet
worksheet = workbook['Sheet1']

# Apply the VLOOKUP formula in cell C2, using A2 as the lookup value and the range B2:D4 as the lookup table
worksheet['C2'] = '=VLOOKUP(A2, Sheet2!A2:B6, 2, FALSE)'

# Save the workbook
workbook.save('D:\Python\ETL Operations with Python\Files\PythonExcelLookupExample1.xlsx')