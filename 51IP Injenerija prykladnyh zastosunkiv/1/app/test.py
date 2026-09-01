import os
import datetime
import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([26, 14, 83, 89, 10, 41, 20, 46, 24, 39, 83])

plt.axhline(y=50, color="#4a00b3")
plt.axvline(x=50, color="#4a00b3")
plt.scatter(x, y)
plt.title("Dots")
plt.grid()
plt.legend()
plt.show()
