from mpi4py import MPI
import numpy as np
import math


def solve_quadratic(n1, target_load):
    a, b, c = 0.5, n1 - 0.5, -target_load
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return 0
    m = (-b + math.sqrt(discriminant)) / (2 * a)
    return int(round(m))


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Параметри задачі
N = 1000
x_val = 1.001

sendcounts = np.zeros(size, dtype=int)
displs = np.zeros(size, dtype=int)
a_full = None

if rank == 0:
    # Генеруємо дані тільки на головному процесі
    a_full = np.random.rand(N).astype(np.float64)

    # Розрахунок рівномірного навантаження
    total_ops = N * (N + 1) / 2
    target_load = total_ops / size

    current_n1, total_assigned = 1, 0
    for i in range(size - 1):
        m_i = solve_quadratic(current_n1, target_load)
        if total_assigned + m_i > N:
            m_i = max(0, N - total_assigned)
        sendcounts[i] = m_i
        displs[i] = total_assigned
        total_assigned += m_i
        current_n1 += m_i
    sendcounts[size - 1] = N - total_assigned
    displs[size - 1] = total_assigned

# Розповсюджуємо параметри
local_n = comm.scatter(sendcounts, root=0)
local_displ = comm.scatter(displs, root=0)

# Передача сегментів масиву коефіцієнтів
local_a = np.empty(local_n, dtype=np.float64)
comm.Scatterv([a_full, sendcounts, displs, MPI.DOUBLE], local_a, root=0)

# --- ПАРАЛЕЛЬНЕ ОБЧИСЛЕННЯ ---
local_sum = 0.0
for i in range(local_n):
    global_idx = local_displ + i + 1
    # Обчислення степеня шляхом перемноження (за умовою задачі)
    power_val = 1.0
    for _ in range(global_idx):
        power_val *= x_val
    local_sum += local_a[i] * power_val

parallel_res = comm.reduce(local_sum, op=MPI.SUM, root=0)

# --- ПЕРЕВІРКА НА НУЛЬОВОМУ ПРОЦЕСІ ---
if rank == 0:
    print("-" * 30)
    print(f"Результат MPI ({size} проц.): {parallel_res:.10f}")

    # Послідовне обчислення з бібліотечною функцією
    sequential_sum = 0.0
    for i in range(N):
        # Використовуємо бібліотечну функцію (оператор **)
        sequential_sum += a_full[i] * (x_val ** (i + 1))

    print(f"Послідовний результат:      {sequential_sum:.10f}")

    # Порівняння
    diff = abs(parallel_res - sequential_sum)
    print(f"Різниця (похибка):          {diff:.2e}")
    print("-" * 30)

    if diff < 1e-7:
        print("Перевірка пройдена успішно! Все на славу Божу.")
    else:
        print("Увага: виявлено значну розбіжність.")
