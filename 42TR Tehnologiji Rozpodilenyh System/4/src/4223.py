from mpi4py import MPI
import numpy as np
import math


def get_balanced_layout(N, size):
    """Розрахунок збалансованого розподілу (Вихідна програма)"""
    sendcounts = np.zeros(size, dtype=int)
    displs = np.zeros(size, dtype=int)
    total_ops = N * (N + 1) / 2
    target_load = total_ops / size
    curr_n1, assigned = 1, 0
    for i in range(size - 1):
        a, b, c = 0.5, curr_n1 - 0.5, -target_load
        m_i = int(round((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)))
        if assigned + m_i > N:
            m_i = max(0, N - assigned)
        sendcounts[i], displs[i] = m_i, assigned
        assigned += m_i
        curr_n1 += m_i
    sendcounts[size - 1] = N - assigned
    displs[size - 1] = assigned
    return sendcounts, displs


def get_equal_layout(N, size):
    """Розрахунок рівного розподілу елементів (Власна програма)"""
    base_n = N // size
    rem = N % size
    sendcounts = np.array([base_n + (1 if i < rem else 0) for i in range(size)])
    displs = np.insert(np.cumsum(sendcounts[:-1]), 0, 0)
    return sendcounts, displs


def compute_sum(local_n, local_displ, x_val):
    """Ядро обчислень: сума ряду з ручним множенням степенів"""
    l_sum = 0.0
    for i in range(local_n):
        global_idx = local_displ + i + 1
        p_val = 1.0
        for _ in range(global_idx):
            p_val *= x_val
        l_sum += 1.0 * p_val  # Припускаємо a_i = 1.0 для чистоти тесту
    return l_sum


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Значення N для тестування
    N_values = [10000, 15000, 20000]
    x_val = 1.0001

    if rank == 0:
        print(f"{'=' * 60}")
        print(f"Performance Testing (Processors: {size})")
        print(f"{'N':>10} | {'Method':>15} | {'Time (sec)':>12} | {'Result':>15}")
        print(f"{'-' * 60}")

    for N in N_values:
        for mode in ["balanced", "equal"]:
            # Визначаємо структуру розподілу
            if mode == "balanced":
                scounts, displs = get_balanced_layout(N, size)
                mode_name = "Balanced"
            else:
                scounts, displs = get_equal_layout(N, size)
                mode_name = "Equal"

            local_n = scounts[rank]
            local_displ = displs[rank]

            # Синхронізація перед вимірюванням
            comm.Barrier()
            start_t = MPI.Wtime()

            # Виконання обчислень
            local_res = compute_sum(local_n, local_displ, x_val)

            # Збір результатів
            final_sum = comm.reduce(local_res, op=MPI.SUM, root=0)
            duration = MPI.Wtime() - start_t
            max_duration = comm.reduce(duration, op=MPI.MAX, root=0)

            if rank == 0:
                print(
                    f"{N:10d} | {mode_name:15} | {max_duration:12.6f} | {final_sum:15.2e}"
                )

        if rank == 0:
            print(f"{'-' * 60}")


if __name__ == "__main__":
    main()
