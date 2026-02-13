import time
from mpi4py import MPI
import numpy as np

N: int = 400000


def main():
    comm = MPI.COMM_WORLD
    P = comm.Get_size()
    myrank = comm.Get_rank()

    x: list[float] = list()
    a: list[float] = list()
    M: float = 0.0
    sum: float = 0.0
    total: float = 0.0

    if myrank == 0:
        np.random.seed(int(time.time()))
        x = (-1.073741824 + np.random.rand(N) * 1e-9).astype("f8")
        a = ((-1.073741824 + np.random.rand(N) * 1e-9) * 0.1).astype("f8")
        M = N / P

    if myrank == 0:
        start_time = MPI.Wtime()
    comm.bcast(M, root=1)
    comm.scatter(x, M, 0)
    comm.scatter(a, M, 0)

    for i in range(M):
        sum += a[i] * x[i]

    comm.barrier()
    comm.reduce([sum, total], MPI.SUM, root=0)
    if myrank == 0:
        end_time = MPI.Wtime()
        eval_time = end_time - start_time
        print(f"time = {eval_time:.3f}")
        print(f"sum in {P} processes: {total:.5f}")


if __name__ == "__main__":
    main()
