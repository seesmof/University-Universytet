import pandas as pd
from matplotlib import pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

classifiers = {
    "ZeroRule": DummyClassifier(strategy="most_frequent"),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Gaussian Naive Bayes": GaussianNB(),
    "Linear SVM": SVC(kernel="linear", C=0.025),
}

results = dict()

for model in classifiers:
    classifiers[model].fit(X_train, y_train)
    y_predict = classifiers[model].predict(X_test)
    results[model] = accuracy_score(y_test, y_predict)

results_table = pd.Series(results)
print(results_table)

plt.tight_layout()
results_table.plot(kind="bar")
plt.show()
