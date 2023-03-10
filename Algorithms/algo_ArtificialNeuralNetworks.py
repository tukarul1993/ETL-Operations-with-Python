import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Define the input and output data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a sequential model
model = Sequential()

# Add a dense layer with 2 input nodes and 4 output nodes
model.add(Dense(4, input_dim=2, activation='sigmoid'))

# Add a dense layer with 1 output node
model.add(Dense(1, activation='sigmoid'))

# Compile the model with binary crossentropy loss and adam optimizer
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model on the input and output data
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate the model performance on the input and output data
_, accuracy = model.evaluate(X, y)
print("Accuracy:", accuracy)
