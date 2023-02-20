import pandas as pd
# List of Tuples
empoyees = [(11, 'jack', 34, 'Sydney', 5) ,
            (12, 'Riti', 31, 'Delhi' , 7) ,
            (13, 'Aadi', 16, 'New York', 11) ,
            (14, 'Mohit', 32,'Delhi' , 15) ,
            (15, 'Veena', 33, 'Delhi' , 4) ,
            (16, 'Shaunak', 35, 'Mumbai', 5 ),
            (17, 'Shaun', 35, 'Colombo', 11)]
# Create a DataFrame object
df = pd.DataFrame(  empoyees,
                    columns=['ID', 'Name', 'Age', 'City', 'Experience'],
                    index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
# Display the DataFrame
#print(df)
# Iterate over rows of DataFrame by Index Labels
#print(df.iterrows())
""""""
for (index_label, row_series) in df.iterrows():
    print('Row Index label : ', index_label)
    print('Row Content as NumPy Array: ', row_series.values)

print("##########################################")
# Iterate over rows of DataFrame by index positions
print(df.shape[0])
for i in range(0, df.shape[0]):
    print('Row Index Position : ', i)
    # Get row contents as NumPy Array from Series
    rowContent = df.iloc[i].values
    print('Row Content as NumPy Array: ', rowContent)

print("##################### Iterate over the sequence of column names")
for column in df.columns:
    # Select column contents by column name using [] operator
    columnSeriesObj = df[column]
    print('Colunm Name : ', column)
    print('Column Contents as NumPy Array: ', columnSeriesObj.values)

print("##################### # Iterate over columns of DataFrame by index positions")
print(df.shape[1])
for i in range(0, df.shape[1]):
    print('Colunm Number/Position: ', i)
    # Get column contents as NumPy Array
    columnContent = df.iloc[:, i].values
    print('Column contents: ', columnContent)