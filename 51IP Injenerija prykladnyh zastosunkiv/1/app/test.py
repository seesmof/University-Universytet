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

rolling_mean = df.rolling(window=12).mean()
rolling_std = df.rolling(window=12).std()
plt.plot(df, color="tab:blue", label="Original Data")
plt.plot(rolling_mean, color="tab:red", label="Rolling Mean")
plt.plot(rolling_std, color="tab:green", label="Rolling Std")
plt.xlabel("Date", size=12)
plt.ylabel("Power Consumption")
plt.legend()
plt.title("Rolling Statistics", size=14)
plt.grid()
plt.show()
