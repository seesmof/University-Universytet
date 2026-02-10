from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

total_data_size = 1000

chunk_size = total_data_size // size
start_index = rank * chunk_size
end_index = (rank + 1) * chunk_size if rank != size - 1 else total_data_size

print(
    f"[Процес {rank}/{size}]: Працюю з індексами від {start_index} до {end_index - 1}"
)

local_sum = sum(range(start_index, end_index))
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"\nЗагальна сума, зібрана з {size} процесів: {total_sum}")
