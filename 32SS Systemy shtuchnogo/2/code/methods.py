# Кількість кластерів та ознак
CLUSTERS=4
FEATURES=4

from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

cluster_names=[f'Cluster {number}' for number in range(CLUSTERS)]

iris=load_iris()
X=iris.data
X_reduced=PCA(n_components=FEATURES).fit_transform(X)
print(X_reduced)
y=iris.target
# Розбиття вибірки на тестову та тренувальну
X_train,X_test,y_train,y_test=train_test_split(X_reduced,y)

kmeans=KMeans(n_clusters=CLUSTERS)
kmeans_results=kmeans.fit_predict(X_test)
# Оцінка похибки методу
kmeans_score=kmeans.score(X_test)/len(X_test)

agglomerative=AgglomerativeClustering(n_clusters=CLUSTERS)
agglomerative_results=agglomerative.fit_predict(X_test)
# Кількість розбіжностей між результатами двох методів
agglomerative_score=sum([agglomerative_results[i]!=kmeans_results[i] for i in range(len(kmeans_results))])

print(f'\n{kmeans_results = }')
print(f'K-Means clustering accuracy: {kmeans_score}')
print(f'\n{agglomerative_results = }')
print(f'Hierarchical clustering results difference: {agglomerative_score}')

fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(10,5),tight_layout=True)
for axis,result in zip(ax,[kmeans_results,agglomerative_results]):
    plot=axis.scatter(X_test[:,0],X_test[:,1],c=result,cmap='viridis')
fig.legend(plot.legend_elements()[0], cluster_names, loc='upper left')
plt.show()