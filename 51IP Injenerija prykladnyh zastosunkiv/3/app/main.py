import re

import tensorflow as tf
import numpy as np
import os
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from string import punctuation

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, "Bible.txt")
with open(data_file_path, encoding="utf-8", mode="r") as f:
    lines = f.readlines()
cleaned_lines = list()
for line in lines:
    no_book_name = line[4:].strip()
    chapter_verse_pattern = r"\d+\:\d+\s"
    no_reference_line = re.sub(chapter_verse_pattern, "", no_book_name).strip()
    cleaned_lines.append(no_reference_line)
corpus = " ".join(cleaned_lines)

sequence_length = 100
BATCH_SIZE = 128
EPOCHS = 30
corpus = corpus.lower()
corpus = corpus.translate(str.maketrans("", "", punctuation))

n_chars = len(corpus)
vocab = "".join(sorted(set(corpus)))
print(f"Unique Characters: {vocab}")
n_unique_characters = len(vocab)
print(f"Number of Characters: {n_chars}")
print(f"Number of Unique Characters: {n_unique_characters}")

char_to_int = {c: i for i, c in enumerate(vocab)}
int_to_char = {i: c for i, c in enumerate(vocab)}

encoded_text = np.array([char_to_int[c] for c in corpus])
