"""
Розробити паралельну програму інтегрування методом Монте-Карло, використовуючи програму 5.3.
"""

import math
import random
import time
from mpi4py import MPI


def f(x):
    return math.sin(x) ** 2


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    numprocs = comm.Get_size()

    a = 0.0
    b = math.pi / 2
    N_total = 1_000_000_000
    n_per_procs = N_total // numprocs

    reference = math.pi / 4
    local_sum = 0.0

    start_time = MPI.Wtime()

    random.seed(time.time() + rank)

    for _ in range(n_per_procs):
        x = random.uniform(a, b)
        local_sum += f(x)

    total_sum = comm.reduce(local_sum, op=MPI.SUM)
    end_time = MPI.Wtime()

    if rank == 0:
        integral_mc = ((b - a) * total_sum) / N_total
        error = abs(reference - integral_mc)

        print(f"Result: {integral_mc:.16f}")
        print(f"Accurate number: {reference:.16f}")
        print(f"Error: {error:.15f}")
        print(f"Execution time: {end_time - start_time:.4f} sec")


if __name__ == "__main__":
    main()
