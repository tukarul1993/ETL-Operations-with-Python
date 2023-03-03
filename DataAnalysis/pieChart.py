import csv
import matplotlib.pyplot as plt

# Open the CSV file and read its contents into a list of dictionaries
with open('sampleCSVdata.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Calculate the sum of salaries for each department
department_sums = {}
for row in data:
    department = row['Department']
    salary = float(row['Salary'])
    if department not in department_sums:
        department_sums[department] = 0.0
    department_sums[department] += salary

# Create a pie chart of the department-wise sums of salaries
fig, ax = plt.subplots()
ax.pie(department_sums.values(), labels=department_sums.keys(), autopct='%1.1f%%')
ax.set_title('Department-wise sums of salaries')

plt.show()
