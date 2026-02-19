"""
Використовуючи опановану техніку інтегрування, розробіть послідовні алгоритм та програму обчислення інтеграла у відповідності до наведених нижче варіантів. В програмі реалізуйте введення кількості інтервалів з клавіатури. Дослідіть точність та швидкодію програми для значень кількості інтервалів 10^3, 10^4, 10^5, 10^6, 10^7, 10^9. Результати подайте у звіті у вигляді таблиці.

Обчислити інтеграл INT_0^PI/2 SIN^2(x)dx
"""

from mpi4py import MPI
import numpy as np


def f(x):
    return np.sin(x) ** 2


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    a = 0.0
    b = np.pi / 2

    if rank == 0:
        n = int(input("Please enter the number of intervals (n): "))
    else:
        n = None

    n = comm.bcast(n, root=0)

    start_time = MPI.Wtime()

    h = (b - a) / n
    local_n = n // size
    local_a = a + rank * local_n * h
    local_b = local_a + local_n * h

    integral = (f(local_a) + f(local_b)) / 2.0
    for i in range(1, local_n):
        x = local_a + i * h
        integral += f(x)
    integral *= h

    total_integral = comm.reduce(integral, op=MPI.SUM, root=0)
    end_time = MPI.Wtime()

    if rank == 0:
        execution_time = end_time - start_time
        print(f"Result: {total_integral:.12f}")
        print(f"Execution time: {execution_time:.6f} sec")


if __name__ == "__main__":
    main()
