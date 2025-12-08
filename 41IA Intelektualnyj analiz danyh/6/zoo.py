import os
import pandas as pd
from matplotlib import pyplot as plt

from scipy.cluster.hierarchy import linkage, dendrogram

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "zoo.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
TARGET_FEATURE = "type"
Y = df[TARGET_FEATURE]
X = df.drop([TARGET_FEATURE, "animal"], axis=1)
print(X)

mergins = linkage(X, method="complete")
dendrogram(mergins, labels=Y.tolist())
plt.show()
