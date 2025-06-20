from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import Normalizer


d = [150, 190, 130, 160, 155, 158, 163]
d = sorted(d)
d = np.array(d)
print(d)

plt.plot(d, "o")
plt.show()

scaler = Normalizer(norm="max")
