from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X=np.array([[0.33],[0.72],[0.1],[0.01],[0.7]])
y=np.array([0,1,0,0,1])

model=LinearRegression()
model.fit(X,y)
predictions=model.predict(X)
print(predictions)