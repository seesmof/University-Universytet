from mpi4py import MPI


def main():
    N: int = 240000

    comm = MPI.COMM_WORLD
    world_size = comm.Get_size()
    rank = comm.Get_rank()

    print(f"{world_size=}")
    print(f"{rank=}")
    print()


if __name__ == "__main__":
    main()
