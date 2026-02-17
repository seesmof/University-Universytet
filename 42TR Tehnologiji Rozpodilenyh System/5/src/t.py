def f(x):
    return x**2


def rectangle_method(a, b, n):
    h = (b - a) / n

    mid_sum = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        mid_sum += f(x_mid)

    return mid_sum * h


start = 0
end = 3
steps = 1_000

result = rectangle_method(start, end, steps)

print(f"Results using central rectangles method: {result:.4f}")
