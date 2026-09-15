import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ]
)
predictions = model(x_train[:1]).numpy()
print(predictions)
result = tf.nn.softmax(predictions).numpy()
print(result)

loss_function = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
result = loss_function(y_train[:1], predictions).numpy()
print(result)

model.compile(optimizer="adam", loss=loss_function, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5)

print(model.evaluate(x_test, y_test, verbose=2))
