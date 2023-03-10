# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data into pandas dataframe
df = pd.read_csv('D:\Ganesh Tukarul - Kiya.ai\Development\Power Bi\Dashboard\SampleSuperStore_CSVFile.csv')


# Convert 'Order Date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')

# Extract year from 'Order Date' column and create a new column 'Year'
df['Year'] = df['Order Date'].dt.year

# Create a dataframe showing year-wise sales
sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()

# Create a bar chart showing year-wise sales
colors = ['#3498db'#, '#f1c40f', '#2ecc71', '#e74c3c', '#9b59b6', '#34495e'
          ]
plt.bar(sales_by_year['Year'], sales_by_year['Sales'], color=colors)
plt.title('Year-wise Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(sales_by_year['Year'])
plt.ticklabel_format(style='plain', axis='y')
plt.legend(['Sales'], fontsize=12, loc='upper left')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
#plt.savefig('year_wise_sales_bar_chart.png', dpi=150)
