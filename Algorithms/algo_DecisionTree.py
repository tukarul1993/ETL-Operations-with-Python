
#https://www.xoriant.com/blog/decision-trees-for-classification-a-machine-learning-algorithm


# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()

# Create feature and target arrays
X = iris.data[:, :2]
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a decision tree model and fit it to the training data
dt_model = DecisionTreeClassifier(max_depth=3)
dt_model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = dt_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = np.mean(y_pred == y_test)

# Plot the decision tree
plt.figure(figsize=(10,8))
plot_tree(dt_model, filled=True)
plt.show()
