import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Read the data file
df = pd.read_csv("D:\Python\ETL Operations with Python\Files\DataForDecisionTree.txt")

# Preprocess the data by mapping string values to numerical values
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Separate the data into features and target variables
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Create a decision tree model and fit it to the data
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(20,10))
tree.plot_tree(dtree, feature_names=features, fontsize=12, filled=True)
plt.show()
