import matplotlib.pyplot as plt
import numpy as np

y = [100, 80, 60, 40, 50, 30, 70, 100]
x = np.arange(1, len(y) + 1)

plt.plot(x, y)
plt.grid()
plt.show()
