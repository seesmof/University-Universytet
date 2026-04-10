def linear(c: int, x: int):
    return c * x


def heavyside(x: int):
    return 1 if x >= 0 else 0


# Linear
c = 5
x = 10
res = linear(c, x)
print(f"{c=} * {x=} = {res=}")

# Heavyside
x = -2
res = heavyside(x)
print(res)
