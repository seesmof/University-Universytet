import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Use Logistic Regression with L1 penalty for feature selection
# Note: 'saga' solver supports L1 penalty for multinomial problems
log_reg = LogisticRegression(
    penalty="l1", solver="saga", multi_class="multinomial", max_iter=500
)

# Fit the model
log_reg.fit(X, y)

# Use SelectFromModel to select features with non-zero coefficients
selector = SelectFromModel(log_reg, prefit=True)

# Transform the dataset to keep only selected features
X_selected = selector.transform(X)

print("Original feature names:", iris.feature_names)
print("Selected features mask:", selector.get_support())
print("Selected features:", np.array(iris.feature_names)[selector.get_support()])
print("Shape before selection:", X.shape)
print("Shape after selection:", X_selected.shape)
