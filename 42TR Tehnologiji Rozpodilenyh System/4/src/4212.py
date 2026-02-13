import matplotlib.pyplot as plt

# --- ВСТАВТЕ ВАШІ ДАНІ СЮДИ ---
P_values = [1, 2, 3, 4]  # Кількість процесорів
# Замініть ці цифри на ті, що ви отримали під час тестів:
Tp_values = [24.6048, 12.5789, 8.4814, 6.6128]  # Приклад часу виконання у секундах
# ------------------------------

# 1. Розрахунок прискорення S
T1 = Tp_values[0]
S_values = [T1 / Tp for Tp in Tp_values]

# 2. Розрахунок ідеального прискорення (для порівняння)
ideal_S = P_values

# 3. Налаштування графіка
plt.figure(figsize=(10, 6))
plt.plot(P_values, S_values, "ro-", label="Реальне прискорення (S)", linewidth=2)
plt.plot(P_values, ideal_S, "b--", label="Ідеальне прискорення (S=P)", alpha=0.7)

# Додавання підписів значень над точками
for i, txt in enumerate(S_values):
    plt.annotate(
        f"{txt:.2f}",
        (P_values[i], S_values[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

# Оформлення осей та заголовка
plt.title("Залежність прискорення від кількості процесорів (N=240000)", fontsize=14)
plt.xlabel("Кількість процесорів (P)", fontsize=12)
plt.ylabel("Прискорення (S)", fontsize=12)
plt.xticks(P_values)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Збереження та показ
plt.savefig("speedup_graph.png")
print("Графік збережено у файл 'speedup_graph.png'")
plt.show()
