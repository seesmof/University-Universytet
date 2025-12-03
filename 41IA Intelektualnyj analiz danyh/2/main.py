import os
import pandas as pd
from matplotlib import pyplot as plt

# Load data
root_folder = os.path.dirname(os.path.abspath(__file__))
file_name = "breast-cancer.csv"
file_path = os.path.join(root_folder, "data", file_name)

# Print table
data = pd.read_csv(file_path, na_values=["?"])
print(data.head())
print()

# Fill missing values
data["node-caps"] = data["node-caps"].fillna(data["node-caps"].mode())
print(data.head())

# Replace categorical with numbers
data["node-caps"].replace({"yes": 1, "no": 0}, inplace=True)
data["breast"].replace({"left": 1, "right": 0}, inplace=True)
data["irradiat"].replace({"yes": 1, "no": 0}, inplace=True)
print(data.head())

# Pie
data.head().plot(kind="pie", y="deg-malig")
# Hist
data.hist(column="deg-malig")
# Scatter
data.plot(kind="scatter", x="age", y="tumor-size")
# Bar
data.head().plot(kind="bar", y="deg-malig")
plt.show()
