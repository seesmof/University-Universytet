import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)

# 1.1 Еталони

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

# 1.2 Вибірка

variant=19
size=5*variant
number_of_features=3*variant

ones_range=range(1,size,4)
twos_range=range(2,size,4)
threes_range=range(3,size,4)

input_array=[]
for data_row in range(1,size):
    row=[]
    for feature_col in range(1,number_of_features):
        result=0
        if feature_col in ones_range:
            result=feature_col*variant-0.1*data_row
        elif feature_col in twos_range:
            result=0.01*feature_col*variant**-1
        elif feature_col in threes_range:
            result=feature_col*random.random()
        row.append(result)
    input_array.append(row)
output_array=np.array(input_array)
print(f'{output_array = }')