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
            print("At least 2 processes needed.")
        return

    if rank == 1:
        # Динамічне виділення пам'яті
        # Використання np.empty для виділення пам'яті
        send_data = np.empty(elements_to_send, dtype=np.int64)

        # Ініціалізація даних
        for i in range(elements_to_send):
            send_data[i] = i + 100

        print(
            f"Process {rank}: Dynamically created an array of {elements_to_send} elements."
        )
        print(f"Process {rank}: Sending data: {send_data}")

        # Передача даних
        comm.Send([send_data, MPI.LONG], dest=0, tag=77)

    elif rank == 0:
        # Динамічне всиділення пам'яті для буфера обміну
        # Виділяємо пам'яті під максимально можливий розмір буфера
        recv_buffer = np.empty(buffer_size, dtype=np.int64)

        status = MPI.Status()

        # Прийом даних у динамічно виділений буфер
        comm.Recv([recv_buffer, MPI.LONG], source=1, tag=77, status=status)

        actual_count = status.Get_count(MPI.LONG)

        print(
            f"Process 0: Received data into a dynamic buffer (buffer size: {buffer_size})"
        )
        print(f"Actual amount of received processes: {actual_count}")
        print(f"Contents of received data: {recv_buffer[:actual_count]}")

    # Явне звільнення пам'яті в Python відбувається автоматично (Garbage Collector)


if __name__ == "__main__":
    main()
