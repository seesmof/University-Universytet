def weighted_sum(x, w):
    return sum([xi * wi for xi, wi in zip(x, w)])


x = [10, 2, 0]
w = [0.8, 0.2, 0]

res = weighted_sum(x, w)
print(res)
