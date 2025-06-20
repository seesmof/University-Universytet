from math import inf
import pprint
import random
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import Normalizer


def get_min(arr):
    min_so_far = 1000 * 1000
    for element in arr:
        if element < min_so_far:
            min_so_far = element
    return min_so_far


def get_max(arr):
    max_so_far = -1000 * 1000
    for element in arr:
        if element > max_so_far:
            max_so_far = element
    return max_so_far


data = [[random.randint(150, 170) for _ in range(10)] for _ in range(1)]
for i, row in enumerate(data):
    low = get_min(row) - 30
    high = get_max(row) + 30
    data[i] = sorted([low] + row + [high])
data = np.array(data)
print(data)

print()
for i, row in enumerate(data):
    print(sum(row))

scaler = Normalizer(norm="max")
normalized_data = scaler.fit_transform(data)
print(normalized_data)
