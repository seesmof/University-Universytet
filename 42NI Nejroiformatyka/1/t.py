from matplotlib import pyplot as plt
import numpy as np

x = [200, 300, 400, 500]
y = [1.0, 1.2, 1.4, 1.6]

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Relationship", color="green")

plt.xlabel("Values")
plt.ylabel("Fractions")
plt.grid(True)
plt.legend()
plt.show()
