import random
from mpi4py import MPI
import numpy as np

N: int = 240_000

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def custom_sin(x, K=500):
    y = x
    s = y
    k = 1

    while k <= K:
        y = -(x**2 / ((k + 1) * (k + 2))) * y
        s = s + y
        k = k + 2

    return s


a_i = random.uniform(-1, 1)
