import threading
from nicegui import ui


class MontgomeryReducer:
    def __init__(self, n):
        self.n = n
        # Вибираємо R як найменшу ступінь 2, більшу за n
        self.k = n.bit_length()
        self.r = 1 << self.k
        self.mask = self.r - 1

        # Знаходимо n_inv, таке що (r * r_inv - n * n_inv) = 1
        # Використовуємо розширений алгоритм Евкліда
        _, _, n_inv = self.extended_gcd(self.r, self.n)
        self.n_inv = -n_inv % self.r

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def reduce(self, t):
        """Алгоритм редукції Монтгомері: обчислює (t * R^-1) mod n"""
        m = ((t & self.mask) * self.n_inv) & self.mask
        u = (t + m * self.n) >> self.k
        if u >= self.n:
            return u - self.n
        return u

    def multiply(self, a_mont, b_mont):
        """Множення у просторі Монтгомері"""
        return self.reduce(a_mont * b_mont)


def task(name, a, b, n):
    """Функція для виконання в окремому потоці"""
    print(f"[Потік {name}] Початок обчислення...")
    mr = MontgomeryReducer(n)

    # Переведення в простір Монтгомері: a' = (a * R) mod n
    a_mont = (a << mr.k) % n
    b_mont = (b << mr.k) % n

    # Множення
    res_mont = mr.multiply(a_mont, b_mont)

    # Повернення з простору Монтгомері
    result = mr.reduce(res_mont)

    print(f"[Потік {name}] Результат {a} * {b} mod {n} = {result}")


"""

# Параметри
n = 7919  # Просте число
data = [(123, 456), (789, 101)]

# Створення потоків
threads = []
for i, (a, b) in enumerate(data):
    t = threading.Thread(target=task, args=(f"Thread-{i + 1}", a, b, n))
    threads.append(t)
    t.start()

# Очікування завершення
for t in threads:
    t.join()
"""

with ui.card().classes("mt-80 mx-auto"):
    with ui.row().classes("w-full"):
        ui.input(label="Simple Number").classes("w-full")
    with ui.row().classes("w-full"):
        ui.input(label="First Pair, First")
        ui.input(label="First Pair, Second")
    with ui.row().classes("w-full"):
        ui.input(label="Second Pair, First")
        ui.input(label="Second Pair, Second")
    ui.button(text="Calculate").classes("w-full")

ui.run(title="TR2. Montgomery", favicon="🔬")
