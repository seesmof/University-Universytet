def linear(c: int, x: int):
    return c * x


def heavyside(x: int):
    return 1 if x >= 0 else 0


def linera_bipolar(x, k, a1, a2):
    return 1 if x > a2 else k * x if a1 <= x <= a2 else -1


# Linear
c = 5
x = 10
res = linear(c, x)
print(f"{c=} * {x=} = {res}")

# Heavyside
x = -2
res = heavyside(x)
print(res)

# Linear Bipolar
x = 3
a1, a2 = 0, 10
k = 5
res = linera_bipolar(x, k, a1, a2)
print(res)
