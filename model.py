import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data.csv")

# Features (inputs)
X = data[['time', 'beds_available', 'oxygen_available', 'staff_available']]

# Target (output)
y = data['patients']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_patients(time, beds, oxygen, staff):
    input_data = np.array([[time, beds, oxygen, staff]])
    prediction = model.predict(input_data)
    return prediction[0]

# Test prediction (optional - for checking)
if __name__ == "__main__":
    print("Sample Prediction:", predict_patients(6, 10, 8, 5))