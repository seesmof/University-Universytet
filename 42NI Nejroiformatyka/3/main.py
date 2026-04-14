from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from minisom import MiniSom
import numpy as np

# Генерація даних
N = 500

X = np.random.rand(N, 18)
y = np.random.randint(0, 2, N)

# Розділення на навчальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42
)

# --- Навчання SOFM ---
# Створюємо карту 8×8 нейронів
map_size = (8, 8)
som = MiniSom(
    x=map_size[0],
    y=map_size[1],
    input_len=18,
    sigma=1.0,  # радіус сусідства
    learning_rate=0.5,
    random_seed=42,
)

# Ініціалізація ваг
som.random_weights_init(X_train)

# --- Маркування нейронів ---
# Кожен нейрон отримує мітку за більшістю зразків, які до нього потрапили

neuron_labels = np.zeros(map_size)
neuron_counts = np.zeros(map_size)

for i, sample in enumerate(X_train):
    winner = som.winner(sample)  # координати нейрона-переможця
    neuron_labels[winner] += y_train[i]
    neuron_counts[winner] += 1

# Перетворюємо в мітку класу (0 або 1) на основі більшості
for i in range(map_size[0]):
    for j in range(map_size[1]):
        if neuron_counts[i, j] > 0:
            # Якщо більшість зразків класу 1
            if neuron_labels[i, j] / neuron_counts[i, j] >= 0.5:
                neuron_labels[i, j] = 1
            else:
                neuron_labels[i, j] = 0
        else:
            neuron_labels[i, j] = -1  # нейрон без зразків

print("\nКарта міток нейронів (8×8):")
print(neuron_labels.astype(int))


# --- Класифікація ---
def classify(sample):
    """Класифікує новий зразок"""
    winner = som.winner(sample)
    return int(neuron_labels[winner])


# Передбачення на тренувальних даних
train_pred = [classify(sample) for sample in X_train]
train_acc = accuracy_score(y_train, train_pred)

# Передбачення на тестових даних
test_pred = [classify(sample) for sample in X_test]
test_acc = accuracy_score(y_test, test_pred)

print(f"\nТочність на тренувальних даних: {train_acc * 100:.2f}%")
print(f"Точність на тестових даних: {test_acc * 100:.2f}%")

"""
Карта 8х8
500 зразків:
- Коли розбиття 80/20, точність тренувальних 79%, на тестових 52%
- Коли розбиття 70/30, точність тренувальних 72.67%, на тестових 53.14%
1000 зразків:
- Коли розбиття 80/20, точність тренувальних 69%, на тестових 50.62%
5000 зразків:
- Коли розбиття 80/20, точність тренувальних 57.30%, на тестових 51.38%

Карта 4х4
500 зразків:
- Коли розбиття 80/20, точність тренувальних 65%, на тестових 51.75%

Карта 5х5
500 зразків:
- Коли розбиття 80/20, точність тренувальних 66%, на тестових 46.50%

Карта 6х6
500 зразків:
- Коли розбиття 80/20, точність тренувальних 73%, на тестових 48.25%

Карта 7х7
500 зразків:
- Коли розбиття 80/20, точність тренувальних 71%, на тестових 46%
"""

# --- Візуалізація ---
# Візуалізація карти нейронів з кольорами класів
plt.figure(figsize=(10, 8))
plt.imshow(neuron_labels, cmap="RdBu", origin="lower", vmin=-1, vmax=1)
plt.colorbar(label="Клас (0=синій, 1=червоний)")
plt.title("Карта SOFM з маркуванням нейронів")
plt.xlabel("X координата")
plt.ylabel("Y координата")

# Додаємо текстові мітки
for i in range(map_size[0]):
    for j in range(map_size[1]):
        if neuron_counts[i, j] > 0:
            color = "white" if neuron_labels[i, j] == 1 else "black"
            plt.text(
                j,
                i,
                str(int(neuron_labels[i, j])),
                ha="center",
                va="center",
                color=color,
                fontsize=8,
            )
        else:
            plt.text(j, i, "?", ha="center", va="center", color="gray", fontsize=8)

plt.show()

"""
Червоні зі знаком питання на графіку це нейрони, які жодного разу не стали переможцями.
"""
