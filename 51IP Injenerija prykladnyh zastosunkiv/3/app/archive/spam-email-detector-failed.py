import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download("stopwords")
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
import warnings

warnings.filterwarnings("ignore")

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, "data", "spam_ham_dataset.csv")
data = pd.read_csv(data_file_path)
print(data.head())

# Visualize the data
sns.countplot(x="label", data=data)
plt.show()

# Downsampling the hams
ham = data[data["label"] == "ham"]
spam = data[data["label"] == "spam"]
ham_balanced = ham.sample(n=len(spam))
balanced_data = pd.concat([ham_balanced, spam]).reset_index(drop=True)
sns.countplot(x="label", data=balanced_data)
plt.title("Balanced Spam and Ham")
plt.xticks(ticks=[0, 1], labels=["Ham (Not Spam)", "Spam"])
plt.show()

# Cleaning the data
balanced_data["text"] = balanced_data["text"].str.replace("Subject: ", "")
punctuation_list = string.punctuation


def remove_punctuation(text):
    tmp = str.maketrans("", "", punctuation_list)
    return text.translate(tmp)


balanced_data["text"] = balanced_data["text"].apply(lambda l: remove_punctuation(l))
print(balanced_data.head())


def plot_word_cloud(data, typ):
    email_corpus = " ".join(data["text"])
    wc = WordCloud(
        background_color="black", max_words=100, width=800, height=400
    ).generate(email_corpus)
    plt.figure(figsize=(7, 7))
    plt.imshow(wc, interpolation="bilinear")
    plt.title(f"WordCloud for {typ} Emails", fontsize=15)
    plt.axis("off")
    plt.show()


plot_word_cloud(balanced_data[balanced_data["label"] == "ham"], typ="Non-Spam")
plot_word_cloud(balanced_data[balanced_data["label"] == "spam"], typ="Spam")

train_x, test_x, train_y, test_y = train_test_split(
    balanced_data["text"], balanced_data["label"], test_size=0.2
)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_x)

train_sequences = tokenizer.texts_to_sequences(train_x)
test_sequences = tokenizer.texts_to_sequences(test_x)

max_len = 100
train_sequences = pad_sequences(
    train_sequences, maxlen=max_len, padding="post", truncating="post"
)
test_sequences = pad_sequences(
    test_sequences, maxlen=max_len, padding="post", truncating="post"
)

train_y = (train_y == "spam").astype(int)
test_y = (test_y == "spam").astype(int)

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Embedding(
            input_dim=len(tokenizer.word_index) + 1, output_dim=32, input_length=max_len
        ),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer="adam",
    metrics=["accuracy"],
)
model.summary()

es = EarlyStopping(patience=3, monitor="val_accuracy", restore_best_weights=True)
lr = ReduceLROnPlateau(patience=2, monitor="val_loss", factor=0.5, verbose=0)
history = model.fit(
    train_sequences,
    train_y,
    validation_data=(test_sequences, test_y),
    epochs=20,
    batch_size=32,
    callbacks=[lr, es],
)

test_loss, test_accuracy = model.evaluate(test_sequences, test_y)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend()
plt.show()
