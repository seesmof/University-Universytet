from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim

# Генерація даних
X = np.random.rand(500, 18)
y = np.random.randint(0, 2, 500)

# Розділення вибірки на навчальну та тестову
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Гіперпараметри
input_size = 1
hidden_size = 18
output_size = 1
epochs = 1000
learning_rate = 0.01

# Перетворення на тензори
X_train = torch.tensor(X_train, dtype=torch.float32).view(-1, 1)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)


# Нейромережа Ельмана
class ElmanNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ElmanNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):
        # Об'єднання поточного входу і прихованого стану
        combined = torch.cat((x, hidden), 1)
        hidden = torch.tanh(self.i2h(combined))
        output = self.h2o(hidden)
        return output, hidden


# Ініціалізація мережі
model = ElmanNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# --- Навчання ---
hidden = torch.zeros(1, hidden_size)
for epoch in range(epochs):
    optimizer.zero_grad()
    loss = 0
    for i in range(len(X_train)):
        output, hidden = model(X_train[i].view(1, -1), hidden)
        loss += criterion(output, y_train[i].view(1, -1))
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Перевірка результату
predictions = []
hidden = torch.zeros(1, hidden_size)
for i in range(len(X_train)):
    output, hidden = model(X_train[i].view(1, -1), hidden)
    predictions.append(output.item())

# Візуалізація
plt.plot(X_train.numpy(), y_train.numpy(), label="Реальні дані", color="blue")
plt.plot(
    X_train.numpy(),
    predictions,
    label="Прогноз мережі Ельмана",
    color="red",
    linestyle="dashed",
)
plt.legend()
plt.show()
