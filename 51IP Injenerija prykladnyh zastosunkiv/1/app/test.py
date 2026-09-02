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
    "Name": ["Keith", "Margaret", "Bryan"],
    "Age": [52, 48, 48],
    "Salary": [1139, 2603, 5559],
}
df = pd.DataFrame(data)
print(df.head())
