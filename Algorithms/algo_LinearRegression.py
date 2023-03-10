# Import the necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Create sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

print(X)
# Create a linear regression model
reg = LinearRegression()

# Fit the model to the data
reg.fit(X, y)

# Make a prediction for a new data point
new_X = np.array([6]).reshape(-1, 1)
predicted_y = reg.predict(new_X)

# Print the coefficients and the predicted value
print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)
print("Predicted value:", predicted_y[0])
