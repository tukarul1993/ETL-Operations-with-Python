import glob
import os
import pandas as pd
all_files = glob.glob("D:\Python\ETL Operations with Python\Files\TextFiles\*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files))
print(df)