from mpi4py import MPI
import numpy as np

N: int = 240000


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if size != 2:
        if rank == 0:
            print("ERROR: Required 2 processes to run correctly.")
        return

    if rank == 0:
        data = {
            "result": "Jesus is LORD",
            "code": 200,
        }
        comm.send(data, dest=1)
        print(f"Process 0: Sending data - {data}")

        response = comm.recv(source=1)
        print(f"Process 0: Received a response - {response}")

    if rank == 1:
        data = ["Jesus is Lord", "Amen"]
        comm.send(data, dest=0)
        print(f"Process 1: Sending data - {data}")

        response = comm.recv(source=0)
        print(f"Process 1: Received response - {response}")


if __name__ == "__main__":
    main()
