import numpy as np


class Coordinates:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = y
        self.y = y


def euclidean_distance(one: Coordinates, two: Coordinates):
    first_part = (two.x - one.x) ** 2
    second_part = (two.y - one.y) ** 2
    return np.sqrt(first_part + second_part)


one = Coordinates(x=0, y=5)
two = Coordinates(x=12, y=1)
distance = euclidean_distance(one, two)
print(distance)
