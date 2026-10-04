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
    # Remove the verse reference's Book name
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
print(corpus)
