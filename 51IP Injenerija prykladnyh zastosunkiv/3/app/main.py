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
