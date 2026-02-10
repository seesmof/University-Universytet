"""
Доповніть вихідну програму так,  щоб процес "1" виконував  посилку,  а процес "0" – прийом елементів масиву цілих чисел типу long, причому, розміри буферів передачі та прийому мають дорівнювати номеру робочого місця, помноженому на 10, а кількість елементів, що передаються – номеру робочого місця, збільшеного на одиницю. В процесі "0" реалізувати виведення кількості фактично прийнятих елементів.
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
        # Процес 1: Посилка
        # Створити масив даних типу Long (int64)
        data = np.arange(elements_to_send, dtype=np.int64) + 100
        print(f"Процес {rank}: Надсилаю {len(data)} елементів: {data}")
        comm.Send([data, MPI.LONG], dest=0, tag=77)

    elif rank == 0:
        # Процес 0: Прийом
        recv_buffer = np.zeros(buffer_size, dtype=np.int64)
        status = MPI.Status()

        comm.Recv([recv_buffer, MPI.LONG], source=1, tag=77, status=status)

        actual_count = status.Get_count(MPI.LONG)
        print("Процес 0: Отримано дані")
        print(f"Фактична кількість прийнятих елементів: {actual_count}")
        print(
            f"Вміст буфера (перші {actual_count} елементів): {recv_buffer[:actual_count]}"
        )


if __name__ == "__main__":
    main()
