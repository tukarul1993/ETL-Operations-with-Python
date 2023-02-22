import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile('D:\Python\ETL Operations with Python\Files\LoadMultipleSheets_Diff_Columns.xlsx')

# Create an empty data frame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Load the sheet into a data frame
    sheet_df = excel_file.parse(sheet_name)

    # Append the sheet data to the combined data frame
    #combined_df = combined_df.append(sheet_df, ignore_index=True)      ##Old version
    # Append the sheet data to the combined data frame
    combined_df = pd.concat([combined_df, sheet_df], ignore_index=True)  ##New version
# Print the combined data frame
print(combined_df)
