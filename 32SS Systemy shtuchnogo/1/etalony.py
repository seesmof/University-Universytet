import math
import pprint
import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
import seaborn as sns

tss_range = (17, 27)
ta_range = (6, 17)
ph_range = (2.8, 4.0)
grape_kinds = ["blue", "green"]

samples = 3
generated_data = {
    "kind": [random.choice(grape_kinds) for _ in range(samples)],
    "ph": [round(random.uniform(*ph_range), 1) for _ in range(samples)],
    "ta": [random.randint(*ta_range) for _ in range(samples)],
    "tss": [random.randint(*tss_range) for _ in range(samples)],
}
kind_labels = {value: number for number, value in enumerate(grape_kinds)}
feature_sums = dict()
class_centers = dict()

df = pd.DataFrame(data=generated_data)
pprint.pprint(df)

for sample_number, sample in df.iterrows():
    df.at[sample_number, "kind"] = kind_labels[df["kind"][sample_number]]

for feature_name, feature_samples in df.items():
    if feature_name == "kind":
        continue

    df[feature_name] = df[feature_name].astype(float)
    samples_sum = math.sqrt(sum(sample**2 for sample in feature_samples))
    for sample_number, sample_value in enumerate(feature_samples):
        normalized_value = sample_value / samples_sum
        df.at[sample_number, feature_name] = round(normalized_value, 2)

    feature_sums[feature_name] = samples_sum
pprint.pprint(df)

"""
# Plotting
plot = plt.scatter(
    x=df["tss"],
    y=df["ta"],
    c=df["kind"],
    label=kind_labels,
)
plt.xlabel("Total Soluble Solids")
plt.ylabel("Titratable (Relative) Acidity")
plt.legend(plot.legend_elements()[0], kind_labels.keys())
plt.show()
"""

for class_number in kind_labels.values():
    center = {
        "ph": float(round(df[df["kind"] == class_number]["ph"].mean(), 2)),
        "ta": float(round(df[df["kind"] == class_number]["ta"].mean(), 2)),
        "tss": float(round(df[df["kind"] == class_number]["tss"].mean(), 2)),
    }
    class_centers[class_number] = center
pprint.pprint(class_centers)

new_sample = {
    "ph": round(random.uniform(*ph_range), 1),
    "ta": random.randint(*ta_range),
    "tss": random.randint(*tss_range),
}
pprint.pprint(new_sample)

for feature, value in new_sample.items():
    feature_sum = feature_sums[feature]
    new_sample[feature] = round(value / feature_sum, 2)
pprint.pprint(new_sample)

distances = dict()
for class_number in class_centers.keys():
    center_values = np.array(list(class_centers[class_number].values()))
    new_sample_values = np.array(list(new_sample.values()))
    distance_to_class = math.sqrt(sum((new_sample_values - center_values) ** 2))
    distances[distance_to_class] = class_number
print(distances)

sorted_distances = sorted(list(distances.keys()))
print(sorted_distances)

predicted_class = 0
if len(sorted_distances) == 1 or sorted_distances[0] != sorted_distances[1]:
    predicted_class = distances[sorted_distances[0]]
elif sorted_distances[0] == sorted_distances[1]:
    number_of_samples_one = len(df[df["kind"] == distances[sorted_distances[0]]])
    number_of_samples_two = len(df[df["kind"] == distances[sorted_distances[1]]])
    predicted_class = (
        distances[sorted_distances[0]]
        if number_of_samples_one >= number_of_samples_two
        else distances[sorted_distances[1]]
    )
pprint.pprint(predicted_class)

df.loc[-1] = [predicted_class] + list(new_sample.values())
df.index = df.index + 1
df = df.sort_index()
df["kind"] = df["kind"].astype(int)
pprint.pprint(df)
