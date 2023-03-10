# Import the necessary libraries
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Load the digits dataset
digits = load_digits()

# Create feature and target arrays
X = digits.data
y = digits.target

# Create a PCA object and fit it to the data
pca = PCA(n_components=2)
pca.fit(X)

# Transform the data into the new coordinate system
X_transformed = pca.transform(X)

# Plot the transformed data
plt.scatter(X_transformed[:,0], X_transformed[:,1], c=y)
plt.colorbar()
plt.show()
