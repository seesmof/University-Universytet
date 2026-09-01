import os
import datetime
import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

data = {
    "Name": ["Harriett", "Olga", "Wayne"],
    "Age": [35, 33, 55],
    "Gender": ["Male", "Female", "Male"],
    "Salary": [4391, 3954, 4648],
}
df = pd.DataFrame(data=data)
df = df.set_index("Age")
print(df.head(10))

data = [55, 44, 37, 48, 47]
labels = ["a", "b", "c", "d", "e"]
s = pd.Series(data, index=labels)
