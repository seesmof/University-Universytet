from matplotlib import pyplot as plt
import numpy as np


def relu(x):
    return np.maximum(0, x)


x = np.linspace(-10, 10, 100)
y = relu(x)

plt.figure(figsize=(10, 7))
plt.plot(x, y, label="ReLU Function")
plt.title("ReLU Activation Function Plot")
plt.xlabel("Input (x)")
plt.ylabel("Output (f(x) = max(0,x))")
plt.grid(True)
plt.legend()
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.show()
