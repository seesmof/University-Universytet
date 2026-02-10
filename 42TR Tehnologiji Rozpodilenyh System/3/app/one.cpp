// Ensure MPI is installed and the include path is set up correctly.
// If you have not installed MPI, install Microsoft MPI (MS-MPI) or OpenMPI.
// Then, add the include directory to your project's include directories.
//
// Example for Visual Studio:
// 1. Right-click your project > Properties.
// 2. Go to C/C++ > General > Additional Include Directories.
// 3. Add the path to the folder containing "mpi.h" (e.g., C:\Program Files (x86)\Microsoft SDKs\MPI\Include).
//
// Do not remove the #include "mpi.h" line if you need MPI functionality.

#include "mpi.h"
#include <stdio.h>

int main(int argc, char *argv[])
{
    int size, rank, i;

    // ������������ ��������
    MPI_Init(&argc, &argv);

    // ʳ������ ������� � �������
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // ������� ����� �������
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0)
        printf("Amount of tasks: %d\n", size);
    printf("Number in MPI_COMM_WORLD: %d\n", rank);

    // ����� �������������, ���� �� ������ 0 ����� ��������� ���������� �����. � ���������� ����� ������ ���� ���������, �� ��������� �������������� MPIRUN.
    MPI_Barrier(MPI_COMM_WORLD);

    if (rank == 0)
        for (puts("CommandLine for task 0: "), i = 0; i < argc; i++)
            printf("%d: '%s'\n", i, argv[i]);

    // �� ������� ���������� ���������
    MPI_Finalize();
    return 0;
}