import random
from matplotlib import pyplot as plt
import pandas as pd

samples = 3
data: dict = {
    "kind": [random.choice(["blue", "green"]) for _ in range(samples)],
    "tss": [random.randint(17, 27) for _ in range(samples)],
    "ta": [random.randint(6, 17) for _ in range(samples)],
    "ph": [round(random.uniform(2.8, 4.0), 1) for _ in range(samples)],
}
print(data)

df = pd.DataFrame(data=data)
print(df)

kind_labels = {value: number for number, value in enumerate(set(df["kind"].to_list()))}
print(kind_labels)

for index, element in enumerate(df["kind"]):
    df.at[index, "kind"] = kind_labels[df["kind"][index]]
print(df)


"""
seat_label = {value: number for number, value in enumerate(set(data["seat"]))}
data["seat"] = [seat_label[element] for element in data["seat"]]
df = pd.DataFrame(data=data)

plot = plt.scatter(
    x=df["age"], y=df["height"], c=df["seat"], cmap="viridis", label=seat_label
)
plt.legend(plot.legend_elements()[0], seat_label.keys())
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()
"""
