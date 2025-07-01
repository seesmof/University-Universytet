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

samples = 4
generated_data = {
    "kind": [random.choice(["blue", "green"]) for _ in range(samples)],
    "tss": [random.randint(*tss_range) for _ in range(samples)],
    "ta": [random.randint(*ta_range) for _ in range(samples)],
    "ph": [round(random.uniform(*ph_range), 1) for _ in range(samples)],
}
kind_labels = {
    value: number for number, value in enumerate(set(generated_data["kind"]))
}
feature_sums = dict()
cluster_centers = dict()

df = pd.DataFrame(data=generated_data)
pprint.pprint(df)

for sample_number, sample in enumerate(df["kind"]):
    df.at[sample_number, "kind"] = kind_labels[df["kind"][sample_number]]

for feature_name, feature_samples in df.items():
    if feature_name == "kind":
        continue

    df[feature_name] = df[feature_name].astype(float)
    samples_sum = math.sqrt(sum(feature**2 for feature in feature_samples))
    for sample_index, sample_value in enumerate(feature_samples):
        normalized_value = sample_value / samples_sum
        df.at[sample_index, feature_name] = round(normalized_value, 2)

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
        "tss": float(round(df[df["kind"] == class_number]["tss"].mean(), 2)),
        "ta": float(round(df[df["kind"] == class_number]["ta"].mean(), 2)),
        "ph": float(round(df[df["kind"] == class_number]["ph"].mean(), 2)),
    }
    cluster_centers[class_number] = center

new_sample = {
    "tss": random.randint(*tss_range),
    "ta": random.randint(*ta_range),
    "ph": round(random.uniform(*ph_range), 1),
}
pprint.pprint(new_sample)

for feature in new_sample:
    sample_value = new_sample[feature]
    feature_sum = feature_sums[feature]
    new_sample[feature] = round(sample_value / feature_sum, 2)
pprint.pprint(new_sample)

distances = dict()
for class_number in cluster_centers:
    values = np.array(list(cluster_centers[class_number].values()))
    new_sample_values = np.array(list(new_sample.values()))
    distance = math.sqrt(sum((values - new_sample_values) ** 2))
    distances[distance] = class_number

sorted_distances = sorted(list(distances.keys()))
predicted_class = 0
if len(sorted_distances) <= 1 or sorted_distances[0] != sorted_distances[1]:
    predicted_class = distances[sorted_distances[0]]
elif sorted_distances[0] == sorted_distances[1]:
    first_length = len(df[df["kind"] == distances[sorted_distances[0]]])
    second_length = len(df[df["kind"] == distances[sorted_distances[1]]])
    predicted_class = (
        distances[sorted_distances[0]]
        if first_length < second_length
        else distances[sorted_distances[1]]
    )
pprint.pprint(predicted_class)

df.loc[-1] = [predicted_class] + list(new_sample.values())
df.index = df.index + 1
df = df.sort_index()
df["kind"] = df["kind"].astype(int)
pprint.pprint(df)
