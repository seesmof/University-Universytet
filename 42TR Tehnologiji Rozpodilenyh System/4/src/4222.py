from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Параметри задачі
N = 1000
x_val = 1.001

# 1. Визначаємо кількість елементів для кожного процесу (рівномірно)
# Використовуємо divmod для обробки випадків, коли N не ділиться на size націло
base_n = N // size
remainder = N % size

# Кожен процес отримує base_n елементів, а перші 'remainder' процесів — ще по одному
local_n = base_n + (1 if rank < remainder else 0)

# Розрахунок зміщень (displacements) для Scatterv та для обчислення степенів
sendcounts = np.array(comm.allgather(local_n))
displs = np.insert(np.cumsum(sendcounts[:-1]), 0, 0)
local_displ = displs[rank]

a_full = None
if rank == 0:
    # Генеруємо коефіцієнти
    a_full = np.random.rand(N).astype(np.float64)
    print(f"Запуск на {size} процесорах для N={N}")
    print(f"Розподіл елементів (однаковий): {sendcounts}")

# Виділяємо буфер для локальної частини масиву
local_a = np.empty(local_n, dtype=np.float64)

# Розподіляємо дані
comm.Scatterv([a_full, sendcounts, displs, MPI.DOUBLE], local_a, root=0)

# --- ПАРАЛЕЛЬНЕ ОБЧИСЛЕННЯ (з вимірюванням часу) ---
start_time = time.time()

local_sum = 0.0
for i in range(local_n):
    global_idx = local_displ + i + 1
    # Обчислення степеня шляхом перемноження
    power_val = 1.0
    for _ in range(global_idx):
        power_val *= x_val
    local_sum += local_a[i] * power_val

end_time = time.time()
local_duration = end_time - start_time

# Збираємо результати та час роботи кожного процесора
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
all_times = comm.gather(local_duration, root=0)

# --- ПЕРЕВІРКА ТА АНАЛІЗ ---
if rank == 0:
    print("-" * 40)
    print(f"Паралельна сума: {total_sum:.10f}")

    # Послідовна перевірка через бібліотечну функцію
    seq_sum = sum(a_full[i] * (x_val ** (i + 1)) for i in range(N))
    print(f"Послідовна сума: {seq_sum:.10f}")
    print(f"Різниця:         {abs(total_sum - seq_sum):.2e}")
    print("-" * 40)

    # Аналіз нерівномірності навантаження
    print("Час роботи кожного процесора (сек):")
    for r, t in enumerate(all_times):
        print(f"Rank {r}: {t:.6f} с")

    max_t = max(all_times)
    min_t = min(all_times)
    print(f"\nНерівномірність: {((max_t - min_t) / max_t) * 100:.2f}%")
