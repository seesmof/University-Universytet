import numpy as np


def circle_area(r: int | float):
    return np.pi * r**2


radius = 3
result = circle_area(radius)
print(f"{result} for {radius} radius.")
