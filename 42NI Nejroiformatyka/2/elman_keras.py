import numpy as np
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense

# 1000 прикладів, 10 кроків, 1 ознака
X_train = np.random.rand(1000, 10, 1)
y_train = np.sum(X_train, axis=1)

model = Sequential(
    [
        SimpleRNN(10, activation="tanh", return_sequences=False, input_shape=(10, 1)),
        Dense(1, activation="linear"),
    ]
)

model.compile(optimizer="adam", loss="mse")

model.fit(X_train, y_train, epochs=20, batch_size=16)

X_test = np.random.rand(10, 10, 1)
y_pred = model.predict(X_test)

print(f"Predicted value: {y_pred.flatten()}")
