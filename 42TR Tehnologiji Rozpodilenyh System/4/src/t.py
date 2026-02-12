import time
from mpi4py import MPI
import numpy as np

N: int = 400000
M = np.array(0, dtype="i")

np.random.seed(int(time.time()))
x = (-1.073741824 + np.random.rand(N) * 1e-9).astype("f8")
a = ((-1.073741824 + np.random.rand(N) * 1e-9) * 0.1).astype("f8")
M.fill(N // 4)
print(a)
