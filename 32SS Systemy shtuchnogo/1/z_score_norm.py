import math
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


def get_mean(data: list) -> float:
    return sum(data) / len(data)


def get_standard_deviation(data: list) -> float:
    mean = get_mean(data=data)
    squares = sum((element - mean) ** 2 for element in data)
    average = squares / len(data)
    return math.sqrt(average)


for column_number in range(COLUMNS):
    column_data = data[:, column_number]
    for el in column_data:
        value = el - get_mean(column_data)
        value /= get_standard_deviation(column_data)
        print(el, float(value))
    print()
