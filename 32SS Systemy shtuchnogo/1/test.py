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
print(data)

survived_label = data.Survived.to_numpy()
data = data.drop(["Survived", "Name"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(data, survived_label)
model = KMeans(n_clusters=3)
model.fit(X_train)
print(f"{model.cluster_centers_ = }")
prediction_results = model.predict(X_test)
print(f"{prediction_results = }")

# 1.2 Вибірка


def get_target_feature(row: list[int]):
    if row[0] ** 2 + row[1] ** 2 < variant**2 + 0.04 * dataset_size**2:
        return 0
    elif row[0] ** 2 + row[1] ** 2 >= variant**2 + 0.04 * dataset_size**2:
        return 1


variant = 19
dataset_size = 5 * variant
features_count = 3 * variant

ones_range = range(1, dataset_size, 4)
twos_range = range(2, dataset_size, 4)
threes_range = range(3, dataset_size, 4)
features_holder = []
targets_holder = []
for sample_number in range(1, dataset_size):
    sample_features = []
    for feature_number in range(1, features_count):
        if feature_number in ones_range:
            prediction_results = feature_number * variant - 0.1 * sample_number
        elif feature_number in twos_range:
            prediction_results = 0.01 * feature_number * variant**-1
        elif feature_number in threes_range:
            prediction_results = feature_number * random.random()
        sample_features.append(prediction_results)

    targets_holder.append(get_target_feature(row=sample_features))
    features_holder.append(sample_features)
features = np.array(features_holder)
target = np.array(targets_holder)
print(f"{features = }")
print(f"{target = }")

df = pd.DataFrame(data=features)
df["target"] = target
print(df)

# 1.3 Нормування

normalized_features = normalize(features)
print(f"{normalized_features = }")

# 1.4 Побудова моделі

features_train, features_test, targets_train, targets_test = train_test_split(
    normalized_features, target
)

start_time = time.perf_counter()
model = KMeans(n_clusters=features_count)
model.fit(features_train)
end_time = time.perf_counter()
learning_time = end_time - start_time
print(f"{learning_time = }")
print(f"{model.cluster_centers_ = }")

# 1.5 Розпізнавання

start_time = time.perf_counter()
prediction_results = model.predict(features_test)
print(f"{prediction_results = }")
end_time = time.perf_counter()
prediction_time = end_time - start_time
print(f"{prediction_time = }")

# 1.6 Помилка

original_prediction_error = model.score(features_test)
print(f"{original_prediction_error = }")
original_error_probability = original_prediction_error / dataset_size * features_count
original_correct_probability = 1 - original_error_probability
print(f"{original_error_probability = }")
print(f"{original_correct_probability = }")

# 1.7 Нова вибірка

single_features = [row[variant] for row in features_holder]
print(f"{single_features = }")
single_center = int(prediction_results[variant])
print(f"{single_center = }")
single_target = get_target_feature(row=single_features)
print(f"{single_target = }")

# 1.8 Розпізнавання

single_features = np.array(single_features).reshape(-1, 1)
model = model.fit(single_features)
prediction_results = model.predict(single_features)
print(f"{prediction_results = }")

# 1.9 Помилка

prediction_error = model.score(single_features)
print(f"{prediction_error = }")
short_error_probability = prediction_error / len(single_features) * 1
short_correct_probability = 1 - short_error_probability
print(f"{short_error_probability = }")
print(f"{short_correct_probability = }")

# 1.10 Порівняння

prediction_error_difference = abs(original_prediction_error - prediction_error)
error_probability_difference = abs(original_error_probability - short_error_probability)
correct_probability_difference = abs(
    original_correct_probability - short_correct_probability
)
print(f"{prediction_error_difference = }")
print(f"{error_probability_difference = }")
print(f"{correct_probability_difference = }")

# 1.10.1 Порівняння таблицею

errors_table = pd.DataFrame(
    {
        "Error": [original_error_probability, short_error_probability],
        "Correct": [original_correct_probability, short_correct_probability],
    },
    index=["Original", "Shortened"],
)
print(errors_table)
