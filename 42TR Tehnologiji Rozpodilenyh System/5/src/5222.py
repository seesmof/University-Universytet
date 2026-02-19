"""
Використовуючи формули (5.9) визначити N таке, щоб похибка EPSILON обчислення числа PI наближено дорівнювала 10^-4.
"""

import math
import random
import time
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    epsilon = 1e-4
    # N = pi*(4-pi) / epsilon^2
    total_n = int(2.697 * (epsilon**-2))

    local_n = total_n // size
    if rank == size - 1:
        local_n += total_n % size

    random.seed(time.time() + rank)
    count = 0

    start_time = MPI.Wtime()

    for _ in range(local_n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            count += 1

    total_count = comm.reduce(count, op=MPI.SUM, root=0)
    end_time = MPI.Wtime()

    if rank == 0:
        pi_approx = 4.0 * total_count / total_n
        actual_error = abs(math.pi - pi_approx)

        print(f"--- Results for epsilon = {epsilon} ---")
        print(f"Total number of dots (N): {total_n}")
        print(f"Calculated PI: {pi_approx:.10f}")
        print(f"Actual error: {actual_error:.10e}")
        print(f"Execution time for {size} processors: {end_time - start_time:.4f} sec")


if __name__ == "__main__":
    main()
