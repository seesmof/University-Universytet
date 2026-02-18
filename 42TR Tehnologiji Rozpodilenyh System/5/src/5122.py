"""
Реалізуйте власну паралельну програму обчислення інтеграла (1) з використанням наведеної програми 1, додайте до неї функцію обчислення часу її виконання. Визначте прискорення паралельної програми для чотирьох процесорів.
"""

from mpi4py import MPI
import math


def parallel_pi(N_total):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    numprocs = comm.Get_size()

    n_local = N_total // numprocs

    comm.Barrier()
    start_time = MPI.Wtime()

    local_sum = 0.0
    start_index = rank * n_local
    end_index = (rank + 1) * n_local

    step = 1.0 / N_total
    for i in range(start_index, end_index):
        x = (i + 0.5) * step
        local_sum += 4.0 / (1.0 + x * x)

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    end_time = MPI.Wtime()
    duration = end_time - start_time

    if rank == 0:
        pi_approx = total_sum * step
        return pi_approx, duration
    return None, duration


if __name__ == "__main__":
    N = 10**8

    pi_value, time_spent = parallel_pi(N)

    rank = MPI.COMM_WORLD.Get_rank()
    if rank == 0:
        pi_ref = math.pi
        print(f"Processes amount: {MPI.COMM_WORLD.Get_size()}")
        print(f"Calculated PI: {pi_value:.16f}")
        print(f"Error: {abs(pi_ref - pi_value):.16e}")
        print(f"Execution time: {time_spent:.6f} sec")
