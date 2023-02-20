############## Exact opposite of "pandasDF2.py"

import pandas as pd
def main():
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', 1500)
    print('*** Creating Dataframe 1 ***')
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
    print("Dataframe 1 : ")
    print(empDfObj)
    print('*** Creating Dataframe 2 ***')
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
    print("Dataframe 2 : ")
    print(salaryDfObj)
    print('**** Merge two Dataframes on index of both dataframes ****')
    # Merge two Dataframes on index of both the dataframes
    mergedDf = empDfObj.merge(salaryDfObj, left_index=True, right_index=True)
    print('Contents of the Merged Dataframe :')
    print(mergedDf)
    print('Change the index of dataframe 2')

    # Modify Dataframe 1 by reseting the Index and adding a new column EmpID
    empDfObj['EmpID'] = empDfObj.index
    empDfObj.reset_index(inplace=True)
    del empDfObj['ID']
    print("Dataframe 1 : ")
    print(empDfObj)
    print('**** Merge two Dataframes on index of one dataframe and some column of other dataframe ****')

    # Merge two Dataframes on index of both the dataframes
    mergedDf = empDfObj.merge(salaryDfObj, right_index=True, left_on='EmpID')
    mergedDf = mergedDf.set_index('EmpID')
    print('Contents of the Merged Dataframe :')
    print(mergedDf)
if __name__ == '__main__':
  main()