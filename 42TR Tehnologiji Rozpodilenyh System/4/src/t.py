from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    comm.bcast


if __name__ == "__main__":
    main()
