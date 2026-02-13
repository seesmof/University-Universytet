import random
import time
import numpy as np

N = 240_000
arr = np.array([random.uniform(-1, 1) for _ in range(N)], dtype="d")
print(arr)
