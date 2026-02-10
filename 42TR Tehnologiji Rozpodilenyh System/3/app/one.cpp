#include "mpi.h"
#include <stdio.h>

int main(int argc, char *argv[])
{
    int size, rank, i;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0)
        printf("Amount of tasks: %d\n", size);
    printf("Number in MPI_COMM_WORLD: %d\n", rank);

    MPI_Barrier(MPI_COMM_WORLD);

    if (rank == 0)
        for (puts("CommandLine for task 0: "), i = 0; i < argc; i++)
            printf("%d: '%s'\n", i, argv[i]);

    MPI_Finalize();
    return 0;
}
