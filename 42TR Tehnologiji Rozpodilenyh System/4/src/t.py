import math
import random

N = 240_000
sum: float = 0.0
for i in range(N):
    a_i = random.uniform(-1, 1)
    x_i = 0.0001 * i
    sum += a_i * math.sin(x_i)
print(f"{sum = }")
