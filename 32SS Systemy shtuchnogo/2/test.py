from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
df=pd.DataFrame(X,columns=iris.feature_names)
print(iris['feature_names'])

pairs=[(i,j) for i in range(len(iris['feature_names'])) for j in range(i+1,len(iris['feature_names']))]
print(pairs)

fig=plt.figure(figsize=(10,8),tight_layout=True)
for i,(f1,f2) in enumerate(pairs):
    plot=plt.scatter(X[:,0],X[:,1],cmap="viridis",c=iris['target'])
    plt.xlabel(iris['feature_names'][0])
    plt.ylabel(iris['feature_names'][1])
    # Colors to legend: https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#:~:text=iris.target_names.tolist()%2C
    fig.legend(plot.legend_elements()[0], iris.target_names.tolist())
    plt.show()
