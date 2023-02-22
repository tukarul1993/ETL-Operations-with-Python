import pandas as pd
# Create first Series object from a list
first = pd.Series(  [100, 200, 300, 400, 500],
                    index = ['a', 'b', 'e', 'f', 'g'])
# Create second Series object from a list
second = pd.Series( [11, 12, 13, 14],
                    index = ['a', 'b', 'h', 'g'])
# Add two Series objects together
total = first.add(second)
# DIsplay the Series object
#print(total)

#Labels matching for adding


# Create first Series object from a list
first = pd.Series(  [100, 200, 300, 400, 500],
                    index = ['a', 'b', 'e', 'f', 'g'])
# Create second Series object from a list
second = pd.Series( [11, 12, 13, 14],
                    index = ['a', 'b', 'h', 'i'])
# Add two Series objects together
total = first.add(second, fill_value=0)
# DIsplay the Series object
#print(total)



# Create first Series object from a list
first = pd.Series(  [100, 200, 300, 400, 500],
                    index = ['a', 'b', 'e', 'f', 'g'])
# Create a Series object from a list
second = pd.Series( [11, 12, 13, 14],
                    index = ['a', 'b', 'h', 'i'])
# Subtract second Series from first Series
finalObj = first.sub(second)
# Display the Series object
print(finalObj)




# Create first Series object from a list
first = pd.Series(  [100, 200, 300, 400, 500],
                    index = ['a', 'b', 'e', 'f', 'g'])
# Create a Series object from a list
second = pd.Series( [11, 12, 13, 14],
                    index = ['a', 'b', 'h', 'i'])
# Subtract second Series from first Series
finalObj = first.sub(second, fill_value=0)
# Display the Series object
print(finalObj)


# Create a Series object from a list
names = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
                    index = ['a', 'b', 'c', 'd', 'e', 'f'])
print('Original Series: ')
print(names)
# Delete elements at given index labels
names = names.drop(['b', 'c', 'e'])
print('Modified Series: ')
print(names)




# Create a Series object from a list
numbers = pd.Series([100, 200, 300, 400, 500],
                    index = ['a', 'b', 'e', 'f', 'g'])
print(numbers)
# Get the sum of all numeric values in Series
total = numbers.sum()
print('Sum is: ', total)
# Get largest value from the Series
max_value = numbers.max()
print('Maximum value is: ', max_value)