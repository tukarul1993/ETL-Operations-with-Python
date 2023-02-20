#Pandas Tutorial #3 – Get & Set Series Values


import pandas as pd
# Create a Series object from a list
names = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
                    index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(names)
# Access first element of the Series object
first_element = names[0]
print('First Element: ', first_element)
# Access 3rd element of the Series object
third_element = names[2]
print('Third Element: ', third_element)

names = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
                    index = ['a', 'b', 'c', 'd', 'e', 'f'])
# Access element at index position 10
print( names[5] )
# Access element with label 'd'
print( names['d'] )
# Access element with label 'k'
#print( names['k'] )

# Select elements from index label 'b' till label 'e'
print(names[1:3])       #start from 1 to (n-1)=3-1=2
print(names['b' : 'e'])


# Select elements at index position 2, 3 and 0 only
few_names = names[[2, 3, 0]]
# Display the subset of Series
print(few_names)


# Change the 3rd value of Series
names[2] = 'Sanjay'