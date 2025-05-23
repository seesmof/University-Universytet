import os
import random
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, normalize

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)

# 1.1 Еталони

needed='Name,Age,Survived'.split(',')
df=df[needed].dropna()
le=LabelEncoder()

target_feature=df.Survived.to_numpy()
df=df.drop(['Survived'],axis=1)
df=df.drop(['Name'],axis=1)

X_train,X_test,y_train,y_test=train_test_split(df,target_feature,test_size=0.3)
model=KMeans(n_clusters=3)
model.fit(X_train)
print(f'{model.cluster_centers_ = }')
prediction_results=model.predict(X_test)
print(f'{prediction_results = }')

# 1.2 Вибірка

def get_target_feature(row: list[int]):
    if row[0]**2+row[1]**2 < variant**2+0.04*size**2: return 0
    elif row[0]**2+row[1]**2 >= variant**2+0.04*size**2: return 1

variant=19
size=5*variant
number_of_features=3*variant

ones_range=range(1,size,4)
twos_range=range(2,size,4)
threes_range=range(3,size,4)
features_input=[]
targets_input=[]
for data_row in range(1,size):
    row=[]
    for feature_col in range(1,number_of_features):
        if feature_col in ones_range:
            result=feature_col*variant-0.1*data_row
        elif feature_col in twos_range:
            result=0.01*feature_col*variant**-1
        elif feature_col in threes_range:
            result=feature_col*random.random()
        row.append(result)

    targets_input.append(get_target_feature(row=row))
    features_input.append(row)
features=np.array(features_input)
targets=np.array(targets_input)
print(f'{features = }')
print(f'{targets = }')

# 1.3 Нормування

normalized_features=normalize(features)
print(f'{normalized_features = }')

# 1.4 Побудова моделі

features_train,features_test,targets_train,targets_test=train_test_split(normalized_features,targets)

start_time=time.perf_counter()
model=KMeans(n_clusters=number_of_features)
model.fit(features_train)
end_time=time.perf_counter()
learning_time=end_time-start_time
print(f'{learning_time = }')
print(f'{model.cluster_centers_ = }')

# 1.5 Розпізнавання

start_time=time.perf_counter()
result=model.predict(features_test)
print(f'{result = }')
end_time=time.perf_counter()
prediction_time=end_time-start_time
print(f'{prediction_time = }')

# 1.6 Помилка

first_prediction_error=model.score(features_test)
print(f'{first_prediction_error = }')
first_error_probability=first_prediction_error/size*number_of_features
first_right_probability=1-first_error_probability
print(f'{first_error_probability = }')
print(f'{first_right_probability = }')

# 1.7 Нова вибірка

new_features=[row[variant] for row in features_input]
print(f'{new_features = }')
new_center=int(result[variant])
print(f'{new_center = }')
new_target=get_target_feature(row=new_features)
print(f'{new_target = }')

# 1.8 Розпізнавання

new_features=np.array(new_features).reshape(-1,1)
model=model.fit(new_features)
result=model.predict(new_features)
print(f'{result = }')

# 1.9 Помилка

prediction_error=model.score(new_features)
print(f'{prediction_error = }')
error_probability=prediction_error/len(new_features)*1
right_probability=1-error_probability
print(f'{error_probability = }')
print(f'{right_probability = }')

# 1.10 Порівняння

prediction_error_difference=abs(first_prediction_error-prediction_error)
error_probability_difference=abs(first_error_probability-error_probability)
right_probability_difference=abs(first_right_probability-right_probability)
print(f'{prediction_error_difference = }')
print(f'{error_probability_difference = }')
print(f'{right_probability_difference = }')

print('У другому випадку помилка більше. Тому, чим більше екземплярів, тим менша помилка.')