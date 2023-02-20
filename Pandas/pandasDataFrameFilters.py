import pandas as pd
# List of Tuples
students = [('Mark',  'Apples', 44),
            ('Aadi',  'Mangos', 31),
            ('Shaun', 'Grapes', 30),
            ('Simi',  'Apples', 32),
            ('Luka',  'Mangos', 43),
            ('Mike',  'Apples', 45),
            ('Arun',  'Mangos', 35),
            ('Riti',  'Grapes', 37),]
# Create a DataFrame object
df = pd.DataFrame(  students,
                    columns = ['Name' , 'Product', 'Sale'])

#print(df)
print(df['Product'] == 'Apples')
print(df[df['Product'] == 'Apples'])
print(df[(df['Sale'] > 30) & (df['Sale'] < 40)])


print(df[df['Sale']==30])
print(df[df['Sale']!=30])
print(df[df['Sale']%2==0])