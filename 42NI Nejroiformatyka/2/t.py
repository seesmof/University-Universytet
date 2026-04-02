from matplotlib import pyplot as plt
import numpy as np


x = np.arange(-5 * np.pi, 5 * np.pi, 0.1)
y = np.tanh(x)

plt.plot(x, y, color="green")
plt.grid()
plt.show()
