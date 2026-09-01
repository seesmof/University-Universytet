import numpy as np

actual = np.array([10, 20, 30, 40, 50])
predicted = np.array([12, 18, 32, 38, 48])

result = sum((actual - predicted) ** 2) / len(actual)
print(result)
