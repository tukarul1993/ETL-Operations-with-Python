import pandas as pd
# List of Tuples
students = [('jack',    34, 'Sydney',   'Australia'),
            ('Riti',    30, 'Delhi',    'India'),
            ('Vikas',   31, 'Mumbai',   'India'),
            ('Neelu',   32, 'Bangalore','India'),
            ('John',    16, 'New York',  'US'),
            ('Mike',    17, 'Las Vegas', 'US')]
# Create a DataFrame object
df = pd.DataFrame( students,
                   columns=['Name', 'Age', 'City', 'Country'],
                   index=  ['a', 'b', 'c', 'd', 'e', 'f'])
# Display the DataFrame
print(df)

# Add a new column to the DataFrame
df['Budget'] = [2000, 3000, 4000, 3500, 4500, 2900]

# Add a new column to the DataFrame
df['Marks'] = 0

# Change the values of a column
df['Age'] = [31, 35, 36, 34, 31, 37]

# Add a new Row to the DataFrame
#df.loc['g'] = ['Aadi', 35, 'Delhi', 'India']       ##Error

df.loc['g'] = ['Aadi', 35, 'Delhi', 'India',56666,0]       ##Error

print(df)