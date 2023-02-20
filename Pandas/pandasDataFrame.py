import pandas as pd
# List of Tuples
students = [('Mark',  'Apples', 44),
            ('Aadi',  'Mangos', 31),
            ('Shaun', 'Grapes', 30),
            ('Simi',  'Apples', 32),
            ('Luka',  'Mangos', 43),
            ('Mike',  'Apples', 45),
            ('Arun',  'Mangos', 35),
            ('Riti',  'Grapes', 37),]
# Create a DataFrame object
df = pd.DataFrame(  students,
                    columns = ['Name' , 'Product', 'Sale'])
# Display the DataFrame
#print(df)
boolSeries = df['Product'] == 'Apples'
boolSeries = df[df['Product'] == 'Apples']
df = df[(df['Sale'] > 30) & (df['Sale'] < 40)]
df1=df[df['Name'] == 'Riti']
#print(df1)


# Create a dictionary of lists
employees = { 'Name': ['John', 'Mark', 'Joseph', 'Ritika', 'Vinod', 'Saurav', 'Lucy'],
              'Age': [29, 24, 28, 31, 33, 32, 31],
              'City': ['London', 'Tokyo', 'Delhi', 'Mumbai', 'Sydney', 'Paris', 'New York'],
              'Experience': [15, 13, 14, 11, 13, 12, 15]}
# Create a Pandas DataFrame from a list of Dictionaries
df = pd.DataFrame(employees)
# Display the DataFrame
# Select row at with label name 'c'
row = df.loc[3]
#print(row)

# Select multiple rows from Dataframe by label names
#print(df.loc[ [True, False, True, False, True, False,True] ])
#print(df.loc[[1, 2, 3]])
#print(df.loc[1:3])


# Select rows of Dataframe based on callable function
subsetDf = df.loc[ lambda x : (x['Age'] > 31).tolist() ]
print(subsetDf)


print(df.loc[:, 'Age'])
print( df.loc[:, ['Age', 'City', 'Name']])
print(df.loc[:, 'Name' : 'City'])
print(df.iloc[:, [True, True, False, False]])

#singel intersect value
print(df.loc[3,'Name'])
print(df.loc[[1,2,3],['Name', 'City']])
print(df.loc[1:3, 'Name':'City'])
