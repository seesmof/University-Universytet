from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y)
print(X_train,y_train)

kmeans=KMeans(n_clusters=2)
kmeans_trains=kmeans.fit(X_train)
kmeans_results=kmeans.predict(X_test)
kmeans_score=kmeans.score(X_test)/len(X_test)

agglomerative=AgglomerativeClustering()
agglomerative_results=agglomerative.fit_predict(X_test)
agglomerative_score=sum([agglomerative_results[i]!=kmeans_results[i] for i in range(len(kmeans_results))])

print(f'{kmeans_results = }')
print(f'{kmeans_score = }')
print(f'{agglomerative_results = }')
print(f'{agglomerative_score = }')