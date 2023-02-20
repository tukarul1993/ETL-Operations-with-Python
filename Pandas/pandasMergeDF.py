import pandas as pd
# List of Tuples
data1= [('Jack', 34, 'Sydney', 5) ,
        ('Riti', 31, 'Delhi' , 7) ,
        ('Aadi', 46, 'New York', 11)]
# List of Tuples
data2= [('Mohit', 34, 'Tokyo', 11) ,
        ('Veena', 31, 'London' , 10) ,
        ('Shaun', 36, 'Las Vegas', 12)]
# List of Tuples
data3= [('Mark', 47, 'Mumbai',   13) ,
        ('Jose', 43, 'Yokohama', 14) ,
        ('Ramu', 49, 'Paris',    15)]
# Create a DataFrame object from list of tuples
firstDf = pd.DataFrame( data1,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['a', 'b', 'c'])
print('First DataFrame:')
# Display the First DataFrame
print(firstDf)
# Create a DataFrame object from list of tuples
secondDF = pd.DataFrame(data2,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['d', 'e', 'f'])
print('Second DataFrame:')
# Display the second DataFrame
print(secondDF)
# Create a DataFrame object from list of tuples
thirdDF = pd.DataFrame( data3,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['g', 'h', 'i'])
print('Third DataFrame:')
# Display the third DataFrame
print(thirdDF)

# Concatenate three DataFrames along the Rows
df = pd.concat([firstDf, secondDF, thirdDF])
# Display the Concatenated DataFrame
print(df)

# Concatenate three DataFrames along the Columns
df = pd.concat([firstDf, secondDF, thirdDF], axis=1)
# Display the Concatenated DataFrame
print(df)



# List of Tuples
empoyees = [(11, 'jack', 34, 'Sydney', 5) ,
            (12, 'Riti', 31, 'Delhi' , 7) ,
            (13, 'Aadi', 16, 'New York', 11) ,
            (14, 'Mohit', 32,'Delhi' , 15) ,
            (15, 'Veena', 33, 'Delhi' , 4) ,
            (16, 'Shaunak', 35, 'Mumbai', 5 ),
            (17, 'Shaun', 35, 'Colombo', 11)]
# Create a DataFrame object
empDfObj = pd.DataFrame(empoyees,
                        columns=['ID', 'Name', 'Age', 'City', 'Experience'],
                        index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
print("Dataframe 1 : ")
print(empDfObj)


# List of Tuples
salaries = [(11, 5, 70000, 1000) ,
            (12, 7, 72200, 1100) ,
            (13, 11, 84999, 1000) ,
            (14, 15, 90000, 2000) ,
            (15, 4, 61000, 1500) ,
            (16, 5, 71000, 1000),
            (34, 10,81000, 2000)]
# Create a DataFrame object
salaryDfObj = pd.DataFrame( salaries,
                            columns=['ID', 'Experience' , 'Salary', 'Bonus'],
                            index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
print("Dataframe 2 : ")
print(salaryDfObj)


# Merge two Dataframes on common columns using default inner join
mergedDf = empDfObj.merge(salaryDfObj)
print('Contents of the Merged Dataframe :')
print(mergedDf)


# Merge two Dataframes on common columns using default inner join
mergedDf = empDfObj.merge(salaryDfObj, how='inner')
print('Contents of the Merged Dataframe :')
print(mergedDf)


# Merge two Dataframes on common columns using Left join
mergedDf = empDfObj.merge(salaryDfObj, how='left')
print('Contents of the Merged Dataframe :')
#print(mergedDf)

# Merge two Dataframes on common columns using right join
mergedDf = empDfObj.merge(salaryDfObj, how='right')
print('Contents of the Merged Dataframe :')
print(mergedDf)


# Merge two Dataframes on common columns using Outer join
mergedDf = empDfObj.merge(salaryDfObj, how='outer')
print('Contents of the Merged Dataframe :')
print(mergedDf)
