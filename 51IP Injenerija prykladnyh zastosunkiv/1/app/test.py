import os
from matplotlib import pyplot as plt
import pandas as pd
from nicegui import ui

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)

df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE")
print(df)

with ui.matplotlib(figsize=(12, 2)).figure as f:
    x = df.index
    y = df
    ax = f.gca()
    ax.plot(x, y, "-")

ui.run(title="IP1", favicon="📊")
