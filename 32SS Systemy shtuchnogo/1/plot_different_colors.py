import random

from matplotlib import pyplot as plt
import pandas as pd

samples = 50
data: dict = {
    "seat": [random.choice(["front", "back"]) for _ in range(samples)],
    "age": [random.randint(18, 50) for _ in range(samples)],
    "height": [random.randint(150, 190) for _ in range(samples)],
}
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
