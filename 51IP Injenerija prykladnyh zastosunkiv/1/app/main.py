# Import necessary libraries
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.model_selection import train_test_split
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA
from keras.layers import LSTM, Dense, Input
from keras.models import Sequential
import matplotlib.pyplot as plt
from prophet import Prophet
import pandas as pd
import numpy as np
import os

# Read the data from a file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "power.csv"
file_path: str = os.path.join(current_dir, file_name)
df = pd.read_csv(file_path, parse_dates=["DATE"], index_col="DATE")

# Convert the date column to a proper date
average = df.rolling(window=12).mean()
df.rename(columns={"IPG2211A2N": "Consumption"}, inplace=True)
print(df)

ets_model = ExponentialSmoothing(
    df["Consumption"], seasonal="add", trend="add", seasonal_periods=12
)
ets_fit = ets_model.fit()
forecast = ets_fit.forecast(steps=12)
plt.figure(figsize=(10, 6))
plt.plot(df, label="Observed")
plt.plot(forecast, label="Forecast", color="red")
plt.title("ETS Model Forecast")
plt.xlabel("Date")
plt.ylabel("Energy Consumption")
plt.legend()
plt.show()
