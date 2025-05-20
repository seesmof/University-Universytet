import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris=load_iris()

X=iris.data
y=iris.target

feature_names=iris.feature_names
target_names=iris.target_names

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)

print(f'{X_train.shape = }')
print(f'{X_test.shape = }')
print(f'{y_train.shape = }')
print(f'{y_test.shape = }')

from sklearn