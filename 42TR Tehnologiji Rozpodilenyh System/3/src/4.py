"""
Напишіть програму, яка складається з чотирьох процесів.

Процес "0" передає до процесів "1", "2" та "3" рядок з прізвищем студента.

Процес "1" конкатенує прийнятий рядок з рядком, відповідним імені студента, і відсилає отриманий рядок назад.

Процес "2" визначає кількість символів в прийнятому рядку та відсилає це число до нульового процесу.

Процес "3" множить число, що дорівнює сумі кодів символів прийнятого рядка на число PI, та відсилає отримане значення до процеса "0".

Після завершення обмінів процес "0" виводить на друк отримані від інших процесів значення.
"""

import math
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size != 4:
        if rank == 0:
            print(f"Error: This program needs 4 processes, but {size} given.")
        return

    surname = "Onyshchenko"

    if rank == 0:
        print(f"[Process 0]: Sending a surname {surname} to processes 1, 2, and 3...")

        for i in range(1, 4):
            comm.send(surname, dest=i)

        full_name = comm.recv(source=1)
        char_count = comm.recv(source=2)
        pi_result = comm.recv(source=3)

        print("--- Results for process 0 ---")
        print(f"From process 1 (Surname and Name): {full_name}")
        print(f"From process 2 (Number of characters): {char_count}")
        print(f"From process 3 (Sum of codes): {pi_result}")

    elif rank == 1:
        received_surname = comm.recv(source=0)
        name = "Oleh"
        result = f"{received_surname} {name}"
        comm.send(result, dest=0)

    elif rank == 2:
        received_surname = comm.recv(source=0)
        result = len(received_surname)
        comm.send(result, dest=0)

    elif rank == 3:
        received_surname = comm.recv(source=0)
        char_sum = sum(ord(char) for char in received_surname)
        result = char_sum * math.pi
        comm.send(result, dest=0)


if __name__ == "__main__":
    main()
