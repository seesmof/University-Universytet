from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = f"Data from {rank}"
# Every rank receives a list of data from all ranks
results = comm.allgather(data)
if rank == 0:
    print(results) # Output: ['Data from 0', 'Data from 1', ...]
