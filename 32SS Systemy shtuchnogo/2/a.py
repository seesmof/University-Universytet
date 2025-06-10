from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
data['species']=pd.Categorical.from_codes(iris.target,iris.target_names)

features=iris.feature_names
feature_pairs=[(i,j) for i in range(len(features)) for j in range(i+1,len(features))]

fig,axes=plt.subplots(2,3,figsize=(20,12),tight_layout=True)
for ax,(feature_one,feature_two) in zip(axes.flatten(),feature_pairs):
    for species in data['species'].unique():
        subset=data[data['species']==species]
        ax.scatter(subset[features[feature_one]],subset[features[feature_two]],label=species,alpha=0.8)
        ax.set_xlabel(features[feature_one])
        ax.set_ylabel(features[feature_two])
fig.legend(data['species'].unique(),loc='upper center',ncol=3,fontsize='medium')
plt.show()
