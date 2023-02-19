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
# Add a new Row to the DataFrame
df.loc['g'] = ['Aadi', 35, 'Delhi', 'India']
# Display the DataFrame
print(df)