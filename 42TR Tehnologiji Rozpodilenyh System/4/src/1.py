from mpi4py import MPI
import random
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def custom_sin(x, this_K=500):
    y = x
    s = y
    k = 1

    while k <= this_K:
        y = -((x**2) / ((k + 1) * (k + 2))) * y
        s = s + y
        k = k + 2

    return s


N = 240_000
K = 500
chunk_size = N // size

a_full = None
x_full = None
if rank == 0:
    a_full = np.array([random.uniform(-1, 1) for _ in range(N)], dtype="d")
    x_full = np.array([0.0001 * i for i in range(N)], dtype="d")

a_local = np.empty(chunk_size, dtype="d")
x_local = np.empty(chunk_size, dtype="d")

t_scatter_start = MPI.Wtime()
comm.Scatter(a_full, a_local, root=0)
comm.Scatter(x_full, x_local, root=0)
t_scatter_end = MPI.Wtime()

start_time = MPI.Wtime()

local_sum = 0.0
for i in range(chunk_size):
    local_sum += a_local[i] * custom_sin(x_local[i], this_K=K)

total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

end_time = MPI.Wtime()

if rank == 0:
    print(f"Proceses amount: {size}")
    print(f"Total sum: {total_sum}")
    print(f"Running time (Tp): {end_time - start_time:.4f} sec")
    print(f"Scatter time: {t_scatter_end - t_scatter_start:.6f} sec")
