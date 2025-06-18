from collections import namedtuple
import pprint
import random
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

names = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Oliver",
    "Amelia",
    "Theodore",
    "Charlotte",
    "James",
    "Mia",
]

Instance = namedtuple("Instance", "name, age, height, chosen_car")

data = [
    Instance(
        name=random.choice(names),
        age=random.randint(30, 70),
        height=random.randint(150, 170),
        chosen_car=random.choice([0, 1, 2]),
    )
    for _ in range(100)
]
pprint.pprint(data)

df = DataFrame(data, columns=Instance._fields)
y = df["chosen_car"]
df = df.drop(["chosen_car", "name"], axis=1)
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3)

model = LinearRegression()
trainings = model.fit(X_train, y_train)
results = model.predict(X_test)
print(results)

plt.scatter(df.age, results)
plt.show()
