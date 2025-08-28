from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import rand_score, silhouette_score
from sklearn.model_selection import train_test_split


data, target = load_iris(as_frame=True, return_X_y=True)
print(data)

data_train, data_test, target_train, target_test = train_test_split(data, target)

kmeans = KMeans().fit(data_train)
kmeans_results = kmeans.predict(data_test)
print(kmeans_results)

silhouette_score()
