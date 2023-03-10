# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data into pandas dataframe
df = pd.read_csv('D:\Ganesh Tukarul - Kiya.ai\Development\Power Bi\Dashboard\SampleSuperStore_CSVFile.csv')

# Convert 'Order Date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')

# Extract year from 'Order Date' column and create a new column 'Year'
df['Year'] = df['Order Date'].dt.year

# Create a dataframe showing year-wise sales by 'Ship Mode'
sales_by_year_shipmode = df.groupby(['Year', 'Ship Mode'])['Sales'].sum().unstack()

# Create a stacked bar chart showing year-wise sales by 'Ship Mode'
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax = sales_by_year_shipmode.plot(kind='bar', stacked=True, color=colors)

# Add data labels vertically
for i, (_, row) in enumerate(sales_by_year_shipmode.iterrows()):
    total = sum(row)
    for j, value in enumerate(row):
        if value > 0:
            ax.text(i, sum(row[0:j+1]) - value/2, '{:.0f}'.format(value), ha='center', va='center',
                    color='white', fontsize=8)

plt.title('Year-wise Sales by Ship Mode')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y')
plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()
#plt.savefig('year_wise_sales_stacked_bar_chart.png', dpi=150)
plt.show()