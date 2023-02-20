import pandas as pd
# Create a Series object from a list
users = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
                    index = ['a', 'b', 'c', 'd', 'e', 'f'],
                    name = "Students")
# Display the Pandas Series
print(users.values)
print(users.dtypes)
print(users.dtype)
print(users.index)
print(users.items())
print(list(users.values))
# Get the count of elements in Series
print(users.size)
# check if series is empty or not
print(users.empty)


# Get first 3 elements of series
subset = users.head(3)
# Display the Subset of Series
print(subset)

# Get last 3 elements of series
subset = users.tail(3)
# Display the Subset of Series
print(subset)
print(users.count())