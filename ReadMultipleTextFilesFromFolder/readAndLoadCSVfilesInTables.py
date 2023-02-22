import os
import pandas as pd
import pyodbc

# specify the folder path
folder_path = 'D:\Python\ETL Operations with Python\Files\SourceData'

def insert_data(df, table_name):
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=ITLNB619;'
            'DATABASE=SSIS_Practice;'
            'UID=sa;'
            'PWD=admin@123'
        )
        # Insert data in tables
        columns = df.axes[1]
        #file_Name = table_name
        query = "Insert into " + table_name + "("
        for column in columns:
            query = query + " " + column + ","
        query = query[:-1] + "\n\t)"
        PlaceHolders = ""
        for name, dtype in df.dtypes.items():
            PlaceHolders = PlaceHolders + "?,"
        for row in df.itertuples():
            cursor = connection.cursor()
            # print(row[1:])
            cursor.execute("INSERT INTO " + table_name + "  VALUES (" + PlaceHolders[:-1] + ")", row[1:])
            #print("INSERT INTO " + file_Name + "  VALUES (" + PlaceHolders[:-1] + ")", row[1:])
            #print("data inserted")
        connection.commit()
        connection.close()

# loop through all subfolders and files in the folder
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        index = file.find('_')
        table_name = file[:index] if index != -1 else file
        file_path = os.path.join(subdir, file)
        # read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)
        df['filepath'] = file_path
        df['filename'] = file

        insert_data(df, table_name)