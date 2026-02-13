from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.arange(5)
result = np.zeros_like(data)

comm.Reduce(data, result)

if rank == 0:
    print(f"Data before reduction:\n{data}")
    print(f"Results after reduction:\n{result}")
