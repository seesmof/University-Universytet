from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
pairs=[(i,j) for i in range(len(iris['feature_names'])) for j in range(i+1,len(iris['feature_names']))]

for i,(f1,f2) in enumerate(pairs):
    fig=plt.figure(figsize=(8,5),tight_layout=True)
    plot=plt.scatter(X[:,f1],X[:,f2],cmap="viridis",c=iris['target'])
    plt.xlabel(iris['feature_names'][f1])
    plt.ylabel(iris['feature_names'][f2])
    # Colors to legend: https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#:~:text=iris.target_names.tolist()%2C
    fig.legend(plot.legend_elements()[0], iris.target_names.tolist())
    plt.show()
