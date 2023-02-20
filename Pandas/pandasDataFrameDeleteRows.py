import pandas as pd

# List of Tuples
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
#Create a DataFrame object
dfObj = pd.DataFrame(students,  columns = ['Name' , 'Age', 'City' , 'Country'],
                                index=['a', 'b', 'c' , 'd' , 'e' , 'f'])
#print(dfObj)

#print(dfObj)
# Delete columns at index 0 & 2
modDfObj = dfObj.drop([dfObj.columns[0] , dfObj.columns[2]] ,  axis='columns')   # Delete columns at index 0 & 2




modDfObj = dfObj.drop('Age' , axis='columns')           ######## drop column by name
#print(modDfObj)

modDfObj = dfObj.drop(['Age' , 'Name'] , axis='columns')   ######## drop column by name

#print(modDfObj)

dfObj.drop(['Age' , 'Name'] , axis='columns', inplace=True)

#print(dfObj)
#print(dfObj.dtype)
