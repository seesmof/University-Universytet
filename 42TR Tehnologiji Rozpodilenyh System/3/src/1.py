"""
Змінити вихідну програму так, щоб кожний процес виводив інформацію щодо парності свого номера.
"""

from mpi4py import MPI
import sys


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    parity = "even" if rank % 2 == 0 else "odd"
    print(f"Process {rank} of {size} is {parity}")

    comm.Barrier()

    if rank == 0:
        print(f"\nTotal processes: {size}")
        print(f"CommandLine for {rank} process:")
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
