from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim

"""
500 екземплярів, 500 епох, 80/20: навчальна 73.75%, тестова 48%
500 екземплярів, 500 епох, 70/30: навчальна 95.71%, тестова 52%
1000 екземплярів, 500 епох, 70/30: навчальна 81.57%, тестова 55.33%
5000 екземплярів, 500 епох, 70/30: навчальна 65.60%, тестова 50.07%
500 екземплярів, 200 епох, 70/30: навчальна 81.43%, тестова 52%
    краще щоб навчальна була хоча б 90-95 (або більше), тестова 60 і вище
"""

INSTANCES = 500
EPOCHS = 500
print(f"{INSTANCES=}, {EPOCHS=}")

np.random.seed(42)
torch.manual_seed(42)

# Генерація даних
X = np.random.rand(INSTANCES, 18)
y = np.random.randint(0, 2, INSTANCES)

# Розділення вибірки на навчальну та тестову
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Гіперпараметри
input_size = 1
hidden_size = 18
output_size = 1
epochs = EPOCHS
learning_rate = 0.01

# Дані для RNN потрібно перетворити у формат (samples, timesteps, features)
X_train_rnn = X_train.reshape(-1, 18, 1)
X_test_rnn = X_test.reshape(-1, 18, 1)
# 18 ознак → 18 часових кроків, 1 ознака на кроці

# Перетворення на тензори
X_train_tensor = torch.tensor(X_train_rnn, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
X_test_tensor = torch.tensor(X_test_rnn, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)


# Нейромережа Ельмана
class ElmanNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ElmanNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)

        self.tanh = nn.Tanh()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, hidden):
        # Об'єднання поточного входу і прихованого стану
        combined = torch.cat((x, hidden), dim=1)
        hidden = torch.tanh(self.i2h(combined))
        output = self.sigmoid(self.h2o(hidden))
        return output, hidden


# Ініціалізація мережі
model = ElmanNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# --- Навчання ---
train_losses = []

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()

    total_loss = 0
    for i in range(len(X_train_tensor)):
        hidden = torch.zeros(1, hidden_size)

        # 18 ознак послідовно
        for t in range(18):
            current_input = X_train_tensor[i, t, :].view(1, -1)  # (1, 1)
            output, hidden = model(current_input, hidden)

        # Втрати (тільки останній вихід)
        loss = criterion(output, y_train_tensor[i].view(1, -1))
        total_loss += loss

    # Зворотне поширення
    total_loss.backward()
    optimizer.step()

    avg_loss = total_loss.item() / len(X_train_tensor)
    train_losses.append(avg_loss)

# Перевірка результату
print("\nОцінка моделі:")
print("-" * 40)

model.eval()

# --- Навчальні дані ---
train_correct = 0
with torch.no_grad():
    for i in range(len(X_train_tensor)):
        hidden = torch.zeros(1, hidden_size)
        for t in range(18):
            current_input = X_train_tensor[i, t, :].view(1, -1)
            output, hidden = model(current_input, hidden)
        pred = 1 if output.item() >= 0.5 else 0
        if pred == y_train[i]:
            train_correct += 1

train_acc = train_correct / len(X_train_tensor)
print(f"Точність на навчальних даних: {train_acc * 100:.2f}%")

# --- Тестові дані ---
test_correct = 0
with torch.no_grad():
    for i in range(len(X_test_tensor)):
        hidden = torch.zeros(1, hidden_size)
        for t in range(18):
            current_input = X_test_tensor[i, t, :].view(1, -1)
            output, hidden = model(current_input, hidden)
        pred = 1 if output.item() >= 0.5 else 0
        if pred == y_test[i]:
            test_correct += 1

test_acc = test_correct / len(X_test_tensor)
print(f"Точність на тестових даних: {test_acc * 100:.2f}%")
