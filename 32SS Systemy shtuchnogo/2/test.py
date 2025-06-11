from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
df=pd.DataFrame(X,columns=iris.feature_names)
print(iris['feature_names'])

plt.scatter(X[:,0],X[:,1])
plt.xlabel(iris['feature_names'][0])
plt.ylabel(iris['feature_names'][1])
plt.show()
