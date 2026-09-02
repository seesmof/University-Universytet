import os
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)

data = pd.read_csv(file_path)
print(data.head())

data.plot()
plt.show()
