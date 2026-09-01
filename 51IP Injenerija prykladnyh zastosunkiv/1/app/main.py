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
print(df.head(10))
print(df.iloc[1])

print(os.path.dirname(os.path.abspath(__file__)))

print(df.columns)
print(df["Age"].std)
