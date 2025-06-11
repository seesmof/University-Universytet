from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
df=pd.DataFrame(X,columns=iris.feature_names)
print(df)

pairs=[(i,j) for i in range(len(iris['feature_names'])) for j in range(i+1,len(iris['feature_names']))]
print(pairs)

legends=list(set(iris['target_names'][iris['target']]))
plt.scatter(X[:,0],X[:,1],cmap='viridis',c=iris['target'])
plt.xlabel(iris['feature_names'][0])
plt.ylabel(iris['feature_names'][1])
plt.show()