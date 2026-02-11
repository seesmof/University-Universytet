from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

array_size = rank * size

data_array = np.zeros(array_size, dtype=int)

print(f"Процес {rank}: Розмір масиву = {rank} * {size} = {array_size}")
print(f"Пам'ять виділено за адресою: {data_array.__array_interface__['data'][0]}")

if array_size > 0:
    print(f"\t-> Перші елементи процесу {rank}: {data_array[:5]}...")
else:
    print(f"\t-> Процес {rank} має порожній масив, (бо rank = 0))")
