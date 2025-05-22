from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X,y=make_classification(random_state=0)
plt.scatter(X[:,0],X[:,1],marker='o',c=y,edgecolors='k')
plt.show()