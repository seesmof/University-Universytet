import math
import multiprocessing
from functools import reduce


def modular_exponentiation_worker(args):
    """
    Функція для виконання на окремому процесорі/потоці.
    Обчислює: base^exponent % modulus
    """
    base, exponent, modulus, thread_id = args
    if exponent == 0:
        return 1

    # Python має вбудовану оптимізовану функцію pow(a, b, m)
    # яка використовує метод "підноси до квадрату і множ" (binary exponentiation)
    result = pow(base, exponent, modulus)
    return result


def solve_comb_method():
    print("=== Метод Гребеня (Comb Method) Модульного Піднесення до Степеня ===")

    try:
        # Введення даних з клавіатури
        a = int(input("Введіть основу (a): "))
        n_val = int(input("Введіть показник степеня (n): "))
        m = int(input("Введіть модуль (m): "))
        p = int(input("Введіть кількість потоків/процесорів (p): "))

        if p <= 0:
            print("Кількість потоків має бути > 0")
            return

    except ValueError:
        print("Будь ласка, вводьте тільки цілі числа.")
        return

    # 1. Розподіл показника степеня (Формування s_i)
    # s_i міститиме біти n, що знаходяться на позиціях j*p + i

    s = [0] * p  # Масив для часткових показників s_0 ... s_{p-1}

    # Отримуємо бітове представлення числа n
    # bit_length() повертає кількість бітів, необхідних для представлення числа
    num_bits = n_val.bit_length()

    print(f"\n[*] Кількість бітів у показнику: {num_bits}")
    print("[*] Розподіл бітів по процесорах (гребінь)...")

    # Проходимо по всіх бітах показника степеня
    # Реалізація формули: s_i = Sum( b_{jp+i} * 2^{jp+i} )
    for k in range(num_bits):
        # Перевіряємо k-й біт числа n
        if (n_val >> k) & 1:
            # Визначаємо, якому процесору належить цей біт (i = k mod p)
            processor_index = k % p

            # Додаємо вагу біта (2^k) до відповідного s_i
            # Використовуємо побітове АБО (OR), що еквівалентно додаванню для степенів двійки
            s[processor_index] |= 1 << k

    # Вивід проміжних значень s_i для перевірки
    print("\nЧасткові показники (s_i):")
    for i, val in enumerate(s):
        print(f"  Procesor {i}: s_{i} = {val} (bin: {bin(val)})")

    # Перевірка: сума всіх s_i повинна дорівнювати n
    if sum(s) != n_val:
        print("Помилка алгоритму розподілу бітів!")
        return

    # 2. Паралельне обчислення y_i = a^(s_i) mod m
    # Підготовка аргументів для воркерів
    tasks = [(a, partial_exp, m, i) for i, partial_exp in enumerate(s)]

    print(f"\n[*] Запуск {p} паралельних процесів для обчислення a^(s_i) mod m...")

    results = []
    # Використовуємо Pool для справжнього паралелізму процесів (обхід GIL)
    with multiprocessing.Pool(processes=p) as pool:
        results = pool.map(modular_exponentiation_worker, tasks)

    print("Результати потоків:", results)

    # 3. Об'єднання результатів
    # y = y_0 * y_1 * ... * y_{p-1} (mod m)
    print("\n[*] Об'єднання результатів...")

    final_result = 1
    for part_res in results:
        final_result = (final_result * part_res) % m

    print(f"\n=== Результат: {final_result} ===")

    # Для перевірки (на малих числах) порівняємо зі звичайним піднесенням
    expected = pow(a, n_val, m)
    if final_result == expected:
        print("✅ Перевірка успішна: результат збігається зі стандартним pow().")
    else:
        print(f"❌ Помилка: очікувалось {expected}")


if __name__ == "__main__":
    # Необхідно для коректної роботи multiprocessing у Windows
    solve_comb_method()
