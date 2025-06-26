import pprint
import random
from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
import seaborn as sns

COLUMNS = 5
ROWS = 5
data = [[random.randint(300, 800) for _ in range(COLUMNS)] for _ in range(ROWS)]
data = np.array(data)
pprint.pprint(data)

for column_number in range(COLUMNS):
    column_data = data[:, column_number]
    for el in column_data:
        value = el - min(column_data)
        value /= max(column_data) - min(column_data)
        print(el, float(value))
    print()
