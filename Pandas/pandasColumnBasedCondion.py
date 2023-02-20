import pandas as pd
import numpy as np
# List of Tuples
employees = [('Shubham', 'India', 'Tech',   5),
            ('Riti', 'India', 'Tech' ,   7),
            ('Shanky', 'India', 'PMO' ,   2),
            ('Shreya', 'India', 'Design' ,   2),
            ('Aadi', 'US', 'Tech', 11),
            ('Sim', 'US', 'Tech', 4)]
# Create a DataFrame object from list of tuples
df = pd.DataFrame(employees,
                  columns=['Name', 'Location', 'Team', 'Experience'])
#print(df)
# creating a new column based on a condition
#df['experience_type'] = np.where(df['Experience']>3, "Senior", "Junior")
print(df)



# define conditions
conditions = [
    (df['Experience'] < 3),
    (df['Experience'] >= 3) & (df['Experience'] <= 10),
    (df['Experience'] > 10)
]
# define values to assign
values = ['Junior', 'Senior', 'Leader']
# pass it in np.select()
df['experience_type'] = np.select(conditions, values)
print (df)