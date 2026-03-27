import json
import os

from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from torch import nn
import numpy as np
import time
import torch

# --- Генерація даних ---
np.random.seed(0)

# Кількість прикладів
N = 500
X = np.random.rand(N, 18)

# Штучна залежність (імітація задачі)
y = (X[:, 0] + X[:, 1] + X[:, 2] > 1.5).astype(int)
y = y.reshape(-1, 1)

# Нормалізація
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Перетворення в torch
X_train_t = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1)
X_test_t = torch.tensor(X_test, dtype=torch.float32).unsqueeze(1)
y_train_t = torch.tensor(y_train, dtype=torch.float32)
y_test_t = torch.tensor(y_test, dtype=torch.float32)


# --- Мережа Ельмана ---
class ElmanNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(input_size=18, hidden_size=8, batch_first=True)
        self.fc = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])
        return self.sigmoid(out)


elman = ElmanNet()

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(elman.parameters(), lr=0.01)

# --- Навчання ---
start_train = time.time()

for epoch in range(100):
    outputs = elman(X_train_t)
    loss = criterion(outputs, y_train_t)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

end_train = time.time()
elman_train_time = end_train - start_train

# --- Оцінка ---
start_test = time.time()
pred_train = (elman(X_train_t) > 0.5).float()
elman_train_accuracy = (pred_train == y_train_t).float().mean().item()
end_test = time.time()
elman_train_test_time = end_test - start_test

start_test = time.time()
pred_test = (elman(X_test_t) > 0.5).float()
elman_test_accuracy = (pred_test == y_test_t).float().mean().item()
end_test = time.time()
elman_test_time = end_test - start_test


# --- Мережа Хопфілда ---
class Hopfield:
    def __init__(self, n):
        self.n = n
        self.W = np.zeros((n, n))

    def train(self, patterns):
        for p in patterns:
            p = p.reshape(-1, 1)
            self.W += p @ p.T
        np.fill_diagonal(self.W, 0)

    def predict(self, x):
        return np.sign(self.W @ x)


# Беремо перші 50 прикладів
patterns = np.where(X_train[:50] > 0, 1, -1)

hopfield = Hopfield(18)

# --- Навчання ---
start_train = time.time()
hopfield.train(patterns)
end_train = time.time()
hopfield_train_time = end_train - start_train


# --- Оцінка ---
def hopfield_accuracy(model, X, y):
    correct = 0
    for i in range(len(X)):
        x = np.where(X[i] > 0, 1, -1)
        pred = model.predict(x)
        pred_class = 1 if pred.sum() > 0 else 0
        if pred_class == y[i]:
            correct += 1
    return correct / len(X)


start_test = time.time()
hopfield_train_accuracy = hopfield_accuracy(hopfield, X_train, y_train.flatten())
end_test = time.time()
hopfield_train_test_time = end_test - start_test

start_test = time.time()
hopfield_test_accuracy = hopfield_accuracy(hopfield, X_test, y_test.flatten())
end_test = time.time()
hopfield_test_time = end_test - start_test

# --- Вивід результатів ---
print("\n=== Ельман ===")
print(f"Train accuracy: {elman_train_accuracy}")
print(f"Test accuracy: {elman_test_accuracy}")

print("\n=== Хопфілд ===")
print(f"Train accuracy: {hopfield_train_accuracy}")
print(f"Test accuracy: {hopfield_test_accuracy}")

# Збереження
torch.save(elman.state_dict(), "elman_weights.pth")

results = {
    "Elman": {
        "train_accuracy": elman_train_accuracy,
        "test_accuracy": elman_test_accuracy,
        "train_time": elman_train_time,
        "train_classification_time": elman_train_test_time,
        "test_classification_time": elman_test_time,
    },
    "Hopfield": {
        "train_accuracy": hopfield_train_accuracy,
        "test_accuracy": hopfield_test_accuracy,
        "train_time": hopfield_train_time,
        "train_classification_time": hopfield_train_test_time,
        "test_classification_time": hopfield_test_time,
    },
}

with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"),
    encoding="utf-8",
    mode="w",
) as f:
    json.dump(results, f, indent=2)
print("\nResults saved in 'results.json'")
