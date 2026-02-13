from mpi4py import MPI
import numpy as np
import random

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def custom_sin(x, K=500):
    y = x
    s = y
    k = 1
    while k <= K:
        y = -((x**2) / ((k + 1) * (k + 2))) * y
        s = s + y
        k = k + 2
    return s


# Experiment settings
N_values = list(range(20_000, 240_001, 20_000))
P = size

if rank == 0:
    print(
        f"{'N':>10} | {'Attempt 1':>14} | {'Attempt 2':>14} | {'Attempt 3':>14} | {'Average Tp':>14}"
    )
    print("-" * 80)

for N in N_values:
    attempts = []

    # Number of tests
    for _ in range(3):
        comm.Barrier()
        start_time = MPI.Wtime()

        # Chunking the work
        chunk_size = N // size
        local_sum: float = 0.0

        for i in range(rank * chunk_size, (rank + 1) * chunk_size):
            a_i = random.uniform(-1, 1)
            x_i = 0.0001 * i
            local_sum += a_i * custom_sin(x_i)

        total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
        end_time = MPI.Wtime()

        attempts.append(end_time - start_time)

    if rank == 0:
        average_tp = sum(attempts) / 3
        print(
            f"{N:10d} | {attempts[0]:14.4f} | {attempts[1]:14.4f} | {attempts[2]:14.4f} | {average_tp:13.4f}"
        )
