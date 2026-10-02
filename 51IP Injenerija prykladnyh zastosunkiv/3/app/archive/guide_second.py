from typing import Any

import tensorflow as tf
import numpy as np
import time
import os

path_to_file = tf.keras.utils.get_file(
    "shakespeare.txt",
    "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt",
)
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
print(f"Length of text: {len(text)} characters.")
print(text[:250])
vocab = sorted(set(text))
print(f"{len(vocab)} unique characters: {vocab}")

example_texts = [
    "For God so loved the world",
    "For whoever calls on the name of the Lord will be saved.",
]
chars = tf.strings.unicode_split(example_texts, input_encoding="UTF-8")
print(f"{chars = }")

ids_from_chars = tf.keras.layers.StringLookup(vocabulary=list(vocab), mask_token=None)
ids = ids_from_chars(chars)
print(f"{ids = }")

chars_from_ids = tf.keras.layers.StringLookup(
    vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None
)
chars = chars_from_ids(ids)
print(f"{chars = }")


def text_from_ids(ids):
    return tf.strings.reduce_join(chars_from_ids(ids), axis=-1)


all_ids = ids_from_chars(tf.strings.unicode_split(text, "UTF-8"))
print(f"{all_ids = }")

ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)
for ids in ids_dataset.take(10):
    print(chars_from_ids(ids).numpy().decode("utf-8"))

seq_length = 100
sequences = ids_dataset.batch(seq_length + 1, drop_remainder=True)
for seq in sequences.take(1):
    print(chars_from_ids(seq))
for seq in sequences.take(5):
    print(text_from_ids(seq).numpy())


def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text


dataset = sequences.map(split_input_target)
for input_example, target_example in dataset.take(1):
    print(f"Input: {text_from_ids(input_example).numpy()}")
    print(f"Target: {text_from_ids(target_example).numpy()}")

BATCH_SIZE = 64
BUFFER_SIZE = 10_000

dataset = (
    dataset.shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE, drop_remainder=True)
    .prefetch(tf.data.experimental.AUTOTUNE)
)
print(f"{dataset = }")

vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 1024


class MyModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, rnn_units):
        super().__init__(self)
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(
            rnn_units, return_sequences=True, return_state=True
        )
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs, states=None, return_state=False, training=False):
        x = inputs
        x = self.embedding(x, training=training)
        if states is None:
            states = self.gru.get_initial_state(x)
        x, states = self.gru(x, initial_state=states, training=training)
        x = self.dense(x, training=training)

        if return_state:
            return x, states
        else:
            return x


model = MyModel(vocab_size=vocab_size, embedding_dim=embedding_dim, rnn_units=rnn_units)

for input_example_batch, target_example_batch in dataset.take(1):
    example_batch_predictions = model(input_example_batch)
    print(example_batch_predictions.shape, "(batch_size, sequence_length, vocab_size)")
model.summary()

sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sample_indices = tf.squeeze(sampled_indices, axis=-1).numpy()
print("===", sampled_indices)
print("Input:\n", text_from_ids(input_example_batch[0]).numpy())
print("\nNext Char Predictions:\n", text_from_ids(sampled_indices).numpy())

loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
example_batch_mean_loss = loss(target_example_batch, example_batch_predictions)
print(
    "Preidction shape: ",
    example_batch_predictions.shape,
    " # (batch_size, sequence_length, vocal_size)",
)
print("Mean loss: ", example_batch_mean_loss)
print(tf.exp(example_batch_mean_loss).numpy())
model.compile(optimizer="adam", loss=loss)

checkpoint_dir = "./training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_dir, f"ckpt_{epoch}")
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix, save_weights_only=True
)

EPOCHS = 20
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])


class OneStep(tf.keras.Model):
    def __init__(self, model, chars_from_ids, ids_from_chars, temperature=1.0):
        super().__init__()
        self.temperature = temperature
        self.model = model
        self.chars_from_ids = chars_from_ids
        self.ids_from_chars = ids_from_chars

        skip_ids = self.ids_from_chars(["UNK"])[:, None]
        sparse_mask = tf.SparseTensor(
            values=[-float("inf")] * len(skip_ids),
            indices=skip_ids,
            dense_shape=[len(ids_from_chars.get_vocabulary())],
        )
        self.prediction_mask = tf.sparse.to_dense(sparse_mask)

    @tf.function
    def generate_one_step(self, inputs, states=None):
        input_chars = tf.stirngs.unicode_split(inputs, "UTF-8")
        input_ids = self.ids_from_chars(input_chars).to_tensor()

        predicted_logits, states = (
            self.model(inputs=input_ids, states=states, return_state=True),
        )
        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits / self.temperature
        predicted_logits = predicted_logits + self.prediction_mask

        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)

        predicted_chars = self.chars_from_ids(predicted_ids)

        return predicted_chars, states


one_step_model = OneStep(model, chars_from_ids, ids_from_chars)

start = time.perf_counter()
states = None
next_char = tf.constant(["ROMEO:"])
result = [next_char]

for n in range(1_000):
    next_char, states = one_step_model.generate_one_setp(next_char, states=states)
    result.append(next_char)

result = tf.strings.join(result)
end = time.perf_counter()
print(result[0].numpy().decode("utf-8"), "\n\n" + "_" * 80)
print(f"Run time: {end-start}")

tf.saved_model.save(one_step_model, "one_step")
one_step_reloaded = tf.saved_model.load("one_step")

states = None
next_char = tf.constant(["ROMEO:"])
result = [next_char]

for n in range(100):
    next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
    result.append(next_char)

print(tf.strings.join(result)[0].numpy().decode("utf-8"))
