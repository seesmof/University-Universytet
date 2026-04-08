from matplotlib import pyplot as plt
import numpy as np

# Гіперпараметри
input_size = 1
hidden_size = 18
output_size = 1
learning_rate = 0.01
epochs = 1000

# Ініціалізація ваг
W_xh = np.random.randn(hidden_size, input_size)
W_hh = np.random.randn(hidden_size, hidden_size)
W_hy = np.random.randn(output_size, hidden_size)

# Навчальні дані
X_train = np.linspace(0, 10, 500).reshape(-1, 1)
y_train = np.sin(X_train)
"""
X_train = np.random.rand(500, 18).reshape(-1, 1)
y_train = np.random.randint(0, 2, 500)
"""

# Початковий прихований стан
hidden = np.zeros((hidden_size, 1))


# Функція активації -- гіперболічний тангенс
def tanh(x):
    return np.tanh(x)


# Навчання
for epoch in range(epochs):
    total_loss = 0
    for i in range(len(X_train)):
        # Вхід
        x = X_train[i].reshape(-1, 1)
        # Реальна відповідь
        target = y_train[i].reshape(-1, 1)

        # Прямий прохід
        hidden = tanh(np.dot(W_xh, x) + np.dot(W_hh, hidden))
        output = np.dot(W_hy, hidden)

        # Помилка
        loss = np.mean((output - target) ** 2)
        total_loss += loss

        # Зворотнє поширення -- градієнтний спуск
        d_output = 2 * (output - target)
        d_W_hy = np.dot(d_output, hidden.T)
        d_hidden = np.dot(W_hy.T, d_output) * (1 - hidden**2)
        d_W_xh = np.dot(d_hidden, x.T)
        d_W_hh = np.dot(d_hidden, hidden.T)

        # Оновлення ваг
        W_hy -= learning_rate * d_W_hy
        W_xh -= learning_rate * d_W_xh
        W_hh -= learning_rate * d_W_hh

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# Прогнозування
predictions = []
hidden = np.zeros((hidden_size, 1))
for i in range(len(X_train)):
    x = X_train[i].reshape(-1, 1)
    hidden = tanh(np.dot(W_xh, x) + np.dot(W_hh, hidden))
    output = np.dot(W_hy, hidden)
    predictions.append(output.item())

# Графік
plt.plot(X_train, y_train, label="Реальні дані", color="blue")
plt.plot(X_train, predictions, label="Прогноз", color="red", linestyle="dashed")
plt.legend()
plt.show()
