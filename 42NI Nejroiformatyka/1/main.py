import time
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# 1. Підготовка фіктивних даних
# 18 вхідних ознак, 1 цільова
X = np.random.rand(500, 18)
y = np.random.randint(0, 2, 500)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

learning_rates = [0.001, 0.01, 0.1, 0.5]
train_times = []

# 2. Дослідження впливу кроку навчання (learning_rate) - п. 6
for rate in learning_rates:
    mlp = MLPClassifier(
        hidden_layer_sizes=(8,),
        activation="logistic",
        learning_rate_init=rate,
        max_iter=1000,
    )
    start = time.time()
    mlp.fit(X_train, y_train)
    end = time.time()
    train_times.append(end - start)

# Побудова графіка
plt.figure(figsize=(8, 4))
plt.plot(learning_rates, train_times, marker="o", color="blue")
plt.title("Залежність чассу навчання від кроку (LR)")
plt.xlabel("Learning Rate")
plt.ylabel("Час (с)")
plt.grid(True)
plt.show()

# Порівняння моделей (п. 5, 8)
models = {
    "SLP": MLPClassifier(hidden_layer_sizes=(), activation="logistic", max_iter=1000),
    "MLP (8-1)": MLPClassifier(
        hidden_layer_sizes=(8,), activation="logistic", max_iter=1000
    ),
    "RBF": GaussianProcessClassifier(),
}

results = []
for name, model in models.items():
    # Навчання
    start_train = time.time()
    model.fit(X_train, y_train)
    end_train = time.time()

    # Тестування
    start_test = time.time()
    predictions = model.predict(X_test)
    end_test = time.time()

    accuracy = accuracy_score(y_test, predictions)
    results.append([name, end_train - start_train, 1 - accuracy])

print(f"{'Модель':<10} | {'Час навчання':<10} | {'Помилка':<10}")
for res in results:
    print(f"{res[0]:<10} | {res[1]:.4f}s      | {res[2]:.4f}")
