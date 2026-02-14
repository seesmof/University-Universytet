from mpi4py import MPI
import numpy as np
import math


def solve_quadratic(n1, target_load):
    """
    Розв'язує рівняння: M^2/2 + M(n1 - 0.5) - target_load = 0
    для знаходження кількості елементів M.
    """
    a = 0.5
    b = n1 - 0.5
    c = -target_load

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return 0

    # Беремо лише додатний корінь
    m = (-b + math.sqrt(discriminant)) / (2 * a)
    return int(round(m))


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Параметри задачі
N = 1000  # Кількість елементів ряду
x_val = 1.001  # Значення x (для прикладу однакове для всіх)

# Підготовка даних на Rank 0
sendcounts = np.zeros(size, dtype=int)
displs = np.zeros(size, dtype=int)
a_full = None
x_full = None

if rank == 0:
    # 1. Створюємо масиви коефіцієнтів
    a_full = np.random.rand(N).astype(np.float64)
    x_full = np.full(N, x_val, dtype=np.float64)

    # 2. Розрахунок розподілу навантаження
    total_ops = N * (N + 1) / 2
    target_load_per_proc = total_ops / size

    current_n1 = 1
    total_assigned = 0

    for i in range(size - 1):
        m_i = solve_quadratic(current_n1, target_load_per_proc)
        # Коригуємо, щоб не вийти за межі N
        if total_assigned + m_i > N:
            m_i = max(0, N - total_assigned)

        sendcounts[i] = m_i
        displs[i] = total_assigned

        total_assigned += m_i
        current_n1 += m_i

    # Останній процесор забирає залишок
    sendcounts[size - 1] = N - total_assigned
    displs[size - 1] = total_assigned

# Розсилаємо всім процесорам інформацію про розміри їхніх частин
local_n = comm.scatter(sendcounts, root=0)
# Також нам потрібно знати зміщення, щоб правильно визначити степінь x
local_displ = comm.scatter(displs, root=0)

# Виділяємо буфери для локальних даних
local_a = np.empty(local_n, dtype=np.float64)
local_x = np.empty(local_n, dtype=np.float64)

# Розподіляємо дані за допомогою Scatterv
comm.Scatterv([a_full, sendcounts, displs, MPI.DOUBLE], local_a, root=0)
comm.Scatterv([x_full, sendcounts, displs, MPI.DOUBLE], local_x, root=0)

# 3. Обчислення локальної суми
local_sum = 0.0
for i in range(local_n):
    # Глобальний індекс i (починаючи з 1) для степеня
    global_idx = local_displ + i + 1

    # Обчислення степеня шляхом перемноження (як вимагає умова)
    power_val = 1.0
    for _ in range(global_idx):
        power_val *= local_x[i]

    local_sum += local_a[i] * power_val

# 4. Збір результатів
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Розрахунок завершено для N={N}, P={size}")
    print(f"Розподіл елементів по процесорах: {sendcounts}")
    print(f"Загальна сума: {total_sum}")
