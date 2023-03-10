# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into pandas dataframe
df = pd.read_csv('D:\Ganesh Tukarul - Kiya.ai\Development\Power Bi\Dashboard\SampleSuperStore_CSVFile.csv')

# Convert Order Date and Ship Date columns to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create a pie chart showing sales by ship mode
sales_by_ship_mode = df.groupby('Ship Mode')['Sales'].sum().reset_index()
plt.pie(sales_by_ship_mode['Sales'], labels=sales_by_ship_mode['Ship Mode'], autopct='%1.1f%%')
plt.title('Sales by Ship Mode')
plt.savefig('sales_by_ship_mode.png', dpi=150)

# Create a line chart showing total sales over time
sales_over_time = df.groupby('Order Date')['Sales'].sum().reset_index()
plt.plot(sales_over_time['Order Date'], sales_over_time['Sales'])
plt.xlabel('Order Date')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.show()

# Create a scatter plot showing the relationship between sales and profit
sns.scatterplot(data=df, x='Sales', y='Profit')
plt.title('Sales vs. Profit')
plt.show()

# Create a bar chart showing sales by category
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
sns.barplot(data=sales_by_category, x='Category', y='Sales')
plt.title('Sales by Category')
plt.show()

# Create a heat map showing the correlation between numeric variables
corr = df.corr()
sns.heatmap(corr, cmap='coolwarm', annot=True)
plt.title('Correlation Matrix')
plt.show()
