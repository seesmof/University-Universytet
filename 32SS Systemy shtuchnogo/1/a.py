import os
import random
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, normalize

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "train.csv")
data = pd.read_csv(file_path)

# 1.1 Еталони

needed = "Name,Age,Survived".split(",")
data = data[needed].dropna()

survived_label = data.Survived.to_numpy()
data = data.drop(["Survived"], axis=1)
data = data.drop(["Name"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(data, survived_label)
model = KMeans(n_clusters=3)
model.fit(X_train)
print(f"{model.cluster_centers_ = }")
prediction_results = model.predict(X_test)
print(f"{prediction_results = }")

# 1.2 Вибірка


def get_target_feature(row: list[int]):
    if row[0] ** 2 + row[1] ** 2 < variant**2 + 0.04 * size**2:
        return 0
    elif row[0] ** 2 + row[1] ** 2 >= variant**2 + 0.04 * size**2:
        return 1


variant = 19
size = 5 * variant
number_of_features = 3 * variant

ones_range = range(1, size, 4)
twos_range = range(2, size, 4)
threes_range = range(3, size, 4)
features_input = []
targets_input = []
for data_row in range(1, size):
    row = []
    for feature_col in range(1, number_of_features):
        if feature_col in ones_range:
            result = feature_col * variant - 0.1 * data_row
        elif feature_col in twos_range:
            result = 0.01 * feature_col * variant**-1
        elif feature_col in threes_range:
            result = feature_col * random.random()
        row.append(result)

    targets_input.append(get_target_feature(row=row))
    features_input.append(row)
features = np.array(features_input)
targets = np.array(targets_input)
print(f"{features = }")
print(f"{targets = }")

# 1.3 Нормування

normalized_features = normalize(features, norm="max")
print([float(round(n, 3)) for n in sorted(features[0])])
print([float(round(n, 3)) for n in sorted(normalized_features[0])])
max_max = max([max(features[i]) for i in range(len(features))])
print(max_max)
