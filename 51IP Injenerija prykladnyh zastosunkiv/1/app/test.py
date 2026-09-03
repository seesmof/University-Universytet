import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = [i + (i % 7) for i in range(1, 100)]
index = pd.date_range(start="2023-01-01", periods=99, freq="D")
ts = pd.Series(data, index=index)

result = sm.tsa.seasonal_decompose(ts, model="additive")
result.plot()
plt.show()
