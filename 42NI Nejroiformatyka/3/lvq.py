from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import json
import os


class LVQ:
    """
    Learning Vector Quantization (LVQ1) - ручна реалізація
    """

    def __init__(self, n_prototypes_per_class=3, learning_rate=0.1, max_epochs=100):
        """
        Параметри:
        - n_prototypes_per_class: кількість прототипів на клас
        - learning_rate: швидкість навчання (α)
        - max_epochs: максимальна кількість епох
        """
        self.n_prototypes_per_class = n_prototypes_per_class
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.prototypes = []  # список прототипів (вектори ваг)
        self.prototype_labels = []  # мітки класів прототипів

    def fit(self, X, y):
        """
        Навчання LVQ
        X: вхідні дані (n_samples, n_features)
        y: цільові мітки (0 або 1)
        """
        n_features = X.shape[1]
        self.prototypes = []
        self.prototype_labels = []

        # Ініціалізація прототипів: випадкові зразки з кожного класу
        for class_label in [0, 1]:
            X_class = X[y == class_label]
            n_prototypes = min(self.n_prototypes_per_class, len(X_class))
            indices = np.random.choice(len(X_class), n_prototypes, replace=False)
            for idx in indices:
                self.prototypes.append(X_class[idx].copy())
                self.prototype_labels.append(class_label)

        self.prototypes = np.array(self.prototypes)
        self.prototype_labels = np.array(self.prototype_labels)

        # Навчання
        for epoch in range(self.max_epochs):
            # Перемішуємо дані
            indices = np.random.permutation(len(X))
            epoch_errors = 0

            for i in indices:
                x = X[i]
                true_label = y[i]

                # Знаходимо найближчий прототип
                distances = np.linalg.norm(self.prototypes - x, axis=1)
                winner_idx = np.argmin(distances)
                winner_label = self.prototype_labels[winner_idx]
                # Оновлення за правилом LVQ
                if winner_label == true_label:
                    # Правильна класифікація → наближаємо прототип
                    self.prototypes[winner_idx] += self.learning_rate * (
                        x - self.prototypes[winner_idx]
                    )
                else:
                    # Помилкова класифікація → віддаляємо прототип
                    self.prototypes[winner_idx] -= self.learning_rate * (
                        x - self.prototypes[winner_idx]
                    )

            # Зменшуємо швидкість навчання з часом
            self.learning_rate *= 0.99

        return self

    def predict(self, X):
        """
        Передбачення класів для нових зразків
        """
        predictions = []
        for x in X:
            distances = np.linalg.norm(self.prototypes - x, axis=1)
            winner_idx = np.argmin(distances)
            predictions.append(self.prototype_labels[winner_idx])
        return np.array(predictions)

    def predict_proba(self, X):
        """
        Повертає ймовірність класу 1 (на основі відстаней)
        """
        proba = []
        for x in X:
            distances = np.linalg.norm(self.prototypes - x, axis=1)
            # Знаходимо найближчі прототипи кожного класу
            min_dist_class0 = min(
                [
                    distances[i]
                    for i in range(len(self.prototypes))
                    if self.prototype_labels[i] == 0
                ],
                default=np.inf,
            )
            min_dist_class1 = min(
                [
                    distances[i]
                    for i in range(len(self.prototypes))
                    if self.prototype_labels[i] == 1
                ],
                default=np.inf,
            )

            # Ймовірність класу 1 (обернено пропорційна відстані)
            if min_dist_class0 + min_dist_class1 > 0:
                prob = min_dist_class0 / (min_dist_class0 + min_dist_class1)
            else:
                prob = 0.5
            proba.append(prob)
        return np.array(proba)


# Генерація даних
N = 500

X = np.random.rand(N, 18)
y = np.random.randint(0, 2, N)

# Розділення на навчальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42
)

# Створення та навчання LVQ
lvq = LVQ(n_prototypes_per_class=5, learning_rate=0.1, max_epochs=30)
lvq.fit(X_train, y_train)

# Передбачення
y_train_pred = lvq.predict(X_train)
y_test_pred = lvq.predict(X_test)

# Точність
train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

print("\n2. Результати LVQ:")
print(f"   Точність на навчальних даних: {train_acc * 100:.2f}%")
print(f"   Точність на тестових даних: {test_acc * 100:.2f}%")

# Інформація про прототипи
print("\n3. Прототипи:")
print(f"   Кількість прототипів: {len(lvq.prototypes)}")
for label in [0, 1]:
    n_protos = np.sum(lvq.prototype_labels == label)
    print(f"   Клас {label}: {n_protos} прототипів")

"""
500 зразків, 5 прототипів, 100 епох
- 80/20: навчальна 87%, тестова 46%
500 зразків, 2 прототипи, 100 епох
- 80/20: навчальна 78%, тестова 49.50%
500 зразків, 5 прототипів, 50 епох
- 80/20: навчальна 82%, тестова 50.25%
500 зразків, 5 прототипів, 30 епох
- 80/20: навчальна 84%, тестова 54%
500 зразків, 5 прототипів, 20 епох
- 80/20: навчальна 86%, тестова 49%
"""

data = {"Train Accuracy": train_acc, "Test Accuracy": test_acc}
current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "lvq_output.json")
with open(file_path, encoding="utf-8", mode="w") as f:
    json.dump(data, f, indent=2)
