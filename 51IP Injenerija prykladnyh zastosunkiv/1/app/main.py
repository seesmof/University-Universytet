"""
This is my own attempt to plot a time series.
"""

import os
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)

df = pd.read_csv(file_path)

df["DATE"] = pd.to_datetime(df["DATE"])
df = df.set_index("DATE")
print(df)

plt.figure(figsize=(12, 6))
plt.plot(df, color="tab:blue", label="Original Data")
plt.title("Rolling Statistics", size=14)
plt.xlabel("Date", size=12)
plt.ylabel("Power Consumption")
plt.legend()
plt.grid()
plt.show()

decomp = seasonal_decompose(df, model="additive", period=12)
decomp.plot()
plt.show()

train = df[:-12]
test = df[-12:]

model = pm.auto_arima(
    train,
    seasonal=False,
    m=12,
    trace=True,
    error_action="ignore",
    suppress_warnings=True,
)
model.summary()

forecast = model.predict(n_preiods=12)
forecast = pd.Series(forecast, index=test.index)

plt.figure(figsize=(12, 6))
plt.plot(train, label="Training Data")
plt.plot(test, label="Actual Values", linewidth=2)
plt.plot(forecast, label="Forecasted Values", linestyle="--")
plt.title("Forecast vs Actual")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
