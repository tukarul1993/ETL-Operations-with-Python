import pandas as pd
import numpy as np
# List of Tuples
empoyees = [('jack',    np.NaN, 'Sydney',  5) ,
            ('Riti',    31,     'Delhi',   7) ,
            ('Aadi',    16,     'Karnal',  11) ,
            ('Mark',    np.NaN, 'Delhi',   np.NaN),
            ('Veena',   33,     'Delhi',   4) ,
            ('Shaunak', 35,     'Noid',    np.NaN),
            ('Sam',     35,     'Colombo', np.NaN)]
# Create a DataFrame object from list of tuples
df = pd.DataFrame(  empoyees,
                    columns=['Name', 'Age', 'City', 'Experience'],
                    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# Display the DataFrame
#print(df)

# Delete all rows with one or more NaN values
#newDf = df.dropna()
# Display the new DataFrame

# Delete all columns with one or more NaN values
#newDf = df.dropna(axis=1)


# Delete columns who dont have at least 5 non NaN values
#newDf = df.dropna(axis=1, thresh=5)
#newDf = df.fillna(value=0)

print(df['Experience'].mean())

df['Experience'] = df['Experience'].fillna(df['Experience'].mean())
print(df)

df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)
#print(df['Age'].mean())