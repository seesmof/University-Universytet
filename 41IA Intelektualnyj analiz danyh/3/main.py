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
print(data.info())

# -- REPORT --
# Classifiers
# Optimized
# Comparison
