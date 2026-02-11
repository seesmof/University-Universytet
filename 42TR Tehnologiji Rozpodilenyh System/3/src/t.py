from mpi4py import MPI
import numpy as np

elements_to_send = 10
data = np.arange(elements_to_send, dtype=np.int64) + 100
print(data)

buffer_size = 20
recv_buffer = np.empty(buffer_size, dtype=np.int64)
print(recv_buffer)
