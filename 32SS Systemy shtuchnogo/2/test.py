from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
df=pd.DataFrame(X,columns=iris.feature_names)
print(iris['feature_names'])

plt.plot(X[:,0],c="g")
plt.xlabel(iris['feature_names'][0])
plt.ylabel('Value')
plt.show()