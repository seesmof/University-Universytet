"""
Програму 5.2 доповніть функцією обчислення часу її виконання та функцією обчислення дисперсії σ2 випадкової величини значення π.
причому, оскільки середнє значення заздалегідь не відомо, зручніше використати формулу
"""

import math
import random
import sys
import time
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    numprocs = comm.Get_size()

    n_in_proc = 1_000_000
    R = 0.5
    pi_reference = math.pi

    n_iterations = 0
    if rank == 0:
        if len(sys.argv) > 1:
            n_iterations = int(sys.argv[1])
        else:
            n_iterations = 10

    n_iterations = comm.bcast(n_iterations, root=0)

    pi_values = []

    start_time = MPI.Wtime()

    for i in range(n_iterations):
        random.seed(time.time() + rank + i)

        in_circle_local = 0
        for _ in range(n_in_proc):
            x = random.uniform(-0.5, 0.5)
            y = random.uniform(-0.5, 0.5)
            if x * x + y * y < R * R:
                in_circle_local += 1

        total_in_circle = comm.reduce(in_circle_local, op=MPI.SUM, root=0)

        if rank == 0:
            total_points_iter = n_in_proc * numprocs
            xi = 4.0 * (total_in_circle / total_points_iter)
            pi_values.append(xi)
            print(f"Iteration {i + 1}: pi = {xi:.10f}")

    end_time = MPI.Wtime()

    if rank == 0:
        n = len(pi_values)
        sum_xi = sum(pi_values)
        sum_xi_sq = sum(x**2 for x in pi_values)

        pi_final = sum_xi / n

        variance = (1.0 / (n + 1)) * (sum_xi_sq - (1.0 / n) * (sum_xi**2))

        execution_time = end_time - start_time

        print("--- Results ---")
        print(f"Amount of iterations (N): {n}")
        print(f"Dots per iteration:       {n_in_proc * numprocs}")
        print(f"Final PI (mean):          {pi_final:.16f}")
        print(f"Error:                    {abs(pi_reference - pi_final):.16f}")
        print(f"Variance (sigma^2):       {variance:.16e}")
        print(f"Execution time:           {execution_time:.6f} sec")


if __name__ == "__main__":
    main()
