import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import contingency_matrix
from sklearn.cluster import DBSCAN

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "zoo.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
TARGET_FEATURE = "type"
Y = df[TARGET_FEATURE]
X = df.drop([TARGET_FEATURE, "animal"], axis=1)
print(X)

model = DBSCAN(eps=0.5, min_samples=5)
Y_predict = model.fit_predict(X)

matrix = pd.DataFrame(contingency_matrix(Y, Y_predict))
matrix.index = Y.unique()
matrix.columns = np.unique(Y_predict)
print(matrix)
