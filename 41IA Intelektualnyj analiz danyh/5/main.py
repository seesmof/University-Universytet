import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "marketbasket.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
df = df.fillna(0)
for column in df.columns:
    df[column] = df[column].astype("bool")
print(df.head())
