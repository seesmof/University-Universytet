from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Завдання вимагає 4 процесори
if size < 4 and rank == 0:
    print("Warning: For this task it is recommended to use 4 processes (-n 4)")

# Значення N для дослідження (як у попередньому пункті)
N_values = list(range(20000, 240001, 20000))

if rank == 0:
    print(f"{'Array length N':>18} | {'Scatter time (sec)':>20}")
    print("-" * 45)

for N in N_values:
    chunk_size = N // size

    # Створюємо масиви тільки на root (процес 0)
    a_full = None
    x_full = None
    if rank == 0:
        a_full = np.random.uniform(-1, 1, N).astype("float64")
        x_full = np.random.uniform(0, 1, N).astype("float64")

    # Буфери для отримання частин масивів
    a_local = np.empty(chunk_size, dtype="float64")
    x_local = np.empty(chunk_size, dtype="float64")

    # Синхронізація перед вимірюванням
    comm.Barrier()

    # Вимірюємо час виконання двох Scatter
    t_start = MPI.Wtime()
    comm.Scatter(a_full, a_local, root=0)
    comm.Scatter(x_full, x_local, root=0)
    t_end = MPI.Wtime()

    scatter_time = t_end - t_start

    if rank == 0:
        print(f"{N:18d} | {scatter_time:20.8f}")
