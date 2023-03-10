# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data into pandas dataframe
df = pd.read_csv('D:\Ganesh Tukarul - Kiya.ai\Development\Power Bi\Dashboard\SampleSuperStore_CSVFile.csv')

# Create a dataframe showing sales by ship mode
sales_by_ship_mode = df.groupby('Ship Mode')['Sales'].sum().reset_index()

# Create a donut chart showing sales by ship mode
colors = ['#FF5733', '#FFC300', '#C70039', '#900C3F']
fig, ax = plt.subplots()
ax.pie(sales_by_ship_mode['Sales'], colors=colors, radius=1, wedgeprops=dict(width=0.3, edgecolor='w'), startangle=90, autopct='%1.1f%%')
ax.pie([1], colors=['white'], radius=0.7, wedgeprops=dict(width=0.3, edgecolor='w'))
plt.title('Sales by Ship Mode')
plt.legend(labels=sales_by_ship_mode['Ship Mode'], fontsize=4, loc='best')
#plt.legend(['Sales'], fontsize=12, loc='upper right')
#plt.title('Sales vs. Profit')
plt.show()
#plt.savefig('sales_by_ship_mode_donut.png', dpi=150)
