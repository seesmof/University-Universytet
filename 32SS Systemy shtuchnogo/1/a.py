import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)

needed='Name,Age,Survived'.split(',')
df=df[needed].dropna()
le=LabelEncoder()

target=df.Survived
df=df.drop(['Survived'],axis=1)
df=df.drop(['Name'],axis=1)

train,test=train_test_split(df,test_size=0.3)
model=KMeans(n_clusters=3)
model.fit(train)
print(f'{model.cluster_centers_ = }')
prediction_results=model.predict(test)
print(f'{prediction_results = }')