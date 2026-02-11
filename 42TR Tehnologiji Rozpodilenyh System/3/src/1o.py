from mpi4py import MPI
import sys


def main():
    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        print(f"Total processes: {size}")

    print(f"Number in MPI_COMM_WORLD: {rank}")

    comm.Barrier()

    if rank == 0:
        print(f"CommandLine for {rank}:")
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
