from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
# Розбиття вибірки на тестову та тренувальну
X_train, X_test, y_train, y_test = train_test_split(X, y)

kmeans = KMeans(n_clusters=2)
kmeans_results = kmeans.fit_predict(X_test)
# Оцінка похибки методу
kmeans_score = kmeans.score(X_test) / len(X_test)

agglomerative = AgglomerativeClustering()
agglomerative_results = agglomerative.fit_predict(X_test)
# Кількість розбіжностей між результатами двох методів
agglomerative_score = sum(
    [agglomerative_results[i] != kmeans_results[i] for i in range(len(kmeans_results))]
) / len(kmeans_results)

print(f"{kmeans_results = }")
print(f"K-Means clustering accuracy: {kmeans_score}")
print(f"\n{agglomerative_results = }")

AgglomerativeClustering()
