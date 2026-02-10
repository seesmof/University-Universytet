"""
Змінити вихідну програму так, щоб кожний процес виводив інформацію щодо парності свого номера.
"""

from mpi4py import MPI
import sys


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    parity = "парний" if rank % 2 == 0 else "непарний"
    print(f"Процес {rank} з {size} є {parity}")

    comm.Barrier()

    if rank == 0:
        print(f"\nВсього процесів: {size}")
        print("Вміст командного рядку для першого процесу:")
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
