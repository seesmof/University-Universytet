from mpi4py import MPI

comm = MPI.COMM_WORLD
numprocs = comm.Get_size()
myid = comm.Get_rank()

PI25DT = 3.141592653589793238462643

while True:
    n = 0
    if myid == 0:
        try:
            line = input("Enter the number of intervals (0 = quit) ")
            n = int(line)
        except EOFError:
            n = 0
        except ValueError:
            n = 0

    n = comm.bcast(n, root=0)

    if n <= 0:
        break

    h = 1.0 / n
    sum_val = 0.0

    for i in range(myid + 1, n + 1, numprocs):
        x = h * (i - 0.5)
        sum_val += 4.0 / (1.0 + x * x)

    mypi = h * sum_val

    pi = comm.reduce(mypi, op=MPI.SUM, root=0)

    if myid == 0:
        print(f"PI is approximately {pi:.16f},\nerror is {abs(pi - PI25DT):.16f}")
