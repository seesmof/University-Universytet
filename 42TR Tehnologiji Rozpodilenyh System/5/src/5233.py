import math
import random
import time
from mpi4py import MPI


def f(x, y):
    return x * y


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    numprocs = comm.Get_size()

    N_total = 100_000_000
    n_per_procs = N_total // numprocs

    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0
    area_rect = (x_max - x_min) * (y_max - y_min)

    local_sum = 0.0
    points_in_S = 0

    random.seed(time.time() + rank)

    start_time = MPI.Wtime()

    for _ in range(n_per_procs):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if x**2 <= y <= math.sqrt(x):
            local_sum += f(x, y)
            points_in_S += 1

    total_f_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    total_points_in_S = comm.reduce(points_in_S, op=MPI.SUM, root=0)
    end_time = MPI.Wtime()

    if rank == 0:
        # I = Area_react * (Sum_f_in_S / N_total)
        integral_mc = (area_rect * total_f_sum) / N_total

        reference = 1.0 / 12.0
        error = abs(reference - integral_mc)

        area_S_approx = (area_rect * total_points_in_S) / N_total

        print("--- Calculated double integral ---")
        print(f"Number of processes: {numprocs}")
        print(f"Total number of points N: {N_total}")
        print(f"Approcimated area of area S: {area_S_approx:.6f} (accurate: 1/3)")
        print(f"Integration results: {integral_mc:.10f}")
        print(f"Accurate value (1/12): {reference:.10f}")
        print(f"Absolute error: {error:.10e}")
        print(f"Execution time: {end_time - start_time:.4f} sec")


if __name__ == "__main__":
    main()
