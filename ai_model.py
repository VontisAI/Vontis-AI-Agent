import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data for training a simple regression model
def train_model():
    X = np.array([[1], [2], [3], [4]])  # Input data
    y = np.array([1, 2, 3, 4])          # Output data

    model = LinearRegression().fit(X, y)
    return model

def make_prediction(model, data):
    prediction = model.predict(np.array([[data]]))
    return prediction[0]
