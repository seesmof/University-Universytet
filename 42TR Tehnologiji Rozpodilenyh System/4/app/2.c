#include <mpi.h>
#include <stdio.h>
#include <math.h>
#define N 10000

int main(int argc, char *argv[])
{
	int P;
	double *x, *a;
	int myrank;
	long i, j;
	double q, an, nn;
	int *pn, *poffset;
	int n, offset;
	double C;
	double mul = 1.0, sum = 0.0, total = 0.0;
	double start_time, use_time;
	MPI_Status status;

	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &P);
	MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
	if (myrank == 0)
	{
		pn = (int *)malloc(P * sizeof(int));
		if (pn == NULL)
		{
			printf("Not memory for n\n");
			return -1;
		}
		poffset = (int *)malloc(P * sizeof(int));
		if (poffset == NULL)
		{
			printf("Not memory for offset\n");
			return -1;
		}
		C = N * (1.0 + N) / P;
		an = 1;
		pn[P - 1] = N;
		poffset[0] = 0;
		for (i = 0; i < P - 1; i++)
		{
			q = (2 * an - 1) / 2.0;
			nn = -q + sqrt(q * q + C);
			an += nn;
			pn[i] = (int)floor(nn);
			pn[P - 1] -= pn[i];
		}
		poffset[0] = 0;
		for (i = 1; i < P; i++)
			poffset[i] = poffset[i - 1] + pn[i - 1];
		for (i = 0; i < P; i++)
			printf("Process %d will be do %d multiples\n", i, pn[i]);
	}

	MPI_Scatter(pn, 1, MPI_INT, &n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Scatter(poffset, 1, MPI_INT, &offset, 1, MPI_INT, 0, MPI_COMM_WORLD);

	if (myrank == 0)
	{
		x = (double *)malloc(N * sizeof(*x));
		if (x == NULL)
		{
			printf("Not memory\n");
			return -1;
		}
		a = (double *)malloc(N * sizeof(*a));
		if (a == NULL)
		{
			printf("Not memory\n");
			free(x);
			return -1;
		}
		srand((unsigned)time(NULL));
		for (i = 0; i < N; i++)
		{
			x[i] = (-1.073741824 + rand() * 1E-9) * 0.8;
			a[i] = (-1.073741824 + rand() * 1E-9) * 0.01;
		}
	}
	if (myrank != 0)
	{
		x = (double *)malloc(n * sizeof(*x));
		if (x == NULL)
		{
			printf("Not memory\n");
			return -1;
		}
		a = (double *)malloc(n * sizeof(*a));
		if (a == NULL)
		{
			printf("Not memory\n");
			free(x);
			return -1;
		}
	}
	if (myrank == 0)
		start_time = MPI_Wtime();

	MPI_Scatterv(x, pn, poffset, MPI_DOUBLE, x, n, MPI_DOUBLE, 0, MPI_COMM_WORLD);
	MPI_Scatterv(a, pn, poffset, MPI_DOUBLE, a, n, MPI_DOUBLE, 0, MPI_COMM_WORLD);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < i + 1 + offset; j++)
			mul *= x[i];
		sum += a[i] * mul;
		mul = 1.0;
	}

	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Reduce(&sum, &total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

	if (myrank == 0)
	{
		use_time = MPI_Wtime() - start_time;
		printf("total = %.12e used=%f sec.\n", total, use_time);
		free(pn);
		free(poffset);
	}
	free(x);
	free(a);
	MPI_Finalize();
	return 0;
}