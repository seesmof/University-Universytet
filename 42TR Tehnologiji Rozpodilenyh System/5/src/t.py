from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print(f"Jesus is LORD! This is process {rank} from size {size}.")
