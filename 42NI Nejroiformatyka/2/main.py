import numpy as np
import random

X = np.random.rand(500, 18)
y = [random.choice([-1, 1]) for _ in range(500)]

for row_i, row in enumerate(X):
    row_average = np.mean(row)

    for cel_i, el in enumerate(row):
        if el < row_average:
            X[row_i][cel_i] = -1
        elif el >= row_average:
            X[row_i][cel_i] = 1

# --- Хопфілд ---

"""
hopfield_net = cpl.HopfieldNet(num_cells=35)
# hopfield = HopfieldNetwork(N=19)
print(hopfield_net.train(X))
"""

# --- Ельман ---
# подивитись ельмана
