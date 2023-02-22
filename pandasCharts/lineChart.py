import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('D:\Python\ETL Operations with Python\Files\ChartCreationCSV_File.csv')

# Convert the 'Order Date' column to a datetime data type
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract the year and sales columns
df['Year'] = df['Order Date'].dt.year
df = df[['Year', 'Sales']]

# Group the data by year and sum the sales for each year
df = df.groupby('Year', as_index=False).sum()



# Create the line chart
plt.plot(df['Year'], df['Sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Year vs Sales')
plt.show()



