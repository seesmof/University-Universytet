import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import contingency_matrix

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "vehicle.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
df = df.dropna()

TARGET_FEATURE = "Class"
Y = df[TARGET_FEATURE]
X = df.drop([TARGET_FEATURE], axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

KM = KMeans(n_clusters=len(Y_train))
KM.fit(X_train)

cluster_centers = pd.DataFrame(KM.cluster_centers_)
cluster_centers.columns = X.columns
print(cluster_centers)

Y_predict = KM.predict(X_test)
matrix = pd.DataFrame(contingency_matrix(Y_test, Y_predict))
matrix.index = Y.unique()
print(matrix)

right_cluster_count = 0
for column in matrix.columns:
    right_cluster_count += matrix[column].max()
    accuracy = right_cluster_count / matrix.sum().sum()
    error_rate = 1 - accuracy

print(f"{right_cluster_count=}")
print(f"{accuracy=}")
print(f"{error_rate=}")
