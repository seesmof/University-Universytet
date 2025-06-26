from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns


iris = load_iris(as_frame=True)
iris.frame["target"] = iris.target_names[iris.target]
_ = sns.pairplot(iris.frame, hue="target")
plt.show()
