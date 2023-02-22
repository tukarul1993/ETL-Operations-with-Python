import os
import pandas as pd

# Folder path containing Excel workbooks
folder_path = 'D:\Python\ETL Operations with Python\Files\ExcelFiles'

# Get a list of file names in the folder
file_names = os.listdir(folder_path)

# Loop through each file name and read data from each workbook

for file_name in file_names:
    df_list = []
    # Check if file is an Excel workbook
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # Construct full path to Excel workbook
        file_path = os.path.join(folder_path, file_name)
        # Create an Excel file object
        xls = pd.ExcelFile(file_path)
        # List of sheet names to read from Excel workbook
        sheet_names = xls.sheet_names
        # Loop through each sheet name and read data into a DataFrame
        for sheet_name in sheet_names:
            # Read data from current sheet name into a DataFrame
            df = pd.read_excel(xls, sheet_name)
            # Append DataFrame to list
            df_list.append(df)

    # Concatenate all DataFrames into one
    final_df = pd.concat(df_list, axis=0, ignore_index=True)
    print(final_df)