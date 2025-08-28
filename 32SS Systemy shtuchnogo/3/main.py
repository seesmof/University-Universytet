import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold

iris = load_iris()
df = pd.DataFrame(data=iris["data"], columns=iris["feature_names"])
print(df)

VarianceThreshold()
