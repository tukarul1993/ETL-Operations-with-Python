import csv
import matplotlib.pyplot as plt

# Open the CSV file and read its contents into a list of dictionaries
with open('sampleCSVdata.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Calculate the sum of salaries for each department and region
department_sums = {}
region_sums = {}
for row in data:
    department = row['Department']
    region = row['Region']
    salary = float(row['Salary'])
    if department not in department_sums:
        department_sums[department] = 0.0
    if region not in region_sums:
        region_sums[region] = 0.0
    department_sums[department] += salary
    region_sums[region] += salary

# Create a figure with two pie charts side by side
fig, (ax1, ax2) = plt.subplots(1, 2)

# Create the first pie chart of the department-wise sums of salaries
ax1.pie(department_sums.values(), labels=department_sums.keys(), autopct='%1.1f%%')
ax1.set_title('Department-wise sums of salaries', bbox={'facecolor':'0.8', 'pad':5}, fontsize=12)

# Create the second pie chart of the region-wise sums of salaries
ax2.pie(region_sums.values(), labels=region_sums.keys(), autopct='%1.1f%%')
ax2.set_title('Region-wise sums of salaries', bbox={'facecolor':'0.8', 'pad':5}, fontsize=12)

# Adjust the spacing between the two pie charts
fig.subplots_adjust(wspace=0.4)

plt.show()
