"""
Напишіть фрагмент паралельної програми, в кожному з процесів якої створюється масив динамічної пам’яті, розмір якого дорівнює добутку номера процесу на загальну кількість процесів.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

array_size = rank * size

data_array = np.zeros(array_size, dtype=int)

print(f"Process {rank}: Array size = {rank} * {size} = {array_size}")
print(f"Memory allocated from address: {data_array.__array_interface__['data'][0]}")

if array_size > 0:
    print(f"\t-> First process's elements {rank}: {data_array[:5]}")
else:
    print(f"\t-> Process {rank} has an empty array, (for, rank = 0))")
