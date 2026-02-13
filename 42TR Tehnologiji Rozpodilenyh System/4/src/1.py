from mpi4py import MPI
import random
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def custom_sin(x, K=500):
    y = x
    s = y
    k = 1

    while k <= K:
        y = -((x**2) / ((k + 1) * (k + 2))) * y
        s = s + y
        k = k + 2

    return s


start_time = MPI.Wtime()

N = 240_000
sum: float = 0.0
for i in range(N):
    a_i = random.uniform(-1, 1)
    x_i = 0.0001 * i
    sum += a_i * custom_sin(x_i)
print(f"{sum = }")

end_time = MPI.Wtime()
time_taken = end_time - start_time
print(f"Time taken: {time_taken}")
print()
