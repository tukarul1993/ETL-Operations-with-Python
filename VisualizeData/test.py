import pandas as pd
import datetime
# Read CSV file
df = pd.read_csv('csvdatafile.csv')

# Display first few rows of data
#print(df.head())

# Display summary statistics
#print(df.describe())
date = datetime.date.today()

df_new=df['StartOfMonth']

# Get start of month
start_of_month = date.replace(day=1)

# Print start of month
print(start_of_month)