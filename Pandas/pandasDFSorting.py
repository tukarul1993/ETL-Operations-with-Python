import pandas as pd
# List of Tuples
empoyees = [(11, 'Jack',    44, 'Sydney',   19) ,
            (12, 'Riti',    41, 'Delhi' ,   17) ,
            (13, 'Aadi',    46, 'New York', 11) ,
            (14, 'Mohit',   45, 'Delhi' ,   15) ,
            (15, 'Veena',   43, 'Delhi' ,   14) ,
            (16, 'Shaunak', 42, 'Mumbai',   10 ),
            (17, 'Shaun',   40, 'Colombo',  12)]
# Create a DataFrame object
df = pd.DataFrame(  empoyees,
                    columns=['ID', 'Name', 'Age', 'City', 'Experience'],
                    index=['b', 'd', 'a', 'c', 'g', 'f', 'e'])
# Display the DataFrame
#print(df)

# Sort DataFrame by column 'Experience'
#df = df.sort_values(by=['City'], ascending=False)
# Display the DataFrame
#print(df)
print(df)
# Sort DataFrame by the Column Names
df = df.sort_index(axis=1)
# Display the DataFrame
print(df)