"""
Розробити послідовні алгоритм та программу обчислення числа πз можливістю вимірювання часу роботи програми для заданого nта визначення помилки апроксимації інтеграла. Для цього використовуйте функцію вимірювання часу бібліотеки MPI, як еталонне значення числа π прийміть 3.141592653589793238462643.

Дослідіть точність та швидкодію програми обчислення π для значень кількості інтервалів 10^3, 10^4, 10^5, 10^6, 10^7, 10^9. Результати подайте у звіті у вигляді таблиці.
"""

from mpi4py import MPI


def calculate_pi(n):
    step = 1.0 / n
    total_sum = 0.0

    start_time = MPI.Wtime()

    for i in range(n):
        x = (i + 0.5) * step
        total_sum += 4.0 / (1.0 + x * x)
    pi_approx = total_sum * step

    end_time = MPI.Wtime()

    return pi_approx, end_time - start_time


def main():
    PI_REF = 3.141592653589793238462643

    n_values = [10**3, 10**4, 10**5, 10**6, 10**7, 10**9]

    print(f"{'n':<12} | {'Calculated PI':<18} | {'Error':<21} | {'Time (sec)':<12}")
    print("-" * 70)

    for n in n_values:
        pi_val, duration = calculate_pi(n)
        error = abs(PI_REF - pi_val)

        print(f"{n:<12e} | {pi_val:<18.15f} | {error:<18.15e} | {duration:<12.6f}")


if __name__ == "__main__":
    main()
