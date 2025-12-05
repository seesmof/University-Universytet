import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "data.csv"
file_path = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
df = df.fillna(df.mean())
Y = df["class"]
X = df.drop(["class"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, Y)

# --- Regressors ---
regressors = {
    "Linear Regression": LinearRegression(),
    "K Neighbors Regressor": KNeighborsRegressor(n_neighbors=5),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth=5),
    "Support Vector Regression": SVR(),
}
results = dict()

for model in regressors:
    regressors[model].fit(X_train, y_train)
    Y_predict = regressors[model].predict(X_test)
    results[model] = mean_absolute_error(y_test, Y_predict)
results_table = pd.Series(results)

print(results_table)
results_table.plot(kind="bar")
plt.tight_layout()
plt.show()

# --- Improved Accuracy for Decision Tree Regressor ---
tree_results = dict()
for i in range(1, 11):
    model = DecisionTreeRegressor(max_depth=i)
    model.fit(X_train, y_train)
    Y_predict = model.predict(X_test)
    tree_results[i] = mean_absolute_error(y_test, Y_predict)

tree_results_table = pd.Series(tree_results)
print()
print(tree_results_table)
tree_results_table.plot()
plt.show()

# --- Identifying Attributes ---
LR = LinearRegression()
LR.fit(X_train, y_train)
coefficients = pd.Series(np.absolute(LR.coef_), index=X.columns)
print()
print(coefficients)
coefficients.plot(kind="barh")
plt.show()
