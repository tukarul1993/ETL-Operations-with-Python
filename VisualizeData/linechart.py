import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('csvdatafile.csv')

# Convert OrderDate column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month and year from OrderDate column
df['MonthYear'] = df['Order Date'].dt.to_period('M')

# Group by MonthYear and calculate total sales
sales_by_monthyear = df.groupby('MonthYear')['Sales'].sum()

# Create line chart
plt.plot(sales_by_monthyear.index.astype(str), sales_by_monthyear.values)

# Add labels and title
plt.xlabel('Month Year')
plt.ylabel('Sales')
plt.title('Monthly Sales')

# Show plot
plt.show()
