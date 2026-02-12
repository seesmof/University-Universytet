from mpi4py import MPI
import numpy as np

N: int = 240000


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    start_time = MPI.Wtime()
    a: list[float] = np.ones(N)
    end_time = MPI.Wtime()
    time_taken = end_time - start_time
    if rank == 0:
        print(f"Init time: {time_taken}")


if __name__ == "__main__":
    main()
