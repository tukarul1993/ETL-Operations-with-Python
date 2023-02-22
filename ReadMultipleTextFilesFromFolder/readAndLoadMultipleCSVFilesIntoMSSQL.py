import datetime
import os
import pandas as pd
import pyodbc
import shutil


"""
drop table tableStudents
create table tableStudents(
Stud_Id	 varchar(100),
Stud_Name	varchar(100),
School varchar(100),
FilePath varchar(max),
FileName varchar(max)
)
drop table tableEmployee
create table tableEmployee(
Id	 int,
Name	varchar(100),
Age int,
FilePath varchar(max),
FileName varchar(max)
)
"""
# specify the folder path
folder_path = 'D:\Python\ETL Operations with Python\Files\SourceData'
archieve_path='D:\Python\ETL Operations with Python\Files\ArchievedFiles'

def insert_data(df, table_name, file_path,file):
        print(file_path)
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
            print("data inserted")

            archieve_path1= os.path.join(archieve_path, file.split('.')[0]+"_"+datetime.datetime.now().strftime('%d%m%Y%H%M%S')+"."+file.split('.')[1])
            #print(datetime.datetime.now().strftime('%d%m%Y%H%M%S'))
            #datetime.date.today().strftime('%d%m%Y')
            #print(file_path)
            shutil.move( file_path, archieve_path1)

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

        insert_data(df, table_name, file_path,file)