import pandas as pd


# List of Tuples
empoyees = [ (11, 'jack', 34, 'Sydney', 5) ,
           (12, 'Riti', 31, 'Delhi' , 7) ,
           (13, 'Aadi', 16, 'New York', 11) ,
           (14, 'Mohit', 32,'Delhi' , 15) ,
           (15, 'Veena', 33, 'Delhi' , 4) ,
           (16, 'Shaunak', 35, 'Mumbai', 5 ),
            (17, 'Shaun', 35, 'Colombo', 11)
            ]
# Create a DataFrame object
empDfObj = pd.DataFrame(empoyees, columns=['ID', 'Name', 'Age', 'City', 'Experience'])
empDfObj = empDfObj.set_index('ID')
#print(empDfObj)


# List of Tuples
salaries = [(11, 'Junior', 70000, 1000) ,
           (12, 'Senior', 72200, 1100) ,
           (13, 'Expert', 84999, 1000) ,
           (14, 'Expert', 90000, 2000) ,
           (15, 'Junior', 61000, 1500) ,
           (16, 'Junior', 71000, 1000),
           (21, 'Senior',81000, 2000)
            ]
# Create a DataFrame object
salaryDfObj = pd.DataFrame(salaries, columns=['ID', 'Experience', 'Salary', 'Bonus'], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
salaryDfObj = salaryDfObj.set_index('ID')
#print(salaryDfObj)


# Merge two Dataframes on index of both the dataframes
mergedDf = empDfObj.merge(salaryDfObj, left_index=True, right_index=True)

print(salaryDfObj)
# Modify Dataframe 2 by reseting the Index and adding a new column EmpID
salaryDfObj['EmpID'] = salaryDfObj.index
salaryDfObj.reset_index(inplace=True)
del salaryDfObj['ID']

print(salaryDfObj)


# Merge two Dataframes on index of both the dataframes
mergedDf = empDfObj.merge(salaryDfObj, left_index=True, right_on='EmpID')
mergedDf = mergedDf.set_index('EmpID')

print(mergedDf)
