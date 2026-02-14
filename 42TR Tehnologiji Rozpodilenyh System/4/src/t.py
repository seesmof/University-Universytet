from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

N = 240_000
chunk_size = N // size
if rank == 0:
    print(f"Chunk size: {chunk_size}\n")

if rank == 0:
    a_full = np.random.uniform(-1, 1, N).astype("d")
else:
    a_full = None

a_local = np.empty(chunk_size, dtype="d")

comm.Barrier()
t_start = MPI.Wtime()

comm.Scatter(a_full, a_local, root=0)

t_end = MPI.Wtime()
t_scatter = t_end - t_start


if rank == 0:
    total_bytes = 2 * N * 8
    if t_scatter > 0:
        speed_bytes_s = total_bytes / t_scatter
    else:
        speed_bytes_s = 0

    print(f"--- Results for N = {N} ---")
    print(f"Scatter time: {t_scatter:.8f} sec")
    print(f"Speed S: {speed_bytes_s:.2f} bytes/s")
    print(f"Speed S: {speed_bytes_s / 1e6:.2f} Mbytes/s")
    print("-" * 30)
