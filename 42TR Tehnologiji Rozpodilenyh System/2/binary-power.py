"""
Реалізувати бінарний метод модульного піднесення до степені.
"""


def power_modular(a, n, m):
    """
    Обчислює (a^e)%m за допомогою бінарного методу.

    - a: основа, base
    - n: ступінь, exponent
    - m: модуль, modulus
    """

    if m == 1:
        return 0
    result = 1
    a = a % m
    while n > 0:
        if n % 2 == 1:  # Якщо exponent непарний
            result = (result * a) % m
        n = n // 2  # Ділимо exponent навпіл
        a = (a * a) % m  # Підносимо основу до квадрата
    return result


# Приклад використання: (3^13)%7 = 1594323%7 = 3
base = 3
exponent = 13
modulus = 7
print(f"({base}^{exponent}) % {modulus} = {power_modular(base, exponent, modulus)}")
