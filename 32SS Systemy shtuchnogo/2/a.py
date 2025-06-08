from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data,target,target_names=load_iris()['data'],load_iris()['target'],load_iris()['target_names']

sepal_lengths=data[:,np.array([True,False,False,False])]
sepal_widths=data[:,np.array([False,True,False,False])]
petal_lenghts=data[:,np.array([False,False,True,False])]
petal_widths=data[:,np.array([False,False,False,True])]

plt.scatter(sepal_lengths,sepal_widths,c=target,cmap='berlin')

plt.legend(target_names)
plt.show()