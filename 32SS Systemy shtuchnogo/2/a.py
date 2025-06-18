from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target

model = KMeans(n_clusters=3)
model.fit(X[2:-1])
print(X[0], y[0], iris.target_names[y[0]])
print(X[1], y[1], iris.target_names[y[1]])
print(X[0:2])
results = model.predict(X[0:2])
print(results, iris.target_names[results])
