"""
Підібрати для знайденого N параметри N_in_proc та n_in_proc для випадку використання двох та чотирьох процесів і за допомогою доповненої програми обчислити число PI, показати, що виконується відношення (5.8).
"""

import math
import random
import time
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size == 2:
        n_iterations = 135
    elif size == 4:
        n_iterations = 67
    else:
        n_iterations = 100

    n_in_proc = 1_000_000
    R = 0.5

    pi_values = []
    start_time = MPI.Wtime()

    for i in range(n_iterations):
        random.seed(time.time() + rank + i)
        in_circle_local = 0
        for _ in range(n_in_proc):
            x = random.uniform(-0.5, 0.5)
            y = random.uniform(-0.5, 0.5)
            if x * x + y * x <= R * R:
                in_circle_local += 1

        total_in_circle = comm.reduce(in_circle_local, op=MPI.SUM, root=0)

        if rank == 0:
            points_this_iter = n_in_proc * size
            xi = 4.0 * (total_in_circle / points_this_iter)
            pi_values.append(xi)

    end_time = MPI.Wtime()

    if rank == 0:
        N_total = n_iterations * n_in_proc * size
        sum_xi = sum(pi_values)
        sum_xi_sq = sum(x**2 for x in pi_values)

        pi_final = sum_xi / n_iterations
        variance = (1.0 / (n_iterations + 1)) * (
            sum_xi_sq - (1.0 / n_iterations) * (sum_xi**2)
        )
        sigma = math.sqrt(abs(variance))

        actual_error = abs(math.pi - pi_final)
        theoretical_limit = 3 * (sigma / math.sqrt(n_iterations))

        print(f"--- Results for {size} processors ---")
        print(f"General N: {N_total}")
        print(f"Calculated PI: {pi_final:.10f}")
        print(f"Actual error: {actual_error:.10e}")
        print(f"Theroretical limit (3*sigma/sqrt(N_iter)): {theoretical_limit:.10e}")
        print(f"Relationship (5.8) succeding: {actual_error <= theoretical_limit}")
        print(f"Execution time: {end_time - start_time:.4f} сек")


if __name__ == "__main__":
    main()
