from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
X=iris['data']
df=pd.DataFrame(X,columns=iris.feature_names)
print(df)

