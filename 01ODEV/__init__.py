import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])


scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(data)

print("Original Data:")
print(data)
print("\nNormalized Data:")
print(normalized_data)


data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])

scaler = StandardScaler()

# Standardize the data
standardized_data = scaler.fit_transform(data)

print("Original Data:")
print(data)
print("\nStandardized Data:")
print(standardized_data)