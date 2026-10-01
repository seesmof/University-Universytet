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
