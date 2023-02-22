import os
import pandas as pd

# specify the folder path
folder_path = 'D:\Python\ETL Operations with Python\Files\TextFiles'

# create an empty list to store the dataframes
dfs = []

# loop through all subfolders and files in the folder
for subdir, dirs, files in os.walk(folder_path):
    print("New Iteration : ")
    print(subdir)
    print(dirs)
    print(files)

    for file in files:
        # check if file is a CSV file
        if file.endswith('.csv'):
            # construct the full file path
            file_path = os.path.join(subdir, file)
            # read the CSV file into a Pandas DataFrame
            df = pd.read_csv(file_path)
            # add a new column to the DataFrame with the filename
            df['filepath'] = file_path
            df['filename'] = file
            # append the DataFrame to the list
            dfs.append(df)

# concatenate all DataFrames into a single DataFrame
result = pd.concat(dfs, ignore_index=True)

# print the result
print(result)
