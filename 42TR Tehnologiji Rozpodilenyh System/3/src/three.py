"""
Переробити програму завдання 2 так,  щоб в якості буферів прийому та передачі використовувались масиви динамічної пам’яті.
"""

from mpi4py import MPI
import numpy as np


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # --- Налаштування згідно з варіантом ---
    WOKRSTATION_ID = 19
    buffer_size = WOKRSTATION_ID * 10
    elements_to_send = WOKRSTATION_ID + 1
    # --- ✝ ---

    if size < 2:
        if rank == 0:
            print("Потрібно принаймні 2 процеси.")
        return

    if rank == 1:
        # Динамічне виділення пам'яті
        # Використання np.empty для виділення пам'яті
        send_data = np.empty(elements_to_send, dtype=np.int64)

        # Ініціалізація даних
        for i in range(elements_to_send):
            send_data[i] = i + 100

        print(f"Процес {rank}: Динамічно створений масив розміром {elements_to_send}")
        print(f"Процес {rank}: Надсилаю дані: {send_data}")

        # Передача даних
        comm.send([send_data, MPI.LONG], dest=0, tag=77)

    elif rank == 0:
        # Динамічне всиділення пам'яті для буфера обміну
        # Виділяємо пам'яті під максимально можливий розмір буфера
        recv_buffer = np.empty(buffer_size, dtype=np.int64)

        status = MPI.Status()

        # Прийом даних у динамічно виділений буфер
        comm.Recv([recv_buffer, MPI.LONG], source=1, tag=77, status=status)

        actual_count = status.Get_count(MPI.LONG)

        print(
            f"Процес 0: Отримано дані у динамічний буфер (розмір буфера: {buffer_size})"
        )
        print(f"Фактична кількість прийнятих елементів: {actual_count}")
        print(f"Вміст отриманих даних: {recv_buffer[:actual_count]}")

    # Явне звільнення пам'яті в Python відбувається автоматично (Garbage Collector)


if __name__ == "__main__":
    main()
