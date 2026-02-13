from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

start_time = MPI.Wtime()

a = np.arange(5)

end_time = MPI.Wtime()
time_taken = end_time - start_time
print(f"Time taken: {time_taken}")
