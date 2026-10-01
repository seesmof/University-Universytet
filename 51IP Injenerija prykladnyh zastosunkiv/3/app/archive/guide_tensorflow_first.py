import numpy as np
import tensorflow_datasets as tfds
import tensorflow as tf

tfds.disable_progress_bar()

dataset, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
train_dataset, test_dataset = dataset["train"], dataset["test"]
print(train_dataset.element_spec)

for example, label in train_dataset.take(1):
    print(f"Text: {example.numpy()}")
    print(f"Label {label.numpy()}")

BUFFER_SIZE = 10_000
BATCH_SIZE = 64
train_dataset = (
    train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
)
# Вивести перші три тексти у навчальній вибірці та відповідні їм мітки
for example, label in train_dataset.take(1):
    print(f"Texts: {example.numpy()[:3]}")
    print(f"\nLabels: {label.numpy()[:3]}")

VOCAB_SIZE = 1_000
encoder = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE)
encoder.adapt(train_dataset.map(lambda text, label: text))

vocab = np.array(encoder.get_vocabulary())
print(vocab[:20])

encoded_example = encoder(example)[:3].numpy()
print(encoded_example)

for n in range(3):
    print(f"Original: {example[n].numpy()}")
    print(f'Round-trip: {", ".join(vocab[encoded_example[n]])}')

model = tf.keras.Sequential(
    [
        encoder,
        tf.keras.layers.Embedding(
            input_dim=len(encoder.get_vocabulary()), output_dim=64, mask_zero=True
        ),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1),
    ]
)
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(1e-4),
    metrics=["accuracy"],
)
history = model.fit(
    train_dataset, epochs=10, validation_data=test_dataset, validation_steps=30
)
test_loss, test_acc = model.evaluate(test_dataset)

print(f"Test Loss: {test_loss}")
print(f"Test Accruacy: {test_acc}")

import matplotlib.pyplot as plt


def plot_graphs(history, metric):
    plt.plot(history.history[metric])
    plt.plot(history.history[f"val_{metric}"], "")
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend([metric, f"val_{metric}"])


plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plot_graphs(history, "accuracy")
plt.ylim(None, 1)
plt.subplot(1, 2, 2)
plot_graphs(history, "loss")
plt.ylim(0, None)
plt.show()
