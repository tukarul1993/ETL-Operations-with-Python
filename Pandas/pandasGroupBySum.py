import pandas as pd
# List of Tuples
employees = [('Shubham', 24, 'Tech',  5),
             ('Riti', 45, 'Tech' ,  7),
             ('Shanky', 12, 'PMO' ,  2),
             ('Shreya', 8, 'Design' ,  2),
             ('Aadi', 15, 'Tech', 11),
             ('Sim', 18, 'Tech', 4)]
# Create a DataFrame object from list of tuples
df = pd.DataFrame(  employees,
                    columns=['Name', 'Salary', 'Team', 'Experience'])


print(df)
# group by team and sum all the columns
print (df.groupby('Team').sum())

# group by team and get the sum of Experience column
print (df.groupby('Team')['Salary'].sum())

# sort the output by Team in descending order
print (df.groupby('Team', sort=True).agg({'Experience':'sum'}))

##Pandas find rows which contain string
print(df[df['Name'].str.contains('it', na=False)])