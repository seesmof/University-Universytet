from collections import namedtuple
import random
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

Person = namedtuple("Person", "age,gender,height,steps")
data = [
    Person(
        age=random.randint(30, 70),
        gender=random.choice([0, 1]),
        height=random.randint(150, 190),
        steps=random.randint(10, 2000),
    )
    for _ in range(100)
]
df = DataFrame(data, columns=Person._fields)
print(df.head())

plt.figure(figsize=(8, 5))
plt.scatter(df.age, df.steps)
plt.xlabel("Age")
plt.ylabel("Steps (thousands)")
plt.show()

y = df.steps.to_numpy()
df = df.drop(["steps"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(df.to_numpy(), y)
model = KMeans(n_clusters=2)
model.fit(X_train, y_train)
results = model.predict(X_test)
print(model.cluster_centers_)
print(results)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), tight_layout=True)
for feature_number, axis in enumerate(ax):
    plot = axis.scatter(X_test[:, feature_number], y_test, c=results, cmap="berlin")
    axis.set_xlabel(Person._fields[feature_number].capitalize())
    axis.set_ylabel("Steps (thousands)")
fig.legend(plot.legend_elements()[0], [f"Cluster {i}" for i in range(2)])
plt.show()
