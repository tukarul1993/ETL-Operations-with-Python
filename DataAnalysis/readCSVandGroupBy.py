import csv

# Open the CSV file and read its contents into a list of dictionaries
with open('sampleCSVdata.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

#1 : Simple sum of all the cells in column (Salary)
total=0.0
for row in data:
    #print(row)
    total=total+float(row['Salary'])
print(total)


#1:  Calculate the total salary for all employees
total_salary = sum(float(row['Salary']) for row in data)
# Print the total salary
#print(f"Total salary: {total_salary}")


#2: Calculate the sum of salaries for each department
sums = {}
for row in data:
    department = row['Department']
    salary = float(row['Salary'])
    #print(sums)
    if department not in sums:
        sums[department] = 0.0
    sums[department] += salary
"""
# Print the department-wise sums of salaries
for department, total_salary in sums.items():
    print(f"{department}: {total_salary}")
"""
# Nested dictionary: 2 levels
#3: Calculate the sum of salaries for each region and department
region_department_sums = {}
for row in data:
    region = row['Region']
    department = row['Department']
    salary = float(row['Salary'])
    if region not in region_department_sums:
        region_department_sums[region] = {}
    if department not in region_department_sums[region]:
        region_department_sums[region][department] = 0.0
    region_department_sums[region][department] += salary
#print(region_department_sums)
"""
# Print the region-wise and department-wise sums of salaries
for region, department_sums in region_department_sums.items():
    print(f"{region}:")
    for department, total_salary in department_sums.items():
        print(f"    {department}: {total_salary}")

"""



# Calculate the sum of salaries for each country, department, and region
country_department_region_sums = {}
for row in data:
    country = row['Country']
    department = row['Department']
    region = row['Region']
    salary = float(row['Salary'])
    #print(country_department_region_sums)

    if country not in country_department_region_sums:
        country_department_region_sums[country] = {}
    if department not in country_department_region_sums[country]:
        country_department_region_sums[country][department] = {}
    if region not in country_department_region_sums[country][department]:
        country_department_region_sums[country][department][region] = 0.0

    country_department_region_sums[country][department][region] += salary
print(country_department_region_sums)

"""
# Print the country-wise, department-wise, and region-wise sums of salaries
for country, department_region_sums in country_department_region_sums.items():
    print(f"{country}:")
    for department, region_sums in department_region_sums.items():
        print(f"    {department}:")
        for region, total_salary in region_sums.items():
            print(f"        {region}: {total_salary}")
"""


# 4: Country- Region- Department wise Sum of salary , 3 level dictionary
country_region_department_sums = {}
for row in data:
    country = row['Country']
    department = row['Department']
    region = row['Region']
    salary = float(row['Salary'])
    #print(country_department_region_sums)

    if country not in country_region_department_sums:
        country_region_department_sums[country] = {}
    if region not in country_region_department_sums[country]:
        country_region_department_sums[country][region] = {}
    if department not in country_region_department_sums[country][region]:
        country_region_department_sums[country][region][department] = 0.0

    country_region_department_sums[country][region][department] += salary

print(country_region_department_sums)

for country, region_department_sums in country_region_department_sums.items():
    print(f"{country}:")
    for region, department_sums in region_department_sums.items():
        print(f"    {region}:")
        for department, total_salary in department_sums.items():
            print(f"        {department}: {total_salary}")