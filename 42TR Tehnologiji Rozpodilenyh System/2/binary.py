def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus  # Обробляємо випадок, коли база більша за модуль

    while exponent > 0:
        # Якщо поточний біт (наймолодший) дорівнює 1
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Підносимо базу до квадрата і зсуваємо степінь вправо
        base = (base * base) % modulus
        exponent //= 2

    return result


a = 636737773
n = 262662666
m = 888272727
print(modular_pow(a, n, m))
print(pow(a, n, m))
