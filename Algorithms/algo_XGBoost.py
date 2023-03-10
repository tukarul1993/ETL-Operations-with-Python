import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate a random classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_classes=2, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an XGBoost classifier with 100 trees
xgb_clf = xgb.XGBClassifier(n_estimators=100, random_state=42)

# Fit the model on the training data
xgb_clf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = xgb_clf.predict(X_test)

# Evaluate the model performance on the testing data
accuracy = xgb_clf.score(X_test, y_test)
print("Accuracy:", accuracy)
