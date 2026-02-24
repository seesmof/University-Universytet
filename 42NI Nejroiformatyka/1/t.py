from matplotlib import pyplot as plt
import numpy as np


def sigmoid(x):
    return 2 / (1 + np.exp(-2 * x)) - 1


x = np.linspace(-10, 10, 100)
y = sigmoid(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Sigmoid Function", color="green")

plt.xlabel("Input (x)")
plt.ylabel("Output (Sigmoid (x))")
plt.title("Sigmoidal Activation Function Plot")
plt.grid(True)
plt.legend()
plt.show()
