#include <mpi.h>
#include <stdio.h>
#include <math.h>
#define N 400000

int main(int argc, char *argv[])
{
    int P, M;
    double x[N], a[N];
    int myrank;
    long i, j;
    double sum = 0.0, total = 0.0;
    double start_time, use_time;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &P);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);

    if (myrank == 0)
    {
        srand((unsigned)time(NULL));
        for (i = 0; i < N; i++)
        {
            x[i] = -1.073741824 + rand() * 1E-9;
            a[i] = (-1.073741824 + rand() * 1E-9) * 0.1;
        }
        M = N / P;
    }

    if (myrank == 0)
        start_time = MPI_Wtime();
    MPI_Bcast(&M, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(x, M, MPI_DOUBLE, x, M, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Scatter(a, M, MPI_DOUBLE, a, M, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    for (i = 0; i < M; i++)
        sum += a[i] * x[i];

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Reduce(&sum, &total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    if (myrank == 0)
    {
        use_time = MPI_Wtime() - start_time;
        printf("t=%lf sec.\n", use_time);
        printf("sum in %d procs is %.5f\n", P, total);
    }
    MPI_Finalize();
    return 0;
}