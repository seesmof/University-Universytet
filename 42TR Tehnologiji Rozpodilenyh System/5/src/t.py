import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = 2 * x**2 + 3 * x + 10

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="y = 2x^2 + 3x + 10")

plt.title("LInear Function: y = 2x^2 + 3x + 10")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()
