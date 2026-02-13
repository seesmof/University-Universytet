from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = {"message": "Jesus is LORD", "status": 200}
result = {}
comm.Scatterv(data, result)
print(result)
