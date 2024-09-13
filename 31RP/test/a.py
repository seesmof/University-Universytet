import numpy as np

data = np.arange(12).reshape(3, 4)
print(data)
print(
    f"{data.shape=}, {data.ndim=}, {data.dtype.name=}, {data.itemsize=}, {data.size=}"
)
