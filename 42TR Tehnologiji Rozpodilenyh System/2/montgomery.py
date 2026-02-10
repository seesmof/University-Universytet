def montgomery(a: int, n: int, m: int) -> int:
    binary_N = int(bin(n)[2:])

    y1 = a % m
    y2 = (a * a) % m

    for i in range(binary_N - 2, 0, -1):
        bit = (n >> i) & 1

        if bit == 1:
            y1 = (y1 * y2) % m
            y2 = (y2 * y2) % m
        else:
            y1 = (y1 * y1) % m
            y2 = (y1 * y2) % m

    return y1


a = 636737773
n = 262662666
m = 888272727
print(montgomery(a, n, m))
print(pow(a, n, m))
