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

from collections import namedtuple
import pprint
import random
from matplotlib import pyplot as plt
from pandas import DataFrame

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
print(df.head())
