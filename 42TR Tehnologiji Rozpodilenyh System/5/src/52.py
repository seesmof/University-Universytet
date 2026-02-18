import math
import random
import sys
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numprocs = comm.Get_size()

n_in_proc = 1_000_000
R = 0.5
pi_reference = math.pi

n_iterations = 0
if rank == 0:
    if len(sys.argv) > 1:
        n_iterations = int(sys.argv[1])
    else:
        n_iterations = 1

n_iterations = comm.bcast(n_iterations, root=0)

in_circle = 0

for i in range(n_iterations):
    random.seed(time.time() + rank)

    for _ in range(n_in_proc):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if x * x + y * y < R * R:
            in_circle += 1

    total_in_circle = comm.reduce(in_circle, op=MPI.SUM, root=0)

    if rank == 0:
        total_points = n_in_proc * (i + 1) * numprocs
        approx = 4.0 * (total_in_circle / total_points)
        print(
            f"pi = {approx:.16f}, error = {abs(pi_reference - approx):.16f}, points = {total_points}"
        )
