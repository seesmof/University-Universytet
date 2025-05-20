from sklearn.datasets import load_iris
iris=load_iris()

X=iris.data
y=iris.target

feature_names=iris.feature_names
target_names=iris.target_names

print(f"{feature_names = }")
print(f"{target_names = }")
print(f"{type(X) = }")
print(f"{X[:5] = }")