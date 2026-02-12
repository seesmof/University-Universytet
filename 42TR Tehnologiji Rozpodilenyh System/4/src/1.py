"""
code taken from https://github.com/MolSSI-Education/parallel-programming/blob/main/examples/mpi4py/example2/example2.py
"""

from mpi4py import MPI
import numpy as np

N: int = 240000


def main():
    N: int = 10_000_000
    a = np.ones(N)
    b = np.zeros(N)
    c: list[float] = list()

    for i in range(N):
        b[i] = 1.0 + i

    for i in range(N):
        c.append(a[i] + b[i])

    sum: float = 0.0
    average: float = 0
    for i in range(N):
        sum += c[i]
    average = sum // N
    print(f"{average=}")


if __name__ == "__main__":
    main()
