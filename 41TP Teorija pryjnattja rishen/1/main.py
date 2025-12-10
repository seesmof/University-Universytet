import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Load file
current_dir: str = os.path.dirname(os.path.abspath(__file__))
file_name = "data.csv"
file_path: str = os.path.join(current_dir, file_name)

# Data preprocessing
VARIANT: int = 19
df: pd.DataFrame = pd.read_csv(file_path)
df["noise"] = df["noise"] * VARIANT
threshold: float = df["coef"].mean()
print(df)

X = df["noise"]
Y = df["coef"]

plt.scatter(X, Y)
plt.xlabel("Noise")
plt.ylabel("Alpha")
plt.tight_layout()
plt.show()

actual_classes = np.where(Y <= threshold, "K1", "K2")
print(actual_classes)
