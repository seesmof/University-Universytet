import random

from matplotlib import pyplot as plt


ages = [random.randint(30, 70) for _ in range(10)]
print(ages)
plt.plot(ages)
plt.show()
