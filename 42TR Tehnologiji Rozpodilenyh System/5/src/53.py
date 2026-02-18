import math
import random
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numprocs = comm.Get_size()

N_total = 1_000_000_000
n_per_proc = N_total // numprocs

pi_reference = math.pi
local_sum = 0.0

random.seed(time.time() + rank)

for _ in range(n_per_proc):
    x = random.random()

    local_sum += 4.0 / (1.0 + x * x)

total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    mc_pi = total_sum / N_total
    error = abs(pi_reference - mc_pi)

    print(f"mc_pi = {mc_pi:.16f} err={error:.15f} points={N_total}")
