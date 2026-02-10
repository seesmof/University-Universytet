# workers.py

def power_worker(args):
    """
    Ця функція повинна бути в окремому модулі, щоб 
    multiprocessing міг її коректно імпортувати (pickle).
    """
    base, exponent, modulus = args
    if exponent == 0:
        return 1
    # Вбудована функція pow(base, exp, mod) дуже швидка
    return pow(base, exponent, modulus)