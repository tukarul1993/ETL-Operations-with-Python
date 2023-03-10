from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate a random classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_classes=2, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a gradient boosting classifier with 100 trees
gbc = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Fit the model on the training data
gbc.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = gbc.predict(X_test)

# Evaluate the model performance on the testing data
accuracy = gbc.score(X_test, y_test)
print("Accuracy:", accuracy)
