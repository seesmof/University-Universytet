import numpy as np
import random

X = np.random.rand(500, 18)
y = [random.choice([-1, 1]) for _ in range(500)]

for row_i, row in enumerate(X):
    row_average = np.mean(row)

    for cel_i, el in enumerate(row):
        if el < row_average:
            X[row_i][cel_i] = -1
        elif el >= row_average:
            X[row_i][cel_i] = 1

# Об'єднання (створення еталонів)
# по першим зразкам кожного класу
prototype_plus = None
prototype_minus = None

for i in range(len(X)):
    if y[i] == 1 and prototype_plus is None:
        prototype_plus = X[i].copy()
    elif y[i] == -1 and prototype_minus is None:
        prototype_minus = X[i].copy()
    if prototype_plus is not None and prototype_minus is not None:
        break

print("Еталон класу +1:", prototype_plus)
print("Еталон класу -1:", prototype_minus)


# --- Хопфілд ---
class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.n = n_neurons
        self.W = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        """Запам'ятовує еталони"""
        for p in patterns:
            p = p.reshape(-1, 1)
            self.W += p @ p.T
        np.fill_diagonal(self.W, 0)  # немає зв'язків нейрона з собою
        self.W /= len(patterns)

    def predict(self, x, max_iters=50):
        """Відновлює найближчий еталон"""
        x = x.copy()
        for _ in range(max_iters):
            x_old = x.copy()
            for i in range(self.n):
                h = self.W[i] @ x
                x[i] = 1 if h >= 0 else -1
            if np.array_equal(x, x_old):
                break
        return x


# Навчання мережі
hopfield = HopfieldNetwork(n_neurons=18)
hopfield.train([prototype_plus, prototype_minus])


def classify(vector):
    restored = hopfield.predict(vector)

    # Відстань Хеммінга до кожного еталону
    dist_to_plus = np.sum(restored != prototype_plus)
    dist_to_minus = np.sum(restored != prototype_minus)

    return 1 if dist_to_plus < dist_to_minus else -1


print("\n" + "=" * 50)
print("ПЕРЕВІРКА ТОЧНОСТІ")
print("=" * 50)

correct = 0
for i in range(len(X)):
    pred = classify(X[i])
    if pred == y[i]:
        correct += 1

accuracy = correct / len(X) * 100
print(f"Точність на навчальних даних: {accuracy:.1f}%")
