import matplotlib.pyplot as plt
import random
import math


def run_monte_carlo_app(total_points):
    in_circle_x, in_circle_y = [], []
    out_circle_x, out_circle_y = [], []

    pi_values = []
    counts = []
    hits = 0

    # 1. Процес генерації точок
    for i in range(1, total_points + 1):
        x, y = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)

        if x * x + y * y <= 0.25:  # Умова P належить Omega (R=0.5)
            hits += 1
            if i <= 2000:  # Обмежуємо малювання для швидкості
                in_circle_x.append(x)
                in_circle_y.append(y)
        else:
            if i <= 2000:
                out_circle_x.append(x)
                out_circle_y.append(y)

        # Зберігаємо прогрес для графіка (кожні 100 кроків)
        if i % 100 == 0:
            pi_values.append(4 * hits / i)
            counts.append(i)

    # 2. Візуалізація
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Лівий графік: Мішень
    ax1.scatter(in_circle_x, in_circle_y, color="green", s=1, label="Всередині (P ∈ Ω)")
    ax1.scatter(out_circle_x, out_circle_y, color="red", s=1, label="Зовні (P ∉ Ω)")
    circle = plt.Circle((0, 0), 0.5, color="blue", fill=False, linewidth=2)
    ax1.add_artist(circle)
    ax1.set_title(f"Візуалізація точок (перші 2000)")
    ax1.set_aspect("equal")
    ax1.legend()

    # Правий графік: Збіжність до Pi
    ax2.plot(counts, pi_values, color="blue", label="Обчислене π")
    ax2.axhline(y=math.pi, color="red", linestyle="--", label="Справжнє π")
    ax2.set_xlabel("Кількість точок (n)")
    ax2.set_ylabel("Значення π")
    ax2.set_title("Збіжність методу Монте-Карло")
    ax2.legend()

    plt.tight_layout()
    plt.show()


# Запуск: спробуємо 50,000 точок
run_monte_carlo_app(50000)
