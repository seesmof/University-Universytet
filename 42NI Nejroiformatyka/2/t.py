from doctest import REPORT_CDIFF

from matplotlib import pyplot as plt
import numpy as np


input_size = 1
hidden_size = 18
output_size = 1
learning_rate = 0.01
epochs = 1000

W_xh = np.random.randn(hidden_size, input_size)
W_hh = np.random.randn(hidden_size, hidden_size)
W_hy = np.random.randn(output_size, hidden_size)

X_train = np.linspace(0, 10, 500).reshape(-1, 1)
y_train = np.sin(X_train)

hidden = np.zeros((hidden_size, 1))


def tanh(x):
    return np.tanh(x)


for epoch in range(epochs):
    total_loss = 0
    for i in range(len(X_train)):
        x = X_train[i].reshape(-1, 1)
        target = y_train[i].reshape(-1, 1)

        hidden = tanh(np.dot(W_xh, x) + np.dot(W_hh, hidden))
        output = np.dot(W_hy, hidden)

        loss = np.mean((output - target) ** 2)
        total_loss += loss

        d_output = 2 * (output - target)
        d_W_hy = np.dot(d_output, hidden.T)
        d_hidden = np.dot(W_hy.T, d_output) * (1 - hidden**2)
        d_W_xh = np.dot(d_hidden, x.T)
        d_W_hh = np.dot(d_hidden, hidden.T)

        W_hy -= learning_rate * d_W_hy
        W_xh -= learning_rate * d_W_xh
        W_hh -= learning_rate * d_W_hh

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

predictions = []
hidden = np.zeros((hidden_size, 1))
for i in range(len(X_train)):
    x = X_train[i].reshape(-1, 1)
    hidden = tanh(np.dot(W_xh, x) + np.dot(W_hh, hidden))
    output = np.dot(W_hy, hidden)
    predictions.append(output.item())

plt.plot(X_train, y_train, label="Реальні дані", color="blue")
plt.plot(X_train, predictions, label="Прогноз", color="red", linestyle="dashed")
plt.legend()
plt.show()
