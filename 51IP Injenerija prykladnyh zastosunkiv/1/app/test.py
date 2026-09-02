"""
This is my own attempt to plot a time series.
"""

import os
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)
print(df.head())

df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE")
print(df.head())
