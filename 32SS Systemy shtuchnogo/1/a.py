import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)

needed='Name,Age,Sex,Survived'.split(',')
df=df[needed].dropna()
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
print(df)

'''

train,test=train_test_split(df,test_size=0.3)
print(train)
model=KMeans()
model.fit(train)
res=model.predict(test)
'''