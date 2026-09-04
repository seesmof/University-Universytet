"""
This is my own attempt to plot a time series.
"""

import os
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pmdarima as pm

# Read the data from a file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)
df = pd.read_csv(file_path)

# Convert the date column to a proper date
df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE")
print(df)
average = df.rolling(window=12).mean()

# Plot the original data
plt.figure(figsize=(12, 6))
plt.plot(df, color="tab:blue", label="Original Data")
plt.plot(average, color="tab:red", label="Average Data")
plt.title("Rolling Statistics", size=14)
plt.xlabel("Date", size=12)
plt.ylabel("Power Consumption")
plt.legend()
plt.grid()
plt.show()
