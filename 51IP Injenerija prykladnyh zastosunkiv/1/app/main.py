import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pmdarima as pm

# Read the data from a file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)
df = pd.read_csv(file_path, parse_dates=["DATE"], index_col="DATE")
df.rename(columns={"IPG2211A2N": "Consumption"}, inplace=True)
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

# Decompose the data into seasonal, periodic and so on
decomp = seasonal_decompose(df, model="additive", period=12)
decomp.plot()
plt.show()

# Split data into test and train
N = 24
train = df[:-N]
test = df[-N:]
print(f"{len(train) = }")

# Make an ARIMA model
model = pm.auto_arima(
    train,
    seasonal=True,
    m=12,
    trace=True,
    error_action="ignore",
    suppress_warnings=True,
)
print(model.summary())
arima_forecast = pd.Series(model.predict(n_periods=N), index=test.index)

# Plot prediction results
plt.figure(figsize=(12, 6))
plt.plot(train, label="Training Data")
plt.plot(test, label="Actual Values", linewidth=2)
plt.plot(arima_forecast, label="Forecasted Values", linestyle="--")
plt.title("ARIMA Forecast")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

# Make an ETS model
ets_model = ExponentialSmoothing(
    train, seasonal="add", trend="add", seasonal_periods=12
)
ets_fit = ets_model.fit()
ets_forecast = pd.Series(ets_fit.forecast(steps=N), index=test.index)

# Plot the prediction results
plt.figure(figsize=(12, 6))
plt.plot(train, label="Training Data")
plt.plot(test, label="Actual Values", linewidth=2)
plt.plot(ets_forecast, label="Forecasted Values", linestyle="--")
plt.title("ETS Forecast")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

# Add methods comparison
arima_score = np.sqrt(mean_squared_error(test, arima_forecast))
ets_score = np.sqrt(mean_squared_error(test, ets_forecast))
print(f"{arima_score = }")
print(f"{ets_score = }")
