import openpyxl
from openpyxl.chart import BarChart, Reference, Series
import pandas as pd

# Open the workbook and select the sheet
workbook = openpyxl.load_workbook('/Files/ChartCreation.xlsx')
sheet = workbook['Sheet1']

# Create a reference to the data range
data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=5)
print(data)
categories = Reference(sheet, min_col=1, min_row=1, max_row=5)

#df = pd.DataFrame(data)

# Create the bar chart
chart = BarChart()
chart.add_data(data=data, titles_from_data=True)
chart.set_categories(categories)
chart.title = "Bar Chart Example"

# Add the chart to the worksheet
sheet.add_chart(chart, "E2")

# Save the workbook
workbook.save('D:\Python\ETL\Files\ChartCreationOP.xlsx')
