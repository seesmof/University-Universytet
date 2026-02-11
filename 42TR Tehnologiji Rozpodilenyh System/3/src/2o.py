from mpi4py import MPI
import numpy as np


def main():
    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()
    size = comm.Get_size()

    if size != 2:
        if rank == 0:
            print(f"Only 2 tasks required instad of {size}, stopping.")
        comm.Barrier()
        comm.Abort(MPI.ERR_OTHER)
        return

    double_data = np.zeros(20, dtype=np.float64)

    if rank == 0:
        double_data[:5] = [1.1, 2.2, 3.3, 4.4, 5.5]

        # MPI_Send(buf, count, datatype, dest, tag, comm)
        comm.Send([double_data, 5, MPI.DOUBLE], dest=1, tag=100)
    else:
        status = MPI.Status()

        # MPI_Recv(buf, count, datatype, source, tag, comm, status)
        comm.Recv([double_data, 5, MPI.DOUBLE], source=0, tag=100, status=status)

        # Getting the amount of actually accepted elements
        count = status.Get_count(MPI.DOUBLE)
        print(f"Received {count} elements")


if __name__ == "__main__":
    main()
