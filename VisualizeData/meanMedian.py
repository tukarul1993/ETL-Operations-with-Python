import pandas as pd

# Read CSV file
df = pd.read_csv('csvdatafile.csv')

# Display first few rows of data
print(df.head())

# Display summary statistics
print(df.describe())

# Calculate mean and median values
mean_value = df['Sales'].mean()
median_value = df['Sales'].median()

# Display insights
print("The mean value is:", mean_value)
print("The median value is:", median_value)