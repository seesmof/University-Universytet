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

x = np.array(range(0, 101, 10))
y = np.array([50, 79, 30, 99, 34, 96, 59, 51, 92, 6, 88])

top_right_mask = (x > 50) & (y > 50)
others_mask = ~top_right_mask

plt.scatter(x[others_mask], y[others_mask], color="tab:blue", label="Regular Dots")
plt.scatter(
    x[top_right_mask], y[top_right_mask], color="tab:red", label="Top Right Corner"
)

plt.axhline(y=50, color="#4a00b3")
plt.axvline(x=50, color="#4a00b3")

plt.title("Dots")
plt.grid()
plt.legend()
plt.show()
